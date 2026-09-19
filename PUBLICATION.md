# Publier — par où commencer

Tout ce qui se publie est dans **`publication/`**. Deux documents suffisent : `LISEZMOI.md`
pour savoir comment poster, `PLAN.md` pour savoir quoi poster et quand. Les trois autres
dossiers sont des ateliers, pas des dossiers de publication.

```
publication/              ← ce que tu publies
  LISEZMOI.md             ← comment poster, et les réglages à faire une seule fois
  PLAN.md                 ← les 17 semaines, semaine par semaine
  calendrier.csv          ← une ligne par publication, pour un tableur
  semaine-01/
    SEMAINE.md            ← les six posts de la semaine, légendes comprises
    1-lundi-fiche-comprendre-anxiete/
      instagram/   les images en 1080 × 1350
      tiktok/      les mêmes en 1080 × 1920
      legende.txt  légende, hashtags, rappels
    2-mardi-bd-lundi-matin-boule-au-ventre/
    3-mercredi-illustre-peur-et-anxiete/
    4-jeudi-fiche-peur-ou-anxiete/
    5-vendredi-bd-reunion-personne-ne-dit-rien/
    6-samedi-illustre-deguisements-anxiete/
```

**99 publications, 17 semaines, six par semaine**, du lundi au samedi. Trois genres, qui
alternent sans jamais se répéter deux jours de suite :

| Genre | Combien | Ce que c'est |
|---|---|---|
| **Fiche** | 39 | texte et pictogrammes — comprendre, distinguer, pratiquer |
| **Illustré** | 30 | personnages dessinés, une idée déroulée écran par écran |
| **BD** | 30 | une scène vécue, bulles et narrateur, la chute à la fin |

Les trois séries n'ont pas la même taille. Un tour de rôle fixe les ferait finir à trois
dates différentes, et les dernières semaines n'offriraient plus qu'un seul genre : elles
sont donc entrelacées proportionnellement, et s'épuisent ensemble. La dernière semaine est
courte — trois publications.

Le fil est tenu par les fiches, qui gardent leur ordre : treize émotions, trois fiches
chacune. Chaque carrousel est ensuite posé près des fiches dont il partage l'émotion, pour
qu'une semaine parle d'une même chose sous trois formes.

Le chiffre en tête de chaque dossier force le bon ordre dans le Finder — sans lui,
« jeudi » passerait avant « lundi ».

## Les trois ateliers

| | |
|---|---|
| `reseaux-sociaux/` | les fiches typographiques — `contenus.py`, `generateur.py` |
| `reseaux-sociaux-illustre/` | les carrousels illustrés — `contenus.json`, `assembleur.py` |
| `reseaux-sociaux-bd/` | les scènes de bande dessinée — `contenus.json`, `assembleur.py` |

Chacun produit ses images dans son propre dossier de sortie. Les images sont hors dépôt :
elles pèsent deux cents mégaoctets.

## Remonter le dossier

Après une modification dans l'un des trois ateliers :

```bash
cd "/Users/cavalier/Dev/Site Emotion"
python3 publication.py
```

Le script efface `publication/` et le remonte entièrement. Il refuse de le faire si le
compte ne tombe pas juste — un carrousel oublié, copié deux fois, ou deux publications du
même genre à la suite.

## Ce qui reste à faire

Neuf illustrations de la série BD datent de la première passe : les crédits nanobanana
étaient épuisés au moment de les refaire. Elles touchent les posts 17, 29 et 30 de cette
série. La marche à suivre est dans `reseaux-sociaux-bd/REPRENDRE.md`.
