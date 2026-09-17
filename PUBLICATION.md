# Publier — par où commencer

Tout ce qui se publie est dans **`publication/`**. Ouvre `publication/PLAN.md` et suis les
semaines : c'est le seul document nécessaire. Les deux autres dossiers sont des ateliers,
pas des dossiers de publication.

```
publication/              ← ce que tu publies
  PLAN.md                 ← les 13 semaines, semaine par semaine
  semaine-01/
    1-lundi-comprendre-anxiete/
      instagram/   6 images en 1080 × 1350
      tiktok/      les mêmes en 1080 × 1920
      legende.txt  légende, hashtags, rappels
    2-mardi-illustre-message-sans-reponse/
    3-mercredi-peur-ou-anxiete/
    4-jeudi-illustre-boule-au-ventre-lundi/
    5-vendredi-respiration-expiration-longue/
    6-samedi-illustre-expiration-longue/
```

**69 publications, 13 semaines, cinq à six par semaine**, en alternant un jour sur deux les
deux formats : typographique le lundi, le mercredi et le vendredi, illustré le mardi, le jeudi,
et le samedi quatre semaines sur treize.

Le chiffre en tête force le bon ordre dans le Finder — sans lui, « jeudi » passerait avant
« lundi ». Le mot `illustre` distingue les deux formats quand ils traitent le même geste :
en semaine 1, le vendredi donne la respiration à expiration longue et le samedi explique
pourquoi elle agit et pourquoi il faut s'y entraîner avant d'en avoir besoin.

---

## Les deux ateliers

| | |
|---|---|
| **`reseaux-sociaux/`** | les 39 carrousels typographiques. Textes dans `contenus.py`, mise en page dans `generateur.py`. |
| **`reseaux-sociaux-illustre/`** | les 30 carrousels illustrés. Textes et prompts dans `contenus.json`, mise en page dans `assembleur.py`, 287 illustrations dans `illustrations/`. |

## Tout reconstruire

```bash
python3 reseaux-sociaux/generateur.py          # 39 posts typographiques, 2 formats
python3 reseaux-sociaux-illustre/assembleur.py # 30 carrousels illustrés, 2 formats
python3 calendrier.py                          # vérifie la répartition, écrit calendrier.json
python3 publication.py                         # monte publication/
```

`calendrier.py` refuse d'écrire si un carrousel illustré est oublié ou placé deux fois : dans
un fichier de treize semaines, l'erreur ne se voit pas à l'œil, mais elle se voit tout de suite
une fois les images copiées.

## Changer la répartition

`repartition.json` dit, pour chaque semaine, quel carrousel illustré tombe le mardi, le jeudi
et le samedi (`null` quand la semaine n'en a que deux). Modifie-le, relance `calendrier.py`
puis `publication.py`. Les contraintes : les 30 carrousels placés une fois chacun, et
exactement quatre semaines avec un samedi — quatre fois trois plus neuf fois deux font trente.

## Après ces treize semaines

Le rythme d'un jour sur deux est fait pour tenir. Si tu veux ralentir, garde lundi, mercredi et
vendredi et publie les illustrés une semaine sur deux : tu tiendras alors près de six mois avec
le même dossier.
