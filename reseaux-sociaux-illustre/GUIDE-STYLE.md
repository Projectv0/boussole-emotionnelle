# Guide de style — carrousels illustrés « Boussole émotionnelle »

*Analyse du compte de référence **@betterwithclara** (130 publications, illustrations générées par IA — le compte l'affiche lui-même via la mention « Contenu IA ») et transposition à l'univers de la Boussole émotionnelle.*

---

## 1. Ce qui fait marcher ce style

Trois ingrédients, dans cet ordre d'importance :

1. **Des personnages illustrés qui JOUENT la scène.** Ce ne sont jamais des icônes ni des symboles : ce sont deux personnes attablées, quelqu'un qui détourne le regard, une main qui se lève. Le lecteur se reconnaît avant même d'avoir lu.
2. **Un titre qui promet une distinction.** « 5 tactiques à reconnaître », « Remplace X par Y », « Ce que personne ne voit ». On apprend à nommer quelque chose qu'on vivait sans le savoir.
3. **Une densité assumée.** Chaque image contient 4 à 6 idées complètes. On s'arrête pour lire, on enregistre pour relire — et c'est l'enregistrement qui fait la portée sur Instagram.

Notre avantage : le site possède déjà la matière (14 émotions, les distinctions, 42 pratiques, 22 articles). Il ne manquait que ce vêtement visuel.

## 2. La facture d'illustration

| | |
|---|---|
| **Technique** | Illustration numérique façon crayon de couleur et aquarelle légère : traits de crayon visibles, aplats doux, ombres granuleuses. Jamais de vectoriel plat, jamais de 3D, jamais de photo. |
| **Personnages** | Jeunes adultes, visages très expressifs, proportions légèrement stylisées mais réalistes. Mains dessinées avec soin (elles portent l'émotion autant que le visage). |
| **Cadrage** | Buste ou demi-corps, deux personnages maximum par vignette, assis ou debout en interaction. |
| **Décor** | Suggéré en trois traits : un bord de table, une tasse, une fenêtre, un canapé. Jamais un décor complet qui volerait la vedette. |
| **Fond** | Crème uni `#F7F3EC`, sans cadre ni bordure : les vignettes flottent. |
| **Vêtements** | Mailles et matières douces, couleurs sourdes : vert sauge, rose poudré, lavande, moutarde, bleu ardoise, crème, terracotta. |
| **Cheveux** | Ondulés ou bouclés, châtain, auburn, brun foncé. Signature visuelle forte du style. |
| **Lumière** | Douce, diffuse, légèrement dorée. Aucune ombre dure. |
| **Interdits** | Texte dans l'image (sauf bulle de dialogue courte), logo, filigrane, cadre, fond blanc pur, style cartoon enfantin, hyperréalisme. |

## 3. Palette

```
Fond             #F7F3EC   crème chaud
Encre            #2B2622   presque noir, chaud
Accent principal #B84A31   terracotta (mots-clés des titres, mot final)
Accent secondaire#3F8271   vert sauge profond (repris du site)
Gris de texte    #6E6779   descriptions
Sauge clair      #A8C0B0   · Rose poudré #E0B7B0 · Lavande #B9AECF
Moutarde         #D9A441   · Bleu ardoise #7C93A8 · Crème #EDE3D4
```

Le terracotta et le sauge profond sont exactement ceux de la Boussole : **le style de Clara et la DA du site se rejoignent naturellement.** C'est ce qui permet d'emprunter la forme sans perdre notre identité.

## 4. Typographie

- **Titre de couverture** : capitales, très gras, condensé. Un ou deux mots-clés en terracotta, le reste en encre. Deux à quatre lignes, cadrage centré.
- **Étiquette d'un point** : gras, terracotta, centré sous l'illustration.
- **Description** : sans-serif régulier, gris, une à deux lignes courtes, centrées.
- **Phrase finale** : gras terracotta, pleine largeur, en bas de la dernière diapositive.
- Polices utilisées par l'assembleur : **Avenir Next** (Demi Bold / Medium / Regular) et **Baskerville** pour les accents éditoriaux — celles du site, déjà installées sur le Mac.

## 5. Les six gabarits de mise en page

Repris du compte de référence, tous validés par ses meilleures publications :

| Gabarit | Structure | Quand l'utiliser |
|---|---|---|
| **grille** | 4 à 5 vignettes en 2 colonnes, étiquette + description sous chacune | inventaires : « 5 façons dont… » |
| **liste** | vignette étroite à gauche, texte à droite, 4 à 5 lignes | énumérations narratives |
| **duo** | deux colonnes opposées, illustration en haut de chaque, puces dessous | oppositions : X contre Y |
| **avant-apres** | deux blocs empilés, « Avant » / « Maintenant » | évolutions, ce qui change |
| **etapes** | 1, 2, 3, 4 numérotés dans des pastilles, illustration à côté | méthodes, protocoles |
| **remplace** | « Au lieu de : … » / « Dis : … », deux illustrations | reformulations de phrases |

## 6. Structure d'un carrousel

Cinq à sept diapositives, format **1080 × 1350** (4:5) :

1. **Couverture** — le titre + deux à quatre vignettes de personnages. C'est elle qui décide si on s'arrête.
2 à 5. **Le développement** — une idée par diapositive, illustration large en haut, étiquette et texte dessous. *(Ou une seule diapositive dense au gabarit « grille » si le sujet s'y prête.)*
6. **La phrase qui reste** — une seule ligne en terracotta sur fond crème, sans illustration.
7. **L'appel** — « Et toi, quelle place occupent-elles&nbsp;? » + boussole-emotionnelle.fr.

## 7. Chaîne de production

```
1. contenus.py        les 30 posts (textes + quelles illustrations il faut)
2. python3 prompts.py  génère les fichiers de prompts Nano Banana, un par post
3. Nano Banana         tu génères les illustrations, tu les déposes dans illustrations/
4. python3 assembleur.py   compose illustrations + typographie → sortie/
5. publication         chaque dossier contient les diapositives et la légende
```

**Règle d'or de la cohérence** : chaque prompt se termine par le **suffixe de style** (défini dans `prompts/00-style.md`). C'est lui, et lui seul, qui garantit que la trentième illustration ressemble à la première. Ne jamais le modifier en cours de série.

## 8. Ce qui nous distingue du compte de référence

Nous reprenons la forme, pas le fond. Trois différences volontaires :

- **Pas de contenu genré.** Le compte de référence s'adresse explicitement aux femmes (« High value woman », « 5 things women carry »). Nos contenus parlent à tout le monde : personnages variés, formulations neutres.
- **Pas de vocabulaire de diagnostic ni d'accusation.** Ni « manipulateur », ni « toxique », ni « narcissique ». On explique des mécanismes, on ne désigne pas des coupables — c'est la ligne du site, et elle nous protège juridiquement autant qu'éditorialement.
- **Une source.** Chaque post renvoie au test ou à un article du guide : notre contenu est adossé à un outil, pas à une opinion.
