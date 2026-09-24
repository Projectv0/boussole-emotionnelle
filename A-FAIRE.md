# Ce que tu as à faire

*État au 21 septembre 2026. Search Console et Bing sont faits ; le bloc A est à moitié
clos, et tout ce qui reste ne dépend plus que de toi.*

Tout ce qui pouvait être fait dans le dépôt l'est. Ce qui reste demande un compte tiers,
une identité, de l'argent ou un arbitrage — donc toi. Ce document ne liste que ça.

Trois blocs indépendants, dans l'ordre de ce qui rapporte le plus vite :

- **A. Se rendre visible** — faisable aujourd'hui, ne dépend de rien. ~2 h.
- **B. Pouvoir vendre** — bloqué par la société. Plusieurs semaines.
- **C. Finir les images** — bloqué par les crédits. ~10 €.

Le site ne vend rien aujourd'hui (`modeTest: true`, liens Stripe de test) : rien n'est en
train de mal tourner. Le bloc B est à faire **avant** de basculer, pas en urgence.

**Ce qui est gratuit, exactement.** À dire juste partout, y compris dans les bios et les
dépôts d'annuaire : **le guide de 57 articles est en accès libre**, et le test se répond
librement — mais **aucun résultat ne s'affiche sans payer**, pas même les trois émotions
dominantes, à partir de 1,99 €. Écrire « test gratuit » quelque part serait faux, et c'est
précisément le schéma qui produit le plus de réclamations : quelqu'un passe dix à quinze
minutes sur seize situations, puis découvre le prix. *(L'audit de mise en marché demande
d'ailleurs d'annoncer le prix avant le test — point 2.4, encore à faire.)*

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

## ~~A4 · Les deux comptes réseaux~~ — ✅ fait le 23 septembre 2026

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

## A6 · Les liens entrants — **le seul vrai frein aujourd'hui**

Constaté en cherchant, le 23 septembre : le site **est** indexé — premier sur son nom de
domaine exact, sixième sur « boussole emotionnelle test emotions ». Mais il n'apparaît pas
sur « boussole émotionnelle » seul, et **5 pages sur 59** sont indexées.

Deux causes, une seule sur laquelle on peut agir.

**Le nom du projet est une expression courante, pas une marque.** « Boussole émotionnelle »
est déjà employée par pauldevaux.fr, emotioncompass.org, ecolepositive.fr, macoherence.com —
des sites installés depuis des années. Personne ne se dispute « Decathlon » ; tout le monde
se dispute celle-ci. C'est une contrainte permanente, pas un retard de démarrage.

**Le site n'a aucun lien entrant.** Zéro. C'est ce qui décide du classement sur une requête
disputée, et c'est la seule chose qui manque vraiment — le contenu, lui, est là.

### Ce qu'on peut faire, et qui fait quoi

**Moi** : repérer les endroits où déposer le site, écrire les textes de présentation aux
bons formats, préparer les fiches.

**Toi** : créer les comptes et valider les dépôts. Je ne crée pas de compte et je ne soumets
pas de formulaire à ta place.

Les pistes qui valent la peine, par ordre d'effet :

- **les annuaires français de bien-être et d'outils gratuits** — lents, mais durables ;
- **les forums et communautés** où le test répond à une question réellement posée (jamais en
  autopromotion : une réponse utile qui cite le test) ;
- **les plateformes d'outils gratuits** (type « ressources psycho », listes d'outils en accès
  libre) ;
- **les profils sociaux**, déjà en place pour Instagram : ils remontent souvent eux-mêmes sur
  le nom.

**Dis-moi quand tu veux t'y mettre** et je prépare le premier lot : la liste des cibles, ce
qu'elles demandent, et les textes prêts à coller.

### En attendant, une consigne pratique

**Donne l'adresse, pas le nom.** `boussole-emotionnelle.fr` sort premier immédiatement ;
« boussole émotionnelle » ne sortira pas avant des mois. C'est ce qu'il faut dire aux gens à
qui tu en parles — ton associé compris.

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

## B2 · Immatriculer, et me donner sept champs

La suite mécanique : signature des statuts → dépôt du capital → annonce légale → dossier sur
<https://procedures.inpi.fr> → Kbis sous une à deux semaines.

**Ce que j'attends du Kbis, exactement sept champs :**

1. dénomination sociale exacte
2. forme juridique
3. montant du capital
4. numéro SIREN
5. ville du greffe (RCS)
6. adresse du siège
7. numéro de TVA intracommunautaire, s'il existe

**Plus un huitième qui n'est pas sur le Kbis :** le nom du directeur de la publication.

Les trois pages légales en version SAS sont déjà écrites dans `societe/site-jour-J/` et
n'attendent que ces champs. Aujourd'hui les pages en ligne déclarent un éditeur **« non
professionnel »** et un site **« proposé gratuitement »** — deux affirmations qui deviennent
fausses, et publiées, le jour du premier euro.

## B3 · Adhérer à un médiateur de la consommation

**Obligation légale** pour tout professionnel vendant à des consommateurs (article L612-1 du
code de la consommation). Quelques dizaines d'euros par an. Organismes agréés : CM2C, Medicys,
AME Conso.

Ça ne s'improvise pas le jour d'une réclamation : compte plusieurs jours à quelques semaines
d'adhésion. **Lance-le en parallèle du dossier d'immatriculation**, pas après.

Je t'attends sur : nom du médiateur, adresse postale, URL. Ces trois éléments doivent figurer
dans les CGV et les mentions légales, où le crochet `[nom et coordonnées du médiateur adhéré]`
attend encore d'être rempli.

## B4 · Trancher le prix barré

Le site affiche aujourd'hui **« 5,99 € au lieu de 20 € »** et un badge **« −70 % »**, à quatre
endroits. L'article L112-1-1 impose que toute annonce de réduction se réfère au prix le plus
bas pratiqué dans les trente jours précédents. **20 € n'a jamais été pratiqué.** C'est le motif
de contrôle le plus courant sur ce type de site, et il se vérifie depuis n'importe quel
navigateur.

Deux options honnêtes, une seule à choisir :

- **vendre réellement le dossier 20 €** pendant au moins trente jours avant d'annoncer une remise ;
- **retirer le prix barré et le badge**, et parler de « tarif de lancement » sans pourcentage.

*Ma recommandation : la seconde. « Tarif de lancement, 5,99 € » se défend seul et personne ne
peut le contester.* Tant que tu n'as pas tranché, je ne touche pas à l'affichage.

## B5 · Le compte Stripe de la SAS, en production

Après l'ouverture du compte bancaire professionnel (il faut le Kbis et l'IBAN société).

**Créer deux produits** aux prix réels : **1,99 €** (résultats) et **5,99 €** (dossier complet).

**Créer deux liens de paiement**, avec ces URL de redirection **exactement** :

```
https://boussole-emotionnelle.fr/merci.html?formule=resultats&session_id={CHECKOUT_SESSION_ID}
```
```
https://boussole-emotionnelle.fr/merci.html?formule=dossier&session_id={CHECKOUT_SESSION_ID}
```

Sans le paramètre `formule`, la page de remerciement ne sait pas quoi débloquer. Sans
`session_id`, rien ne peut être vérifié.

**Deux réglages à activer sur les deux liens :**

- **« Exiger l'acceptation des conditions de vente »**, en y mettant l'URL des CGV. Stripe
  produit alors une preuve horodatée de l'acceptation — ce qu'aucun code côté navigateur ne
  peut faire.
- **Collecte de l'adresse e-mail** du client, pour le reçu.

**Ce que tu me donnes ensuite :** les deux URL de paiement, **et les deux identifiants de prix**
(`price_...`, visibles sur la fiche produit). Les identifiants de prix permettent au Worker de
reconnaître le produit acheté au lieu de deviner d'après le montant — sans eux, un code promo
de −20 % ferait passer un acheteur du dossier sous le seuil et il recevrait un produit amputé.

## B6 · La clé Stripe du Worker

**Le Worker est déjà déployé** — c'est celui de la mesure, `boussole.projectv0-0.workers.dev`.
Le code de vérification d'achat y est, et il répond déjà correctement : référence mal formée
rejetée, et 501 tant qu'il n'a pas sa clé. Il ne manque que la clé.

1. Créer dans Stripe une **clé restreinte**, en lecture seule, avec **deux** permissions :
   **Checkout Sessions (lecture)** et **PaymentIntents (lecture)**. La seconde est
   indispensable : sans elle, une session remboursée resterait valable indéfiniment, sur
   autant d'appareils que la personne veut — le remboursement coûterait le prix **et** le
   produit.
2. La poser depuis `worker/` :

   ```bash
   wrangler secret put STRIPE_CLE
   ```

   La valeur se tape au clavier, comme pour `MESURE_CLE`. Je ne la vois jamais.

3. Poser une **règle de limitation de débit** Cloudflare : 10 requêtes par minute et par IP
   sur la route du Worker. Elle protège à la fois le compteur d'audience et la vérification
   d'achat.

Ensuite je renseigne `VENTE.verification` dans le site — une ligne — et **deux choses
s'allument d'un coup** : la vérification d'achat, et le code à offrir (B6 bis).

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
8. Le montant débité correspond au prix affiché.
9. Le client reçoit sa référence d'achat et peut l'imprimer.
10. **Le code à offrir** : l'achat du dossier fait apparaître l'encadré « Offrir le test à
    quelqu'un » ; le code créé ouvre les résultats sur un *autre* appareil, et refuse de
    servir une deuxième fois. Un achat à 1,99 €, lui, ne montre pas cet encadré.

**Le point 6 demande une vraie carte bancaire, sur un vrai paiement de 1,99 € que tu te
rembourseras ensuite. Je ne peux pas le faire : je n'entre jamais de numéro de carte, même de test.**

## B7 bis · Deux choses à savoir avant d'ouvrir la vente

**Le passage de 1,99 € à 5,99 € refait payer le plein tarif.** Quelqu'un qui a pris la formule
simple puis clique « Passer au dossier complet » paie 5,99 € en plus de ses 1,99 € — donc
7,98 € pour un produit affiché à 5,99 €. C'était déjà le cas avant aujourd'hui, mais la
carte réservée au dossier va pousser bien plus de monde vers ce bouton. Deux sorties possibles :
créer dans Stripe un **lien de complément à 4 €** et le brancher sur ce bouton-là, ou l'assumer
et l'écrire noir sur blanc à côté du prix. Dis-moi laquelle et je la pose. Ne laisse pas la
troisième, qui est de ne rien faire.

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
| les 7 champs du Kbis + directeur de publication | je publie les trois pages légales SAS |
| le médiateur (nom, adresse, URL) | je l'inscris dans les CGV et les mentions légales |
| ta décision sur le prix barré | je l'applique aux 4 endroits + les CGV |
| les 2 liens Stripe + les 2 `price_...` | je branche et je prépare la bascule |
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
