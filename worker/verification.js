/* Cloudflare Worker — deux services sur la même adresse.

   1. VÉRIFICATION D'ACHAT
      GET /?session_id=cs_...  →  { valide, niveau }
      Le Worker interroge Stripe côté serveur : impossible à contourner depuis le
      navigateur.

   2. MESURE D'AUDIENCE
      POST /mesure             →  204, enregistre un événement anonyme
      GET  /mesure?cle=…       →  le tableau, réservé à l'éditeur

   Secrets à configurer dans Cloudflare (Settings → Variables → Secret) :
     STRIPE_CLE  clé restreinte Stripe, lecture seule sur les sessions Checkout
                 ET sur les PaymentIntents — sans la seconde, une session
                 remboursée resterait valable indéfiniment.
     MESURE_CLE  mot de passe de ton choix, pour lire le tableau de mesure.

   Liaison à ajouter (Settings → Bindings → D1) :
     MESURE      base D1, avec la table créée par le SQL de worker/MESURE.md

   Chaque service se tait si ce qu'il lui faut manque : sans STRIPE_CLE la
   vérification répond 501, sans la base D1 la mesure répond 204 sans rien écrire.
   Le site fonctionne dans les deux cas. */

const ORIGINES = [
  "https://boussole-emotionnelle.fr",
  "https://www.boussole-emotionnelle.fr",
];

/* Seuil en centimes séparant la formule Résultats (199) du Dossier (599).
   À revoir si les prix changent : c'est le montant payé qui décide du palier. */
const SEUIL_DOSSIER = 400;
const DEVISE = "eur";

/* Les six seuls événements acceptés. Une liste fermée plutôt qu'un champ libre :
   sans elle, n'importe qui pourrait remplir la base de lignes inventées, et le
   tableau deviendrait illisible sans qu'aucune alerte ne se déclenche. */
const EVENEMENTS = new Set([
  "accueil",      // arrivée sur la page du test
  "article",      // arrivée sur une page du guide
  "test-debut",   // clic sur « Commencer le test »
  "test-fin",     // seize situations répondues
  "paywall",      // la fenêtre de choix de formule s'ouvre
  "stripe",       // départ vers le paiement
]);

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const origine = req.headers.get("Origin") || "";
    const cors = {
      "Access-Control-Allow-Origin": ORIGINES.includes(origine) ? origine : ORIGINES[0],
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "content-type",
      "Vary": "Origin",
    };
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });

    if (url.pathname === "/mesure") {
      return req.method === "POST"
        ? ecrireMesure(req, env, origine, cors)
        : lireMesure(url, env, cors);
    }
    return verifierAchat(url, env, cors);
  },
};

/* ————————————————————————— mesure d'audience —————————————————————————
   Ce qui est écrit : un jour, un nom d'événement, et pour les articles le chemin
   de la page. Rien d'autre. Pas d'adresse IP, pas de cookie, pas d'identifiant de
   visite, pas d'en-tête de navigateur. On ne peut donc pas relier deux événements
   à la même personne — c'est délibéré, et c'est ce qui permet au site de continuer
   à dire que tes réponses ne quittent jamais ton navigateur.

   Le prix de ce choix : on compte des événements, pas des visiteurs. « 300
   arrivées et 4 départs vers Stripe » se lit très bien ; « combien de personnes
   distinctes » ne se saura jamais, et c'est un renseignement auquel on renonce. */
async function ecrireMesure(req, env, origine, cors) {
  /* Répondre 204 même quand on n'écrit rien : le navigateur n'a rien à faire de
     l'erreur, et une mesure qui échoue ne doit jamais se voir sur le site. */
  if (!ORIGINES.includes(origine)) return vide(cors);
  if (!env.MESURE) return vide(cors);

  let corps;
  try {
    /* text/plain à dessein : sendBeacon ne sait pas négocier de requête
       préalable, et un content-type JSON en déclencherait une. */
    corps = JSON.parse(await req.text());
  } catch (_) {
    return vide(cors);
  }

  const evenement = String(corps && corps.e || "");
  if (!EVENEMENTS.has(evenement)) return vide(cors);
  const page = evenement === "article" ? chemin(corps.p) : "";
  const jour = new Date().toISOString().slice(0, 10);

  try {
    await env.MESURE.prepare(
      "INSERT INTO compteur (jour, evenement, page, n) VALUES (?, ?, ?, 1) " +
      "ON CONFLICT(jour, evenement, page) DO UPDATE SET n = n + 1"
    ).bind(jour, evenement, page).run();
  } catch (_) { /* la mesure ne casse jamais la page */ }
  return vide(cors);
}

/* Un chemin de page du guide, et rien qui puisse servir à autre chose : pas de
   chaîne de requête (elle pourrait porter un identifiant), pas de fragment, et
   seulement les caractères d'un nom de fichier. */
function chemin(p) {
  const s = String(p || "").split("?")[0].split("#")[0];
  return /^\/guide\/[a-z0-9-]{1,80}\.html$/.test(s) ? s : "";
}

async function lireMesure(url, env, cors) {
  const cle = url.searchParams.get("cle") || "";
  if (!env.MESURE_CLE || !egal(cle, env.MESURE_CLE))
    return json({ erreur: "réservé à l'éditeur" }, 403, cors);
  if (!env.MESURE) return json({ erreur: "base non liée" }, 501, cors);

  const jours = Math.min(Math.max(parseInt(url.searchParams.get("jours") || "30", 10) || 30, 1), 365);
  const depuis = new Date(Date.now() - jours * 86400000).toISOString().slice(0, 10);
  try {
    const parJour = await env.MESURE.prepare(
      "SELECT jour, evenement, SUM(n) AS n FROM compteur WHERE jour >= ? " +
      "GROUP BY jour, evenement ORDER BY jour DESC"
    ).bind(depuis).all();
    const total = await env.MESURE.prepare(
      "SELECT evenement, SUM(n) AS n FROM compteur WHERE jour >= ? GROUP BY evenement"
    ).bind(depuis).all();
    const articles = await env.MESURE.prepare(
      "SELECT page, SUM(n) AS n FROM compteur WHERE jour >= ? AND evenement = 'article' " +
      "AND page <> '' GROUP BY page ORDER BY n DESC LIMIT 40"
    ).bind(depuis).all();
    return json({ depuis, jours, total: total.results, parJour: parJour.results,
                  articles: articles.results }, 200, cors);
  } catch (e) {
    return json({ erreur: String(e && e.message || e) }, 500, cors);
  }
}

/* Comparaison à durée constante : comparer deux chaînes avec === laisse fuir la
   longueur du préfixe juste, ce qui suffit à retrouver une clé à l'usure. */
function egal(a, b) {
  if (a.length !== b.length) return false;
  let d = 0;
  for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return d === 0;
}

/* ————————————————————————— vérification d'achat ————————————————————————— */
async function verifierAchat(url, env, cors) {
  const id = url.searchParams.get("session_id") || "";
  if (!/^cs_(live|test)_[A-Za-z0-9]{10,}$/.test(id))
    return json({ valide: false, erreur: "référence invalide" }, 400, cors);

  if (!env.STRIPE_CLE)
    return json({ valide: false, erreur: "clé non configurée" }, 501, cors);

  let s;
  try {
    /* On demande le paiement complet : sans lui, une session remboursée ou
       contestée reste « paid » et continuerait d'ouvrir l'accès indéfiniment. */
    const r = await fetch(
      `https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(id)}`
        + "?expand[]=payment_intent.latest_charge",
      { headers: { Authorization: `Bearer ${env.STRIPE_CLE}` } }
    );
    if (!r.ok) return json({ valide: false }, 200, cors);
    s = await r.json();
  } catch (_) {
    return json({ valide: false, erreur: "stripe injoignable" }, 502, cors);
  }

  const charge = s.payment_intent && s.payment_intent.latest_charge;
  const rembourse = !!(charge && (charge.refunded || (charge.amount_refunded | 0) > 0));
  const conteste = !!(charge && charge.disputed);
  const bonneDevise = (s.currency || "").toLowerCase() === DEVISE;
  const paye = s.payment_status === "paid" && bonneDevise && !rembourse && !conteste;

  /* Le palier suit le montant réellement encaissé, dans la devise attendue. */
  const niveau = (s.amount_total | 0) >= SEUIL_DOSSIER ? "dossier" : "resultats";
  return json({ valide: paye, niveau: paye ? niveau : null }, 200, cors);
}

function vide(cors) {
  return new Response(null, { status: 204, headers: { "cache-control": "no-store", ...cors } });
}

function json(objet, status, cors) {
  return new Response(JSON.stringify(objet), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store", ...cors },
  });
}
