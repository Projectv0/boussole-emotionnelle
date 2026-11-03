# Ce que tu as à faire

*État au 3 novembre 2026. La SAS existe depuis le 2 novembre. Le bloc A est clos — il ne
reste qu'à configurer TikTok et à publier. Le bloc B avance : Kbis reçu.*

Tout ce qui pouvait être fait dans le dépôt l'est. Ce qui reste demande un compte tiers,
une identité, de l'argent ou un arbitrage — donc toi. Ce document ne liste que ça.

Trois blocs indépendants, dans l'ordre de ce qui rapporte le plus vite :

- **A. Se rendre visible** — clos, sauf une chose : configurer TikTok, puis publier.
- **B. Pouvoir vendre** — la société existe ; restent le médiateur, la TVA, Stripe et la clé.
- **C. Finir les images** — bloqué par les crédits. ~10 €.
- **D. Les vingt vidéos** — prêtes à publier.

Le site ne vend rien aujourd'hui (`modeTest: true`, liens Stripe de test) : rien n'est en
train de mal tourner. Le bloc B est à faire **avant** de basculer, pas en urgence.

**Ce qui est gratuit, exactement.** À dire juste partout, y compris dans les bios et les
dépôts d'annuaire : **le guide de 57 articles est en accès libre**, et le test se répond
librement — mais **aucun résultat ne s'affiche sans payer**, pas même les trois émotions
dominantes, à partir de 1,99 €. Écrire « test gratuit » quelque part serait faux, et c'est
précisément le schéma qui produit le plus de réclamations : quelqu'un passe dix à quinze
minutes sur seize situations, puis découvre le prix. *Ta décision, confirmée le 13 octobre :
le paiement n'est annoncé nulle part avant la fin du test (le point 2.4 de l'audit est
écarté). Le prix, le lien des CGV et la case de renonciation vivent donc dans la fenêtre de
paiement, au moment où la personne décide.*

**Le Kbis ne bloque que la vente, jamais l'audience.** C'est la distinction qui décide du
calendrier : tout le bloc A — publier, mesurer, se rendre visible — se fait sans lui. Et
comme une audience met des semaines à se construire, ce sont précisément les semaines
d'attente du Kbis. Publier maintenant, c'est arriver au jour de la mise en vente avec des
gens qui lisent déjà ; attendre, c'est ouvrir une boutique dans une rue vide.

---

# A — Se rendre visible

*Aucune dépendance. C'est le bloc le plus rentable et le seul qui soit entièrement entre tes
mains dès maintenant.*

## ~~A1 · Search Console~~ — ✅ fait le 21 septembre 2026

Propriété à préfixe d'URL `https://boussole-emotionnelle.fr/`, validée par balise HTML —
la zone DNS chez IONOS n'a pas été touchée. La balise est dans le `<head>` d'`index.html` :
**ne la retire jamais**, Google revérifie périodiquement et la propriété se perd avec elle.

`sitemap.xml` envoyé, **59 URL lues, « Opération effectuée »**. Réexploration demandée pour
`/guide/`, dont la refonte en six sections date du 19 septembre.

Ce qu'on sait déjà : l'accueil et `/guide/` **sont indexés**. Le rapport d'indexation complet
affiche encore « traitement des données en cours » — il faut environ 24 h après validation.

> Le compte propriétaire n'est **pas** `mcavalier2011@gmail.com`, qui était connecté en
> premier dans Chrome. Une propriété non validée traîne sous ce compte-là ; sans effet, à
> supprimer un jour où tu passes par là.

## ~~A2 · Bing Webmaster Tools~~ — ✅ fait le 21 septembre 2026

Site ajouté **manuellement** et validé par balise méta, sur le compte `odem-app`. Le
sitemap est soumis, statut « Traitement », 0 erreur. Bing alimente aussi DuckDuckGo et
Ecosia, où la concurrence est bien plus faible que sur Google.

Deux voies ont été écartées, volontairement :

- **l'import depuis Google Search Console**, qui aurait accordé à Microsoft un accès en
  lecture au Search Console du site ;
- **la vérification DNS automatique**, que Bing recommandait en première position : il
  avait détecté que le domaine est chez IONOS et proposait de s'y connecter pour poser un
  CNAME. On ne donne pas à Microsoft la zone DNS du domaine pour un service de
  statistiques.

La balise `msvalidate.01` est dans le `<head>` d'`index.html`, à côté de celle de Google.
**Ne les retire ni l'une ni l'autre** : les deux services revérifient périodiquement.

## ~~A3 · La redirection `contact@`~~ — ✅ vérifiée le 21 septembre 2026

**La réception marche.** Six messages adressés à `contact@boussole-emotionnelle.fr` sont
bien dans la boîte `contact@odem-app.com`, le plus récent aujourd'hui à 19 h 01. Ce n'est
pas un test : c'est de la livraison réelle, déjà arrivée. Les MX des deux domaines pointent
chez IONOS, avec SPF et DMARC déclarés.

**Mais on ne peut pas répondre depuis cette adresse.** La boîte n'a qu'une seule identité
d'expéditeur — `contact@odem-app.com`, au nom d'affichage « Jimmy Blettner ». Aucun alias,
et le champ « Répondre à » est vide.

Le scénario que ça produit, et il arrivera : un client écrit à l'adresse du site parce qu'il
a payé et n'a rien reçu. Il reçoit une réponse de **« Jimmy Blettner » via un domaine qu'il
n'a jamais vu**, au sujet de son argent. Une partie classera ça en hameçonnage ; ceux qui
doutent demanderont un remboursement plutôt que de répondre.

Deux corrections possibles, toutes deux dans ton espace IONOS — je ne m'y connecte pas :

1. **La bonne** : ajouter `contact@boussole-emotionnelle.fr` comme adresse d'expéditeur sur
   cette boîte, si la formule IONOS le permet. La réponse part alors de l'adresse du site.
2. **La gratuite, en attendant** : renseigner « Répondre à » avec
   `contact@boussole-emotionnelle.fr` et remplacer le nom d'affichage par « Boussole
   émotionnelle ». L'expéditeur reste `odem-app.com`, mais le nom et l'adresse de réponse
   cessent de contredire le site. À décider avec Jimmy : c'est sa boîte.

## A4 · Les deux comptes réseaux — Instagram ✅, **TikTok à finir**

Instagram et TikTok existent. Les 99 publications de `publication/` sont prêtes : six par
semaine, du lundi au samedi, sur 17 semaines, sans jamais deux fois le même genre deux
jours de suite. Le mode d'emploi d'une journée tient en deux minutes :
`publication/LISEZMOI.md`.

### Ce qui reste à faire une fois, sur les comptes

- **Lien en bio** sur les deux : `https://boussole-emotionnelle.fr` — toutes les légendes y
  renvoient, et aucune ne peut être cliquable dans le texte.
- **Compte professionnel ou créateur** des deux côtés : c'est ce qui ouvre les statistiques.
- **Heures** : 12 h-13 h ou 19 h-21 h. La régularité compte plus que l'heure parfaite.
- **Les trente premières minutes** : répondre aux commentaires. C'est le signal
  d'engagement le plus fort sur les deux plateformes.

### Instagram — configuré le 23 septembre 2026

`instagram.com/boussole.emotionnelle` · nom affiché « Boussole Émotionnelle » · photo de
profil posée · bio de 140 caractères. Le pseudo généré `contact9393` a été remplacé pendant
que le compte était encore à zéro publication : plus tard, ça aurait cassé des liens.

Le site est branché : `sameAs` dans le balisage `Organization` de l'accueil, et lien en pied
de page sur les 59 pages.

**Il reste une chose, et elle ne se fait que depuis le téléphone.** Instagram n'autorise la
modification des liens que dans son application : *Modifier le profil → Liens →*
`https://boussole-emotionnelle.fr`. Sans ça, la flèche de la bio ne désigne rien, et les 99
publications n'ont aucun chemin vers le site.

### TikTok — à finir depuis le téléphone

Le compte existe, sous le pseudo généré `user4327198114255`. **Je n'ai pas pu le configurer
depuis le navigateur** : après quelques tentatives, TikTok a cessé d'ouvrir sa fenêtre
d'édition — une protection contre l'automatisation, vraisemblablement. Les réglages du
compte, eux, répondaient normalement.

De toute façon le téléphone est le bon endroit, pour une raison qui compte : **le formulaire
web de TikTok n'a aucun champ de site web.** TikTok le réserve aux comptes professionnels.

Dans l'application, *Modifier le profil* :

| Champ | Valeur |
|---|---|
| **Nom d'utilisateur** | `boussole.emotionnelle` — vérifié libre sur TikTok, et identique à Instagram |
| **Nom** | `Boussole Émotionnelle` |
| **Bio** (80 car. max) | `Des scènes qu'on reconnaît, et un guide libre : boussole-emotionnelle.fr` — 72 caractères |
| **Photo** | `logo-instagram.png`, le même fichier que sur Instagram |

**Bascule d'abord le compte en professionnel** (*Paramètres → Gérer le compte → Passer à un
compte professionnel*). C'est gratuit et ça débloque le champ de site web — sans quoi aucun
lien cliquable n'existe sur TikTok.

> **À ne pas confondre avec « Vérification de l'entreprise »**, qui figure juste à côté dans
> les réglages TikTok. Celle-là demande des pièces justificatives et attend donc ton Kbis.
> Le passage en compte professionnel, lui, est un simple basculement : ni document, ni SIREN,
> ni vérification. Si l'application te réclame malgré tout une pièce, dis-le-moi — ça voudra
> dire que TikTok a changé son parcours, et on s'adaptera.

> À savoir : les légendes des 99 publications disent « (lien en bio) ». Sur TikTok, cette
> phrase est fausse tant que le compte n'est pas professionnel et le lien posé. C'est
> pourquoi la bio ci-dessus écrit l'adresse en toutes lettres : elle reste vraie dans les
> deux cas.

**Ensuite, donne-moi l'adresse du profil** et je l'ajoute au `sameAs` et aux pieds de page,
comme Instagram.

**Et, dans Search Console**, tu peux maintenant rattacher Instagram et TikTok comme
« comptes de plate-forme » : tu verras dans un même tableau ce qui vient du site et ce qui
vient des réseaux. Ça passe par une autorisation que tu accordes toi-même.

## ~~A5 · Mesure d'audience~~ — ✅ en service depuis le 23 septembre 2026

Worker déployé sur `boussole.projectv0-0.workers.dev`, base D1 « boussole » créée en région
**EEUR — donc dans l'Union européenne**, ce que la politique de confidentialité annonçait
déjà. Les 59 pages envoient leurs repères : la mesure tourne.

Vérifié de bout en bout sur le site réel avant de te le dire : une visite d'article, une
visite d'accueil et un clic sur « Commencer le test » sont bien arrivés dans la base, avec
le bon chemin de page. Un événement inventé et une requête venue d'une autre origine
n'écrivent rien. La lecture sans clé renvoie 403. Le compteur a ensuite été remis à zéro —
il ne contient aucune de mes visites d'essai.

### Lire les chiffres

`MESURE_CLE` est posée. Ouvre :

```
https://boussole.projectv0-0.workers.dev/mesure?cle=TON_MOT_DE_PASSE&jours=30
```

Enregistre la réponse dans un fichier, puis `python3 mesure.py chiffres.json` — tu obtiens
l'entonnoir, les pages les plus lues et les quatorze derniers jours. Le compteur tourne
depuis le 23 septembre : laisse-lui une semaine avant d'y chercher du sens.

### À faire aussi, quand tu passeras sur Cloudflare

Une **règle de limitation de débit** sur la route du Worker — 10 requêtes par minute et par
IP. Elle protège le compteur d'un gonflage à la main, et elle sera de toute façon nécessaire
pour la vérification d'achat.

---

## ~~A6 · Les liens entrants~~ — ❌ abandonné le 24 septembre 2026

**Ta décision, et elle est la bonne : on ne démarche personne.** Tu n'as pas de réseau à
mobiliser aujourd'hui, et sans réseau, demander un lien ne donne rien — personne ne renvoie
vers un test payant d'un inconnu. Les seuls qui accepteraient sont les annuaires qui acceptent
tout le monde, et c'est exactement pourquoi ils ne valent rien.

**Il n'y a donc rien à faire ici.** Ce n'est pas un abandon par négligence : ton site se fera
trouver par trois chemins qui ne demandent l'accord de personne.

1. **Publier.** Les 99 publications produisent ce qui compte le plus — des gens qui tapent
   « boussole émotionnelle » dans la barre de recherche, et des visites directes. C'est ton
   canal. Il n'attend que TikTok (A4).
2. **Le guide, en longue traîne.** Les 57 articles ne visent pas le nom du site, disputé par
   quatre sites installés, mais « pourquoi je suis toujours fatigué malgré le sommeil »,
   « la jalousie dans le couple ». Sur ces phrases-là, un bon article peut sortir **sans aucun
   lien entrant**. C'est lent, c'est déjà lancé.
3. **La carte à partager et les codes de comparaison.** Chaque image emporte l'adresse du site,
   et comparer son profil suppose d'envoyer son code à quelqu'un. Le bouche-à-oreille est dans
   le produit.

### Une consigne pratique, elle, qui reste valable

**Donne l'adresse, pas le nom.** `boussole-emotionnelle.fr` sort premier immédiatement ;
« boussole émotionnelle » ne sortira pas avant des mois — l'expression est déjà employée par
pauldevaux.fr, emotioncompass.org, ecolepositive.fr, macoherence.com, installés depuis des
années. C'est une contrainte permanente, pas un retard de démarrage. Dis l'adresse aux gens à
qui tu en parles, ton associé compris.

### Deux choses à ne pas oublier plus tard

**Revérifier l'indexation en novembre.** Le 23 septembre, 5 pages sur 59 étaient indexées.
Ce n'est pas un manque de liens, c'est un site de trois semaines que Google découvre lentement.
Si le compte n'a pas bougé d'ici novembre, on regardera pourquoi — mais il aura bougé.

**Si un jour la situation change** — tu rencontres un psy, un coach, quelqu'un dans une
association, ou la presse locale s'intéresse à la société une fois créée — dis-le-moi : ce
sont les deux seuls cas où une demande aurait du sens, et elle porterait sur **le guide
gratuit**, jamais sur le test payant. Ce n'est pas une tâche, c'est une porte laissée ouverte.

### Ce qu'il ne faut pas faire, si on t'en parle

- **Acheter des liens.** Google les repère, et la sanction porte sur le site, pas sur le vendeur.
- **Les annuaires génériques à la chaîne.** Sans effet, et certains font activement du mal.
- **Poster le lien dans des forums.** C'est de l'autopromotion, ça se fait supprimer, et ça
  abîme le nom du projet — le seul actif que tu aies pour l'instant.

---

# B — Pouvoir vendre

*L'ordre compte : chaque étape débloque la suivante. C'est plusieurs semaines, l'essentiel
étant l'attente du Kbis.*

## B1 · Les dix décisions, avec Jimmy

Tout part de là. Le document est écrit et prêt à remplir : **`societe/1-decisions-a-prendre.md`**.
Dix cases à cocher, une soirée à deux. Les trois qui pèsent le plus :

- **la répartition du capital** (le 50/50 est confortable et juridiquement dangereux) ;
- **la cession de la propriété intellectuelle à la société** — aujourd'hui le site, le code,
  les contenus, le domaine et les 99 carrousels t'appartiennent personnellement ; sans cession
  formalisée, la SAS vendrait un produit qu'elle ne possède pas ;
- **le budget réel** : ~250 € pour créer, puis 1 000 à 1 800 €/an de frais fixes. Ça
  représente environ 150 dossiers vendus par an, juste pour équilibrer. À valider les yeux
  ouverts, avant et pas après.

Dès que les dix cases sont cochées, je mets à jour les statuts et le pacte (documents 2 et 3,
déjà rédigés) avec vos choix.

## ~~B2 · Immatriculer, et me donner sept champs~~ — ✅ Kbis reçu le 3 novembre 2026

**BC LABS**, société par actions simplifiée au capital de 1 000 €, RCS Paris 130 916 968,
immatriculée le 2 novembre 2026, siège 8 rue Abel, 75012 Paris (domiciliation), président
Martial Cavalier — directeur de la publication, donc. Le SIREN est confirmé dans le registre
national (annuaire des entreprises). L'extrait est rangé dans `societe/` (privé, hors dépôt) :
il porte des dates de naissance et des adresses personnelles, il ne doit jamais être commité.

Les trois pages légales en ligne portent maintenant cette identité (mentions légales, CGV,
confidentialité). **La TVA est tranchée** (options fiscales de l'immatriculation, relues le 3 novembre) : la
société est **assujettie, au réel simplifié**, sans option pour les déclarations trimestrielles.
Le numéro intracommunautaire **FR50 130 916 968** est dans les pages légales. Voir B2 bis pour
ce que ça change.

**Le téléphone est en ligne** (06 59 88 56 55, donné le 3 novembre). Les trois pages
légales version SAS sont **publiées** : mentions légales, conditions de vente, confidentialité.
Il ne reste, dans les CGV, que le crochet du médiateur (B3).

## B2 bis · La TVA, concrètement

Être au réel simplifié veut dire que **chaque vente contient 20 % de TVA**, à reverser :

| Prix affiché (TTC) | TVA incluse | Ce qui reste à la société |
|---|---|---|
| 1,99 € | 0,33 € | 1,66 € |
| 5,99 € | 1,00 € | 4,99 € |
| 4,00 € (complément) | 0,67 € | 3,33 € |

Ce que ça demande :

- **Dans Stripe** (à créer en même temps que les produits, B5) : les prix sont saisis
  **TVA incluse** ; dans *Paramètres → Informations fiscales*, ajoute le numéro FR50 130 916 968
  pour qu'il figure sur les reçus. Tant que les ventes à des particuliers d'autres pays de l'UE
  restent sous 10 000 € par an, c'est la TVA française qui s'applique à tout le monde : pas
  besoin de Stripe Tax au départ.
- **Les déclarations** : une déclaration annuelle (CA12) dans les trois mois qui suivent la
  clôture du 30 septembre, et deux acomptes (juillet, décembre) — dispensés si la TVA de
  l'année précédente est inférieure à 1 000 €, ce qui sera le cas au début. Ton comptable sait
  faire.
- **À savoir** : à 1,99 € la vente, la TVA pèse un sixième du chiffre. La franchise en base
  (pas de TVA sous 37 500 € de chiffre d'affaires) aurait été plus avantageuse pour ce site,
  et elle reste possible plus tard : le choix du réel vaut pour deux ans (2026 et 2027), on
  peut y renoncer pour 2028 par courrier au service des impôts. À voir avec ton comptable le
  moment venu — ce n'est pas urgent, et ça dépend des autres activités de la société.

## B3 · Adhérer à un médiateur de la consommation

**Obligation légale** pour tout professionnel vendant à des consommateurs (article L612-1 du
code de la consommation). Quelques dizaines d'euros par an. Organismes agréés : CM2C, Medicys,
AME Conso.

Ça ne s'improvise pas le jour d'une réclamation : compte plusieurs jours à quelques semaines
d'adhésion. **Lance-le en parallèle du dossier d'immatriculation**, pas après.

Je t'attends sur : nom du médiateur, adresse postale, URL. Ces trois éléments doivent figurer
dans les CGV et les mentions légales, où le crochet `[nom et coordonnées du médiateur adhéré]`
attend encore d'être rempli.

## ~~B4 · Trancher le prix barré~~ — ✅ tranché et appliqué le 13 octobre 2026

**« Tarif de lancement, 5,99 € »**, sans prix barré ni pourcentage : c'est en ligne, sur la
fenêtre de paiement, sur l'encart du dossier de la page de résultats et dans les CGV.

La règle, pour mémoire (art. L112-1-1 du code de la consommation, DGCCRF) : une remise ne
peut s'annoncer que par rapport au **prix le plus bas réellement pratiqué pendant les
30 jours précédents**, pour tous les clients. Le dossier n'ayant jamais été vendu 20 €,
« 5,99 € au lieu de 20 € » était un faux rabais — sanction : pratique commerciale trompeuse.

**Si un jour tu veux une vraie promotion** : vends le dossier à son prix normal pendant au
moins trente jours, puis annonce la remise par rapport à ce prix. Il suffira de renseigner
`prixDossierRef` et `remiseDossier` dans `VENTE` : le prix barré et le badge reviennent seuls.

## ~~B5 · Le compte Stripe de la SAS, en production~~ — ✅ fait le 3 novembre 2026

**Le compte Stripe est celui de BC LABS**, activé le 3 novembre (profil de l'entreprise,
représentant, associé, compte bancaire, double authentification). BC LABS est le nom global
du compte : c'est lui que les clients voient sur la page de paiement, les reçus et leurs
relevés bancaires (libellé « BC LABS »), pour ce site comme pour les suivants. Les
informations publiques portent l'e-mail de contact, le téléphone, et les adresses des
conditions de vente et de la politique de confidentialité.

**Trois produits et trois liens de paiement, en production**, chacun nommé « Boussole
émotionnelle · … » pour être reconnu au premier coup d'œil dans Stripe, avec l'acceptation
des conditions de vente exigée avant de payer et le retour vers `merci.html` :

| Formule | Prix | Identifiant de prix | Retour |
|---|---|---|---|
| Tes résultats | 1,99 € | `price_1UXoEu3FK7OJuB9z7THgWoiu` | `formule=resultats` |
| Résultats + Dossier complet | 5,99 € | `price_1UXoGg3FK7OJuB9zceZSTOOy` | `formule=dossier` |
| Complément | 4 € | `price_1UXoHE3FK7OJuB9zD8HCaeQ2` | `formule=dossier` |

Les trois liens et les trois identifiants sont dans `VENTE`. **Comment les paiements de la
Boussole sont identifiés dans un compte partagé entre plusieurs sites :** par le nom des
produits (chaque paiement affiche « Boussole émotionnelle · … » dans Stripe, les reçus et les
exports), et par le Worker, qui ne débloque la Boussole que pour ces trois identifiants de
prix — un achat fait sur un autre site de la société, même du même montant, n'ouvre rien ici.
Ce qui n'est **pas** distinct par site : le libellé sur le relevé bancaire du client, « BC LABS »
pour tout le compte. Si un jour tu veux un libellé par site, c'est un compte Stripe par site.

**Les trois liens de test** (dossier à 5,99 €, complément à 4 €, résultats) existent
toujours dans l'environnement de test, pour rejouer le parcours sans payer.

**Ce que Stripe ne permet pas :** une phrase de renonciation en pied de reçu. En échange,
Stripe enregistre lui-même, horodaté, l'acceptation des conditions de vente que le client
coche avant de payer — c'est la preuve qui compte.

## B5 bis · Activer le compte Stripe — j'ai fait la moitié, il te reste quatre écrans

**Fait le 3 novembre 2026, dans ton Chrome, sur le parcours « Activez votre compte »** —
Stripe enregistre chaque étape, rien n'est à refaire :

- type d'entreprise : Société · structure « Société non cotée » (c'est la case des SAS) ;
- informations sur l'entreprise : BC LABS, nom commercial « Boussole émotionnelle », SIREN,
  TVA FR50130916968, siège 8 rue Abel 75012 Paris, téléphone, site ;
- représentant du compte : toi, président, avec les éléments du Kbis ;
- produits : catégorie « Autres biens numériques », description des formules ;
- service client : le 06 59 88 56 55, affiché sur les reçus ;
- libellé de relevé bancaire : **BOUSSOLE EMOTIONNELLE**, abrégé **BOUSSOLE**.

**Avancement au 3 novembre au soir** : le compte bancaire, le SMS et la double
authentification sont faits ; j'ai décliné les étapes facultatives (calcul des taxes par
Stripe — inutile, TVA française à 20 % pour tous — et contribution Climate). **Le
récapitulatif est complet sauf une section**, et Stripe refuse l'envoi tant qu'elle ne l'est pas :

1. **« Gestion et propriété » → la fiche de ton associé est marquée « Incomplet ».** Il manque
   sa date de naissance et son adresse (sur le Kbis, dans `societe/`). Je ne saisis pas
   l'identité d'un tiers : c'est à toi, avec son accord, ou à lui. Bouton *Modifier* sur sa ligne.
2. **« Accepter et envoyer »**, en bas du récapitulatif : c'est l'acceptation du contrat
   Stripe au nom de BC LABS — toi aussi. Stripe pourra ensuite demander une pièce d'identité.

L'onglet est resté ouvert dans ton Chrome sur le récapitulatif.

Une fois le compte actif, dis-le-moi : je crée les trois produits et les trois liens en
production, je pose l'URL des CGV dans les informations publiques (ce qui débloque l'option
« exiger l'acceptation » sur les liens), le numéro de TVA sur les reçus, et je bascule le site.

## B6 · La clé Stripe du Worker — tout est prêt, il reste deux gestes à toi

**Le Worker est déployé** (`boussole.projectv0-0.workers.dev`), avec le code de vérification
d'achat et, depuis le 3 novembre, **sa propre limitation de débit** : dix demandes par minute et
par adresse sur la vérification d'achat et les codes à offrir, soixante sur la mesure d'audience
(`ratelimits` dans `wrangler.jsonc`). Plus rien à poser dans le tableau de bord Cloudflare. La
limite est approximative, comme Cloudflare l'annonce — un flot est coupé après une quinzaine de
demandes rapides, pas pile à la dixième — et c'est suffisant : on ne peut ni essayer des codes en
masse, ni faire interroger Stripe en boucle.

Il ne manque que la clé, et je ne peux pas la générer ni la manipuler à ta place : c'est un
identifiant secret de ton compte de paiement. Tout est préparé pour que ça te prenne une minute :

1. Dans ton Chrome, la page **« Créer une clé API limitée »** est ouverte, nom et permissions
   déjà remplis : **Checkout Sessions (lecture)**, **PaymentIntents (lecture)** et **Charges
   (lecture)**. Les deux dernières sont indispensables : sans elles, une session remboursée ou
   contestée resterait valable indéfiniment, sur autant d'appareils que la personne veut — le
   remboursement coûterait le prix **et** le produit. Clique **« Créer une clé »** en bas, puis
   **copie la clé** affichée (elle ne s'affiche qu'une fois).
2. Dans le Terminal, l'onglet « clé Stripe du Worker » attend sur `Enter a secret value:` —
   **colle la clé, Entrée**. Rien ne s'affiche pendant la frappe, c'est normal. Si l'onglet a été
   fermé, relance depuis `worker/` :

   ```bash
   npx wrangler secret put STRIPE_CLE
   ```

   Je ne vois jamais la valeur. Si la page Stripe a été fermée : Développeurs → Clés API →
   « Créer une clé limitée », mêmes trois permissions en lecture.

Ensuite je renseigne `VENTE.verification` dans le site et je passe `modeTest` à faux — et **deux
choses s'allument d'un coup** : la vérification d'achat, et le code à offrir (B6 bis). À partir de
là, un paiement de test n'ouvre plus rien : la clé est de production, elle ne connaît que les vrais
paiements. Le premier essai sera donc un vrai achat à 1,99 € (B7), que tu te rembourses ensuite
depuis Stripe si tu veux — et le remboursement doit alors **fermer** l'accès : c'est le test.

## B6 bis · Le code à offrir — prêt, en sommeil

Fait le 24 septembre 2026, et **déjà en ligne côté serveur**. Acheter le dossier ouvre le
droit d'offrir le test à une personne : un code unique, valable vingt-quatre heures à partir
du moment où l'acheteur le crée, utilisable une seule fois, qui donne **les résultats** —
jamais le dossier.

Le Worker vérifie auprès de Stripe que le dossier a bien été payé avant d'engendrer quoi que
ce soit. Donc, très concrètement : **tant que `STRIPE_CLE` n'est pas posée, aucun code ne peut
exister**, et le site n'en propose aucun — ni le bouton sur la page de résultats, ni le lien
« On m'a offert un code » dans la fenêtre de paiement. Rien à faire de ton côté : la même
ligne `VENTE.verification` allume les deux.

**Un code perdu est perdu** — ta décision du 24 septembre. Passé les vingt-quatre heures,
qu'il ait servi ou non, l'achat n'en ouvre pas d'autre. Comme c'est irréversible, la carte le
dit **avant** le clic, et le bouton demande une confirmation : le premier clic annonce ce qui
va se passer, le second le fait.

La règle de limitation de débit du point 3 ci-dessus devient plus importante avec cette
fonction : elle est ce qui empêche d'essayer des codes en masse.

## B7 · Le test réel, avant d'annoncer quoi que ce soit

Une fois que j'ai basculé le site, à faire **dans l'ordre**, en production :

1. Le pied de page mène aux CGV, et les CGV portent le nom réel de la société.
2. Les boutons de paiement sont inertes tant que la case de renonciation n'est pas cochée —
   **sur les deux parcours** (la pop-up de fin *et* le bouton « dossier complet » de la page
   de résultats).
3. `?apercu=1` ne montre plus rien de spécial.
4. `merci.html?formule=dossier` sans `session_id` ne débloque rien.
5. Une référence inventée dans « J'ai déjà payé » est refusée.
6. **Un vrai achat à 1,99 € donne les résultats et *pas* le dossier** — et le bouton
   « Créer ma carte à partager » n'apparaît pas ; à sa place, l'encart « Ta boussole, en image »
   mène à la vitrine du dossier.
7. **Un vrai achat du dossier fait apparaître le bouton de la carte**, et l'image se fabrique
   aux deux formats (post et story).
8. **Le complément** : avec un accès « resultats », la vitrine affiche 4 € et non
   « 5,99 € ~~20 €~~ », le badge de lancement disparaît, et la ligne « Tes 1,99 € sont déjà
   réglés » s'affiche. Le paiement de 4 € ouvre le dossier **et** la carte à partager.
9. Le montant débité correspond au prix affiché.
10. Le client reçoit sa référence d'achat et peut l'imprimer.
11. **Le code à offrir** : l'achat du dossier fait apparaître l'encadré « Offrir le test à
    quelqu'un » ; le code créé ouvre les résultats sur un *autre* appareil, et refuse de
    servir une deuxième fois. Un achat à 1,99 €, lui, ne montre pas cet encadré.

**Le point 6 demande une vraie carte bancaire, sur un vrai paiement de 1,99 € que tu te
rembourseras ensuite. Je ne peux pas le faire : je n'entre jamais de numéro de carte, même de test.**

## ~~B7 bis · Le lien de complément~~ — ✅ lien de production branché le 3 novembre

**Ta décision du 24 septembre : le complément.** Quelqu'un qui a pris la formule à 1,99 € et
qui veut le dossier ne paie plus que la **différence, 4 €**, au lieu de 5,99 € par-dessus ses
1,99 € (soit 7,98 € pour un produit affiché à 5,99 €).

Tout est posé côté site : la vitrine bascule d'elle-même sur le complément dès qu'elle voit un
accès « resultats », affiche 4 € au lieu de « 5,99 € ~~20 €~~ », retire le badge de lancement
et ajoute la ligne « Tes 1,99 € sont déjà réglés : il ne reste que la différence ».
**Il ne manque que le lien.** Tant qu'il est vide, le bouton reste celui du dossier entier au
plein tarif — c'est-à-dire exactement le comportement d'avant.

Dans Stripe, à créer **en même temps que les deux autres** (B5) :

- un produit **« Complément — Dossier complet »**, prix unique **4,00 € TTC**
- URL de retour, exactement comme les deux autres :

  ```
  https://boussole-emotionnelle.fr/merci.html?formule=dossier&session_id={CHECKOUT_SESSION_ID}
  ```

  `formule=dossier` et pas autre chose : ce qu'ouvre ce paiement, c'est le dossier.

Donne-moi le lien et je le pose dans `VENTE.lienComplement` — une ligne.

**Ce que le Worker en fait.** Il ne regarde pas quel lien a été cliqué, il regarde le montant
encaissé : au-dessus de 2,50 €, c'est un dossier. Donc 4 € ouvre le dossier, 1,99 € non, et
5,99 € non plus. J'ai descendu ce seuil de 4 € à 2,50 € aujourd'hui : à 4 € il tombait pile
sur le montant du complément, et un centime de moins aurait livré la formule à 1,99 € à
quelqu'un qui a payé le double, sans que rien ne le signale. **Ne crée aucun produit entre
2,00 € et 2,50 €** sans me le dire.

**Une limite, que j'assume et que tu dois connaître.** Rien n'empêche techniquement quelqu'un
qui n'a jamais payé les 1,99 € d'utiliser le lien de complément et d'avoir le dossier pour 4 €
au lieu de 5,99 €. Il faudrait pour cela qu'il trouve le lien — il ne s'affiche que pour un
accès « resultats ». J'ai écarté le verrou qui l'aurait empêché : il aurait aussi puni les gens
honnêtes dont le navigateur a perdu la référence, et qui auraient payé 4 € pour ne recevoir que
les résultats. Un manque à gagner de 1,99 € vaut mieux qu'un client qui paie et ne reçoit pas.
Pour que tu puisses le voir : chaque complément part chez Stripe avec la référence de l'achat
qu'il complète (`de:cs_…` dans la colonne « client reference »). Une ligne sans référence, c'est
un complément sans achat antérieur.

## B7 ter · Ce qui reste vrai quoi qu'il arrive

**La carte n'a jamais été vendue à personne.** Si tu t'étais demandé si quelqu'un ayant acheté
à 1,99 € avant ce changement se retrouvait lésé : non. Le mode test est encore actif, aucun
paiement réel n'a eu lieu, et les CGV disent aujourd'hui qu'aucune formule payante n'est
proposée. La question ne se posera plus jamais si la vente ouvre après ce changement.

## B8 · Le test depuis Instagram et TikTok, sur un vrai téléphone

**À faire avant la première publication, pas après.** Les navigateurs intégrés d'Instagram et
de TikTok isolent leur stockage. Si l'un d'eux bascule le lien de paiement vers Safari ou
Chrome plutôt que d'ouvrir un onglet interne, le client voit une page « Merci ! » d'un côté et
son test toujours verrouillé de l'autre.

Fais un achat de bout en bout depuis chacune des deux applications, sur ton téléphone, et
regarde si l'onglet du test se débloque. C'est précisément le canal que les 99 publications
vont ouvrir : si ça casse, ça casse sur tous les clients à la fois.

---

# D — Les vidéos

## D1 · Publier les vidéos — tout est prêt

Quarante vidéos de **45 secondes**, en **4:3**, dans **`Vidéos à publier/`** à la racine, chacune
avec sa légende à côté, prête à coller. Les mêmes vingt textes, en deux versions :

- **`Photos/`** : des photos Pexels sur le thème de chaque vidéo — paysages, orages, lumière,
  jamais un humain ; cinq vidéos en images imaginaires ;
- **`Illustrations/`** : les illustrations nanobanana des carrousels, une scène par phrase.
  Elles ont été générées par IA : en publiant, active l'étiquette prévue par la plateforme.

Dans les deux, les mots apparaissent un à un au rythme d'une voix off, les images bougent
lentement et changent avec chaque phrase, par une transition. Pas de voix pour l'instant ;
une voix ElevenLabs pourra s'ajouter plus tard, sans rien changer d'autre.

**Une seule règle à respecter en publiant : garder la ligne de crédit musique** qui est dans
chaque légende (« Musique : … — Kevin MacLeod (incompetech.com), licence CC BY 4.0 »). Ce n'est
pas une politesse, c'est la condition de la licence. Les photos Pexels et nos illustrations
n'ont rien à créditer.

**Le dossier `Video tiktok/` est resté sur ton disque mais a été retiré du dépôt public** le
24 septembre : il y était depuis le 23, servi par GitHub Pages — ce sont les vidéos d'un autre
créateur, elles n'avaient rien à y faire.

---

# C — Finir les images

## C1 · Recharger nanobanana — ~10 €

L'API répond `You need to recharge to create task`. Le compte est `cavalier1231@hotmail.fr` —
c'est sur celui-là que toute la série a été générée. Recharger sur
<https://nanobanana.io/pricing>.

| | Images | Crédits |
|---|---|---|
| **Prioritaire** — les 9 illustrations en attente (posts 17, 29, 30) | 9 | 180 |
| Défauts trouvés à l'audit des 591 diapositives (continuité de personnage, cadrage, un plat qui ne ressemble pas à une blanquette) | jusqu'à 17 | 340 |

**Le plus petit forfait couvre largement les 9 prioritaires.** Sans elles, le post 30 est
inutilisable en l'état (les cinq diapositives datent de la première passe) — il est en
semaine 17, donc tu as le temps, mais autant le faire en une fois.

La marche à suivre complète, moteur de génération compris, est dans
**`reseaux-sociaux-bd/REPRENDRE.md`**. Une fois les images récupérées, je remonte les
carrousels et le dossier `publication/` en une commande.

---

# Récapitulatif — ce que j'attends de toi, et ce que j'en fais

| Tu me donnes | Je fais |
|---|---|
| ~~la balise Search Console~~ | ✅ propriété validée, sitemap envoyé, Bing aussi |
| ~~ton choix de mesure d'audience~~ | ✅ compteur en service depuis le 23 septembre |
| ~~les adresses de profil Instagram~~ | ✅ `sameAs` et pied de page sur les 59 pages |
| l'adresse du profil TikTok | je l'ajoute au `sameAs` et aux pieds de page |
| les 10 décisions | je complète statuts et pacte |
| ~~les 7 champs du Kbis + directeur de publication~~ | ✅ Kbis reçu le 3 novembre, pages légales préparées |
| ~~le régime de TVA~~ | ✅ réel simplifié, numéro FR50 130 916 968 posé le 3 novembre |
| ~~un numéro de téléphone~~ | ✅ pages légales SAS publiées le 3 novembre |
| le médiateur (nom, adresse, URL) | je l'inscris dans les CGV et les mentions légales |
| ~~ta décision sur le prix barré~~ | ✅ « tarif de lancement », appliqué le 13 octobre |
| ~~les 3 liens Stripe (résultats, dossier, complément)~~ | ✅ créés et branchés le 3 novembre |
| `wrangler secret put STRIPE_CLE` | je renseigne `VENTE.verification` et je bascule |
| les 9 images régénérées | je remonte les carrousels et `publication/` |

**Rien de tout cela ne se fait à ta place.** Chacun de ces points demande un compte à ton nom,
une pièce d'identité, une carte bancaire ou un arbitrage qui t'appartient.

---

## Ce que tu dois savoir, et qui ne se corrigera pas

**Le contenu vendu 5,99 € est présent dans la page gratuite.** Le verrou est côté navigateur :
il cache, il n'empêche pas. Quelqu'un qui sait ouvrir une console récupère le dossier sans
payer. Ce n'est pas un défaut d'implémentation, c'est la conséquence d'un site sans serveur.

À 1,99 € et 5,99 €, c'est une décision commerciale plutôt qu'un problème technique : le public
visé n'ouvre pas de console, et bâtir la génération du dossier côté serveur coûterait bien plus
que ce que la fuite fera perdre. **Mais il faut le savoir avant de lancer, pas après.**
