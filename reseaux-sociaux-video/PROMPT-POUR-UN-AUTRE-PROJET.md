# Prompt : vingt vidéos dans le style de l'atelier Boussole, pour un autre projet

Copie tout ce qui suit dans une nouvelle session Claude Code ouverte dans le dossier
du nouveau projet. Remplis d'abord la fiche du § 1 ; tout le reste est prêt.

---

Je veux vingt vidéos d'une minute pour les réseaux sociaux, dans un style précis que
j'ai déjà mis au point sur un autre projet et que tu vas reproduire à l'identique :
des phrases entières qui se lisent à l'écran, en grandes capitales, sur des photos
assombries qui changent à chaque phrase, avec une musique libre de droits, sans voix
pour l'instant, et une page de fin discrète qui renvoie au lien en bio. Tout ce qui
concerne le sujet des vidéos (textes, images, page de fin, légendes) doit être adapté
au projet décrit au § 1, rien ne doit rester du projet d'origine.

Réponds-moi en français et tutoie-moi. Ne me pose des questions qu'au tout début, en
une seule fois, et seulement sur ce que la fiche ne dit pas. Ensuite, avance seul et
montre-moi des résultats : trois vidéos d'abord, puis les vingt.

## 1 · Le projet (à compléter avant de coller)

- **Nom du projet :** [À COMPLÉTER]
- **Adresse du site (sans https://) :** [À COMPLÉTER]
- **Ce que le lien en bio ouvre** (un test, une appli, une boutique, une newsletter…) : [À COMPLÉTER]
- **En une phrase, ce que le projet apporte à la personne :** [À COMPLÉTER]
- **À qui ça s'adresse :** [À COMPLÉTER]
- **Le ton :** tutoiement / vouvoiement — [À COMPLÉTER] ; registre : doux et bienveillant / direct / autre — [À COMPLÉTER]
- **Les vingt sujets** (un par vidéo ; si tu n'en donnes pas, Claude les propose et attend ton accord avant d'écrire) : [À COMPLÉTER]
- **L'univers visuel :** ce que les photos doivent montrer (paysages, objets, matière, architecture, nature, ville, imaginaire…) et ce qu'elles ne doivent jamais montrer : [À COMPLÉTER]
- **Faut-il des humains dans les images ?** Par défaut non (ça fait « pub santé ») : [À COMPLÉTER]
- **L'image du projet** pour le médaillon de la page de fin (chemin d'un fichier, idéalement carré ou une image dont on peut découper un rond) : [À COMPLÉTER]
- **Ce qu'il ne faut jamais dire :** un prix, « gratuit », une promesse de résultat, une allégation médicale, autre — [À COMPLÉTER]
- **Les mots-dièse de base** (trois ou quatre) : [À COMPLÉTER]
- **Une page ou un article par sujet, s'il y en a** (le lien va dans la légende) : [À COMPLÉTER ou « aucun »]

## 2 · D'où part le travail

L'atelier d'origine est sur cette machine, dans
`/Users/cavalier/Dev/Site Emotion/reseaux-sociaux-video/`. Copie-le dans le nouveau
projet sous le nom `reseaux-sociaux-video/`, mais seulement ces fichiers :

    generateur.py        la fabrique (PIL pour les images-clés, ffmpeg pour l'assemblage)
    photos.py            la récolte des photos par thème (API Pexels)
    scripts.py           les vingt textes — à réécrire entièrement, garde juste la structure
    voix_eleven.py       la voix ElevenLabs, prête mais inactive
    voix.swift           la voix macOS de secours, inactive
    LISEZMOI.md          à réécrire pour le nouveau projet
    MUSIQUES-CREDITS.md  la liste des musiques et ce que leur licence exige
    musiques/            douze morceaux MP3 de Kevin MacLeod (incompetech.com, CC BY 4.0)

Ne copie **ni** `photos/`, **ni** `.cache/`, **ni** `Vidéos à publier/` : ce sont les
matériaux de l'autre projet, ils se régénèrent. Ne copie rien d'autre non plus.

Ajoute au `.gitignore` du nouveau projet :

    reseaux-sociaux-video/musiques/
    reseaux-sociaux-video/photos/
    reseaux-sociaux-video/.cache/
    Vidéos à publier/

Il faut `ffmpeg` (`brew install ffmpeg`) et Pillow (`pip3 install pillow`). Vérifie
avant de commencer, et dis-moi s'il manque quelque chose.

## 3 · Ce qui est propre au projet dans le code, et qu'il faut changer

Tout le reste du code reste tel quel. Dans `generateur.py` :

- `SITE` : l'adresse du site.
- `PRODUIT` : l'image du projet (`../og.jpg` dans l'original). La fonction `medaillon()`
  découpe un rond dans cette image avec la boîte `(50, 30, 610, 590)` : adapte la boîte
  à la nouvelle image pour que le rond cadre bien le visuel.
- `cadre_produit()` : la page de fin. La question en haut (« ET TOI, / OÙ EN ES-TU ? »),
  le nom en italique (« Boussole émotionnelle »), la ligne de détail (« Fais le test ·
  16 situations · 14 émotions ») et l'étiquette (« LIEN EN BIO ») : réécris-les pour le
  projet. Garde la mise en page : photo entière, question en escalier à gauche dans le
  style des phrases, bandeau sombre de 150 px en bas avec le médaillon (104 px),
  le nom, la ligne de détail, l'adresse en vert, l'étiquette jaune à droite.
- La légende, en fin de `construire()` : le lien vers l'article (`{SITE}/guide/…` dans
  l'original), la ligne « Le test : … (lien en bio) », les mots-dièse. Adapte au projet.
  **Garde absolument** la ligne de crédit musique et la ligne « Photos : Pexels ».

Dans `photos.py` :

- `CLE_PEXELS` : `~/.config/boussole/pexels.cle` dans l'original. Utilise
  `~/.config/<nom-du-projet>/pexels.cle`. **La clé existe déjà** dans
  `~/.config/boussole/pexels.cle` : copie le fichier, ne la demande pas, ne l'affiche
  jamais, ne la mets jamais dans le dépôt.
- `UA` : l'adresse de contact du nouveau projet.
- `ANIMAUX` : le filtre sur la description des photos, qui écarte humains et animaux.
  Adapte-le selon la fiche (§ 1).

Dans `voix_eleven.py` : le chemin de la clé, même règle. Pas de clé ElevenLabs pour
l'instant, la voix reste désactivée (`SANS_VOIX = True` dans `generateur.py`).

Dans `scripts.py` : tout est à réécrire (voir § 5).

## 4 · Le format, exactement

- Paysage 16:9, **1024 × 576**, 30 images par seconde, H.264 (crf 19), AAC 160 kb/s à
  44,1 kHz, `+faststart`. Entre **55 et 64 secondes** par vidéo.
- Une vidéo se déroule ainsi :
  1. 0,6 s de noir ;
  2. **l'accroche** : trois groupes de mots sur fond noir, posés en escalier depuis un
     coin, un mot en couleur ;
  3. **le corps** : dix à treize phrases, chacune sur **sa propre photo**. La photo et la
     phrase changent au même instant, jamais l'une sans l'autre. C'est la règle la plus
     importante du style. Le texte se déplace d'une phrase à l'autre entre six
     emplacements fixes (`ANCRES`), à gauche ou à droite, jamais centré ;
  4. **la page de fin** : 4 secondes, la dernière photo reste, la question et le bandeau.
- Le temps d'affichage d'une phrase se calcule sur sa longueur : `1,1 s + 0,30 s par
  mot`, borné entre 1,8 et 4,6 s ; les trois groupes de l'accroche gagnent 0,4 s.
  C'est `instants_lecture()`, ne change pas ces valeurs.
- Le texte : Georgia Bold, en capitales, 50 px pour la première ligne d'une phrase et
  30 px pour les suivantes, contour noir de 3 px et ombre portée, blanc par défaut.
  Trois couleurs d'accent : jaune `*mot*`, rouge `!mot!`, vert `+mot+`. La barre `/`
  coupe la ligne. Les lignes trop larges se replient d'elles-mêmes.
- Les photos sont assombries (mélange à 42 % avec du noir) et vignettées. Les photos
  trop sombres (luminance moyenne sous 40) sont écartées d'office.
- La musique : un des douze morceaux, fondu d'entrée 1,5 s, fondu de sortie 3 s,
  volume à 0,55. Un morceau différent d'une vidéo à l'autre autant que possible.

## 5 · Les textes (`scripts.py`)

Chaque vidéo est un dictionnaire avec ces champs, tous obligatoires :

```python
{
  "id": "07-nom-court",            # deux chiffres, un tiret, un mot-clé sans accent
  "titre": "Le titre lisible",     # sert au nom du fichier
  "article": "nom-de-page",        # la page du site liée (ou "" s'il n'y en a pas)
  "penseur": "Sénèque",            # une référence citée dans la vidéo (voir plus bas)
  "musique": "fichier.mp3",        # dans musiques/
  "noir": 3,                       # les trois premiers groupes sont sur fond noir
  "fantastique": False,            # True pour les vidéos en images imaginaires
  "images": ["storm clouds", "lava flow", …],   # six mots-clés en anglais, pour Pexels
  "groupes": [ … ],                # les phrases, dans l'ordre (voir plus bas)
  "legende": "Deux ou trois phrases pour la légende du post.",
}
```

Les règles d'écriture, non négociables :

- **Des phrases entières**, en bon français, fluides, explicites, douces à l'oreille.
  Pas de fragments à deviner, pas de style télégraphique. Chaque groupe est une phrase
  ou une proposition complète, qu'on peut lire à voix haute sans buter.
- Le ton et la personne de la fiche (§ 1). Dans l'original c'est le tutoiement.
- **Une idée par phrase.** Entre 4 et 14 mots par groupe ; la barre `/` coupe en deux
  lignes ; un seul mot en couleur par groupe, jamais plus, et pas dans tous les groupes.
- Le déroulé d'une vidéo : l'accroche (trois groupes) part d'une situation concrète et
  reconnaissable, que la personne vit ; le corps explique ce qui se passe, avec une
  idée d'un penseur, d'un auteur ou d'une référence du domaine, citée pour quelque
  chose qu'il a **réellement** écrit ou dit (pas de citation inventée, pas de citation
  apocryphe ; en cas de doute, une paraphrase attribuée) ; puis ce qu'on peut en faire,
  concrètement ; et une conclusion commune aux vingt vidéos, définie une fois dans une
  liste `CTA` ajoutée en fin de chaque `groupes`, qui amène au lien en bio.
- **Jamais** : un prix, le mot « gratuit », une promesse de résultat, une allégation
  médicale ou un diagnostic, un « tu souffres de », un conseil qui remplace un
  professionnel, et rien de ce que la fiche interdit.
- Les apostrophes s'affichent courbes (le générateur s'en charge), les majuscules
  accentuées aussi (É, À…).
- Relis les vingt textes avec un correcteur avant de me les montrer. Montre-moi les
  vingt textes **avant** de fabriquer les vidéos ; j'ai le dernier mot dessus.

Le fichier se termine par deux `assert` : vingt identifiants distincts, et le compte de
vidéos « fantastiques » annoncé (cinq dans l'original ; adapte à la fiche).

## 6 · Les images (`photos.py`)

- Source : **Pexels** (usage commercial libre, sans attribution). Six mots-clés
  anglais par vidéo, en rapport direct avec le sujet et l'émotion ou l'idée de la
  vidéo, pas avec le mot du titre. Exemples de l'original : pour la colère, « storm
  clouds », « lava flow », « wildfire », « crashing waves » ; pour une rupture,
  « ice crystals », « frozen lake », « broken glass macro », « winter fog ».
- Trente photos par thème, format paysage, au moins 1 000 px de large, pas de
  détourage sur fond transparent, pas d'aplat.
- Par défaut **aucun humain** (visage, main, silhouette, foule) **ni animal**, sauf si
  la fiche dit autrement. Le filtre lit la description de chaque photo ; regarde tout
  de même les planches de photos pour repérer ce qui lui échappe, et corrige les
  mots-clés plutôt que de trier à la main.
- Une partie des vidéos en **images imaginaires** (aurores, nébuleuses, cristaux,
  labyrinthes, brume…) et le reste en images « réelles » (paysages, orages, matière,
  lumière, objets). La proportion vient de la fiche ; cinq sur vingt dans l'original.
- Une photo n'est jamais réutilisée dans la même vidéo : il faut au moins autant de
  photos assez claires que de phrases sur photo. `photos.py` en récolte trente pour
  être large.

## 7 · Les musiques

Les douze morceaux de `musiques/` sont de Kevin MacLeod, licence **CC BY 4.0** : le
crédit est **obligatoire**, et le générateur l'écrit dans chaque légende. Ne le retire
jamais. Si tu remplaces un morceau, il faut une licence qui permet l'usage commercial,
et `MUSIQUES-CREDITS.md` tenu à jour.

## 8 · La sortie

Un dossier **`Vidéos à publier/`** à la racine du projet, hors dépôt, avec pour chaque
vidéo :

    NN - Titre.mp4
    NN - Titre (légende).txt     le texte du post, le lien, les mots-dièse, le crédit musique, « Photos : Pexels »

et un `LISEZMOI.txt` qui dit comment publier : coller la légende telle quelle, garder
le crédit musique, pas de voix pour l'instant.

## 9 · Les clés et la sécurité

- Les clés d'API vivent dans `~/.config/<projet>/<service>.cle`, lisibles par moi
  seul (`chmod 600`), hors du dépôt. Les scripts les lisent, ne les affichent jamais,
  ne les copient nulle part.
- **Ne me demande jamais de coller une clé dans le chat.** Si une clé manque, donne-moi
  la commande Terminal pour la poser, sur ce modèle :

      mkdir -p ~/.config/<projet> && printf '%s' 'LA_CLÉ' > ~/.config/<projet>/pexels.cle && chmod 600 ~/.config/<projet>/pexels.cle

- Ne crée aucun compte, n'achète rien, ne saisis aucun mot de passe ni moyen de
  paiement à ma place.
- Rien de ce qui appartient à quelqu'un d'autre dans le dépôt : ni vidéo de référence,
  ni photo hors licence, ni musique hors licence.

## 10 · La méthode, dans l'ordre

1. Lis la fiche (§ 1). Pose-moi en une seule fois, avec des choix, les questions que la
   fiche laisse ouvertes. Pas plus de quatre.
2. Copie l'atelier (§ 2), vérifie ffmpeg et Pillow, adapte le code (§ 3).
3. Écris les vingt textes (§ 5), relis-les au correcteur, montre-les-moi, attends mon
   accord.
4. Récolte les photos (`python3 photos.py`), regarde les planches, corrige les
   mots-clés si nécessaire, re-récolte.
5. Fabrique trois vidéos (`python3 generateur.py 02 07 14` par exemple), envoie-les-moi,
   attends mon retour.
6. Fabrique les vingt, vérifie sur chacune : durée entre 55 et 64 s, nombre de plans
   égal au nombre de phrases plus un, aucune photo répétée, aucun humain, audio à
   44,1 kHz. Dis-moi ce que tu as vérifié et comment.
7. Réécris `LISEZMOI.md` pour le nouveau projet, commite le code (jamais les photos,
   musiques, vidéos ni clés), pousse.

Quand tu me montres quelque chose, fais court : ce qui a été fait, ce qui reste, ce que
je dois regarder.
