# Prompt : un site jumeau de « Boussole émotionnelle », sur l'astrologie

Copie tout ce qui suit dans une nouvelle session Claude Code, ouverte dans un dossier vide
qui sera celui du nouveau projet. Remplis d'abord la fiche du § 1 ; tout le reste est prêt.

---

Je veux construire un site jumeau de **Boussole émotionnelle** (`https://boussole-emotionnelle.fr`,
dépôt local `/Users/cavalier/Dev/Site Emotion/`), avec exactement le même système — un test par
mises en situation, un journal, des résultats notés, une analyse payante, un dossier complet,
une carte à partager, un code à offrir, un guide d'articles, des pages légales, un atelier de
publications et de vidéos — mais **sur l'astrologie**, avec une thématique et une direction
artistique astrologiques. Ce document dit ce qu'on reprend, ce qu'on transpose, ce qu'on
change, et dans quel ordre.

Réponds-moi en français et tutoie-moi. Pose-moi tes questions **une seule fois, au début,
en un seul message, quatre au plus**, avec des choix. Ensuite, avance seul, en respectant les
points d'arrêt du § 12 : à chacun, tu me montres et tu attends mon accord.

## 1 · La fiche du projet (à compléter avant de coller)

- **Nom du site :** [À COMPLÉTER — ou « propose-m'en cinq », voir § 3]
- **Domaine :** [À COMPLÉTER — ou « vérifie la disponibilité des noms proposés »]
- **Adresse de contact :** [À COMPLÉTER]
- **Dépôt GitHub (public, GitHub Pages) :** [À COMPLÉTER — nom du dépôt]
- **Compte Cloudflare pour le Worker :** le même que Boussole (`Projectv0.0@proton.me`), sauf indication contraire
- **Société vendeuse :** la même SAS que Boussole émotionnelle (en cours de création) — les pages légales reprennent les mêmes champs, dès qu'ils existent
- **Prix :** les mêmes que Boussole — résultats 1,99 €, dossier complet 5,99 €, complément 4 € — sauf indication contraire : [À COMPLÉTER si différent]
- **Thème visuel :** nuit étoilée (sombre) / aube dorée (clair) / « laisse-moi choisir sur trois planches » — [À COMPLÉTER]

## 2 · Qui je suis et comment on travaille

Je m'appelle Martial. Je ne suis pas développeur : je décide, je teste sur mon téléphone, je
fournis ce qui demande un compte, une identité ou de l'argent. Toi, tu fais tout le reste.

**Les règles de sécurité, absolues, qui ne se discutent jamais :**

- Tu ne crées aucun compte, tu n'entres aucun mot de passe, aucun numéro de carte (même une
  carte de test Stripe), aucun IBAN, aucune pièce d'identité. Quand une action le demande,
  tu me dis quoi faire et tu me laisses le faire.
- **Tu ne manipules jamais une clé d'API.** Les clés vivent dans `~/.config/<nom-du-projet>/<service>.cle`
  (chmod 600, hors du dépôt), ou dans des secrets `wrangler` que je pose moi-même au clavier.
  Tu ne me demandes jamais de coller une clé dans le chat : tu me donnes la commande Terminal.
  Si j'en colle une par erreur, tu me dis de la régénérer.
- Tu n'accordes aucune autorisation OAuth, tu ne touches pas à la zone DNS, tu n'achètes rien,
  tu ne publies jamais l'identité d'un tiers sans son accord.
- Rien qui appartienne à quelqu'un d'autre dans un dépôt public : ni vidéo de référence, ni
  image hors licence, ni musique hors licence.
- Une action irréversible ou visible de l'extérieur (publier, supprimer, envoyer), tu la
  confirmes avec moi, sauf si je t'ai dit « go ».

**Les décisions déjà prises sur Boussole, qui valent ici aussi :**

- **Le paiement n'est annoncé nulle part avant la fin du test.** Ni sur l'accueil, ni dans
  le déroulé, ni dans le pied de page, ni dans les publications. C'est la fenêtre de fin de
  test qui porte le prix, le lien des conditions de vente et la case d'acceptation.
- **Jamais le mot « gratuit »** à propos du test ou des résultats. Les articles du guide sont
  en accès libre ; le test se répond librement ; les résultats sont payants. C'est tout.
- **Une seule case** au moment de payer : « J'accepte les conditions de vente et je renonce à
  mon droit de rétractation pour un accès immédiat. » Jamais pré-cochée, sans détail, et aucun
  bouton ne mène au paiement tant qu'elle n'est pas cochée — sur les deux parcours.
- **« Tarif de lancement »** sans prix barré ni pourcentage : une remise ne peut se référer
  qu'à un prix réellement pratiqué pendant 30 jours (art. L112-1-1 du code de la consommation).
- Aucune allégation médicale, aucun diagnostic, aucune prédiction présentée comme un fait.
- Contenus **tutoyés**, bienveillants, non genrés (écriture inclusive discrète : « né·e »,
  ou tournures neutres).

## 3 · Le nom, le domaine, la marque

Si la fiche ne donne pas de nom, propose-m'en cinq, courts, en français, qui disent « se
comprendre par le ciel » sans promettre de prédiction — par exemple sur le modèle « Boussole
émotionnelle » : *Ciel intérieur*, *Boussole céleste*, *Mon ciel du moment*, *Zodiaque
intérieur*, *Constellation intime*. Pour chacun : vérifie que le `.fr` est libre (whois ou
une recherche), et qu'aucune marque identique n'est déposée à l'INPI (`data.inpi.fr`, base
Marques). Donne-moi le tableau, je choisis. Le dépôt de marque se fera au nom de la SAS,
comme pour Boussole : rappelle-le-moi dans la liste des tâches, ne le fais pas.

## 4 · Le site source : ce qu'il contient, ce que tu reprends

Avant d'écrire une ligne, **lis le site source** : `index.html` (4 600 lignes, autonome, sans
dépendance ni build), `merci.html`, `sw.js`, `manifest.webmanifest`, `worker/`, `legal/`,
`guide/anxiete.html` (le gabarit d'article), `guide/style.css`, `A-FAIRE.md`,
`societe/audit-mise-en-marche.md` (72 constats d'audit : tu éviteras les mêmes erreurs),
`PUBLICATION.md`, et les mémoires du projet dans
`~/.claude/projects/-Users-cavalier-Dev-Site-Emotion/memory/` (les pièges rencontrés y sont
écrits — lis-les tous).

**La structure à reproduire, vue par vue** (`index.html` est une application à vues,
`#v-accueil`, `#v-emotions`, `#v-methode`, `#v-perso`, `#v-test`, `#v-resultats`, `#v-rapport`) :

1. **Accueil** : héros, « à quoi ça sert », « l'esprit du test », « le déroulé en quatre
   temps » (découvrir · partir du réel · se projeter · se comprendre), encarts
   confidentialité et « pas un diagnostic », pied de page. **Aucun prix.**
2. **Les 14 émotions** → ici **les 12 énergies** (§ 5) : une carte par énergie, dépliable,
   avec définition, à quoi elle sert, comment elle se manifeste.
3. **La méthode** : la mesure, le parcours, le calcul, les limites assumées, les données,
   « quand consulter ». Ici s'ajoute **une section entière sur ce que l'astrologie est et n'est
   pas dans ce site** (§ 8).
4. **Partir du réel** (`#v-perso`) : le journal. Jusqu'à 5 moments vécus récents, en
   7 questions (le moment et son contexte ; l'activation du corps 1-5 ; les sensations ; les
   mots = 1 à 3 énergies avec intensité 1-4 et une antisèche ; la sûreté du mot 1-3 ; l'élan
   d'action ; le besoin touché, 2 au plus). Les moments comptent dans le résultat et
   **raccourcissent le test** : `max(8, 16 − 2 × moments)` situations. Historique, motifs
   (à partir de 10 entrées sur 90 jours), export/import JSON, effacement — tout en
   `localStorage`, rien n'est envoyé.
5. **Le test** : 16 situations tirées d'une banque de 24, par **rotations** (3 jeux de 16 ;
   chaque situation dans 2 jeux sur 3 ; 8 nouvelles entre deux jeux consécutifs ; au re-test,
   le jeu change). Chaque situation propose **4 à 6 réactions plausibles**, chacune notée sur
   un **spectre de 5 crans en mots** : Pas du tout · Un peu · Moyennement · Beaucoup ·
   Énormément (valeurs 0-4), avec un bouton « tout à “pas du tout” ». Brouillon automatique
   (reprise 7 jours), barre de progression, clavier et lecteur d'écran (radiogroups, flèches).
6. **Les résultats** : une note de 0 à 10 par énergie, le nombre de mesures sur lequel elle
   repose, le classement, la répartition en pourcentage, le radar (ici : **la roue
   zodiacale**, § 6), l'analyse par énergie selon la note, la synthèse croisée, « la couleur
   du moment » (ici « ton ciel du moment »), la comparaison avec un proche par code, le code à
   offrir, la carte à partager (réservée au dossier), l'encart du dossier, le rappel quotidien
   (fichier `.ics`), l'installation en application.
7. **Le dossier** (`#v-rapport`, payant) : couverture, profil en une phrase, sommaire,
   tableau récapitulatif, trois leviers prioritaires, les moments relus, une fiche par énergie
   (mécanisme · dans le corps et la tête · 3 pratiques · point de vigilance · question de
   réflexion), les croisements, le plan de 30 jours en 4 semaines, la page de suivi à J30,
   export PDF par `window.print` (une fiche par page, `@page{margin:14mm 12mm}`, ~20 pages).

**Le calcul**, à reprendre tel quel (`computeScores`) : la note est une **intensité moyenne**
quand l'énergie est là (somme des crans ÷ (4 × nombre de mesures) × 10), **tempérée par la
confiance** : facteur `(mesures / (mesures + K)) / plafond`, avec `K = 3` et `plafond =
scènes / (scènes + K)`, pour qu'une énergie retenue une seule fois à fond ne coiffe pas une
énergie présente partout. Une énergie jamais désignée n'a **pas de note** (« pas mesurée »),
jamais un zéro — et aucune phrase du site ne se bâtit sur une énergie non mesurée (c'est le
bug le plus coûteux que Boussole ait eu : lis `leviers()`, `listeCombos()`, `archetype()`,
`planTrenteJours()` et leurs commentaires). Les « places » (répartition) servent aux
croisements et à la couleur du moment ; les intensités servent aux fiches.

**Les auto-tests** (`runSelfTests()`, affichés en `console.info` à chaque chargement) : tout à
4 → 10/10 ; tout à 1 → 2,5/10 ; jamais désignée → 0 mesure ; une seule mesure ne vaut plus
10/10 ; répartition cohérente ; journal + test court ; couverture des rotations (chaque
énergie ≥ 5 fois par jeu) ; code cadeau refusé comme il faut ; carte réservée au dossier.
Tu les reprends, tu les adaptes, et tu en ajoutes pour tout ce que tu inventes.

**Ce que tu copies tel quel, en changeant seulement les noms :** `sw.js` (cache nommé et
**incrémenté à chaque déploiement**), `manifest.webmanifest`, `worker/` entier (§ 7),
`merci.html`, la structure des trois pages légales, `guide/style.css` comme base, les scripts
`sitemap.py`, `balisage.py`, `controle-textes.py`, `orthographe.swift`, `mesure.py`, et les
trois ateliers de réseaux sociaux (§ 10).

**Ce que tu ne copies pas :** les textes (tous à réécrire), les images (toutes à refaire),
`og.jpg`, les icônes, les 57 articles, les données `EMOTIONS`, `SITUATIONS`, `DOSSIER`,
`QUESTIONS`, les règles d'`archetype` et de `listeCombos`, `Video tiktok/`, `societe/`.

## 5 · Le cœur : la transposition astrologique

### 5.1 · Les 12 énergies, à la place des 14 émotions

Le test mesure **douze énergies**, une par signe. On ne dit pas à la personne « tu es Bélier » :
on mesure **la place que chaque énergie occupe dans sa vie en ce moment**, exactement comme
Boussole mesure la place de chaque émotion. Chaque énergie a un **verbe**, un élément, une
modalité, une planète maîtresse (astrologie classique), des mots-clés, une **lumière** (ce
qu'elle apporte) et une **ombre** (son excès). Le verbe est ce qui s'affiche partout ; le nom
du signe vient après.

| Énergie | Verbe | Élément | Modalité | Maître | Lumière | Ombre |
|---|---|---|---|---|---|---|
| Bélier | **oser** | Feu | cardinal | Mars | élan, courage, franchise | impulsivité, impatience |
| Taureau | **ancrer** | Terre | fixe | Vénus | stabilité, patience, sens du concret | entêtement, inertie |
| Gémeaux | **relier** | Air | mutable | Mercure | curiosité, parole, agilité | dispersion, superficialité |
| Cancer | **protéger** | Eau | cardinal | Lune | tendresse, mémoire, soin | repli, susceptibilité |
| Lion | **rayonner** | Feu | fixe | Soleil | générosité, confiance, chaleur | besoin d'être vu, orgueil |
| Vierge | **affiner** | Terre | mutable | Mercure | précision, service, discernement | perfectionnisme, auto-critique |
| Balance | **équilibrer** | Air | cardinal | Vénus | diplomatie, sens de l'autre, harmonie | indécision, évitement du conflit |
| Scorpion | **transformer** | Eau | fixe | Pluton (et Mars) | intensité, loyauté, profondeur | contrôle, rancune |
| Sagittaire | **explorer** | Feu | mutable | Jupiter | optimisme, sens, liberté | fuite, excès |
| Capricorne | **bâtir** | Terre | cardinal | Saturne | persévérance, responsabilité, structure | rigidité, froideur |
| Verseau | **libérer** | Air | fixe | Uranus (et Saturne) | originalité, idéal, indépendance | détachement, rupture |
| Poissons | **ressentir** | Eau | mutable | Neptune (et Jupiter) | empathie, imagination, intuition | confusion, dilution |

Les textes du site parlent **d'énergies et de verbes** (« l'énergie Bélier, celle d'oser ») :
jamais « les Béliers sont… », jamais une étiquette posée sur une personne.

**Les deux lectures transversales**, qui remplacent le partage agréable/désagréable de
Boussole (il n'y a pas d'énergie « désagréable ») :

- **les 4 éléments** — Feu (agir), Terre (concrétiser), Air (penser et relier), Eau
  (ressentir) : la moyenne des trois énergies de chaque élément donne un **profil élémentaire**
  en quatre nombres, affiché en quatre jauges ;
- **les 3 modalités** — cardinal (lancer), fixe (tenir), mutable (adapter) : même principe,
  trois jauges.

Les leviers du dossier se lisent dessus : **l'énergie la plus présente** (ta force du moment),
**l'énergie la plus en retrait parmi celles mesurées** (ce qui manque peut-être), **l'énergie
dont l'ombre domine** (quand une énergie dépasse 7/10, sa fiche parle d'abord de l'excès). Les
croisements (`listeCombos`, 15 règles) portent sur des paires : Bélier + Capricorne (foncer
et bâtir : le bâtisseur pressé), Cancer + Scorpion (protéger et transformer : la loyauté qui
retient), Gémeaux + Sagittaire (relier et explorer : l'esprit qui ne se pose pas), Vierge +
Balance (affiner et équilibrer : la peur de mal faire), Lion + Poissons (rayonner et
ressentir : l'artiste à fleur de peau), un élément entier absent (« aucune des trois énergies
d'Eau n'a été retenue »), un élément qui écrase les autres… Chaque règle doit exiger que les
énergies concernées aient été **mesurées**.

« Ton ciel du moment » (`archetype`, 9 règles sur le duo dominant + repli sur le profil
élémentaire) donne un titre et une phrase : *Le feu qui bâtit*, *L'eau qui veille*, *L'air
qui cherche*, *La terre qui tient*… — une saison, jamais une identité.

### 5.2 · Le signe de naissance : optionnel, local, après les résultats

Sur la page de résultats, **après** les notes, un encart facultatif : « Et ton signe de
naissance ? ». La personne saisit **jour et mois seulement** (jamais l'année, l'heure ni le
lieu), le signe solaire est calculé **dans le navigateur** avec une table de dates — et, les
dates de passage variant d'un an sur l'autre, un jour limite propose les deux signes et laisse
choisir. Le site affiche alors « ton signe de naissance » à côté de « ton énergie la plus
présente », avec un court texte pour chacun des cas : c'est le même, c'est de la même famille
(même élément ou même modalité), c'est tout autre — toujours sur le ton « voilà une chose à
regarder », jamais « ce qui devait arriver ». Ce choix reste en `localStorage`, n'entre dans
aucun calcul, et n'est jamais envoyé. **Pas de thème astral complet** : pas d'éphémérides, pas
de géolocalisation, pas de donnée de naissance qui quitte l'appareil. Si un jour je veux
l'ascendant, on en reparlera ; ce n'est pas ce projet.

### 5.3 · Le test : 24 situations, à l'aveugle

Tu réécris les **24 situations** sur le même principe que Boussole — des scènes concrètes du
quotidien dans **18 domaines** (travail, famille, couple, amitié, argent, maison, imprévu,
réseaux sociaux, fête, santé, société, souvenirs, courses, calme, réussite, soirée…), deux à
quatre phrases, à la deuxième personne, sans jugement. Pour chacune, **4 à 6 réactions
possibles**, chacune rattachée à une énergie, écrites comme un **comportement concret** et
jamais comme un signe : « Tu prends la parole avant d'avoir fini de réfléchir » (Bélier), « Tu
attends d'avoir tous les éléments avant de bouger » (Vierge), « Tu cherches ce que chacun
ressent autour de la table » (Cancer)… **Le nom de l'énergie n'apparaît pas pendant le test** :
la personne note des comportements, pas des signes, pour ne pas répondre « comme son signe ».
L'association ne se révèle qu'aux résultats.

Contraintes de la banque, comme sur Boussole : environ 125 évaluations au total ; chaque
énergie évaluée **8 à 10 fois** sur les 24 ; dans chaque jeu de 16, chaque énergie **au moins
5 fois** ; les 8 premières situations de chaque jeu couvrent les 12 énergies au moins 2 fois
(plancher quand il y a des moments réels). Recalcule les trois rotations avec un petit script
(recherche gloutonne puis vérification), et un auto-test les contrôle.

**Montre-moi les 24 situations et leurs réactions avant de coder la moindre vue** : j'ai le
dernier mot sur les textes.

### 5.4 · Le journal

Même page, mêmes sept questions, avec « les mots » = 1 à 3 énergies (verbes) et l'antisèche
des douze. Les motifs (contexte dominant, jour de semaine, tendance 14 jours, top 5 sur
30 jours, sensation ↔ énergie dominante, élan et besoin dominants) sont repris à l'identique.

### 5.5 · Les contenus d'analyse

- **Analyse par énergie selon la note** (trois paliers : discrète, présente, dominante), sur
  la page de résultats : douze fois trois textes.
- **Le dossier** : douze fiches (`DOSSIER[id]` = `essence`, `corps` (comment elle se sent,
  comment elle se pense), `exo` × 3 pratiques graduées, `ombre` (point de vigilance — remplace
  l'alerte médicale de Boussole, qui n'a plus lieu ici), plus `QUESTIONS[id]` (une question de
  réflexion par énergie). Soit 36 pratiques. Un plan de 30 jours en quatre semaines :
  observer et nommer ; nourrir l'énergie en retrait ; apaiser l'excès de la dominante quand
  elle dépasse 7 ; ancrer ce qui a marché. Une page de suivi à J30.
- **Longueur visée** : 4 500 à 5 000 mots pour le dossier, comme Boussole (20 pages PDF).

### 5.6 · La carte à partager et la comparaison

- **Carte** (réservée au dossier, promue en fin de page de résultats) : format post 4:5 et
  story 9:16, générée en canvas — la roue zodiacale, le top 3 des énergies, l'élément
  dominant, le nom du site ; précédée d'une courte animation (la roue qui tourne).
- **Comparaison** entre proches sans serveur : un code `CI1-` + 12 caractères (alphabet de
  21 symboles, notes au demi-point), deux profils côte à côte, pourcentage de ressemblance,
  commentaires sur ce qui rapproche et ce qui distingue. Le préfixe est versionné : changer
  l'ordre des énergies plus tard invaliderait les codes, on passerait alors à `CI2-`.

## 6 · La direction artistique

Boussole est crème, sauge et lavande, avec Fraunces et Plus Jakarta Sans, des halos, un grain
de film et des marges botaniques. **Ici, c'est le ciel.** Propose-moi **trois planches** (des
PNG rendus avec PIL, 1 600 × 1 000, montrant l'accueil, une situation du test et la page de
résultats) avant de coder :

1. **Nuit étoilée** — fond encre de nuit (`#0F1424` à `#1A2140`), cartes bleu nuit
   légèrement plus claires, texte ivoire lunaire (`#F2EBDD`), accents or (`#D4B06A`) et cuivre,
   une touche de bleu glacier pour les liens ; constellations en filets fins, étoiles en
   points, un croissant de lune dans le héros ; grain de film discret ; marges fixes aux bords
   de la fenêtre avec des cartes du ciel en filigrane sur écran large.
2. **Aube dorée** — fond ivoire chaud, encre bleu nuit pour le texte, accents or et bleu
   lavande, les mêmes constellations en filets bleu nuit sur fond clair. La plus proche de
   Boussole en lisibilité.
3. **Observatoire** — fond gris-bleu profond, cuivre et vert-de-gris, instruments anciens
   (astrolabe, sextant) en filigrane, plus « cabinet de curiosités ».

Pour les trois : **police de titres** à empattements avec du caractère (Cormorant Garamond,
Fraunces ou Playfair Display, via Google Fonts avec repli local) ; **police de texte** sans
empattement très lisible (Jost, Manrope ou Plus Jakarta Sans) ; rayons `--r-outer: 2rem`,
ombres douces, `--ease: cubic-bezier(.32,.72,0,1)` ; focus visible partout ; contraste AA au
minimum sur tous les textes, **AAA sur le corps** (vérifie-le avec un calcul, pas à l'œil).
Un thème sombre impose deux choses à ne pas oublier : `color-scheme: dark` et un `@media print`
qui **repasse en clair** le dossier PDF (fond blanc, encre noire, or → gris foncé), sinon
l'impression est illisible et vide les cartouches.

**Les illustrations.** Pas de crédits nanobanana disponibles aujourd'hui, et pas de photo de
banque pour les douze signes : **dessine les douze constellations en SVG dans le code**
(coordonnées réelles simplifiées des étoiles principales, filets, étoiles de tailles
proportionnelles à la magnitude), avec le glyphe du signe en dessous. Ce sont les
« vignettes » (`ILLUS`) des douze énergies, la roue des résultats, les cartes à partager et
les icônes. Si un jour on génère des images par IA, l'étiquette « contenu généré par IA » sera
activée sur les plateformes.

**La roue zodiacale** remplace le radar : douze secteurs dans l'ordre classique (Bélier en
haut à gauche, sens antihoraire comme sur un thème, ou sens horaire si plus lisible — choisis
et justifie), chaque secteur rempli proportionnellement à la note, coloré par élément (Feu
rouge-orangé, Terre vert olive, Air bleu clair, Eau bleu profond), les quatre éléments en
légende, l'élément dominant surligné. Elle doit se lire en 2 secondes sur un téléphone.

`og.jpg` (1200 × 630), les icônes 192/512/maskable, le logo Instagram : tu les fabriques en
PIL ou en SVG à partir de la même roue.

## 7 · Ce qui est vendu, et comment

**Identique à Boussole, jusqu'au détail :**

- **Deux formules** à la fin du test : « Tes résultats » 1,99 € et « Résultats + Dossier
  complet » 5,99 € (badge « Tarif de lancement », sans prix barré), et **le complément** à 4 €
  pour qui a payé 1,99 € et veut le dossier (l'encart bascule de lui-même : « Tes 1,99 € sont
  déjà réglés : il ne reste que la différence »). La fenêtre porte aussi la case « Préviens-moi
  quand l'application sort » (consentement jamais pré-coché, transmis à Stripe en
  `client_reference_id`), **la case unique CGV + renonciation**, « J'ai déjà payé », « On m'a
  offert un code », « Revenir au questionnaire ».
- **`VENTE`** dans la configuration : `actif`, `modeTest` (true tant qu'on teste entre amis :
  un bouton « Passer le paiement — version test » débloque tout, et il disparaît quand
  `modeTest` passe à false), prix, liens Stripe, identifiants de prix, `lienComplement`,
  `verification` (l'URL du Worker), `cadeau`.
- **Le Worker Cloudflare** (`worker/verification.js`, `schema.sql`, `wrangler.toml`) : les
  routes `/` (vérifie une référence Stripe : formule selon le montant, seuil dossier à 2,50 €,
  session remboursée refusée), `/mesure` (le compteur d'audience, D1 en région **EEUR**, quatre
  colonnes, événements sur liste blanche : accueil, article, test-debut, test-fin, paywall,
  stripe, promo-carte ; lecture protégée par `MESURE_CLE`), `/cadeau` et `/cadeau/utiliser`
  (le code à offrir). Deux secrets, **posés par moi** : `wrangler secret put MESURE_CLE` et
  `wrangler secret put STRIPE_CLE` (clé Stripe restreinte, lecture des Checkout Sessions et des
  PaymentIntents). Une règle de limitation de débit Cloudflare, 10 requêtes par minute et par
  IP, que je pose aussi.
- **Le code à offrir** : l'achat du dossier ouvre le droit d'engendrer **un** code
  `XX-XXXX-XXXX` (préfixe de deux lettres propre au site, alphabet sans O/0/I/1), valable
  24 heures, utilisable une fois, qui donne **les résultats**, jamais le dossier. Un code perdu
  est perdu. Deux clics pour le créer (le premier annonce, le second fait). Contrainte UNIQUE
  sur la session d'achat.
- **`merci.html`** : lit `formule` et `session_id`, interroge le Worker, n'écrit dans le
  navigateur que ce que le Worker confirme, affiche la référence d'achat avec un bouton
  copier, rappelle l'acceptation des conditions, propose les étapes si l'onglet du test est
  fermé.
- **La carte à partager** n'est ouverte qu'avec le dossier (`carteOuverte`), et promue à la
  fin de la page de résultats (événement `promo-carte`).
- **Stripe** : trois produits, trois liens de paiement avec les URL de retour
  `…/merci.html?formule=resultats|dossier&session_id={CHECKOUT_SESSION_ID}`, « exiger
  l'acceptation des conditions de vente » activé avec l'URL des CGV, collecte de l'e-mail, et
  **la phrase de renonciation en pied de reçu**. Tout ça, c'est moi qui le crée ; toi, tu
  prépares la liste exacte et tu branches les liens quand je te les donne.

**Tant que la vente n'est pas ouverte** (`modeTest: true`, liens de test), le site tourne
« gratuitement » en pratique sans jamais le dire. Le jour J : pages légales SAS, `modeTest`
à false, liens de production, `verification` renseignée, cache du service worker incrémenté,
puis **les onze vérifications** de `A-FAIRE.md` § B7, dont un vrai achat à 1,99 € depuis
Instagram et TikTok sur mon téléphone — que **je** fais.

## 8 · Le ton, et ce que ce site ne dit jamais

**L'astrologie, ici, est un langage de réflexion sur soi, pas une science et pas une
prédiction.** La page méthode le dit en une section claire, la page de résultats le rappelle
en une ligne, les CGV (article « Nature du produit ») l'écrivent : le site propose un contenu
de réflexion et de divertissement, il ne prédit rien, ne conseille aucune décision de vie, de
santé, d'argent ni de relation, et ne remplace aucun professionnel. Rien d'ésotérique dans la
forme : pas de voyance, pas de « les astres ont décidé », pas de prévisions datées, pas de
compatibilité amoureuse chiffrée entre signes de naissance (la comparaison entre proches
compare des **profils mesurés**, pas des signes).

**Le registre** est celui de Boussole : la voix d'un ami qui explique au café, des phrases
complètes avec un sujet et un verbe, une idée par phrase, le concret avant l'abstrait,
jamais une maxime à décoder. Chaque texte se lit à voix haute sans buter. Relis tout au
correcteur (`orthographe.swift`) avant de me montrer.

**Interdits** : « gratuit » ; un prix avant la fin du test ; une étiquette (« tu es… ») ;
une allégation de santé ; une prédiction ; le genre présumé ; les numéros d'urgence dans les
publications réseaux (ils restent sur le site, dans une phrase douce : « si une période te
pèse durablement, en parler à un professionnel est une bonne porte »).

## 9 · Les contenus autour du test

**Le guide** (`guide/`), en accès libre, est ce qui amène le trafic. Même gabarit que
`guide/anxiete.html` : 880 à 1 070 mots, sept `h2`, trois `h3` numérotés (les pratiques), un
encart doux et un encart attention, un appel vers le test (**sans prix**), quatre liens « à
lire aussi », `JSON-LD Article`, `canonical`, `style.css` partagé. **Au lancement, 40 articles
au moins** :

- 12 articles **énergies** (« L'énergie Bélier : oser, et quand ça déborde ») ;
- 4 articles **éléments** et 3 articles **modalités** ;
- 1 page pilier (`guide/index.html`) qui organise tout en familles ;
- 20 articles **situations vécues**, les vraies recherches des gens : « pourquoi je veux tout
  contrôler », « je n'arrive pas à me décider », « j'ai besoin qu'on me voie », « je m'ennuie
  dès que c'est acquis », « je fuis dès que ça devient sérieux », « je dis oui pour ne pas
  déplaire », « je rumine une remarque pendant des jours »… — chacun rattaché à une ou deux
  énergies, avec une pastille « Situation vécue ».

Puis un **sitemap** (`sitemap.py`), `robots.txt`, le balisage (`balisage.py`), les balises de
vérification Search Console et Bing (que **je** pose en me donnant les balises), le `sameAs`
vers les comptes réseaux.

**Les pages légales** (`legal/`) : mentions légales, politique de confidentialité, CGV — la
version SAS dès que les sept champs du Kbis existent (ils sont les mêmes que Boussole :
regarde `societe/site-jour-J/` du site source), avec le médiateur de la consommation. La
politique de confidentialité ajoute **le jour et le mois de naissance**, saisis
facultativement, conservés dans le navigateur seulement.

## 10 · Les publications et les vidéos

Les trois ateliers de Boussole se copient et se transposent :

- **`reseaux-sociaux/`** (fiches : texte et pictogrammes, 5 diapositives), **`reseaux-
  sociaux-illustre/`** (personnages dessinés, 30 carrousels, prompts nanobanana — ces
  illustrations demandent des crédits, à prévoir) et **`reseaux-sociaux-bd/`** (scènes vécues
  en BD, 30 carrousels) ; puis `publication/` qui fusionne tout en semaines de six publications,
  sans jamais deux fois le même genre deux jours de suite. Lis `PUBLICATION.md` et
  `reseaux-sociaux-illustre/GUIDE-STYLE.md` du site source : la méthode, les gabarits et les
  pièges y sont. Pour ce site, l'univers des carrousels est céleste : fonds nuit, or,
  constellations — pas de personnages « pub santé ».
- **Les vidéos** : un prompt complet existe déjà,
  `/Users/cavalier/Dev/Site Emotion/reseaux-sociaux-video/PROMPT-POUR-UN-AUTRE-PROJET.md`.
  Tu le liras le moment venu ; il décrit un atelier qui rend vingt vidéos de 45 secondes en
  4:3, mots au rythme d'une voix off, images qui bougent, transitions, page de fin. Les images
  seront des ciels, des nuits, des aurores, des nébuleuses, des instruments anciens — jamais un
  humain.

Les publications et les vidéos viennent **après** le site : étape 7 du § 12.

## 11 · La technique, exactement

- **Un seul fichier** `index.html`, HTML + CSS + JS en ligne, aucune dépendance obligatoire
  (Google Fonts avec repli), aucun build, hébergé sur **GitHub Pages** avec `CNAME`. Boussole
  pèse 554 Ko (300 Ko transférés) : reste sous ce poids ; ne mets pas d'image en base64 dans
  le `<style>` (ça bloque le premier affichage).
- **PWA** : `manifest.webmanifest` (`display: standalone`, icônes 192/512/maskable), `sw.js`
  réseau d'abord avec un cache nommé `<projet>-v1` **incrémenté à chaque déploiement** ; le
  service worker n'est enregistré qu'en https.
- **Stockage** : tout en `localStorage` sous des clés préfixées (`<projet>.journal.v1`,
  `<projet>.brouillon.v1`, l'accès acheté, le signe de naissance), chaque accès dans un
  `try/catch`, un bandeau si le stockage est indisponible. Validation stricte à l'import JSON
  (identifiants connus, intensités 1-4, listes filtrées) et échappement `esc()` de toute valeur
  affichée : Boussole a eu une faille XSS par le journal importé.
- **Accessibilité** : `[hidden]{display:none !important}` global (un `display:flex` écrasait
  `hidden` sur Boussole), focus visible, radiogroups au clavier, `aria-pressed`, Échap ferme
  les fenêtres, les fenêtres modales sont déplacées dans `body` au chargement (sinon le
  contexte d'empilement de `main` les passe sous la navigation), `prefers-reduced-motion`.
- **Balisage** : `title`, `description`, `canonical`, Open Graph, `JSON-LD WebApplication`
  avec `isAccessibleForFree: false` et les deux offres, `Organization` avec `sameAs`.
- **Mesure** : `mesurer("accueil"|"test-debut"|"test-fin"|"paywall"|"stripe"|"promo-carte")`
  et `article` sur les pages du guide, vers le Worker ; `mesure.py` lit l'entonnoir.
- **Déploiement** : `git push` suffit (GitHub Pages). Après chaque déploiement, vérifie en
  ligne avec un marqueur unique (la version du cache), pas avec un `grep` qui peut matcher une
  vieille règle.
- **Hors dépôt** (`.gitignore`) : `societe/`, les images générées, les vidéos, `.cache/`, les
  musiques, et bien sûr les clés.

## 12 · La méthode, dans l'ordre, avec les points d'arrêt

1. **Lis** le site source et ses mémoires. Pose-moi tes quatre questions au plus, en une fois.
2. **Le nom et la DA** : le tableau des noms et domaines (§ 3), puis les trois planches
   (§ 6). ⏸ *J'attends ton choix.*
3. **Les données** : les 12 énergies (fiches complètes), les 24 situations avec leurs
   réactions, les rotations, les 15 croisements, les 9 ciels du moment, les 36 pratiques, les
   12 questions — dans un fichier de travail lisible, relu au correcteur. ⏸ *Je relis tout.*
4. **Le site** : `index.html` complet avec les sept vues, le calcul, les auto-tests, le
   paywall en mode test, `merci.html`, `sw.js`, le manifeste, les icônes, `og.jpg` ; le Worker
   prêt à déployer ; les trois pages légales (version « éditeur non professionnel, aucune
   vente » tant que la SAS n'existe pas — comme Boussole aujourd'hui, et la version SAS prête
   dans `societe/site-jour-J/`). Tu me donnes une adresse locale pour tester, puis tu publies
   sur GitHub Pages. ⏸ *Je teste sur mon téléphone.*
5. **Le guide** : les 40 articles, la page pilier, le sitemap, le balisage. ⏸ *Je lis cinq
   articles au hasard.*
6. **Le Worker** : je crée le Worker et la base D1 (EEUR) si ce n'est pas le même compte, je
   pose les secrets, tu déploies le code et tu vérifies de bout en bout (référence inventée
   refusée, événement inconnu ignoré, lecture sans clé refusée, compteur remis à zéro après tes
   essais).
7. **Les publications et les vidéos** (§ 10), selon le même mode d'emploi que Boussole.
8. **La liste des tâches** `A-FAIRE.md`, tenue à jour en permanence sur le modèle de celle de
   Boussole : ce qui est fait, ce qui m'attend (Kbis, médiateur, Stripe, clés, comptes
   réseaux, test réel), et ce qu'il faut savoir qui ne se corrige pas (le dossier payant est
   dans la page : le verrou cache, il n'empêche pas).

À chaque livraison : **ce que tu as fait, ce que tu as vérifié et comment, ce qui reste, ce
que je dois regarder.** Fais court. Ne me demande jamais de « confirmer que c'est bon » sans
m'avoir donné quelque chose à regarder.

## 13 · Ce que je sais déjà et que tu n'as pas à me réexpliquer

- Le Kbis ne bloque que la vente, jamais l'audience : on publie avant de vendre.
- Un site sans serveur ne peut pas protéger techniquement un contenu payant ; à 5,99 €, c'est
  une décision commerciale, pas un défaut.
- Les navigateurs intégrés d'Instagram et TikTok isolent leur stockage : le parcours de
  paiement se teste depuis les deux applications, sur un vrai téléphone, avant la première
  publication.
- Donner l'adresse plutôt que le nom : un nom commun à plusieurs sites ne sort pas sur Google
  avant des mois.
