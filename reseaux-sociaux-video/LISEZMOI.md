# Atelier vidéo — vingt vidéos dans le style des références

Vingt vidéos de 50 secondes, en 4:3 (1024 × 768), dans le style des trois vidéos de
référence du dossier `Video tiktok/` : une accroche sur fond noir, puis des
phrases entières qui se lisent à l'écran sur la musique, chacune sur sa propre
photo assombrie — la photo et la phrase changent au même instant, jamais l'une
sans l'autre. Paysages, orages, lumière, matière, jamais un humain, et toujours
sur le thème de la vidéo (cinq en images imaginaires). À la fin, la photo reste
entière : une question — « Et toi, où en es-tu ? » — et un bandeau discret en
bas avec la boussole, le nom du site, l'adresse et l'étiquette « LIEN EN BIO ».

**Sans voix pour l'instant** (`SANS_VOIX = True` en tête de `generateur.py`) : les mots
apparaissent un à un, au rythme où une voix off posée les dirait. Passer `SANS_VOIX` à
`False` rebranche une voix — ElevenLabs si la clé est là, sinon celle de macOS — et les
mots s'affichent alors quand elle les dit.

## Le montage (`montage.py`)

Pour que ce ne soit pas un diaporama, chaque vidéo est rendue image par image, à
30 images par seconde :

- **le rythme des mots** : environ 160 mots par minute — chaque vidéo dure 50 s
  (`DUREE_VISEE`), le rythme s'accélère d'autant —, un mot long prend plus de temps
  qu'un mot court (on compte ses syllabes), une virgule fait respirer, un point marque un
  vrai temps. Quand la phrase est dite en entier, elle reste le temps de finir de la lire
  (`TENUE`), puis la suivante arrive ;
- **les mots** arrivent en fondu en remontant un peu ; ceux en couleur arrivent plus gros
  et se posent. La phrase d'avant s'efface quand la suivante commence ;
- **les images** bougent lentement pendant la lecture : elles avancent, reculent ou
  glissent d'un côté — vers les visages, sur les illustrations ;
- **les transitions** : l'image change à l'instant exact où la phrase change, par un
  fondu, une poussée latérale, un zoom ou un flou, en alternance ;
- **la fin** : le bandeau monte du bas, la question « Et toi, où en es-tu ? » se pose
  mot à mot.

Tous les réglages sont en tête de `montage.py`. `--apercu` pose dans `.cache/` une image
par phrase, au moment où elle est entière — de quoi faire des planches de contrôle sans
rendre la vidéo.

## Refaire les vidéos

    python3 photos.py          # une fois : ~30 photos par vidéo, sur le thème de chacune
    python3 generateur.py      # les vingt vidéos photos, dans « Vidéos à publier/Photos/ »
    python3 generateur.py 07   # une seule
    python3 generateur.py --legendes   # réécrire les légendes seules, sans refaire les vidéos

## La version illustrée

    python3 generateur.py --illustrations        # les vingt illustrées, dans « Vidéos à publier/Illustrations/ »
    python3 generateur.py --illustrations 07     # une seule

Mêmes textes, même musique, même rythme ; les fonds sont les illustrations nanobanana des
carrousels (`../reseaux-sociaux-illustre/illustrations/`, crayon et aquarelle, et
`../reseaux-sociaux-bd/illustrations/`, bande dessinée). Le choix est fait à la main, phrase
par phrase, dans **`choix_illustrations.py`** — une image par phrase, aucune image utilisée
deux fois sur les vingt vidéos. `illustrations/catalogue.json` décrit les 437 images
disponibles (d'après leurs prompts) pour en choisir d'autres.

Ces illustrations montrent des personnages ; le générateur s'en arrange :

- **le cadrage** se centre sur les visages. Ils sont repérés par
  `../reseaux-sociaux-bd/detecter-visages.swift` (`illustrations/visages-illustre.json`
  pour les illustrations ; celui des cases de BD existait déjà dans
  `../reseaux-sociaux-bd/file/visages.json`). Les visages que le détecteur ratait sont dans
  `illustrations/visages-complement.json` : retrouvés sur l'image agrandie, ou relevés à l'œil
  puis vérifiés ;
- **le texte** se pose là où il ne couvre aucun visage — couvrir des yeux coûte dix fois plus
  que couvrir des cheveux —, avec une ombre douce derrière lui pour se lire sur un fond clair ;
- **les cases de BD** gardent leur mur vide au-dessus des personnages (dessiné pour les
  bulles, c'est la place du texte), mais perdent leur marge, leur filet de cadre et le
  bandeau crème que certaines avaient en haut.

Les illustrations ont été générées par IA : à la publication, activer l'étiquette prévue
par la plateforme. Rien à créditer dans la légende.

Il faut deux clés, gratuites ou presque, rangées hors du dépôt dans `~/.config/boussole/` :

| Clé | Pour | Comment l'obtenir | Où la ranger |
|---|---|---|---|
| **Pexels** | les photos de chaque thème | compte gratuit sur pexels.com → *Image & Video API* → la clé s'affiche | `~/.config/boussole/pexels.cle` |
| **ElevenLabs** | la voix off | compte sur elevenlabs.io, abonnement *Starter* (5 $/mois, le premier avec usage commercial) → *API keys* | `~/.config/boussole/elevenlabs.cle` |

Pour ranger une clé, dans le Terminal (une seule ligne, en remplaçant la clé et le nom) :

    mkdir -p ~/.config/boussole && printf '%s' 'LA_CLÉ' > ~/.config/boussole/pexels.cle && chmod 600 ~/.config/boussole/pexels.cle

Les scripts lisent ces fichiers ; ils ne les affichent jamais et ne les copient nulle part.
Sans clé Pexels, pas de fonds : le générateur s'arrête et le dit. Sans clé ElevenLabs, la
voix de macOS prend le relais — nettement moins bien.

Choisir la voix : `python3 voix_eleven.py --voix` liste les voix du compte avec un extrait
à écouter ; l'identifiant retenu va dans `VOIX_ELEVEN`, en tête de `generateur.py`.

Chaque vidéo sort avec sa légende à côté d'elle, prête à coller.
Changer un texte dans `scripts.py` puis relancer suffit : la voix ne se
resynthétise que si le texte a changé.

Il faut `ffmpeg` (`brew install ffmpeg`).

## Ce qu'il y a dedans, et d'où ça vient

| Quoi | D'où | Licence | À faire |
|---|---|---|---|
| Les photos | Pexels | licence Pexels : usage commercial libre, sans attribution | rien — `photos/<id>.json` garde la trace de chacune |
| Les musiques | Kevin MacLeod, incompetech.com | CC BY 4.0 | **créditer** : la ligne est déjà dans chaque légende, il suffit de la laisser |
| La voix | ElevenLabs (abonnement Starter ou plus) | usage commercial inclus dans l'abonnement | rien |
| Les textes | les articles du guide, et un penseur par vidéo | à nous | rien |

Le crédit musique n'est pas une politesse : c'est la condition de la licence.
Voir `MUSIQUES-CREDITS.md`.

## Ce que les textes ne disent jamais

- que le test est gratuit — il ne l'est pas, seuls les articles du guide le sont ;
- un prix ;
- quoi que ce soit qui ressemble à un diagnostic.

Chaque penseur est cité pour une idée qu'il a réellement écrite, paraphrasée :
Sénèque sur la colère comme courte folie (*De la colère*), Marc Aurèle sur le
jugement (*Pensées*), Alain sur le pessimisme d'humeur (*Propos sur le bonheur*),
La Rochefoucauld sur la jalousie (*Maximes*, 32), Sénèque sur l'imagination
(*Lettres à Lucilius*, 13), Montaigne sur la peur (*Essais*, I, 18) et sur être à
soi (III), Descartes sur l'admiration (*Passions de l'âme*, 53), William James sur
les larmes (1884), Kierkegaard sur le vertige de la liberté (*Le Concept
d'angoisse*), Épictète sur ce qui dépend de nous (*Manuel*), Aristote sur la juste
émotion (*Éthique à Nicomaque*, IV) et les trois amitiés (VIII), Stendhal sur la
cristallisation (*De l'amour*), Épicure sur les désirs vains (*Lettre à Ménécée*),
Pascal sur la chambre (*Pensées*), Simone Weil sur l'attention (lettre à Joë
Bousquet), Cicéron sur la gratitude (*Pro Plancio*), Spinoza sur la joie et la
tristesse comme passages (*Éthique*, III), Darwin sur l'expression involontaire
(*L'Expression des émotions*).

## Le format

**4:3, 1024 × 768** depuis le 5 octobre 2026 (les références étaient en 16:9). Le
format tient dans une ligne, `L, H, FPS = 1024, 768, 30` en tête de `generateur.py` :
les hauteurs du texte (`ANCRES`), les emplacements essayés pour éviter les visages, la
question de fin et les cadrages suivent la hauteur d'eux-mêmes. Pour un format portrait
(9:16), il faudrait en plus revoir la largeur des lignes, pensée pour un cadre plus
large que haut.
