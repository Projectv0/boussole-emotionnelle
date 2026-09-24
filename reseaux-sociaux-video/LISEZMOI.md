# Atelier vidéo — vingt vidéos dans le style des références

Vingt vidéos d'une minute, paysage 16:9, dans le style des trois vidéos de
référence du dossier `Video tiktok/` : une accroche sur fond noir, des tableaux
de maître assombris qui changent toutes les deux secondes, le médaillon de la
Boussole en personnage fixe, les mots qui apparaissent quand la voix les dit,
et un badge rouge « LIEN EN BIO » à la fin.

## Refaire les vidéos

    python3 tableaux.py        # une fois : va chercher ~200 tableaux du domaine public
    python3 generateur.py      # les vingt vidéos, dans sortie/
    python3 generateur.py 07   # une seule

Chaque vidéo sort avec sa légende, `sortie/<id>.legende.txt`, prête à coller.
Changer un texte dans `scripts.py` puis relancer suffit : la voix ne se
resynthétise que si le texte a changé.

Il faut `ffmpeg` (`brew install ffmpeg`) et la voix française **Jacques** de macOS.

## Ce qu'il y a dedans, et d'où ça vient

| Quoi | D'où | Licence | À faire |
|---|---|---|---|
| Les tableaux | The Met, Art Institute of Chicago, Cleveland Museum of Art (Open Access) | CC0 | rien — mais `tableaux.json` garde la trace de chaque toile |
| Les musiques | Kevin MacLeod, incompetech.com | CC BY 4.0 | **créditer** : la ligne est déjà dans chaque légende, il suffit de la laisser |
| La voix | Jacques, synthèse vocale de macOS | usage libre | rien |
| Le médaillon | le logo du site | à nous | rien |
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
