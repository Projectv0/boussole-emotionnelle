# Le style « scène vécue » — analyse et charte

*Écrit après l'analyse du compte @darkybloom (162 k abonnés, 212 publications), que Martial
a désigné comme référence visuelle. Ce document dit ce qu'on lui emprunte, ce qu'on ne lui
emprunte pas, et pourquoi.*

---

## Ce que fait le compte de référence

Chaque publication est une **scène de la vie courante qui se déroule diapositive après
diapositive**, comme une planche de bande dessinée. Pas une liste de conseils : un moment
qu'on regarde se jouer.

Trois éléments portent tout le format.

**Le titre est un horodatage.** « CE MIDI. UNE TENSION. RIEN DE GRAVE. » « 7 H 30. ELLE SE
LÈVE. BONNE ÉNERGIE. » « DANS LE LIT. IL SE RAPPROCHE. » On sait quand, on sait qui, on ne
sait pas encore quoi. C'est ce qui fait glisser vers la deuxième diapositive.

**Les bulles disent la banalité.** Les répliques sont volontairement plates — « T'inquiète,
c'est bon, on en parle plus », « Je t'aime », « Ça va ». Personne ne déclame. C'est un
dialogue de tous les jours.

**Le narrateur dit la vérité.** De courtes phrases en majuscules, posées dans l'image, qui
révèlent ce que les personnages ne disent pas : « ELLE Y CROIT VRAIMENT. » « IL PEUT PAS
SAVOIR. » « SON CORPS GARDE LA MÉMOIRE DE SA JOURNÉE. » « MÊME GESTE. PAS LE MÊME SOIR. »

**C'est l'écart entre les deux qui fait le post.** La bulle dit « ça va », le narrateur dit
« elle fait semblant ». Sans cet écart, il ne reste qu'une illustration bavarde. C'est la
seule chose qu'il faut vraiment comprendre de ce format.

Une diapositive revient souvent, et elle est remarquable : le personnage seul, entouré de
bulles de pensée contenant des mini-scènes de sa journée — la réunion de 9 h, la collègue,
le trajet bondé. Le monde intérieur rendu visible. À reprendre.

## Ce qu'on lui emprunte

- Le registre graphique : illustration de bande dessinée, traits noirs épais, visages très
  expressifs, grands yeux, couleurs chaudes.
- La palette : terre cuite et rouille, crème, bruns, roses poudrés, verts de plantes éteints.
- La typographie : une condensée grasse pour le titre, en capitales, sur un bandeau crème.
- Le format narratif : horodatage en titre, bulles banales, narrateur qui révèle.
- Le rythme : quatre à cinq diapositives, la dernière fait basculer la lecture.

## Ce qu'on ne lui emprunte pas, et pourquoi

**Sa distribution.** Le compte met en scène une héroïne unique — longs cheveux noirs bouclés,
créoles, t-shirt noir — et un gros chat roux qui revient dans presque chaque image. C'est sa
signature de marque, reconnaissable entre mille par ses 162 000 abonnés. La reprendre nous
ferait passer pour une copie, et à juste titre.

**Nous faisons l'inverse, et c'est un choix éditorial autant qu'une précaution.** Aucun
personnage récurrent, aucune mascotte. D'une scène à l'autre, les âges tournent — vingtaine,
trentaine, quarantaine, cinquantaine, personnes âgées —, les carnations et les origines
varient, les genres s'équilibrent, les morphologies aussi. Le lecteur ne suit pas une
héroïne : il se reconnaît dans des gens différents de lui.

**Son sujet.** Le compte parle d'hypersensibilité. Nous parlons des quatorze émotions. Le
territoire se recoupe, la promesse n'est pas la même : eux proposent une identité à laquelle
appartenir, nous proposons de nommer ce qu'on ressent. Aucune de nos scènes ne doit reprendre
un de leurs sujets.

**Ses publications.** Aucun texte, aucune réplique, aucun concept de post repris. Les trente
scènes sont écrites depuis nos propres thèmes.

## Les règles de fabrication

**Le texte n'est jamais demandé à l'image.** Le générateur déforme systématiquement les mots.
Le prompt décrit la scène, les visages, les gestes — jamais un mot écrit. L'assembleur dessine
ensuite les bulles et le narrateur en vrai français. Un prompt contenant `speech bubble`,
`text`, `sign`, `writing` est à refaire.

**Deux personnages maximum par image.** Au-delà, les visages se dégradent.

**Chaque main visible appartient à un personnage visible**, avec cinq doigts séparés. C'est
la règle qui a coûté le plus cher sur la série précédente : tous les bras fantômes venaient
d'un prompt qui parlait d'une main sans dire à qui elle était.

**De la place pour les bulles.** Les personnages se tiennent plutôt dans le bas du cadre, le
haut reste calme. Sans ça, une bulle finit sur un visage.

**Ne demande jamais une heure précise sur une horloge.** Le modèle dessine des aiguilles au
hasard et ajoute une main à chaque tentative. Si la scène a besoin d'une heure, c'est le titre
qui la donne.

## Le suffixe de style

À coller à la fin de chaque prompt, sans jamais le modifier en cours de série — c'est lui qui
tient l'unité des cent cinquante illustrations.

```
Style: bold comic book illustration, thick clean black outlines, flat warm colours with soft
cel shading, expressive faces with large round eyes, slightly stylized proportions. Warm
palette: terracotta, rust orange, cream, warm brown, dusty rose, muted sage. Cosy domestic
setting suggested with few props. Characters placed in the lower two thirds of the frame, the
upper area calm and uncluttered. Portrait composition, characters framed from the waist up.
NO text, NO letters, NO words, NO speech bubbles, NO signage, NO watermark anywhere in the
image. Not photorealistic, not 3D, not vector flat, not manga.
```

## Les quatre pièges

1. **Un narrateur qui répète la bulle.** S'il dit la même chose, il ne sert à rien. Il doit
   dire ce que le personnage ne s'avoue pas.
2. **Un autre personnage traité en méchant.** Il ne sait pas, c'est tout. C'est ce qui rend
   la scène utile plutôt que revancharde — et c'est ce que le compte de référence réussit.
3. **Un diagnostic déguisé.** On nomme l'émotion, jamais la personne.
4. **Une scène trop générale.** « Elle est fatiguée » n'accroche personne. « Elle a répondu
   "ça va" trois fois aujourd'hui » accroche tout le monde.
