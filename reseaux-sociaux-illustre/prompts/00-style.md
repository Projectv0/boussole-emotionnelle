# Le suffixe de style — à coller à la fin de CHAQUE prompt

C'est la pièce la plus importante du dossier. Ce bloc garantit que les centaines d'illustrations de la série se ressemblent. **Ne le modifie jamais en cours de série** : une seule variation et la grille Instagram perd son unité.

---

## Suffixe (à copier tel quel)

```
Style: soft digital illustration, colored pencil and light watercolor texture, visible
pencil linework, gentle grain, warm diffused lighting, no harsh shadows. Semi-realistic
young adult characters with very expressive faces and carefully drawn hands, slightly
stylized proportions. Wavy or curly hair in auburn, chestnut or dark brown. Cozy knitwear
in muted tones: sage green, dusty rose, lavender, mustard, slate blue, cream, terracotta.
Minimal setting suggested with just a few elements. Plain warm cream background #F7F3EC,
no frame, no border, the vignette floats on the background. Square composition, characters
framed from the waist up. NO text, NO letters, NO words, NO watermark, NO logo anywhere in
the image. Not cartoon, not 3D, not photorealistic, not vector flat.
```

## Mode d'emploi dans Nano Banana

1. **Une image à la fois**, format carré (1:1). L'assembleur recadre ensuite.
2. Structure d'un prompt complet :
   ```
   [LA SCÈNE — deux ou trois phrases précises]
   [LES ÉMOTIONS SUR LES VISAGES — explicite, c'est le cœur du sujet]
   [LE SUFFIXE DE STYLE ci-dessus]
   ```
3. **Nomme le fichier exactement** comme indiqué dans le fichier de prompts du post (`p03-02.png` = post 3, illustration 2). L'assembleur ne trouve rien sans ça.
4. Dépose tout dans `illustrations/`. Le format PNG ou JPG, au moins 1024 × 1024.

## Les six réglages qui font la différence

- **Nomme l'émotion sur le visage, jamais l'étiquette abstraite.** « sourcils légèrement froncés, regard qui fuit, épaules rentrées » fonctionne ; « elle ressent de la honte » ne donne rien.
- **Deux personnages maximum.** Au-delà, les visages se dégradent.
- **Donne un propriétaire à chaque main.** C'est la règle la plus rentable du dossier : sur 287 illustrations, tous les bras fantômes venaient d'un prompt qui parlait d'« une main sur son épaule » sans dire de qui. Écris toujours « sa main à elle », « l'une de ses deux mains », et compte les mains de la scène avant de lancer.
- **Décris les mains** quand elles portent la scène (une main qui se lève, qui tient une tasse, qui repose sur le bras de l'autre).
- **Interdis le texte explicitement** — c'est la première cause d'image inutilisable, le modèle ajoute spontanément des mots déformés.
- **Si une bulle de dialogue est prévue**, ne la demande PAS à Nano Banana : l'assembleur la dessine proprement avec du vrai texte français.

## Si une illustration rate

Les ratés classiques et leur correction :

| Symptôme | Correction à ajouter au prompt |
|---|---|
| Du texte apparaît | `absolutely no text, no signage, no writing of any kind, no numbers, any screen is blank and dark` |
| Visage déformé, œil manquant | réduire à **un seul** personnage, ajouter `clear detailed face, both eyes clearly visible, open and symmetrical` |
| Main fondue, doigts en trop, bras sans personne | `Each character has exactly two arms and two hands; every visible hand connects to a visible arm and shoulder that are themselves in frame, with exactly five clearly separated fingers and no extra hand anywhere` |
| Fond coloré ou décor envahissant | `completely plain flat cream background, subject isolated, minimal props` |

**Ce qu'il ne sert à rien de demander.** Une heure précise sur une horloge : le modèle dessine des aiguilles au hasard et ajoute une main de plus à chaque tentative. Si la scène a besoin d'une heure, change la scène — c'est le regard qui doit dire la fin de journée, pas un cadran.

## Variété des personnages

Le compte de référence n'illustre presque que des femmes jeunes et blanches. **Nous faisons autrement**, à la fois par justesse et parce que notre public est plus large. Fais tourner, d'une illustration à l'autre :

- âges : jeune adulte, trentaine, quarantaine, personne âgée ;
- carnations et origines variées ;
- hommes et femmes en proportions équilibrées ;
- morphologies différentes.

Chaque prompt du dossier précise déjà le personnage. Suis-les : la rotation est calculée à l'échelle des 30 posts.
