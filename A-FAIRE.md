# Ce que tu as à faire

*État au 21 septembre 2026, mis à jour après la validation Search Console.*

Tout ce qui pouvait être fait dans le dépôt l'est. Ce qui reste demande un compte tiers,
une identité, de l'argent ou un arbitrage — donc toi. Ce document ne liste que ça.

Trois blocs indépendants, dans l'ordre de ce qui rapporte le plus vite :

- **A. Se rendre visible** — faisable aujourd'hui, ne dépend de rien. ~2 h.
- **B. Pouvoir vendre** — bloqué par la société. Plusieurs semaines.
- **C. Finir les images** — bloqué par les crédits. ~10 €.

Le site ne vend rien aujourd'hui (`modeTest: true`, liens Stripe de test) : rien n'est en
train de mal tourner. Le bloc B est à faire **avant** de basculer, pas en urgence.

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

## A2 · Bing Webmaster Tools — 3 minutes · **c'est le prochain**

<https://www.bing.com/webmasters> → « Importer depuis Google Search Console ». Tout est
repris automatiquement, y compris le sitemap. Search Console étant maintenant validé,
l'import n'a plus aucun préalable. Bing alimente aussi DuckDuckGo et Ecosia, et
la concurrence y est bien plus faible que sur Google.

## A3 · Vérifier que `contact@` arrive vraiment

Les CGV promettent le service après-vente à `contact@boussole-emotionnelle.fr`, qui redirige
vers `contact@odem-app.com`. **Envoie un message à l'adresse publique depuis une autre boîte
et vérifie qu'il arrive.** Si la redirection est cassée, un client qui a payé et n'a rien reçu
n'a aucun moyen de te joindre — et c'est écrit noir sur blanc dans un document contractuel.

## A4 · Créer les deux comptes réseaux

99 publications sont prêtes dans `publication/`, six par semaine sur 17 semaines. Il manque
les comptes.

- **Instagram** et **TikTok** : même nom, même photo, même bio.
- **Lien en bio** sur les deux : `https://boussole-emotionnelle.fr` — toutes les légendes y
  renvoient et aucune ne peut être cliquable dans le texte.
- Compte **professionnel/créateur** des deux côtés : c'est ce qui donne accès aux statistiques.
- Mode d'emploi complet du calendrier : `publication/LISEZMOI.md`.

Tu peux commencer à publier **avant** que la vente soit ouverte. C'est même préférable : le
temps que l'audience se construise, le parcours d'achat sera prêt.

## A5 · Décider de la mesure d'audience

Aujourd'hui les 59 pages n'ont **aucune** mesure. Le jour de la première semaine de vente, si
zéro commande arrive, rien ne permettra de distinguer « personne n'est venu » de « des gens
sont venus et ont refusé de payer » — deux diagnostics dont les remèdes sont opposés.

Deux options honnêtes, à trancher :

| | Coût | Ce que ça donne | Contrainte |
|---|---|---|---|
| **Plausible** ou **Simple Analytics** | abonnement mensuel | interface prête, sans cookie ni bandeau | un compte à créer, un script tiers |
| **Compteur maison** sur ton Worker Cloudflare | gratuit | uniquement les événements que je code | pas d'interface, je te fais un tableau |

Dans les deux cas, je pose les mêmes repères : arrivée sur un article, clic « Faire le test »,
fin du test, ouverture de la pop-up, clic vers Stripe. **Dis-moi laquelle tu veux** — le
choix est à toi, l'installation est à moi.

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

## B6 · Déployer le Worker de vérification

Le Worker Cloudflare existe mais contient encore le Hello World. Sans lui, deux des trois
portes qui donnent le produit payant gratuitement restent ouvertes : on ne peut pas vérifier
un paiement sans interroger Stripe côté serveur.

1. Coller le contenu de **`worker/verification.js`** dans le Worker (je l'aurai mis à jour
   avec tes identifiants de prix et le contrôle des remboursements).
2. Créer dans Stripe une **clé restreinte**, en lecture seule, avec **deux** permissions :
   **Checkout Sessions (lecture)** et **PaymentIntents (lecture)**. La seconde est
   indispensable : sans elle, une session remboursée resterait valide indéfiniment, sur autant
   d'appareils que la personne veut — le remboursement coûterait le prix **et** le produit.
3. Ajouter cette clé comme secret nommé **`STRIPE_CLE`**.
4. Poser une **règle de limitation de débit** Cloudflare : 10 requêtes par minute et par IP
   sur la route du Worker.
5. **Me donner l'URL du Worker.**

> Je n'ai jamais accès à cette clé et je ne la manipule pas : elle se colle dans l'interface
> Cloudflare, par toi.

## B7 · Le test réel, avant d'annoncer quoi que ce soit

Une fois que j'ai basculé le site, à faire **dans l'ordre**, en production :

1. Le pied de page mène aux CGV, et les CGV portent le nom réel de la société.
2. Les boutons de paiement sont inertes tant que la case de renonciation n'est pas cochée —
   **sur les deux parcours** (la pop-up de fin *et* le bouton « dossier complet » de la page
   de résultats).
3. `?apercu=1` ne montre plus rien de spécial.
4. `merci.html?formule=dossier` sans `session_id` ne débloque rien.
5. Une référence inventée dans « J'ai déjà payé » est refusée.
6. **Un vrai achat à 1,99 € donne les résultats et *pas* le dossier.**
7. Le montant débité correspond au prix affiché.
8. Le client reçoit sa référence d'achat et peut l'imprimer.

**Le point 6 demande une vraie carte, sur un vrai paiement de 1,99 € que tu te rembourseras
ensuite. Je ne peux pas le faire : je n'entre jamais de numéro de carte, même de test.**

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
| ~~la balise `google-site-verification`~~ | ✅ en ligne, propriété validée, sitemap envoyé |
| ton choix de mesure d'audience | j'installe et je pose les cinq repères |
| les 10 décisions | je complète statuts et pacte |
| les 7 champs du Kbis + directeur de publication | je publie les trois pages légales SAS |
| le médiateur (nom, adresse, URL) | je l'inscris dans les CGV et les mentions légales |
| ta décision sur le prix barré | je l'applique aux 4 endroits + les CGV |
| les 2 liens Stripe + les 2 `price_...` | je branche et je prépare la bascule |
| l'URL du Worker | je branche la vérification, je passe `modeTest` à `false`, j'incrémente le cache |
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
