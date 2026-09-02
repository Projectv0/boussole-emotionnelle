/* Vérification d'achat — Cloudflare Worker
   Le site appelle  GET /?session_id=cs_...  et reçoit { valide, niveau }.
   Le Worker interroge Stripe côté serveur : impossible à contourner depuis le navigateur.

   Secret à configurer dans Cloudflare (Settings → Variables → Secret) :
     STRIPE_CLE = clé secrète restreinte Stripe (lecture seule des sessions Checkout)
   Tant qu'il n'est pas configuré, le Worker répond 501 et le site garde son
   comportement actuel (VENTE.verification restant vide, il n'est pas appelé). */

const ORIGINES = [
  "https://boussole-emotionnelle.fr",
  "https://www.boussole-emotionnelle.fr",
];

/* seuil en centimes : 500 sépare la formule Résultats (199) du Dossier (999) */
const SEUIL_DOSSIER = 500;

export default {
  async fetch(req, env) {
    const origine = req.headers.get("Origin") || "";
    const cors = {
      "Access-Control-Allow-Origin": ORIGINES.includes(origine) ? origine : ORIGINES[0],
      "Access-Control-Allow-Methods": "GET, OPTIONS",
      "Vary": "Origin",
    };
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });

    const id = new URL(req.url).searchParams.get("session_id") || "";
    if (!/^cs_(live|test)_[A-Za-z0-9]{10,}$/.test(id))
      return json({ valide: false, erreur: "référence invalide" }, 400, cors);

    if (!env.STRIPE_CLE)
      return json({ valide: false, erreur: "clé non configurée" }, 501, cors);

    let s;
    try {
      const r = await fetch(
        `https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(id)}`,
        { headers: { Authorization: `Bearer ${env.STRIPE_CLE}` } }
      );
      if (!r.ok) return json({ valide: false }, 200, cors);
      s = await r.json();
    } catch (_) {
      return json({ valide: false, erreur: "stripe injoignable" }, 502, cors);
    }

    const paye = s.payment_status === "paid";
    const niveau = (s.amount_total | 0) >= SEUIL_DOSSIER ? "dossier" : "resultats";
    return json({ valide: paye, niveau: paye ? niveau : null }, 200, cors);
  },
};

function json(objet, status, cors) {
  return new Response(JSON.stringify(objet), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store", ...cors },
  });
}
