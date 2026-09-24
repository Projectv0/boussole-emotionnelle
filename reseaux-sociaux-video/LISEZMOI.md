# Atelier vidéo — vingt vidéos dans le style des références

Vingt vidéos d'une minute, paysage 16:9, dans le style des trois vidéos de
référence du dossier `Video tiktok/` : une accroche sur fond noir, des photos
assombries qui changent toutes les deux secondes — paysages, orages, lumière,
matière, jamais un humain, et toujours sur le thème de la vidéo (cinq en images
imaginaires) —, des phrases entières qui se lisent à l'écran sur la musique, et
un badge rouge « LIEN EN BIO » à la fin.

**Sans voix pour l'instant** (`SANS_VOIX = True` en tête de `generateur.py`) : le temps
de lecture fait le rythme. Passer `SANS_VOIX` à `False` rebranche une voix — ElevenLabs
si la clé est là, sinon celle de macOS — et les mots s'affichent alors quand elle les dit.

## Refaire les vidéos

    python3 photos.py          # une fois : ~30 photos par vidéo, sur le thème de chacune
    python3 generateur.py      # les vingt vidéos, dans « Vidéos à publier/ » à la racine
    python3 generateur.py 07   # une seule

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

Les références sont en paysage, ce qui est inhabituel sur TikTok ; on a gardé le
même format. Pour passer en 9:16, changer `L, H = 1024, 576` dans `generateur.py`
et revoir les ancres du texte — tout le reste suit.
