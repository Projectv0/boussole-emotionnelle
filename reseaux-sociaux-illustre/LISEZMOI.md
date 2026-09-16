# Carrousels illustrés — mode d'emploi

30 carrousels Instagram et TikTok dans le style de **@betterwithclara** : personnages illustrés,
fond crème, titres percutants — appliqué aux 14 émotions de la Boussole.

---

## Ce que contient le dossier

| | |
|---|---|
| **GUIDE-STYLE.md** | l'analyse du style de référence et la charte à respecter. À lire en premier. |
| **contenus.json** | les 30 posts : titres, textes, prompts. La source de tout le reste. |
| **prompts/00-style.md** | le suffixe de style — la pièce qui garantit la cohérence des 285 illustrations. |
| **prompts/post-XX-*.md** | une fiche par post : chaque prompt prêt à coller, avec le nom de fichier attendu. |
| **prompts/TOUS-LES-PROMPTS.md** | tous les prompts à la suite, pour enchaîner les générations. |
| **illustrations/** | les 285 images sorties de Nano Banana. Hors dépôt (206 Mo). |
| **sortie/** | les carrousels finis : 186 diapositives + une légende par post. Hors dépôt. |
| **assembleur.py** | compose illustrations + typographie. |
| **prompts.py** | régénère les fiches de prompts depuis contenus.json. |

## La boucle de production

```bash
# 1. voir la mise en page AVANT de générer quoi que ce soit
python3 assembleur.py 1
#    → sortie/01-.../ avec des cadres pointillés à la place des illustrations

# 2. ouvrir prompts/post-01-....md, générer les illustrations dans Nano Banana,
#    les déposer dans illustrations/ avec EXACTEMENT le nom indiqué

# 3. recomposer — cette fois avec les vraies images
python3 assembleur.py 1

# 4. quand tout est généré
python3 assembleur.py          # les 30 posts d'un coup
```

**Commence par un seul post.** Génère ses illustrations, regarde le résultat composé, ajuste si
besoin le suffixe de style — puis enchaîne les 29 autres avec le réglage validé. C'est ce qui
évite de refaire cent images.

## Nommer les fichiers

Chaque fiche de prompt indique le nom attendu, par exemple `p03-02.png`. L'assembleur ne cherche
rien d'autre : un fichier mal nommé laisse un cadre pointillé. Formats acceptés : `.png`, `.jpg`,
`.jpeg`, `.webp`. Taille minimale conseillée : 1024 × 1024 (carré — l'assembleur recadre au centre).

## Modifier un texte

Tout est dans `contenus.json`. Change un titre, une phrase, une étiquette, puis relance
`python3 assembleur.py <numéro>`. Si tu touches à un prompt, relance aussi `python3 prompts.py`
pour mettre à jour les fiches.

## Publier

Chaque dossier de `sortie/` contient les diapositives numérotées et `legende.txt` (légende +
hashtags + rappel de publication).

- **Instagram** : nouvelle publication → carrousel → les images dans l'ordre → coller la légende.
- **TikTok** : mode Photo → les mêmes images → un son doux en tendance.

Le rythme conseillé reste **3 posts par semaine**. Avec 30 carrousels, tu tiens dix semaines —
et le dossier `reseaux-sociaux/` (39 posts typographiques, sans illustration) en couvre treize
autres si tu veux alterner les deux formats.

## Les trois pièges à éviter

1. **Modifier le suffixe de style en cours de série.** La grille Instagram perd son unité
   immédiatement, et ça se voit plus que n'importe quel défaut individuel.
2. **Laisser Nano Banana écrire du texte.** Il déforme systématiquement les mots. Les bulles de
   dialogue sont dessinées par l'assembleur, en vrai français : ne les demande jamais à l'image.
3. **Générer les 285 illustrations avant d'en avoir composé une seule.** Une passe de validation
   sur un post complet coûte dix minutes et peut en économiser des heures.
