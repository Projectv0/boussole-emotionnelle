# Audit des 591 diapositives

*Mené le 19 septembre 2026 sur le dossier `publication/` : 99 publications, 591
diapositives, aux deux formats. Chaque image a été ouverte et regardée ; chaque défaut
signalé a ensuite été soumis à un second lecteur chargé de le réfuter. Seuls les
constats ayant survécu à cette contradiction figurent ici — 201 sur un bien plus grand
nombre de signalements bruts.*

## Ce qui a été vérifié mécaniquement, donc exhaustivement

Ces contrôles ne dépendent d'aucun jugement et couvrent la totalité du corpus.

| Contrôle | Outil | Résultat |
|---|---|---|
| Orthographe et grammaire | `orthographe.swift` — correcteur français de macOS | **aucune faute** sur 150 868 caractères |
| Caractère sans glyphe | `controle-textes.py` | 1 trouvé (« → »), corrigé |
| Apostrophe et ponctuation | `controle-textes.py` | 784 apostrophes droites, corrigées |
| Texte coupé ou débordant | mesure de chaque ligne dans les trois générateurs | **0** |
| Ordre de lecture des bulles | `assembleur.py` | **0 inversion** |
| Bulle sur le bandeau, hors cadre, chevauchement | idem | **0** |
| Arrondi dégénéré | idem | **0** sur 744 formes |
| Position des têtes visées | `controle-tetes.py` | 30 vérifiées une à une |

## Ce que la relecture à l'œil a trouvé

| Axe | Constats | dont bloquants |
|---|---|---|
| francais | 104 | 1 |
| autre | 44 | 4 |
| placement-bulle | 20 | 1 |
| forme-de-bulle | 18 | 0 |
| visibilite-personnage | 11 | 3 |
| texte-coupe | 3 | 0 |
| ordre-de-lecture | 1 | 0 |
| **Total** | **201** | **9** |

Réparties sur 77 publications des 99. Par genre : BD 114 · Illustré 47 · Fiche 40.

## Déjà corrigé depuis l'audit

20 constats sont traités — la cause était commune à plusieurs diapositives :

- question réécrite sans son « Et toi » initial — 14 constats
- « PERSONNE NE PARLE » rétabli — 1 constat
- flèche « → » remplacée : Avenir Next n'a pas ce glyphe — 2 constats
- phrase réécrite en nommant la soirée et le corps — 1 constat
- letterbox noir rogné (calme-soir-fenetre-ouverte) — 2 constats

## Ce qui reste

181 constats. Presque tous sont des choix d'écriture — une répétition, une
tournure lourde — qui demandent un arbitrage, pas une correction automatique. Ils sont
rangés par gravité puis par semaine.

### Bloquant — 5

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 3 · *visibilite-personnage*

> Le mari n'est pas reconnaissable : il change de teint et de chevelure par rapport aux autres diapositives.

À faire : Régénérer la diapositive 3 avec le mari tel qu'il apparaît sur les diapos 1, 2, 4 et 5 : peau brune soutenue, dessus du crâne chauve et front dégagé, cheveux blancs seulement sur les tempes et les côtés, visage large, grosse moustache blanche.

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 4 · *visibilite-personnage*

> La bulle « EN FAIT NON. MERCI D’ÊTRE VENUE, ÇA ME TOUCHE. » est posée en plein sur le visage du garçon et lui masque les deux yeux. C'est la diapositive du basculement de l'histoire (il dit merci pour la première fois) et on ne voit pas son regard. Il faut remonter la bulle au-dessus de sa tête ou la décaler vers la droite, dans le vide au-dessus de l'oreiller.

À faire : Déplacer la bulle « EN FAIT NON. MERCI D'ÊTRE VENUE, ÇA ME TOUCHE. » vers le haut et la droite, dans le mur vide au-dessus de l'oreiller (bord inférieur du cadre remonté au-dessus de la chevelure, vers y≈440 max, et cadre décalé pour démarrer à droite de la tête), en laissant la queue descendre en oblique vers sa bouche sans recouvrir les yeux.

**semaine-15 · 6-samedi-bd-quarante-longueurs** — diapositive 5 · *visibilite-personnage*

> La bulle de pensée « Ça fait cet effet-là, quand quelqu’un me prend au sérieux. » est posée en plein sur le visage de la nageuse de gauche et masque tout le haut de sa figure : front, sourcils et yeux. Il ne reste visible que la bouche ouverte et le menton. C’est précisément la case où le bandeau annonce « ELLE SOURIT ENFIN POUR DE BON, SANS SE RETENIR » : l’émotion que la case doit montrer est cachée. La bulle devrait être remontée dans l’espace vide au-dessus de sa tête ou décalée vers la gauche.

À faire : Remonter la bulle de pensée d'environ 180 px, dans l'espace de carrelage vide entre la bulle « SIX LONGUEURS EN JANVIER, ET QUARANTE CE MATIN. » et le haut de ses cheveux, afin de dégager entièrement son front et ses yeux.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 3 · *placement-bulle*

> La bulle de dialogue « ALLEZ, IL FAUT QUE J'Y AILLE MAINTENANT. » est posée hors du dessin, dans la bande beige vide du haut, et sa queue ne désigne personne : elle s'arrête sur le trait noir qui borde le haut de la case.

À faire : Descendre la bulle « ALLEZ, IL FAUT QUE J'Y AILLE MAINTENANT. » à l'intérieur du dessin, en haut du cadre et légèrement à droite au-dessus de la tête du personnage — plus haut que la bulle de pensée pour qu'elle se lise en premier — avec une queue courte, d'épaisseur régulière, dirigée vers son visage et ne franchissant aucun bord de case.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 3 · *autre*

> Rupture de continuité : le compagnon n'est plus le même personnage qu'aux diapositives 1 et 2, et l'homme aux cheveux blancs a rajeuni de trente ans. Le lecteur ne peut plus suivre qu'il s'agit du même couple d'une image à l'autre.

À faire : Régénérer la diapositive 3 avec les mêmes personnages que les diapositives 1 et 2 : à droite, l'homme noir d'environ 70 ans, cheveux blancs ras et crépus, lunettes rondes en écaille et gilet crème ; à gauche, le même homme aux cheveux blancs avec son visage marqué de septuagénaire (rides frontales, sillons naso-géniens, bajoues), en conservant les bulles et le bandeau actuels.

### Visible — 97

**semaine-02 · 1-lundi-fiche-respiration-expiration-longue** — diapositive 1 · *autre*

> La publication est programmée le lundi (dossier « 1-lundi », SEMAINE.md : « Lundi — Fiche · La respiration ») mais l'étiquette imprimée sur la couverture annonce le vendredi. Le générateur code cette mention en dur : reseaux-sociaux/generateur.py ligne 38, « pratique » : jour="vendredi", etiq="LA PRATIQUE DU VENDREDI · {n}/13 ».

À faire : Retirer la mention du jour de l'étiquette de la série : remplacer, à la ligne 38 de reseaux-sociaux/generateur.py, etiq="LA PRATIQUE DU VENDREDI · {n}/13" par etiq="LA PRATIQUE · {n}/13", puis régénérer les couvertures des 13 fiches de la série « pratique » (à défaut, reprogrammer cette publication le vendredi, mais cela ne réglerait que 1 des 10 cas fautifs).

**semaine-02 · 2-mardi-bd-message-du-patron-samedi** — diapositive 1 · *placement-bulle*

> La queue de la bulle de la mère part vers le bas alors que sa tête est au-dessus de la bulle : elle désigne son avant-bras/sa manche au lieu de son visage. Sur toutes les autres cases, les queues remontent vers la tête du locuteur (voir diapositive 3), l'incohérence saute aux yeux.

À faire : Déplacer la queue de la bulle de la mère du bord inférieur vers le bord SUPÉRIEUR de la bulle, en la faisant sortir vers x ≈ 330–370 et pointer vers le haut en direction de son menton (~355, 800), sans le toucher — ou, à défaut, remonter la bulle entière au-dessus de sa tête comme sur les diapositives 2 et 3 et garder la queue descendante.

**semaine-02 · 2-mardi-bd-message-du-patron-samedi** — diapositive 2 · *francais*

> Répétition du mot « MESSAGE » d'une ligne à l'autre dans le bandeau du narrateur. La deuxième occurrence est inutile : « elle a déjà imaginé dix versions » suffit, ou « dix versions de ce qu'il contient ».

À faire : Remplacer la deuxième phrase du bandeau par « DANS SA TÊTE, ELLE EN A DÉJÀ IMAGINÉ DIX VERSIONS. » — la répétition disparaît et le bandeau tient sur deux lignes, sans ligne orpheline.

**semaine-02 · 3-mercredi-illustre-deguisements-colere** — diapositive 4 · *francais*

> Trois lignes consécutives, deux répétitions : « trop loin » revient dans le titre puis dans la phrase suivante, et « quand » est employé trois fois de suite (titre, « quand quelqu'un », « Quand tu n'arrives pas »). Le texte tourne en rond. De plus le pronom de « à le dire » n'a pas d'antécédent clair (la colère est féminine).

À faire : Remplacer les deux lignes du corps par « La colère te signale qu'une limite a été franchie. / Si tu ne dis rien, elle ressort autrement. » — le titre « Quand on va trop loin » peut rester tel quel, il n'est plus repris ; cela supprime les trois « quand », l'écho « va trop loin » et le pronom « le » ambigu, et répond enfin au titre de la diapositive « À QUOI ELLE SERT ».

**semaine-02 · 5-vendredi-bd-la-phrase-repetee-depuis-deux-ans** — diapositive 4 · *placement-bulle*

> La bulle « LAISSE TOMBER, JE VAIS LA FIXER MOI-MÊME. » est posée tout en haut à gauche, très loin du personnage qui la prononce, et sa queue se termine en plein mur vide sans jamais désigner personne. Il faut descendre des yeux sur la moitié de l'image pour deviner qui parle. Rapprocher la bulle du personnage aux dreadlocks (la descendre d'environ 300 px) et raccourcir la queue.

À faire : Descendre la bulle d'environ 330 px (bas de la bulle amené de y≈222 à y≈550, dans l'espace crème libre au-dessus du personnage) et raccourcir sa queue de 233 px à ~80 px, pour que la pointe s'arrête vers y≈630, soit une cinquantaine de pixels au-dessus des dreadlocks — comme sur les diapositives 02, 03 et 05.

**semaine-02 · 5-vendredi-bd-la-phrase-repetee-depuis-deux-ans** — diapositive 1 · *forme-de-bulle*

> La queue de la bulle de droite (« OUI JE SAIS, JE VAIS LE FAIRE CE WEEK-END. ») est démesurément longue et fine : elle traverse toute l'étagère et ses bocaux avant de venir se planter dans les cheveux du personnage, alors qu'une queue doit s'arrêter à distance de la tête. Son tracé est aussi plus mince que le contour de la bulle. À comparer avec la queue de la bulle de gauche, courte et bien proportionnée, qui est correcte.

À faire : Raccourcir la queue de la bulle de droite en un triangle court et large, comme celle de gauche, dont la pointe s'arrête nettement au-dessus de l'étagère et à bonne distance des cheveux de l'homme au pull gris, au lieu du long V effilé qui descend devant les bocaux et se plante dans sa chevelure.

**semaine-02 · 5-vendredi-bd-la-phrase-repetee-depuis-deux-ans** — diapositive 1 · *francais*

> « Samedi » apparaît trois fois dans le tiers supérieur, et le titre annonce déjà la réplique que la bulle va dire juste en dessous, ce qui tue l'effet. Alléger, par exemple : titre « SAMEDI, 11 H. LA MÊME PHRASE QUE LA SEMAINE DERNIÈRE. », ou retirer « SAMEDI DERNIER » de la bulle.

À faire : Remplacer le texte de la bulle de gauche par « TU DEVAIS FIXER CETTE ÉTAGÈRE. », le titre portant déjà « samedi dernier ».

**semaine-02 · 6-samedi-illustre-dispute-en-boucle** — diapositive 1 · *visibilite-personnage*

> Dans la vignette en haut à droite, un deuxième personnage est coupé par le bord du cadre et réduit à une manche verte sans tête ni visage : on ne le distingue pas comme une personne, on voit un bras vert isolé. Recadrer pour faire entrer le visage, ou recadrer plus serré pour l'exclure complètement.

À faire : Dans la vignette en haut à droite, effacer entièrement le personnage vert (manche, main et bande de torse) et prolonger le mur clair jusqu'au bord de la vignette, pour ne laisser que l'homme au pull orange bras croisés près de la fenêtre ; ou, si l'on tient à garder un second personnage, régénérer la vignette avec une tête et un visage entièrement visibles.

**semaine-02 · 6-samedi-illustre-dispute-en-boucle** — diapositive 3 · *francais*

> Le verbe « écouter » revient trois fois sur la même diapositive, et le corps de texte reprend mot pour mot la fin du titre. Varier : par exemple « plus rien ne passe » dans le corps de texte, pour garder « plus personne n'écoute » au titre seul.

À faire : Dans le corps de texte de la diapositive 3, remplacer « À partir de là, vous avez beau parler, plus personne n'écoute. » par « À partir de là, vous avez beau parler, plus rien ne passe. » (titre et bulle inchangés).

**semaine-03 · 1-lundi-fiche-colere-ou-agressivite** — diapositive 2 · *francais*

> Tournure bancale : « quelque chose d’important vient d’être franchi ». On franchit une limite, un seuil, une ligne — pas « quelque chose ». Écrire par exemple « une limite importante vient d’être franchie ».

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py ligne 102, remplacer « quelque chose d’important vient d’être franchi » par « une limite importante vient d’être franchie », puis régénérer 02.jpg (dossiers instagram/ et tiktok/).

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 1 · *francais*

> La même formule revient deux fois dans la même image : « comme tous les soirs » en haut, « comme presque tous les soirs » dans le bandeau du bas. L’effet d’écho tombe à plat parce que les deux se lisent en même temps. En garder une seule.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json, remplacer le "titre" de la publication « meme-geste-pas-le-meme-soir » par "22 H 40.|IL SE RAPPROCHE." (supprimer « COMME TOUS LES SOIRS. »), puis régénérer la diapositive 1 — le bandeau du bas conservant « IL POSE SA MAIN SUR LA SIENNE, COMME PRESQUE TOUS LES SOIRS DEPUIS VINGT-DEUX ANS. »

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 1 · *autre*

> Bande blanche non dessinée sur tout le bord droit de l’image (environ 30 à 40 px de large sur les 1350 px de hauteur), après le trait noir du cadre. Sur un carrousel plein cadre, ce liseré blanc se voit tout de suite. Recadrer ou étendre le dessin jusqu’au bord.

À faire : Recadrer la diapositive sur ses 1032 px de gauche (en retirant le trait noir vertical, le trait parasite et les 41 px blancs), puis la remettre au format 1080×1350 — ou, à défaut, prolonger le décor jusqu'au bord droit.

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 3 · *visibilite-personnage*

> Le visage de l’homme est coupé en deux par le bord droit du cadre : on ne voit que l’oreille, la joue, la barbe et la moitié d’un œil, le nez et la bouche sont hors champ. Le deuxième personnage de la scène devient difficile à identifier. Élargir ou décaler le cadrage.

À faire : Régénérer la diapositive en décalant le cadrage vers la droite (ou en l'élargissant d'environ 120 px) pour que la tête de l'homme tienne entièrement dans l'image, nez et bouche compris — ou, à l'inverse, reculer la coupe pour ne laisser que l'arrière du crâne et l'épaule, comme sur la diapositive 2.

**semaine-03 · 3-mercredi-fiche-la-pause-annoncee** — diapositive 1 · *autre*

> Le nom de rubrique annonce le mauvais jour : « LA PRATIQUE DU VENDREDI » sur une publication programmée le mercredi (SEMAINE.md : mercredi = « La pause annoncée », vendredi = la fiche sur la honte). Corriger le libellé ou déplacer la publication.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/generateur.py ligne 38, rendre l'étiquette neutre comme les deux autres rubriques — remplacer etiq="LA PRATIQUE DU VENDREDI · {n}/13" par etiq="LA PRATIQUE · {n}/13" — puis régénérer et recopier les 13 couvertures « pratique » dans publication/, ce qui corrige d'un coup cette diapositive et les huit autres mal étiquetées sans toucher au calendrier.

**semaine-03 · 6-samedi-bd-le-silence-du-retour** — diapositive 2 · *visibilite-personnage*

> Le personnage masculin (le passager) n'est pas lisible : son visage est coupé par le bord droit du cadre et toute la zone des yeux est avalée par une masse noire qui se confond avec le fond de nuit. On ne voit ni ses yeux ni son regard, alors que c'est lui dont la planche raconte le silence.

À faire : Régénérer la diapositive 2 en recadrant vers la gauche pour que la tête entière du passager (nez et bouche compris) tienne dans le cadre, et en éclairant son visage (lueur du tableau de bord ou des lampadaires) pour que ses yeux et ses sourcils soient réellement dessinés au lieu de se fondre dans le noir du fond de nuit.

**semaine-03 · 6-samedi-bd-le-silence-du-retour** — diapositive 1 · *forme-de-bulle*

> La queue de la bulle de gauche (« C'ÉTAIT BIEN, NON ?… ») est une aiguille très longue et très fine : son intérieur blanc s'éteint bien avant la pointe, et les 20 derniers pixels ne sont plus qu'un trait noir plein qui entre dans la chevelure de la conductrice au lieu de s'arrêter au-dessus. Rien à voir avec la queue de la bulle de droite, courte et franchement triangulaire, sur la même diapositive.

À faire : Refaire la queue de la bulle de gauche sur le modèle de celle de droite : un triangle court et large (environ 40 px de haut, partant de la bordure basse de la bulle à y=518 et s'arrêtant vers y=560), à intérieur blanc jusqu'à la pointe, à contour d'épaisseur constante, se terminant nettement au-dessus de la chevelure de la conductrice (dont le contour commence à y≈682) sans jamais la toucher.

**semaine-04 · 3-mercredi-bd-repas-de-famille-la-remarque** — diapositive 6 · *francais*

> « Elle croit sincèrement s'inquiéter » dit qu'elle se trompe sur son propre sentiment, alors que toute la publication dit l'inverse : elle s'inquiète pour de bon.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json ligne 974, remplacer « Elle croit sincèrement s’inquiéter pour ta santé » par « Elle s’inquiète sincèrement pour ta santé », puis régénérer la diapositive 6.

**semaine-04 · 6-samedi-bd-diner-faire-semblant** — diapositive 5 · *placement-bulle*

> La queue de la bulle de dialogue descend jusque dans la chevelure de l'homme et s'arrête à la racine des cheveux, au lieu de s'arrêter à distance de la tête.

À faire : Raccourcir la queue pour qu'elle s'arrête nettement au-dessus du crâne sans jamais franchir le contour noir des cheveux (fin vers y≈360 au lieu de y≈459), et lui donner la même épaisseur de contour que la bulle (≈13 px au lieu de 4 px), avec un intérieur blanc continu jusqu'à la pointe.

**semaine-04 · 6-samedi-bd-diner-faire-semblant** — diapositive 1 · *autre*

> Le bandeau du narrateur coupe sa première phrase de façon à laisser « VA. » seul, centré, sur une ligne entière.

À faire : Rééquilibrer le retour à la ligne du bandeau pour que la première phrase tienne sur deux lignes comparables — « À TABLE, CHEZ DES AMIS, ON LUI DEMANDE » / « COMMENT IL VA. » — afin qu'aucun mot ne reste seul sur une ligne.

**semaine-04 · 6-samedi-bd-diner-faire-semblant** — diapositive 4 · *autre*

> Même défaut de coupe dans le bandeau du narrateur : « CHOSE. » se retrouve seul, centré, sur une ligne entière.

À faire : Forcer la césure du bandeau après « LUI » pour garder « QUELQUE CHOSE » sur une seule ligne : « LA FEMME ASSISE À CÔTÉ DE LUI / A REMARQUÉ QUELQUE CHOSE. / ELLE POSE LA QUESTION DOUCEMENT. »

**semaine-05 · 2-mardi-illustre-phrases-culpabilite** — diapositive 2 · *francais*

> Le titre annonce des « phrases » mais aucune des cinq entrées n'en est une : ce sont cinq comportements formulés à l'infinitif. Le titre ne décrit pas ce que la liste montre.

À faire : Dans slide_liste (assembleur.py, l. 337-358), afficher pour chaque item le champ "bulle" déjà présent dans contenus.json — la réplique entre guillemets (« Ça ne me dérange pas. », « Laisse, je m'en occupe. », « Pardon de te déranger. », « C'est de ma faute. », « J'aurais dû le voir venir. ») en intertitre rouge à la place de l'infinitif, celui-ci passant en petite étiquette au-dessus ou disparaissant — pour que les cinq phrases promises par le titre et par la diapositive 01 apparaissent réellement.

**semaine-05 · 2-mardi-illustre-phrases-culpabilite** — diapositive 1 · *francais*

> Dans legende.txt (et non sur une image) : le pronom objet manque, « éloigner » reste sans complément. Il faudrait « qui te rapprochent des autres au lieu de t'en éloigner ».

À faire : Dans legende.txt, remplacer « qui rapprochent des autres au lieu d’en éloigner » par « qui te rapprochent des autres au lieu de t’en éloigner ».

**semaine-05 · 5-vendredi-illustre-excuse-qui-repare** — diapositive 1 · *francais*

> Le sous-titre annonce « un mot de trois lettres », alors que le mot visé est « mais », qui en compte quatre. Il faut lire « un mot de quatre lettres » (ou supprimer le décompte).

À faire : Dans le sous-titre de la diapositive 1, remplacer « un mot de trois lettres » par « un mot de quatre lettres » (ce qui supprime au passage la répétition de « trois »), en modifiant le champ sousTitre à la ligne 1963 de /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json et la ligne 3 de /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-19-excuse-qui-repare.md, puis regénérer l'image.

**semaine-05 · 6-samedi-fiche-la-reparation-en-une-phrase** — diapositive 1 · *autre*

> L'étiquette de série annonce vendredi alors que la publication est programmée le samedi (nom du dossier « 6-samedi- » et ligne « 5,samedi,6,Fiche,… » du calendrier). L'étiquette est codée en dur dans reseaux-sociaux/generateur.py ligne 38 : dict(jour="vendredi", etiq="LA PRATIQUE DU VENDREDI · {n}/13").

À faire : Dans `/Users/cavalier/Dev/Site Emotion/reseaux-sociaux/generateur.py` ligne 38, remplacer l'étiquette qui nomme un jour par une étiquette neutre — `"pratique": dict(jour="vendredi", etiq="LA PRATIQUE · {n}/13")` — puis relancer `generateur.py` et `publication.py` pour réimprimer les 13 fiches « pratique », dont 10 affichent aujourd'hui un jour faux.

**semaine-06 · 4-jeudi-bd-il-raconte-la-troisieme-fois** — diapositive 3 · *placement-bulle*

> La queue de la bulle de gauche ne s'arrête pas au-dessus de la tête : elle traverse le contour des cheveux et s'enfonce dans le crâne du grand-père.

À faire : Raccourcir la queue de la bulle gauche pour que sa pointe s'arrête dans le fond vert au-dessus de la chevelure (vers y≈415-420 px au lieu de y≈490), sans jamais croiser le trait des cheveux ni empiéter sur le front.

**semaine-06 · 5-vendredi-fiche-tristesse-ou-depression** — diapositive 3 · *autre*

> Le pictogramme de « La dépression » ne correspond pas à celui annoncé en couverture : c'est la pelote emmêlée (le picto de l'anxiété) au lieu de la lune au-dessus de l'eau montrée sur la diapositive 1. Le lecteur qui enchaîne les deux images ne retrouve pas le même symbole.

À faire : Régénérer la diapositive 3 (et son équivalent TikTok) en remplaçant la pelote de laine rose par le pictogramme bleu de la couverture — la demi-lune blanche au-dessus de la demi-sphère d'eau — pour qu'il soit identique à celui montré à droite sur la diapositive 1.

**semaine-06 · 5-vendredi-fiche-tristesse-ou-depression** — diapositive 1 · *francais*

> Défaut dans la légende (legende.txt), pas dans l'image : elle promet « les trois différences qui comptent », or le carrousel ne présente pas trois différences — il présente les deux mots (LA PREMIÈRE / LA SECONDE) puis une seule comparaison (vague / chape). Annoncer « la différence qui compte » ou numéroter réellement trois écarts.

À faire : Dans /Users/cavalier/Dev/Site Emotion/publication/semaine-06/5-vendredi-fiche-tristesse-ou-depression/legende.txt, ligne 2, remplacer « Voici les trois différences qui comptent. » par « Voici la différence qui compte. » — au singulier, pour coller au titre de la diapositive 4 (« D'où la différence ») et à la formulation déjà employée ailleurs dans la série.

**semaine-06 · 6-samedi-illustre-apres-la-rupture** — diapositive 2 · *francais*

> « ton côté du lit » ne tient pas : ton propre côté du lit n'a pas disparu, c'est celui de l'autre qui est vide. Il faut « son côté du lit ».

À faire : Dans le troisième bloc, remplacer « ton côté du lit » par « son côté du lit ».

**semaine-06 · 6-samedi-illustre-apres-la-rupture** — diapositive 4 · *francais*

> « et vise juste le minimum » ne veut rien dire de clair accolé à « Mange de vrais repas même sans faim » : on ne sait pas ce qu'il faut viser, et « vise juste » se lit aussi comme « vise avec justesse ». À reformuler (« contente-toi du minimum », par exemple).

À faire : Remplacer la fin du bloc 2 par : « Mange de vrais repas même sans faim, quitte à faire au plus simple. » (la formulation « contente-toi du minimum » lève l'ambiguïté de « vise juste » mais garde la contradiction avec « de vrais repas »).

**semaine-07 · 2-mardi-bd-amitie-qui-s-eloigne** — diapositive 4 · *autre*

> L'amie blonde est physiquement présente dans la cuisine, alors que le bandeau du narrateur et la pensée disent que les deux femmes sont séparées et que chacune attend l'appel de l'autre. La scène contredit son propre texte.

À faire : Régénérer la diapositive 04 avec la femme brune seule dans sa cuisine, en supprimant entièrement la femme blonde à lunettes du côté droit du cadre.

**semaine-07 · 2-mardi-bd-amitie-qui-s-eloigne** — diapositive 4 · *forme-de-bulle*

> La bulle de pensée du haut porte une queue alors qu'elle est empilée au-dessus d'une autre bulle du même personnage : cette chaîne de ronds ne rejoint personne et s'interrompt sur la bulle du dessous.

À faire : Supprimer les deux ronds blancs situés entre les deux bulles (x≈343/y≈287 et x≈362/y≈353) : la bulle du haut, empilée, ne doit porter aucune queue, seule la bulle du bas conserve sa chaîne de trois ronds vers la tête.

**semaine-07 · 5-vendredi-bd-la-jalousie-qu-on-ose-pas-nommer** — diapositive 1 · *francais*

> Le titre du haut et le bandeau du narrateur disent exactement la même chose, à quelques centimètres l'un de l'autre : « rit toute seule » et « son téléphone » sont répétés dans la même image. En prime, « rire à son téléphone » est bancal — le bandeau écrit d'ailleurs « devant son téléphone », la bonne forme.

À faire : Remplacer le titre du haut par une accroche qui ne redit pas le bandeau, par exemple « 21 H 10. / ET CE RIRE QUI N’EST PAS POUR MOI. », en laissant le bandeau du narrateur inchangé.

**semaine-07 · 5-vendredi-bd-la-jalousie-qu-on-ose-pas-nommer** — diapositive 5 · *placement-bulle*

> La chaîne de ronds de la bulle de pensée s'écarte du personnage qui pense. Elle descend vers la droite et s'arrête très haut dans le vide ; prolongée, sa trajectoire aboutit sur la blonde endormie, alors que la pensée est celle de la femme à lunettes, seule éveillée, couchée à gauche.

À faire : Redessiner la chaîne de trois ronds en la faisant descendre du bas-gauche de la bulle vers le bas et vers la GAUCHE, le plus petit rond s'arrêtant juste au-dessus de la chevelure bouclée (environ x 300, y 830) au lieu de dériver à droite et de s'arrêter à y 424.

**semaine-07 · 5-vendredi-bd-la-jalousie-qu-on-ose-pas-nommer** — diapositive 5 · *francais*

> Deux « elle » se suivent avec des référents différents : le premier désigne la femme à lunettes, le second aussi, alors que le sujet grammatical le plus proche est « sa compagne ». Il faut relire pour savoir qui regarde le plafond.

À faire : Remplacer la deuxième phrase du bandeau par « LA FEMME BLONDE DORT CONTRE SA COMPAGNE, QUI REGARDE LE PLAFOND. » — le sujet est nommé comme sur les autres diapositives, « sa compagne » retrouve son référent habituel (la protagoniste), et le relatif « qui » supprime les deux « elle » consécutifs.

**semaine-07 · 6-samedi-illustre-jalousie-dans-le-couple** — diapositive 2 · *autre*

> La mise en relief rouge coupe l'expression en deux : seul « UNE » est coloré, en fin de ligne, tandis que « FOIS » retombe en noir au début de la ligne suivante. Le titre de la diapositive 1 met bien « UNE MINUTE » en entier en rouge, ce qui rend l'irrégularité plus voyante.

À faire : Dans reseaux-sociaux-illustre/contenus.json, remplacer le titre de la diapositive « Pourquoi vérifier une fois ne suffit jamais » par « Pourquoi vérifier ne suffit jamais » (sans le mot « une »), ou bien corriger la cause en faisant correspondre titreAccent à la suite de mots contiguë au lieu d'un ensemble de mots isolés, pour qu'« UNE » ne soit jamais coloré seul.

**semaine-08 · 2-mardi-bd-message-lu-sans-reponse** — diapositive 1 · *francais*

> Les deux mêmes heures sont annoncées deux fois chacune sur la même image : le titre, la bulle et le bandeau répètent la même information.

À faire : Remplacer le texte de la bulle de pensée, qui ne fait que redire le titre, par une pensée qui avance — par exemple « Qu'est-ce que j'ai bien pu dire de travers ? » — et supprimer la première ligne « IL EST 22 H 10. » du bandeau, l'heure étant déjà dans le titre.

**semaine-08 · 2-mardi-bd-message-lu-sans-reponse** — diapositive 2 · *texte-coupe*

> Le bandeau du narrateur casse le groupe « vingt minutes » et laisse le mot « MINUTES » seul sur une ligne, suivi d’un retour forcé.

À faire : Supprimer le retour à la ligne forcé après « minutes » et rééquilibrer le bandeau sur trois lignes en gardant « VINGT MINUTES » d'un seul tenant, par exemple : « ELLE REGARDE LES PHOTOS DE SON AMIE / DEPUIS VINGT MINUTES, ET SE DIT / QUE C'EST POUR SE RASSURER. »

**semaine-08 · 2-mardi-bd-message-lu-sans-reponse** — diapositive 4 · *forme-de-bulle*

> La queue de la bulle de dialogue est une très longue aiguille qui se termine par un filet noir dépassant de la pointe, et ce filet entre dans les cheveux du personnage au lieu de s’arrêter avant.

À faire : Raccourcir la queue de la bulle « PARDON POUR HIER… » pour qu'elle s'arrête vers y≈450, à une trentaine de pixels au-dessus du contour des cheveux (y=490), et la terminer en pointe effilée nette au lieu du moignon à bout plat qui traverse aujourd'hui la ligne des cheveux jusqu'à y=502.

**semaine-08 · 5-vendredi-bd-ami-qui-reussit** — diapositive 1 · *francais*

> Le bandeau du narrateur reformule les deux bulles presque mot pour mot : « pris pour le poste » (bulle) / « pris pour un poste » (bandeau), « je suis trop contente pour toi » (bulle) / « elle est vraiment contente pour lui » (bandeau). Le bandeau n'ajoute rien et répète deux fois les mêmes mots à quelques centimètres d'écart. Il pourrait apporter ce que l'image ne dit pas (le contexte, la situation d'elle) plutôt que redire les répliques.

À faire : Remplacer le bandeau par une phrase qui apporte uniquement ce que ni le dessin ni les bulles ne disent, en supprimant « pris pour un poste » et « contente pour lui » — par exemple : « ILS SE VOIENT UNE FOIS PAR MOIS DEPUIS LA FAC. CE MIDI, C'EST LUI QUI A QUELQUE CHOSE À ANNONCER. »

**semaine-08 · 5-vendredi-bd-ami-qui-reussit** — diapositive 3 · *placement-bulle*

> Les deux appendices se télescopent au-dessus de la tête de la jeune femme : sous la bulle de pensée, un trait noir épais redescend et se plante dans les cheveux, et les trois ronds de la chaîne de pensée sont posés par-dessus ce trait. On ne distingue plus ce qui appartient à la bulle de dialogue et ce qui appartient à la bulle de pensée, et l'attribution des deux répliques devient floue. Il faudrait décaler la bulle de dialogue (vers la gauche ou vers le haut) pour que sa queue atteigne la tête sans croiser la chaîne de pensée, et arrêter cette chaîne avant les cheveux.

À faire : Décaler la bulle de dialogue « C'EST QUOI EXACTEMENT, LE POSTE ?… » vers la gauche (environ 80 px) pour que sa queue descende dans l'espace libre à gauche de la bulle de pensée au lieu de passer derrière elle, et la raccourcir pour qu'elle s'arrête nettement au-dessus de la chevelure ; arrêter de même la chaîne de pensée avant les cheveux, son dernier rond flottant au-dessus du crâne.

**semaine-09 · 3-mercredi-bd-invitation-annulee-soulagement** — diapositive 1 · *francais*

> La même information est écrite trois fois sur la même image : « annule »/« annuler » apparaît trois fois et « le dîner de ce soir » deux fois, entre le titre, la bulle et le bandeau.

À faire : Réécrire le bandeau de la diapositive 1 pour qu'il n'apporte que l'information neuve, sans reprendre l'annulation ni le dîner : « IL EST DÉJÀ EN MANTEAU, UNE CHAUSSURE À LA MAIN. IL RELIT LE MESSAGE TROIS FOIS. »

**semaine-09 · 3-mercredi-bd-invitation-annulee-soulagement** — diapositive 3 · *francais*

> « IL A REMIS SON MANTEAU AU PORTEMANTEAU » : écho sonore manteau/portemanteau dans le même souffle, et ambiguïté de sens — « remettre son manteau » se comprend d'abord comme « le renfiler », ce que la suite contredit. « IL A RACCROCHÉ SON MANTEAU » lèverait les deux problèmes.

À faire : Dans le bandeau narrateur, remplacer « IL A REMIS SON MANTEAU AU PORTEMANTEAU ET FAIT CHAUFFER DE L'EAU. » par « IL A RACCROCHÉ SON MANTEAU ET FAIT CHAUFFER DE L'EAU. » (la ligne « IL SOURIT TOUT SEUL. » reste inchangée).

**semaine-09 · 6-samedi-bd-fatigue-qui-ne-passe-pas** — diapositive 1 · *francais*

> La même information est écrite trois fois sur la même image : le titre, la bulle de pensée et le bandeau du narrateur répètent l'heure, la durée du sommeil, le jour et la fatigue.

À faire : Réécrire le bandeau du narrateur pour qu'il n'énonce plus ni l'heure, ni le jour, ni la fatigue déjà donnés par le titre et la bulle, et qu'il apporte le fait nouveau (la durée du phénomène), par exemple : « IL S'EST COUCHÉ TÔT. COMME LES SAMEDIS D'AVANT. ÇA N'A RIEN CHANGÉ. »

**semaine-09 · 6-samedi-bd-fatigue-qui-ne-passe-pas** — diapositive 5 · *placement-bulle*

> Le dernier rond de la chaîne de pensée ne s'arrête pas avant la tête : il est posé sur les cheveux du personnage.

À faire : Remonter le troisième rond de la chaîne d'environ 25 px vers le haut (centre vers (668, 387) au lieu de (663, 413)), ou supprimer ce troisième rond, pour que la chaîne se termine entièrement dans le fond crème avec un écart net au-dessus du contour de la chevelure.

**semaine-09 · 6-samedi-bd-fatigue-qui-ne-passe-pas** — diapositive 5 · *autre*

> Contrairement à toutes les autres cases du carrousel (pleine page), le dessin est enfermé dans un cadre qui ne commence qu'au tiers de la hauteur, et le trait noir de ce cadre passe en travers de la tête du personnage.

À faire : Régénérer la diapositive 05 en pleine page comme les cases 01 à 04 — supprimer le cadre noir (trait horizontal y = 439–443 et montants verticaux x = 35–40 et x = 1040–1044) ainsi que les marges crème, pour que le dessin occupe tout le 1080×1350 et qu'aucun trait ne passe au-dessus de la tête du personnage.

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 1 · *francais*

> La même phrase apparaît deux fois dans la même image, mot pour mot.

À faire : Dans reseaux-sociaux-bd/contenus.json, à posts[4].slides[0].narrateur, supprimer la phrase en doublon pour ne garder que « SON MARI A COMMENCÉ CE PLAT À SEPT HEURES CE MATIN. », puis régénérer la diapositive 01.

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 4 · *autre*

> Le bandeau du narrateur se répartit sur quatre lignes avec deux mots isolés, et la troisième ligne touche presque le bord.

À faire : Raccourcir le texte du bandeau pour qu'il tienne en deux lignes pleines sans mot orphelin, en supprimant « de prudence » et « vraiment » : « ELLE S'EN VA AVEC UN CONSEIL DANS LA TÊTE, / SANS AVOIR ENTENDU CE QU'IL VOULAIT LUI DIRE. » (42 et 45 caractères, soit moins que les 47–48 caractères qui tiennent déjà sur une ligne du bandeau).

**semaine-11 · 1-lundi-bd-la-question-du-soir** — diapositive 1 · *visibilite-personnage*

> Le voile blanc posé sous le titre décolore la moitié haute du crâne du père : le sommet de sa tête se fond dans le fond crème et le contour du crâne disparaît. La deuxième ligne du titre passe en plus au ras de son sourcil droit.

À faire : Réduire le voile blanc du bandeau de titre pour qu'il s'arrête au-dessus de la tête du père (ou plafonner son opacité à ~25 %) et remonter le bloc de titre d'environ 60 px, afin que le contour du crâne reste encré et que la ligne « IL FERME LE LIVRE. ELLE NE DORT PAS. » cesse de traverser son sourcil et sa paupière supérieure.

**semaine-11 · 1-lundi-bd-la-question-du-soir** — diapositive 4 · *forme-de-bulle*

> Même aiguille que sur la diapositive 2 : la queue de la bulle « TU AS LE DROIT D'ÊTRE TRISTE, TU SAIS, PAPA. » fait environ 245 px de long pour 30 px de base et se termine en trait fin dans le vide, très loin au-dessus de la tête de la fille.

À faire : Redessiner la queue de la bulle « TU AS LE DROIT D’ÊTRE TRISTE, TU SAIS, PAPA. » en triangle plein et fermé : base élargie à environ 60 px sous le bord de la bulle et longueur réduite à environ 110 px (pointe vers y≈330), avec l’intérieur blanc conservé jusqu’à la pointe et un contour noir de 8 px d’épaisseur constante, identique à celui du cadre.

**semaine-11 · 2-mardi-illustre-recevoir-sans-rembourser** — diapositive 3 · *francais*

> Le verbe rendre revient trois fois sur trois lignes consécutives (titre, intertitre, corps). En plus, le titre reprend presque mot pour mot le sous-titre de la diapositive 1.

À faire : Remplacer le titre « QUAND TU RENDS DANS L'HEURE » par « TU AS DÉJÀ SORTI TON TÉLÉPHONE » (qui colle à l'illustration et au virement évoqué) et l'intertitre « LE RÉFLEXE DE RENDRE » par « LE RÉFLEXE D'ÉQUILIBRER », en ne gardant que le « tu rends aussitôt » du corps.

**semaine-11 · 3-mercredi-fiche-comprendre-gratitude** — diapositive 2 · *francais*

> « le manquant » n'existe pas en français au sens de « le manque » : « un manquant » désigne un élément absent d'un ensemble (un inventaire). La formule attendue est « du manque vers le présent ».

À faire : Remplacer « du manquant vers le présent » par « du manque vers le présent » (image 02.jpg à régénérer, et ligne 431 de /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py à corriger).

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 4 · *forme-de-bulle*

> La queue de la première bulle (« DÉSOLÉ, JE TE PRENDS ENCORE TA SOIRÉE… ») est un coin très allongé et très étroit qui ne s'arrête pas au-dessus de la tête : il entre dans les cheveux et y creuse une fente blanche jusqu'au front. Queue à raccourcir nettement, et à arrêter avant la chevelure.

À faire : Raccourcir la queue de la première bulle d'environ 70 px pour que sa pointe s'arrête vers y≈340, nettement au-dessus du sommet de la chevelure (y≈362), et l'élargir un peu à la base pour qu'elle ne soit plus un trait-aiguille.

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 3 · *forme-de-bulle*

> Même défaut sur la bulle de droite (« ARRÊTE DE T’EXCUSER ET MANGE PENDANT QUE C’EST CHAUD. ») : queue d'environ 230 px, effilée en pointe. Comme le mur est crème et la bulle blanche, l'intérieur de la queue ne se distingue pas du fond : on ne lit plus une queue de bulle mais deux traits noirs, comme une fissure dans le mur.

À faire : Raccourcir la queue de la bulle de droite d'environ 243 px à 80-100 px et élargir sa base d'environ 32 px à 70-80 px, pour qu'elle forme un triangle dont l'intérieur blanc reste visible sur toute sa longueur et ne se referme jamais en trait noir plein.

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 5 · *forme-de-bulle*

> Même queue-aiguille sur la bulle de droite (« TU ME RACONTERAS TA JOURNÉE DEMAIN, QUAND TU IRAS MIEUX. ») : très longue, effilée, terminée par un trait unique en plein mur, loin au-dessus de la tête de celle qui parle. Homogénéiser avec les queues courtes et larges de la diapositive 1.

À faire : Redessiner la queue de la bulle de droite en triangle court et large, à la manière de celles de la diapositive 1 : environ 70 à 90 px de long au lieu de 238, base d'au moins 60 px, contour noir continu et de même épaisseur sur les deux côtés jusqu'à la pointe, intérieur blanc conservé jusqu'au bout, soudé au cadre de la bulle et orienté vers la tête de la jeune femme.

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 2 · *francais*

> La bulle de pensée et le bandeau du narrateur disent la même chose avec les mêmes mots, à deux lignes d'écart : « Il s’excuse pour tout depuis qu’il a emménagé ici. » puis « DEPUIS SIX MOIS, IL S’EXCUSE DE PRENDRE DE LA PLACE… ». « il s’excuse » et « depuis » sont repris tels quels. Il faudrait faire dire autre chose à l'un des deux (par exemple, la pensée sur ce qu'elle ressent, le bandeau sur les faits).

À faire : Remplacer le texte de la bulle de pensée par une phrase de ressenti sans aucun mot commun avec le bandeau, par exemple « Ça me serre le cœur de l’entendre. » (ou « J’aimerais juste qu’il se sente chez lui. »), en laissant le bandeau porter seul les faits.

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 6 · *francais*

> « …il demande pardon d’occuper une place qu’il croit ne pas mériter, et il met l’autre dehors. » La fin de phrase ne dit pas vraiment quelque chose : « mettre l’autre dehors » s'entend au sens propre (chasser quelqu'un de chez soi) et on ne comprend pas ce qu'elle veut dire ici. À reformuler, par exemple « et il met l’autre à distance » ou « et il oblige l’autre à le rassurer ».

À faire : Dans /Users/cavalier/Dev/Site Emotion/publication/semaine-11/4-jeudi-bd-la-soupe-et-le-merci (diapositive 06, instagram et tiktok), remplacer « et il met l'autre dehors » par « et il oblige l'autre à le rassurer » — qui garde le parallèle avec « merci » ; à défaut, la variante minimale « et il met l'autre à distance » convient aussi.

**semaine-11 · 5-vendredi-illustre-merci-plutot-que-desole** — diapositive 0 · *francais*

> Légende (fichier legende.txt) : « C’est la même situation et le même début de phrase, et pourtant tout change entre vous. » contredit tout le carrousel — c'est justement le début de la phrase qui change (« Désolé… » devient « Merci… »). Écrire plutôt « la même situation et le même moment » ou « la même situation, une phrase de plus ».

À faire : Dans /Users/cavalier/Dev/Site Emotion/publication/semaine-11/5-vendredi-illustre-merci-plutot-que-desole/legende.txt, remplacer « C’est la même situation et le même début de phrase, et pourtant tout change entre vous. » par « C’est la même situation, un seul mot de différence, et pourtant tout change entre vous. »

**semaine-11 · 6-samedi-fiche-gratitude-ou-dette** — diapositive 2 · *francais*

> Le paragraphe se contredit et se répète : « Elle » (la gratitude) « reçoit ce qui est donné » alors que c'est la personne qui reçoit, « donné » et « donne » se suivent à trois mots d'écart, et « reçoit » revient en fin de paragraphe avec un autre sujet. Reformuler, par exemple : « Tu accueilles ce qu’on t’offre, tu le savoures, et ça te donne envie de rendre — librement, sans obligation. »

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py ligne 445, remplacer « Elle reçoit ce qui est donné, le savoure, et donne envie de rendre » par « Elle accueille ce qu’on t’offre, le savoure, et donne envie de rendre » — la personnification est conservée, l’écho donné/donne disparaît, et « recevoir » ne reste qu’une fois, dans « celui qui la reçoit ».

**semaine-11 · 6-samedi-fiche-gratitude-ou-dette** — diapositive 4 · *francais*

> Dernière phrase lourde : « laisser l’autre avoir le plaisir d’avoir donné » enchaîne deux « avoir » à trois mots d'écart, et « Recevoir » ouvre les deux phrases du paragraphe. Écrire « …c’est laisser à l’autre le plaisir d’avoir donné. »

À faire : Remplacer la dernière phrase par : « Recevoir sans rembourser tout de suite, c'est laisser à l'autre le plaisir d'avoir donné. » (ne pas toucher à la première phrase ni au mot « Recevoir »)

**semaine-12 · 3-mercredi-illustre-angoisse-dimanche-soir** — diapositive 3 · *francais*

> La phrase « Tu mets ton réveil à 22 h. » dit littéralement que le réveil est réglé pour sonner à 22 h, alors que le sens visé est : il est 22 h et tu règles le réveil de demain matin. Le reste du bloc (« tu n'es même pas couché ») confirme qu'on parle de l'heure à laquelle tu le règles, pas de l'heure de la sonnerie. À reformuler, par exemple « À 22 h, tu règles ton réveil. ».

À faire : Remplacer « Tu mets ton réveil à 22 h. » par « Il est 22 h et tu mets ton réveil pour demain matin. » (éviter « tu règles », déjà dans le titre du bloc deux lignes plus haut).

**semaine-12 · 5-vendredi-bd-compliment-esquive-devant-equipe** — diapositive 1 · *visibilite-personnage*

> La bulle de l'homme est posée sur son propre visage : elle lui masque entièrement la bouche et le menton, alors que c'est lui qui parle.

À faire : Descendre la bulle de l'homme d'environ 80–90 px (bord supérieur à y≈880 au lieu de 797) pour qu'elle commence sous son menton et ne recouvre plus que le bureau et le clavier, tout en restant plus basse que la bulle de la femme afin de conserver l'ordre de lecture question puis réponse.

**semaine-12 · 5-vendredi-bd-compliment-esquive-devant-equipe** — diapositive 1 · *placement-bulle*

> La queue de la bulle de l'homme part vers le bas, vers son torse, alors que sa tête est au-dessus de la bulle : elle ne désigne pas la bouche du locuteur.

À faire : Déplacer la queue de la bulle de l'homme du bord inférieur vers le bord supérieur de la bulle (vers x ≈ 330), pointe dirigée vers le haut en direction de sa bouche (environ y 785), exactement comme la queue de la bulle de la femme, et supprimer la queue qui descend actuellement sur son gilet.

**semaine-12 · 5-vendredi-bd-compliment-esquive-devant-equipe** — diapositive 2 · *placement-bulle*

> La chaîne de ronds de la bulle de pensée s'éloigne du personnage au lieu d'y mener : elle descend vers la gauche et se termine au niveau de la tête d'une collègue du second plan, qui semble donc être celle qui pense.

À faire : Inverser la diagonale de la chaîne pour qu'elle descende vers la droite en direction du penseur, en plaçant les trois ronds décroissants aux environs de (395, 272), (368, 332) et (342, 398) sur le cadre 1080×1350, le plus petit s'arrêtant juste au-dessus de la chevelure grise de l'homme (qui commence vers y ≈ 444) et loin de la collègue rousse.

**semaine-12 · 5-vendredi-bd-compliment-esquive-devant-equipe** — diapositive 3 · *placement-bulle*

> La queue de la bulle de la femme entre dans sa chevelure et descend jusqu'au crâne, au lieu de s'arrêter à distance de la tête.

À faire : Raccourcir la queue de la bulle de la femme pour que sa pointe s'arrête vers y ≈ 415 px, soit une trentaine de pixels au-dessus du bord de la chevelure, sans jamais la toucher — comme le fait déjà la queue de l'homme à gauche.

**semaine-13 · 2-mardi-bd-liste-du-dimanche** — diapositive 4 · *forme-de-bulle*

> Queue de la bulle de dialogue mal soudée : le trait de son bord droit remonte à l'intérieur de la bulle, et le contour bas de la bulle reste tracé en ligne droite au-dessus d'elle.

À faire : Raccourcir le bord droit de la queue pour qu'il s'arrête net sur le contour bas de la bulle (y ≈ 217 px) au lieu de remonter de 7 px dans le blanc intérieur sous le « M » de MINUTES.

**semaine-13 · 2-mardi-bd-liste-du-dimanche** — diapositive 4 · *forme-de-bulle*

> La chaîne de pensée de l'homme est dégénérée (trois ronds identiques collés) et touche son menton.

À faire : Sur la diapositive 4, redessiner la chaîne de pensée en trois ronds nettement séparés et décroissants de la bulle vers la tête (comme sur 02 et 03), et décaler la chaîne — en descendant ou en déplaçant légèrement la bulle vers la gauche — pour que le plus petit rond s'arrête à quelques pixels du trait de la mâchoire au lieu de se fondre dedans.

**semaine-13 · 2-mardi-bd-liste-du-dimanche** — diapositive 1 · *francais*

> La même information est dite trois fois sur la même image ; « dimanche », « semaine » et « liste » y figurent chacun deux fois.

À faire : Réécris le bandeau du bas pour qu'il n'y redise ni « dimanche », ni « liste », ni « faire » — le chapeau a déjà donné le jour, l'heure et l'action — par exemple « IL S'ASSOIT TOUJOURS À LA MÊME PLACE, À LA MÊME HEURE, AVEC LE MÊME CARNET. », et remplace « je prépare la semaine » par « je m'organise » dans la bulle pour supprimer le dernier écho.

**semaine-13 · 3-mercredi-illustre-ce-que-ta-colere-defend** — diapositive 0 · *autre*

> Légende : le renvoi au post de mardi ne correspond pas au post de mardi.

À faire : Supprimer la première phrase de legende.txt du mercredi et faire commencer la légende à « Une colère arrive rarement pour rien : … », ou, si l'on tient au lien avec mardi, la remplacer par une phrase fidèle du type « Après la liste du dimanche soir, une autre émotion qu'on n'écoute pas assez : la colère. »

**semaine-13 · 3-mercredi-illustre-ce-que-ta-colere-defend** — diapositive 4 · *francais*

> Tournure bancale : « venir de » suivi d'un infinitif à la forme négative.

À faire : Remplacer « Demande-toi ce que l'autre vient de ne pas respecter. » par « Demande-toi ce que l'autre n'a pas respecté. » (ou, pour garder l'immédiateté, « Demande-toi quelle limite l'autre vient de franchir. »)

**semaine-13 · 4-jeudi-fiche-la-minute-de-credit** — diapositive 1 · *autre*

> L'étiquette de série annonce le vendredi alors que la publication est celle du jeudi (dossier « 4-jeudi »). Le libellé vient du générateur, où la série « pratique » est codée en dur « LA PRATIQUE DU VENDREDI · {n}/13 » (reseaux-sociaux/generateur.py, ligne 38), mais cette semaine la fiche pratique est programmée le jeudi et c'est la BD qui occupe le vendredi.

À faire : Dans `/Users/cavalier/Dev/Site Emotion/reseaux-sociaux/generateur.py` ligne 38, retirer le jour du libellé de la série pratique — `"pratique": dict(jour="vendredi", etiq="LA PRATIQUE · {n}/13")` — puis régénérer la couverture 01.jpg (instagram et tiktok) des 10 fiches pratiques qui ne paraissent pas un vendredi, dont celle-ci ; à défaut, faire lire le jour réel depuis `publication/calendrier.csv` au lieu de le coder en dur.

**semaine-13 · 4-jeudi-fiche-la-minute-de-credit** — diapositive 4 · *francais*

> La phrase d'ouverture enfile trois participes passés sans sujet ni auxiliaire ; « Tenu une journée difficile » ne se dit pas (on tient le coup, on tient une journée), et « dit non » se lit d'abord comme un verbe conjugué avant qu'on comprenne qu'il s'agit d'une énumération. Une forme infinitive — « Tenir une journée difficile, dire non, demander de l'aide : ça compte. » — dirait la même chose sans faire trébucher.

À faire : Remplacer la phrase d'ouverture par « Traverser une journée difficile, dire non, demander de l’aide : ça compte. » (ligne 516 de /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py, puis regénérer la diapositive 4).

**semaine-13 · 5-vendredi-bd-un-non-d-une-seconde** — diapositive 5 · *placement-bulle*

> Les deux bulles de pensée empilées à gauche sont celles de la même femme : une seule chaîne de ronds devrait partir de la bulle du bas. Ici chacune a la sienne. Celle de la bulle du haut descend sur la porte et s'interrompt au milieu du panneau, à environ 200 px au-dessus et à gauche du crâne, sans jamais rejoindre personne ; puis une seconde chaîne repart sous la bulle du bas et atteint, elle, la tête. On lit deux trajets parallèles qui laissent croire à deux penseurs.

À faire : Supprimer les trois ronds situés sous la bulle « Ce refus a duré une seconde, à peine. » et les remplacer par un fin trait droit reliant cette bulle à celle du dessous, en ne gardant que la chaîne de ronds de la bulle du bas vers la tête — exactement comme sur la diapositive 2.

**semaine-13 · 5-vendredi-bd-un-non-d-une-seconde** — diapositive 4 · *visibilite-personnage*

> D'une case à l'autre les deux personnages échangent leur tenue, et le frère change de tête : on ne reconnaît plus qui est qui. En diapositive 3 la sœur porte le pull rouille et le frère la veste vert sauge avec une sacoche crème à l'épaule ; en diapositive 4 c'est le frère qui porte le pull rouille et la sœur le haut vert sauge avec la sangle crème sur son épaule. Les cheveux du frère passent au même moment du noir court et hérissé au châtain clair plus long, et son visage s'allonge.

À faire : Régénérer la diapositive 4 en rendant à chacun sa tenue de la diapositive 3 : la sœur en pull rouille uni avec sa natte brun très foncé, et le frère en veste vert sauge sur t-shirt brun, sangle de sac crème à l'épaule, cheveux noirs courts et hérissés.

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 1 · *visibilite-personnage*

> La bulle de dialogue est posée trop haut sur le visage : elle recouvre le nez et la bouche du personnage. Il faudrait la descendre ou la décaler vers la droite pour dégager le bas du visage.

À faire : Descendre la bulle d'environ 200 px (bord supérieur vers y≈560 au lieu de y≈355) pour qu'elle passe sous le menton et vienne se poser sur l'épaule/le torse, en la décalant légèrement à droite (x≈620-1030) et en réorientant la queue vers le haut-gauche pour qu'elle pointe la bouche redevenue visible.

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 1 · *autre*

> Le personnage de la première diapositive n'est pas le même homme que dans les diapositives 2 à 5 : cheveux et barbe gris, visage nettement plus âgé, alors que le héros de la suite est un homme brun d'une trentaine d'années. La rupture est immédiate dès la deuxième image.

À faire : Regénérer la diapositive 1 avec le même personnage que les diapositives 2 à 5 : cheveux châtain foncé, sourcils brun sombre et barbe brune sur un visage d'homme d'une trentaine d'années — supprimer tout gris des cheveux, des sourcils et de la barbe.

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 6 · *francais*

> Anacoluthe : le sujet du gérondif n'est pas celui de la proposition. « En rentrant, son corps était encore en mode journée de travail » laisse entendre que c'est le corps qui rentre. Écrire par exemple « Quand il est rentré, son corps était encore en mode journée de travail ».

À faire : Remplacer « En rentrant, » par « Quand il est rentré, » — soit : « Quand il est rentré, son corps était encore en mode journée de travail : il a tourné en rond, rangé un coussin, envisagé de travailler alors que personne ne le lui demandait. »

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 0 · *francais*

> Légende de la publication (fichier legende.txt, pas une diapositive) : après « Ce n'est pas que », le français demande le subjonctif, pas le conditionnel. Lire « Ce n'est pas que tu ne saches pas te reposer ».

À faire : Dans legende.txt, remplacer « Ce n'est pas que tu ne saurais pas te reposer » par « Ce n'est pas que tu ne saches pas te reposer ».

**semaine-14 · 4-jeudi-illustre-expiration-longue** — diapositive 4 · *francais*

> « souffler plus longtemps » apparaît trois fois en quatre lignes, dans le titre, l'intertitre et la première ligne du corps. L'intertitre n'est qu'une étiquette qui n'apporte aucune information nouvelle.

À faire : Remplacer l'intertitre « Souffler plus longtemps » par une étiquette qui apporte une information neuve, par exemple « Un frein intégré à ton corps », pour que « souffler … longtemps » n'apparaisse plus qu'une fois dans le titre et une fois dans le corps.

**semaine-14 · 6-samedi-bd-atelier-en-fait-ca-va-pas** — diapositive 2 · *placement-bulle*

> La queue de la bulle de dialogue de l'artisan ne désigne personne : elle plonge dans sa bulle de pensée et disparaît derrière elle. Aucune queue ne relie donc la réplique parlée à celui qui la prononce.

À faire : Raccourcir la queue de la bulle « OUAIS, ÇA VA, COMME D'HABITUDE. » pour qu'elle s'effile et se referme en une pointe franche dans la bande libre entre le bas de cette bulle (y ≈ 215) et le haut de la bulle de pensée (y ≈ 307), orientée vers la tête de l'homme, sans jamais toucher ni chevaucher la bulle de pensée.

**semaine-14 · 6-samedi-bd-atelier-en-fait-ca-va-pas** — diapositive 0 · *francais*

> Légende (pas une diapositive) : collocation fautive « dépenser ses journées ». En français on passe ses journées à faire quelque chose ; on dépense de l'argent ou de l'énergie.

À faire : Dans legende.txt, remplacer « dépense » par « passe » : « Mais il ne passe plus ses journées à le cacher, et ça pèse déjà beaucoup moins lourd. »

**semaine-14 · 6-samedi-bd-atelier-en-fait-ca-va-pas** — diapositive 0 · *francais*

> Légende (pas une diapositive) : l'appel au test est écrit deux fois de suite, dans deux phrases consécutives qui disent exactement la même chose.

À faire : Supprimer la phrase « Le test des 14 émotions est dans la bio. » à la fin du premier paragraphe de legende.txt, pour que le paragraphe se termine sur « …et ça pèse déjà beaucoup moins lourd. », le pied de légende standard portant déjà l'appel au test.

**semaine-15 · 3-mercredi-bd-telephone-dans-le-noir** — diapositive 1 · *francais*

> Le bandeau du narrateur redit mot pour mot ce que le titre du haut vient d'annoncer : l'heure « 23 h 40 » est écrite deux fois sur la même image, et l'idée « le téléphone, non » est reformulée en « elle regarde encore son téléphone au lit ». Avec la bulle de pensée, le mot « téléphone » apparaît trois fois sur cette seule diapositive. Le bandeau pourrait se limiter à l'information neuve (« son réveil sonne à 6 h 30 »).

À faire : Remplacer tout le bandeau du narrateur par la seule information neuve — « SON RÉVEIL SONNE À 6 H 30. » — en supprimant « IL EST 23 H 40 ET » ainsi que la phrase « ELLE REGARDE ENCORE SON TÉLÉPHONE AU LIT. »

**semaine-15 · 3-mercredi-bd-telephone-dans-le-noir** — diapositive 6 · *francais*

> Rupture de concordance des temps dans la même phrase. Le texte commence à l'imparfait (« Elle ne relisait pas », « elle le relisait »), bascule au présent (« Chaque relecture la calme dix secondes, puis rallume l'alarme »), puis revient à l'imparfait et au passé composé (« il n'y avait aucun message caché : quelqu'un a lu, puis s'est endormi »). Il faudrait « la calmait […] puis rallumait » pour rester cohérent avec le reste.

À faire : Sur la diapositive 6, mettre la phrase du milieu à l'imparfait pour l'aligner sur les deux autres : remplacer « Chaque relecture la calme dix secondes, puis rallume l'alarme un cran plus haut. » par « Chaque relecture la calmait dix secondes, puis rallumait l'alarme un cran plus haut. » (texte final : « Elle ne relisait pas son message pour le comprendre, elle le relisait pour être rassurée. Chaque relecture la calmait dix secondes, puis rallumait l'alarme un cran plus haut. Et en face, il n'y avait aucun message caché : quelqu'un a lu, puis s'est endormi. »)

**semaine-15 · 6-samedi-bd-quarante-longueurs** — diapositive 0 · *francais*

> Dans la légende, la fin du premier paragraphe répète mot pour mot le bloc de rappel qui suit deux lignes plus bas : « Tes 14 émotions notées sur 10, le test est en bio. » puis « Le test complet est sur boussole-emotionnelle.fr (lien en bio) : 14 émotions, une note sur 10 pour chacune. » Même information (14 émotions, note sur 10, lien en bio) dite deux fois d’affilée. Supprimer la phrase du premier paragraphe, qui casse en plus la chute (« c’est exactement le moment où ta joie devient réelle »).

À faire : Supprimer la dernière phrase du premier paragraphe, « Tes 14 émotions notées sur 10, le test est en bio. », pour que le paragraphe s'achève sur « … c'est exactement le moment où ta joie devient réelle. », le bloc de rappel deux lignes plus bas portant déjà le CTA.

**semaine-15 · 6-samedi-bd-quarante-longueurs** — diapositive 2 · *forme-de-bulle*

> La queue de la bulle « BOF, J’AI JUSTE FAIT QUELQUES LONGUEURS, RIEN DE SPÉCIAL. » est coupée en deux par la bulle de pensée posée par-dessus. Le contour n’est donc plus continu ni d’épaisseur constante : pointe blanche cerclée de noir en haut, simple trait noir en bas. Il faudrait décaler la bulle de pensée vers la gauche (ou la queue vers la droite) pour que la queue descende d’un seul tenant jusqu’à la tête.

À faire : Raccourcir la queue de la bulle « BOF, J'AI JUSTE FAIT QUELQUES LONGUEURS, RIEN DE SPÉCIAL. » pour qu'elle se termine en pointe nette et fermée juste au-dessus du bord supérieur de la bulle de pensée (vers y≈300), et supprimer le fragment de trait noir qui ressort sous cette bulle de pensée.

**semaine-16 · 1-lundi-fiche-la-seconde-de-suspension** — diapositive 1 · *autre*

> Le bandeau de série annonce le vendredi alors que la publication est programmée le lundi : le lecteur qui la voit paraître en début de semaine lit « LA PRATIQUE DU VENDREDI ».

À faire : Dans reseaux-sociaux/generateur.py ligne 38, retire le jour de l'étiquette — etiq="LA PRATIQUE · {n}/13", dans le style sans jour des deux autres séries — puis régénère les 13 fiches « pratique » et relance publication.py pour que les images recopiées portent le nouveau bandeau.

**semaine-16 · 2-mardi-illustre-dire-non-sans-se-justifier** — diapositive 2 · *autre*

> Dans la troisième vignette, les rôles sont inversés par rapport au texte : c'est le commerçant qui fait le geste de refus, alors que le texte demande au lecteur (la cliente) de dire « non merci » à la carte de fidélité.

À faire : Régénérer la troisième vignette en échangeant les rôles : c'est le commerçant qui tend la carte de fidélité par-dessus le comptoir, et la cliente au pull moutarde qui lève la paume ouverte dans un « non merci » poli.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 3 · *forme-de-bulle*

> Le contour de cette même bulle n'a pas la même épaisseur partout : la queue est tracée en trait fin alors que le cadre de la bulle est en trait épais, et le contour est interrompu à l'endroit où la queue se greffe.

À faire : Fermer la soudure de la queue de la bulle 1 : prolonger le trait gauche de la queue vers le haut jusqu'au bas du cadre pour combler le manque blanc des lignes 221-226 (x≈315), et raccourcir le trait droit qui dépasse de ~4 px à l'intérieur de la bulle (x≈339-343, lignes 214-216) — l'épaisseur, elle, ne doit pas être touchée : elle est déjà uniforme à 4 px, cadre et queue compris.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 4 · *autre*

> Le bandeau du narrateur dit l'inverse de ce que montre le dessin : « ELLE DÉTOURNE LA TÊTE DU MIROIR DU COULOIR. ELLE LE FAIT SANS S'EN RENDRE COMPTE. » alors qu'elle regarde vers le miroir, les yeux grands ouverts.

À faire : Refaire la diapositive 4 avec la tête tournée vers la droite, vers la porte d'entrée, paupières relâchées et regard droit devant (ou baissé sur les clés), le bras seul partant vers la gauche attraper le trousseau près du miroir — de sorte que le miroir reste hors de sa ligne de regard, comme l'annonce le bandeau.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 4 · *autre*

> Le dessin n'occupe que le bas de l'image : plus d'un tiers de la diapositive est un aplat dégradé vide, sans titre ni bulle, alors que les diapositives 1, 2 et 5 sont dessinées bord à bord.

À faire : Régénérer la diapositive 4 en plein cadre 1080×1350, sans case encastrée ni marges : la scène du couloir doit occuper toute l'image bord à bord comme sur les diapositives 01, 02, 03 et 05, le bandeau de narration restant posé par-dessus en bas.

**semaine-16 · 5-vendredi-illustre-ok-et-tu-relis-trois-fois** — diapositive 3 · *francais*

> Phrase bancale et redondante : « Poser la question prend dix secondes, alors qu'y penser toute la semaine te prend des jours. » Le verbe « prend » revient deux fois dans la même phrase, et « toute la semaine » puis « des jours » disent deux fois la même durée, ce qui rend la comparaison confuse.

À faire : Remplacer la ligne grise par : « Poser la question prend dix secondes ; y penser en boucle te prend des jours. » — la durée n'est plus énoncée deux fois, le parallélisme « prend dix secondes / te prend des jours » devient un vrai contraste, et l'écho de « semaine » avec la ligne du dessus disparaît.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 4 · *autre*

> Le compagnon change encore d'identité : troisième visage différent en quatre diapositives.

À faire : Régénérer la diapositive 4 (et la 3) en reprenant la fiche du compagnon des diapositives 1-2 — homme noir âgé, peau foncée, cheveux courts crépus gris-blanc, lunettes rondes en écaille ambrée, sans moustache, gilet crème — et fixer aussi le pull gris de l'homme aux cheveux blancs sur toute la série.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 5 · *autre*

> Quatrième version du compagnon sur la diapositive de conclusion, celle qui doit justement montrer le couple soudé.

À faire : Régénérer la diapositive 05 avec le compagnon verrouillé sur la description des diapositives 01-02 — homme noir aux cheveux gris courts, lunettes rondes à monture écaille, rasé de près — au lieu de l'homme blanc à barbe rousse (et harmoniser de même les diapositives 03 et 04).

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 2 · *placement-bulle*

> La queue de la bulle « NON, T'AS RIEN FAIT DU TOUT, JE TE PROMETS. » ne va pas jusqu'au personnage : elle s'arrête net sur le bord supérieur de la bulle de pensée placée juste en dessous, et disparaît derrière elle.

À faire : Raccourcir et redresser la queue de la bulle « NON, T'AS RIEN FAIT DU TOUT, JE TE PROMETS. » pour qu'elle se termine en pointe franche et fermée vers y≈370, au-dessus du trait supérieur de la bulle de pensée (ou, au choix, décaler la bulle de pensée vers la droite pour libérer le passage), de sorte que la queue ne soit plus tranchée par une autre bulle.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 3 · *placement-bulle*

> Même défaut : la queue de la bulle « J'AI BESOIN DE SILENCE CE SOIR, C'EST TOUT. » se termine sur la bulle du dessous au lieu de désigner celui qui parle.

À faire : Supprimer entièrement la queue de la bulle « J'AI BESOIN DE SILENCE CE SOIR, C'EST TOUT. » : les deux bulles empilées à gauche appartiennent au même personnage, seule celle du bas doit porter une queue.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 5 · *forme-de-bulle*

> La bulle de pensée « Il m'a vraiment écouté, cette fois. » n'a qu'un seul rond au lieu de la chaîne de trois, et ce rond isolé ne rejoint personne. Il colle en plus les deux bulles de gauche en une seule colonne, ce qui invite à lire la réponse avant la réplique à laquelle elle répond.

À faire : Rétablir la chaîne de trois ronds décroissants (≈22, 14, 10 px) partant du bas de la bulle « Il m'a vraiment écouté, cette fois. » et descendant en diagonale jusqu'à la tête de l'homme aux cheveux blancs, comme sur la diapositive 04 — ce qui suppose de décaler la bulle « JE SAIS, ET ÇA ME FAIT DU BIEN. » (vers la droite ou vers le bas) pour libérer le passage, au lieu du rond unique actuel.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 5 · *visibilite-personnage*

> Un gribouillis en croix barre le verre droit des lunettes de l'homme à barbe rousse et vient sur son œil.

À faire : Effacer les deux traits marron en croix à l'intérieur du verre droit (côté droit de l'image) et redessiner l'arc de paupière fermée complet et continu, identique à celui de l'autre œil.

### Mineur — 79

**semaine-01 · 3-mercredi-illustre-peur-et-anxiete** — diapositive 3 · *francais*

> « déjà » et « juste après » disent deux fois l'immédiateté dans la même phrase. Supprimer l'un des deux : « La réponse te calme une minute, et tu as déjà envie de reposer la question. »

À faire : Supprimer « juste après » : le bloc doit se lire « La réponse te calme une minute, et tu as déjà envie de reposer la question. » — à corriger dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json (ligne 197) et dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-02-peur-et-anxiete.md (ligne 65), puis régénérer la diapositive 03.

**semaine-01 · 3-mercredi-illustre-peur-et-anxiete** — diapositive 1 · *autre*

> Le sous-titre se coupe en laissant le seul mot « non. » sur la deuxième ligne, sous une première ligne pleine. La chute de la phrase, qui porte tout le sens, se retrouve isolée et déséquilibre le bloc. Réduire la largeur du bloc pour couper après « La peur s'arrête quand le danger passe. », ou raccourcir la phrase.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json:131, remplacer sousTitre par « La peur s’arrête quand le danger passe.\nL’anxiété, non. » pour forcer la coupe après « passe. », puis régénérer la diapositive 01.

**semaine-01 · 5-vendredi-bd-reunion-personne-ne-dit-rien** — diapositive 3 · *ordre-de-lecture*

> La réponse est placée à gauche et la question à droite, à des hauteurs presque identiques. La bulle de droite (la question) n'est plus haute que d'environ 70 px et les deux corps de bulle se chevauchent verticalement sur une cinquantaine de pixels : l'œil qui balaie de gauche à droite prend d'abord « NON, DE MON CÔTÉ ÇA ME PARAÎT TRÈS BIEN. », c'est-à-dire la réponse avant la question. La diapositive 1 applique pourtant le bon écart (question nettement plus haut, réponse très en dessous).

À faire : Descendre la bulle de réponse de gauche d'environ 90 px (haut du cadre passant de y≈167 à y≈255, bas de y≈287 à y≈375), afin que son corps commence nettement sous le bas de la bulle de question (y≈217) et supprime tout chevauchement vertical — sa queue vers la tête de l'homme s'en trouvera simplement raccourcie, comme sur la diapositive 01.

**semaine-01 · 5-vendredi-bd-reunion-personne-ne-dit-rien** — diapositive 2 · *autre*

> Rupture de continuité du personnage assis à la droite de l'homme. Sur les diapositives 1, 3 et 4, la collègue placée à sa droite a les cheveux gris-blanc (relevé couleur ≈ RVB 215/205/200). Sur la diapositive 2, à la même place dans la même réunion, elle a les cheveux brun-rosé (≈ RVB 147/96/90). Le lecteur, qui suit la même scène, croit reconnaître la même personne et bute sur le changement.

À faire : Régénérer la diapositive 02 en donnant à la collègue du bord droit le même carré gris-blanc (≈ RVB 215/205/200) que sur les diapositives 01, 03 et 04, le blazer gris foncé et le cadrage restant inchangés.

**semaine-01 · 5-vendredi-bd-reunion-personne-ne-dit-rien** — diapositive 4 · *francais*

> Le bandeau du narrateur annonce un remerciement qui n'existe pas dans le dialogue. La réplique de la femme est un compliment sur la réunion, pas un merci : « elle le remercie » ne décrit pas ce qui est montré. Il faudrait soit « Elle le félicite en souriant », soit une réplique qui contienne effectivement un merci.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json (ligne 590), remplacer « ELLE LE REMERCIE EN SOURIANT. » par « ELLE LE FÉLICITE EN SOURIANT. » dans le champ "narrateur", puis régénérer la diapositive 4.

**semaine-02 · 2-mardi-bd-message-du-patron-samedi** — diapositive 4 · *autre*

> Le bandeau du narrateur décrit un objet qui n'est nulle part dans la case : aucun téléphone posé face cachée n'est visible, ni sur le canapé à côté d'elle, ni sur la table basse. Le lecteur cherche l'objet dont on lui parle et ne le trouve pas.

À faire : Ajouter le téléphone, écran retourné, posé sur le coussin du canapé à sa gauche dans la bande visible au-dessus du bandeau (environ x 620-800 / y 960-1070), là où son regard se dirige déjà ; à défaut de pouvoir régénérer l'image, réécrire le bandeau pour qu'il ne désigne plus d'objet absent du cadre, par exemple « ELLE A MIS SON TÉLÉPHONE FACE CACHÉE. / SA TÊTE Y REVIENT TOUTES LES DEUX MINUTES. »

**semaine-02 · 2-mardi-bd-message-du-patron-samedi** — diapositive 5 · *autre*

> L'illustration ne remplit pas le cadre 1080×1350 : il reste une bande de couleur plate, uniforme sur toute la hauteur, le long des bords latéraux — 20 px à gauche, 8 px à droite. L'asymétrie fait lire ça comme un défaut de recadrage et non comme une bordure voulue ; aucune autre case du carrousel n'en a.

À faire : Régénérer ou recadrer la 05 pour que l'illustration remplisse les 1080 px de large : agrandir l'image de ≈ 3,5 % en largeur (ou rogner de 19 px à gauche et 18 px à droite puis remettre à l'échelle en 1080×1350) afin de supprimer les deux liserés mauve clair verticaux, sans toucher aux bords haut et bas qui sont déjà pleins.

**semaine-02 · 3-mercredi-illustre-deguisements-colere** — diapositive 2 · *francais*

> Répétition de « fatigue » à deux lignes d'écart dans le bloc en bas à droite (titre puis dernière ligne), et une troisième occurrence juste à gauche dans le bloc « Les oublis ». Remplacer par « ça épuise » ou « ça use » dans la dernière ligne.

À faire : Dans le bloc « La fatigue du soir », remplacer la dernière phrase par « Te retenir toute la journée, ça épuise. » (supprimer « ça fatigue énormément »).

**semaine-02 · 4-jeudi-fiche-comprendre-colere** — diapositive 2 · *francais*

> Attelage bancal : on franchit une limite, mais on ne franchit pas une valeur. Écrire par exemple « quand une limite est franchie ou qu'une valeur importante est bafouée ».

À faire : Dédoubler le verbe : remplacer le corps de texte par « La colère se lève quand une limite est franchie ou qu'une valeur importante est bafouée : une injustice, un manque de respect, une promesse trahie. »

**semaine-02 · 5-vendredi-bd-la-phrase-repetee-depuis-deux-ans** — diapositive 5 · *francais*

> « Comme ça » est répété à deux lignes d'écart, de la bulle au bandeau, ce qui donne un effet de bégaiement. Remplacer l'un des deux, par exemple « pourquoi la matinée a tourné ainsi » ou « pourquoi la matinée s'est terminée comme ça ».

À faire : Remplacer la fin du bandeau du narrateur par une formulation qui ne reprend ni « pourquoi » ni « comme ça », par exemple : « IL RESTE SEUL DEVANT L'ÉTAGÈRE DE TRAVERS, SANS COMPRENDRE CE QUI A FAIT BASCULER LA MATINÉE. »

**semaine-02 · 6-samedi-illustre-dispute-en-boucle** — diapositive 2 · *francais*

> Deux répétitions rapprochées. « Téléphone » est repris dès la première ligne du bloc qu'il titre, alors que les trois autres blocs évitent justement de reprendre leur mot-clé ; et « surtout » revient dans deux blocs qui se suivent. Écrire par exemple « Pendant tout le repas, l'écran reste posé sur la table » et supprimer l'un des deux « surtout ».

À faire : Dans contenus.json ligne 1163, remplacer « Pendant tout le repas, son téléphone reste posé sur la table. » par « Pendant tout le repas, l'écran reste posé sur la table. », puis régénérer la diapositive 2 (instagram/ et tiktok/).

**semaine-02 · 6-samedi-illustre-dispute-en-boucle** — diapositive 4 · *francais*

> Après un deux-points, une citation qui forme une phrase complète commence par une majuscule : « Je suis à cran, je reviens dans vingt minutes. »

À faire : Mettre une majuscule au début de la citation : « Avant de sortir, dis-le : « Je suis à cran, je reviens dans vingt minutes. » » — à corriger dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json (ligne 1200) et /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-11-dispute-en-boucle.md (ligne 87), puis régénérer la diapositive 04.

**semaine-03 · 1-lundi-fiche-colere-ou-agressivite** — diapositive 4 · *francais*

> « Et ce qui est tu finit par déborder ailleurs » : « tu » est ici le participe passé de taire, mais sur un compte qui tutoie le lecteur en permanence il se lit d’abord comme le pronom, et la phrase se casse à la première lecture. Préférer « ce qu’on tait » ou « ce qui reste tu ».

À faire : Remplacer « Et ce qui est tu finit par déborder ailleurs, souvent sur les mauvaises personnes. » par « Et ce qu'on tait finit par déborder ailleurs, souvent sur les mauvaises personnes. » (le « on » reprend celui de la diapositive 03).

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 1 · *forme-de-bulle*

> La queue de la bulle de l’homme ne s’arrête pas avant la tête : sa pointe entre dans le crâne et franchit le trait de contour du front, d’une vingtaine de pixels. Remonter la pointe pour qu’elle s’arrête au-dessus du crâne.

À faire : Raccourcir la queue de la bulle de l'homme d'environ 35 px : remonter sa pointe de y≈435 à y≈398, pour qu'elle s'arrête nettement au-dessus du trait de contour du crâne (y≈406) sans le toucher ni l'interrompre.

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 4 · *autre*

> Même défaut de bord qu’en diapositive 1 : une bande blanche verticale d’environ 15 px non dessinée longe tout le bord droit de l’image.

À faire : Régénérer ou étendre la case 04 pour que le mur brun et le trait de cadre noir aillent jusqu'à x = 1079 (à défaut, recadrer l'image à 1065 px de large puis la remettre à l'échelle 1080×1350), afin de supprimer la bande blanche de 15 px sur tout le bord droit.

**semaine-03 · 2-mardi-bd-meme-geste-pas-le-meme-soir** — diapositive 6 · *francais*

> Phrase alourdie par deux répétitions rapprochées : « encore » deux fois et « qui » deux fois dans la même relative. Par exemple : « c’est sa journée de travail, qui n’est pas redescendue et qui occupe encore tout son corps ».

À faire : Supprimer le second « encore » : « c'est sa journée de travail, qui n'est pas encore redescendue et qui occupe tout son corps. »

**semaine-03 · 4-jeudi-illustre-pause-annoncee** — diapositive 4 · *francais*

> Répétition dans la même phrase : « reste seul » puis « une seule question », à quelques mots d'écart. On pourrait écrire « L'autre reste seul avec une question en tête » ou « L'autre reste seul, avec une question qui tourne ».

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json ligne 1733 (et dans prompts/post-16-pause-annoncee.md ligne 79), remplacer « L'autre reste seul avec une seule question en tête » par « L'autre reste seul avec une question qui tourne en tête » — cette formulation supprime l'écho tout en gardant l'idée d'une question unique et obsédante ; si la longueur de ligne pose problème à la composition, « L'autre reste seul avec une question en tête » suffit.

**semaine-03 · 6-samedi-bd-le-silence-du-retour** — diapositive 3 · *francais*

> Répétition de « toute la soirée » sur la même diapositive, à deux lignes d'écart : une fois dans la bulle de pensée, une fois dans le bandeau du narrateur juste en dessous. Une des deux occurrences devrait changer (par exemple « … de s'être senti de trop du début à la fin »).

À faire : Remplacer la fin du bandeau narrateur de la diapositive 3 par « IL N'EST PAS FÂCHÉ CONTRE ELLE : IL A HONTE DE S'ÊTRE SENTI DE TROP DU DÉBUT À LA FIN. », en laissant la bulle inchangée.

**semaine-04 · 3-mercredi-bd-repas-de-famille-la-remarque** — diapositive 1 · *autre*

> Le plat annoncé par la narration ne correspond pas à celui qui est dessiné, ni à celui des diapositives suivantes.

À faire : Régénérer la diapositive 1 avec le même plat que les diapositives 2 et 3 — sauce blanche crème, morceaux de viande clairs et rondelles de carotte orange — dans la cocotte, dans la louche et dans l'assiette du fils, pour que la blanquette annoncée par le titre soit bien celle qui est dessinée.

**semaine-04 · 4-jeudi-illustre-deguisements-honte** — diapositive 2 · *autre*

> Sur la rangée du bas, la gouttière entre les deux colonnes de texte est environ deux fois plus étroite que sur la rangée du haut : les lignes les plus longues des deux colonnes se frôlent et se lisent presque comme une seule ligne.

À faire : Réduire la largeur maximale des blocs de texte des colonnes d'environ 438 px à ~380 px (soit une gouttière minimale d'au moins 70 px) et laisser le texte se réenrouler — concrètement, la ligne « Tu as quelque chose à dire et tu » doit se couper après « dire ».

**semaine-05 · 6-samedi-fiche-la-reparation-en-une-phrase** — diapositive 2 · *francais*

> Le titre « Une vraie excuse referme » laisse le verbe sans complément : on ne sait pas ce qui est refermé. Le corps de texte reprend la même construction avec « reconnaît », juxtaposé à « nomme l'effet » qui, lui, a un complément — l'énumération boite.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py ligne 215-216, remplacer le titre « Une vraie excuse referme » par « Une vraie excuse ne plaide pas » (verbe complet, qui reprend le « elles plaident » du corps) et, dans le corps, « Une excuse qui répare reconnaît, nomme l'effet, et propose » par « Une excuse qui répare nomme l'acte, nomme l'effet, et propose », pour aligner l'énumération sur les trois morceaux de la diapositive 03.

**semaine-06 · 1-lundi-bd-l-appel-qu-on-repousse** — diapositive 4 · *placement-bulle*

> La chaîne de trois ronds de la bulle de pensée est très étirée et reste suspendue loin au-dessus de la dormeuse : le lien entre la bulle et la personne qui pense est lâche, alors qu’il est serré sur les diapositives 01 et 03.

À faire : Descendre la bulle de pensée d'environ 250 px (bas de bulle vers y≈470, la bulle reste sur le mur au-dessus de la tête de lit) et resserrer la chaîne à ~30 px entre ronds comme sur 01 et 03, de façon que le dernier et plus petit rond s'arrête à une trentaine de pixels au-dessus des cheveux (y≈600) — ou, si la bulle doit rester en haut, allonger la chaîne à cinq ou six ronds décroissants régulièrement espacés jusqu'à ce même point.

**semaine-06 · 4-jeudi-bd-il-raconte-la-troisieme-fois** — diapositive 5 · *placement-bulle*

> Le dernier rond de la chaîne de pensée tombe pile sur le trait noir du toit de la voiture : il s'y confond et la chaîne semble s'arrêter net, sans relier la bulle à la conductrice.

À faire : Descendre le dernier rond de la chaîne d'environ 20 px (centre de y≈425 à y≈447, x≈764 inchangé) pour qu'il repose entièrement sur l'aplat brun du toit, dégagé du contour noir.

**semaine-06 · 6-samedi-illustre-apres-la-rupture** — diapositive 3 · *francais*

> Le titre est répété mot pour mot dans les intertitres placés juste en dessous : on lit deux fois « le manque » et deux fois « les moments où ça va » en trois lignes.

À faire : Remplacer le titre par une formule qui cadre sans reprendre les intertitres, par exemple « ÇA VA PAR VAGUES » (ou « DEUX JOURS NE SE RESSEMBLENT PAS »), en laissant « Le manque qui revient » et « Les moments où ça va » inchangés.

**semaine-07 · 1-lundi-fiche-laisser-passer-la-vague** — diapositive 1 · *autre*

> L'étiquette de rubrique annonce le vendredi alors que la publication est programmée le lundi (dossier « 1-lundi », calendrier.csv ligne « 7,lundi,1,Fiche », SEMAINE.md « ## Lundi — Fiche »). Le lecteur voit « vendredi » un lundi.

À faire : Retirer le jour de l'étiquette dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/generateur.py ligne 38 — remplacer etiq="LA PRATIQUE DU VENDREDI · {n}/13" par etiq="LA PRATIQUE · {n}/13" — puis régénérer les fiches et relancer publication.py, pour que la couverture ne nomme plus un jour que le calendrier contredit.

**semaine-07 · 5-vendredi-bd-la-jalousie-qu-on-ose-pas-nommer** — diapositive 3 · *francais*

> « la question suivante » annonce une série de questions numérotées qui n'existe pas ; on attend « et ne pose pas la question » ou « et garde sa question pour elle ».

À faire : Dans le bandeau du narrateur de la diapositive 03, supprimer le mot « SUIVANTE » : écrire « SA COMPAGNE GARDE UN VISAGE PARFAITEMENT CALME ET NE POSE PAS LA QUESTION. »

**semaine-07 · 6-samedi-illustre-jalousie-dans-le-couple** — diapositive 2 · *francais*

> « retomber » s'emploie pour ce qui était monté et redescend — la tension, la pression, l'excitation. Appliqué au calme, l'image se retourne et l'intertitre devient bancal ; « le calme ne dure pas » dirait exactement la même chose.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json ligne 2881, remplacer l'étiquette « LE CALME RETOMBE VITE » par « LE SOULAGEMENT NE DURE PAS » — qui dit exactement ce que veut dire le paragraphe et supprime au passage la répétition avec « te calme une minute » (à défaut, « LE CALME NE DURE PAS ») — puis régénérer la diapositive 02 pour instagram/ et tiktok/.

**semaine-07 · 6-samedi-illustre-jalousie-dans-le-couple** — diapositive 0 · *francais*

> Légende de la publication : les deux possessifs « son » qui se suivent renvoient à deux personnes différentes — le prénom est celui d'un tiers, le téléphone celui du partenaire. À la première lecture on attribue les deux à la même personne.

À faire : Remplacer la première phrase par : « Un prénom revient souvent dans vos conversations, le téléphone de l’autre est posé à l’envers, et te voilà en alerte. » — le tiers devient indéfini et le partenaire est nommé « l’autre », vocabulaire déjà employé plus bas dans la légende.

**semaine-08 · 2-mardi-bd-message-lu-sans-reponse** — diapositive 1 · *texte-coupe*

> Le retour à la ligne coupe l’heure en deux à l’intérieur de la bulle.

À faire : Réécrire le texte de la bulle avec des espaces insécables dans « 20 h 07 » — ou couper la ligne après « message » — pour que l'heure reste entière sur une seule ligne, par exemple : « Elle a lu mon message / à 20 h 07, et elle / n'a pas répondu. »

**semaine-08 · 3-mercredi-illustre-signaux-du-corps** — diapositive 2 · *francais*

> « souvent » revient dans deux blocs qui se suivent immédiatement, et le mot était déjà dans le sous-titre de la diapositive précédente.

À faire : Dans le bloc « Ventre noué » de la diapositive 02, remplacer « Le plus souvent, c'est l'anxiété, parfois la tristesse. » par « C'est l'anxiété la plupart du temps, parfois la tristesse. » — un seul changement qui supprime à la fois l'écho avec le bloc précédent et la reprise mot pour mot du sous-titre de la diapositive 01.

**semaine-08 · 3-mercredi-illustre-signaux-du-corps** — diapositive 3 · *francais*

> Le verbe « arriver » est employé deux fois dans la même phrase, dans deux sens différents.

À faire : Dans la colonne de droite, remplacer « quand le message n’arrive pas » par « quand le message ne vient pas » (garder le « Ça arrive » initial, qui fait volontairement écho à la colonne de gauche) — à corriger dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json ligne 1083 et /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-10-signaux-du-corps.md ligne 77, puis régénérer l’image.

**semaine-08 · 4-jeudi-fiche-traduire-le-pincement** — diapositive 1 · *autre*

> L'étiquette de rubrique annonce le vendredi alors que la publication est programmée le jeudi (dossier « 4-jeudi… », et SEMAINE.md : « Jeudi — Fiche · Traduire le pincement »). Le lecteur verra « LA PRATIQUE DU VENDREDI » sur un post publié un jeudi. Le gabarit du générateur lie la rubrique « pratique » au vendredi (reseaux-sociaux/generateur.py, ligne 38).

À faire : Retirer le jour de l'étiquette dans reseaux-sociaux/generateur.py ligne 38 — remplacer « LA PRATIQUE DU VENDREDI · {n}/13 » par « LA PRATIQUE · {n}/13 » — puis régénérer les fiches et relancer publication.py.

**semaine-08 · 4-jeudi-fiche-traduire-le-pincement** — diapositive 4 · *francais*

> « le radar » arrive avec un article défini alors que la métaphore n'a jamais été posée dans ce carrousel : les diapositives 2 et 3 parlent de « pincement », d'« information » et de « boussole », jamais de radar. Le lecteur ne sait pas de quoi on parle. Reprendre le mot déjà employé (« à quel point le pincement s'apaise ») ou introduire la métaphore avant.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py ligne 320, remplacer « le radar s'apaise » par « le pincement s'apaise », puis régénérer la diapositive 04 (Instagram et TikTok).

**semaine-09 · 1-lundi-illustre-la-regle-des-vingt-secondes** — diapositive 2 · *francais*

> Chaque titre de bloc est répété mot pour mot dans la ligne qui suit immédiatement : « LA PREMIÈRE GORGÉE » → « la première gorgée est parfaite » ; « LES CHAUSSURES DU SOIR » → « Le soir, tu retires tes chaussures » ; « LA PORTE QUI S'OUVRE » → « La porte s'ouvre ». S'ajoute « entre deux portes » (bloc 3) juste au-dessus du titre « LA PORTE QUI S'OUVRE » (bloc 4).

À faire : Casser l'écho du titre dans le corps du texte : bloc 4, écrire « Quelqu'un que tu aimes rentre, et tu lèves à peine les yeux de ton écran. » ; bloc 1, « Le café est encore trop chaud, et c'est justement là que c'est le meilleur. Ça passe pendant que tu lis tes messages. » ; bloc 2, « Tu retires tes chaussures et tes pieds touchent le sol. Cette seconde-là fait vraiment du bien. » ; et remplacer « entre deux portes » (bloc 3) par « en marchant », pour ne pas annoncer le titre suivant.

**semaine-09 · 1-lundi-illustre-la-regle-des-vingt-secondes** — diapositive 3 · *francais*

> Répétition de « reste » à deux lignes d'écart : « reste dessus vingt secondes » puis « c'est comme ça qu'il reste dans ta mémoire ». « reste dessus » est par ailleurs une tournure bancale.

À faire : Remplacer la phrase par : « Quand un bon moment arrive, attarde-toi dessus vingt secondes : regarde, écoute, ne fais rien d'autre. C'est comme ça qu'il s'imprime dans ta mémoire. » — ce qui supprime d'un coup la répétition de « reste » et la tournure « reste dessus ».

**semaine-09 · 3-mercredi-bd-invitation-annulee-soulagement** — diapositive 2 · *placement-bulle*

> La chaîne de trois ronds de la bulle de pensée est posée sur l'oreille du personnage au lieu de s'arrêter à distance de la tête : les deux plus petits ronds chevauchent le trait de l'oreille. La chaîne est en outre presque horizontale et très courte, donc peu lisible comme chaîne de pensée.

À faire : Déplacer la chaîne de trois ronds vers le bas et la droite, hors de la silhouette de l'oreille — le plus petit rond démarrant à au moins 20 px du contour de l'oreille, à hauteur de la mâchoire — et l'orienter en diagonale montante vers le coin inférieur gauche de la bulle, avec des ronds de taille croissante et régulièrement espacés.

**semaine-09 · 4-jeudi-illustre-serenite-ou-indifference** — diapositive 4 · *francais*

> Le quatrième bloc répète son propre titre : même amorce « Ce qui » et deux synonymes (agacer / énerver) sur deux lignes qui se suivent.

À faire : Remplacer la première phrase du bloc « Ce qui t'énervait avant ne te fait plus rien non plus. » par « Aujourd'hui, ça glisse sur toi sans rien déclencher. », pour que le corps ne recopie plus l'amorce du titre.

**semaine-09 · 4-jeudi-illustre-serenite-ou-indifference** — diapositive 0 · *francais*

> Légende (fichier legende.txt, pas une diapositive) : trois verbes de perception quasi identiques dans la même phrase d'ouverture.

À faire : Remplacer la fin de la première phrase pour supprimer le second « voir » et la redite : « Le calme, on ne le remarque pas : ce qui dérange se voit tout de suite, alors qu'un moment paisible, lui, ne fait aucun bruit. »

**semaine-09 · 5-vendredi-fiche-la-joie-notee** — diapositive 4 · *francais*

> Répétition du mot « tout » entre le sur-titre et le titre, placés l'un sous l'autre.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py ligne 368, remplacer le titre « La précision fait tout » par « Le vague ne se retient pas » (le sur-titre « LE DÉTAIL QUI CHANGE TOUT » reste inchangé), puis régénérer la diapositive 04 pour Instagram et TikTok.

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 1 · *autre*

> Le bandeau du narrateur déborde sur trois lignes et laisse un mot seul sur la dernière.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json, pour la diapositive 1 de « la-tendresse-qu-on-avale », remplacer le champ "narrateur" par « SON MARI A COMMENCÉ CE PLAT À SEPT HEURES CE MATIN. » (supprimer le premier segment, qui répète le titre), puis régénérer 01.jpg : le bandeau tiendra alors sur deux lignes, sans mot isolé.

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 2 · *francais*

> Le bandeau du narrateur paraphrase la bulle de pensée qui est juste au-dessus.

À faire : Réécrire le bandeau sans reprendre les mots de la bulle, par exemple : « CES MOTS-LÀ, IL EST À DEUX DOIGTS DE LES DIRE À VOIX HAUTE — ET ÇA L’EFFRAIE. »

**semaine-10 · 3-mercredi-bd-la-tendresse-qu-on-avale** — diapositive 5 · *placement-bulle*

> La chaîne de trois ronds est détachée aux deux extrémités et flotte au milieu d'un mur vide.

À faire : Sur la diapositive 5, resserrer la chaîne de pensée au gabarit des diapositives 2 et 4 : placer le premier rond à 6–10 px sous le contour de la bulle, réduire les écarts entre ronds à 3–5 px et ramener les diamètres à 10/7/4 px, en inclinant la chaîne vers la tempe gauche de l'homme.

**semaine-10 · 6-samedi-fiche-la-question-qui-rapproche** — diapositive 1 · *autre*

> Le bandeau de rubrique de la couverture annonce le vendredi alors que la publication est programmée le samedi.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/generateur.py ligne 38, remplacer etiq="LA PRATIQUE DU VENDREDI · {n}/13" par une étiquette sans jour, etiq="LA PRATIQUE · {n}/13" (cohérente avec « COMPRENDRE · ÉPISODE » et « DEUX MOTS, DEUX CHOSES »), puis relancer python3 generateur.py et régénérer les couvertures des 13 posts « pratique ».

**semaine-11 · 1-lundi-bd-la-question-du-soir** — diapositive 2 · *autre*

> Le bandeau du narrateur est composé sur trois lignes centrées dont la deuxième ne contient que deux mots : la coupure « ... SOUPIRER DANS / LA CUISINE, » laisse une ligne orpheline au milieu du bandeau. Même découpage bancal sur la diapositive 5 (« ... LA MAIN / SUR LA BOUCHE, »).

À faire : Dans reseaux-sociaux-bd/contenus.json, déplacer la coupure « / » du champ « narrateur » pour que chaque ligne tienne dans la largeur du bandeau : diapo 2 → « DEPUIS UNE SEMAINE, ELLE L'ENTEND SOUPIRER / DANS LA CUISINE, ET ELLE A COMPRIS / QUE QUELQUE CHOSE N'ALLAIT PAS. » et diapo 5 → « IL RESTE TROIS SECONDES DANS LE COULOIR, / LA MAIN SUR LA BOUCHE, PUIS IL REPREND / SA VOIX NORMALE. », puis regénérer les deux images.

**semaine-11 · 2-mardi-illustre-recevoir-sans-rembourser** — diapositive 1 · *francais*

> Répétition du verbe rendre entre le titre et le sous-titre placé juste dessous ; de plus « rendre en échange » est pléonastique, « rendre » contient déjà l'idée d'échange.

À faire : Remplacer le verbe du titre par « DONNER » — « RECEVOIR SANS RIEN DONNER EN ÉCHANGE » — ce qui supprime d'un coup la répétition avec « rends » du sous-titre et la redondance de « rendre en échange » (sous-titre inchangé).

**semaine-11 · 2-mardi-illustre-recevoir-sans-rembourser** — diapositive 0 · *francais*

> Légende : la dernière phrase répète « dis » deux fois puis « dire », et « merci » deux fois, en une seule phrase.

À faire : Remplacer « Écoute, dis merci, puis dis ce que ça te fait : l'article du guide montre comment dire merci en nommant précisément ce qui t'a touché. » par « Écoute, dis merci, puis dis ce que ça te fait : l'article du guide montre comment nommer précisément ce que son geste a changé pour toi. »

**semaine-11 · 4-jeudi-bd-la-soupe-et-le-merci** — diapositive 0 · *francais*

> Légende (fichier legende.txt) : la dernière phrase du texte et le bloc qui suit répètent la même information à une ligne d'écart — « test », « 14 émotions » et « en bio » sont redits. Supprimer la phrase « Ton test des 14 émotions est en bio. », le bloc suivant la contient déjà.

À faire : Dans legende.txt, supprimer la dernière phrase du paragraphe, « Ton test des 14 émotions est en bio. », et terminer sur « Ensuite, c’est la façon dont les gens te reçoivent qui change. », le bloc suivant portant déjà la totalité de l'appel au test.

**semaine-11 · 5-vendredi-illustre-merci-plutot-que-desole** — diapositive 4 · *francais*

> Les deux cartes du haut sont côte à côte et emploient la même formule mot pour mot : « Tu remercies l’autre …, au lieu de t’excuser … ». Lues ensemble, elles donnent une impression de copier-coller ; « au lieu de » revient d'ailleurs cinq fois dans le carrousel (diapositives 2, 3 et 4). Varier au moins une des deux.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json ligne 1824, remplacer le texte de la carte « Désolé pour ce pavé » par « Merci d’avoir lu jusqu’au bout. » Écrire longuement n’est pas une faute : quelqu’un t’a lu, et c’est déjà beaucoup. — puis régénérer instagram/04.jpg et tiktok/04.jpg.

**semaine-11 · 5-vendredi-illustre-merci-plutot-que-desole** — diapositive 2 · *francais*

> « autre » revient deux fois dans la même phrase de deux lignes. Écrire par exemple « …passe son temps à te rassurer au lieu de parler du reste. »

À faire : Remplacer la fin de la phrase pour supprimer la seconde occurrence : « Chaque « désolé » demande une réponse. L'autre passe son temps à te rassurer au lieu de parler du reste. » (variante équivalente : « …au lieu d'aborder le vrai sujet. » — éviter « au lieu de passer à la suite », qui créerait un nouvel écho avec « passe ».)

**semaine-12 · 2-mardi-fiche-les-trois-du-soir** — diapositive 3 · *francais*

> « C'est le parce que qui grave. » est bancal sur deux points : « graver » est transitif et reste ici sans complément (graver quoi ?), et « le parce que » est écrit sans guillemets alors que la même expression est entre guillemets deux fois dans les trois lignes précédentes. Quelque chose comme « C'est le « parce que » qui grave la trace. » lèverait les deux problèmes.

À faire : Remplacer « C'est le parce que qui grave. » par « C'est le « parce que » qui grave la trace. »

**semaine-12 · 3-mercredi-illustre-angoisse-dimanche-soir** — diapositive 1 · *francais*

> Le sous-titre reprend mot pour mot deux mots du titre placé juste au-dessus : « déjà » et « lundi ». L'écho est immédiat (une ligne d'écart) et affaiblit l'accroche, d'autant que « DÉJÀ LÀ » est mis en valeur en rouge. Le sous-titre gagnerait à dire la même idée avec d'autres mots.

À faire : Remplacer le sous-titre de la diapositive 1 par « Ton corps est encore en week-end, ta tête a repris le travail. » — la contradiction corps/tête est conservée et renforcée, sans redoubler « déjà » ni « lundi » du titre.

**semaine-12 · 3-mercredi-illustre-angoisse-dimanche-soir** — diapositive 4 · *francais*

> Le texte du second bloc répète mot pour mot l'étiquette verte posée juste au-dessus : « dix minutes » et « vendredi » reviennent tous les deux à une ligne d'écart. Le paragraphe pourrait enchaîner directement (« Tu notes ce qui t'attend lundi… ») puisque l'étiquette a déjà posé le cadre.

À faire : Dans le second bloc, remplacer « Vendredi, tu notes en dix minutes ce qui t'attend lundi. » par « Tu notes ce qui t'attend lundi. » — la pastille verte porte déjà « dix minutes » et « vendredi », et la phrase suivante (« Dimanche, tu cuisines… ») reste inchangée.

**semaine-13 · 2-mardi-bd-liste-du-dimanche** — diapositive 5 · *autre*

> Le bandeau du narrateur annonce un objet qui n'est pas dessiné.

À faire : Retirer l'objet non dessiné du bandeau — écrire « IL ÉTEINT LA LUMIÈRE. / CETTE SEMAINE, IL A FAIT QUATORZE CHOSES SANS EN COMPTER AUCUNE. » — ou, si l'on tient au détail, régénérer l'image avec un carnet visible coincé sous le bras gauche.

**semaine-13 · 3-mercredi-illustre-ce-que-ta-colere-defend** — diapositive 4 · *francais*

> « Dis » répété du titre à la première ligne du paragraphe, deux lignes qui se suivent.

À faire : Dans le bloc 3, remplacer la première phrase du paragraphe par « Préfère « j'ai besoin de finir mes phrases » à un reproche général. » (contenus.json ligne 2439 et le prompt ligne 101), pour que le paragraphe ne redémarre pas sur le « Dis » du titre.

**semaine-13 · 4-jeudi-fiche-la-minute-de-credit** — diapositive 1 · *francais*

> La couverture se contredit d'une ligne à l'autre : le titre promet une minute, le sous-titre juste en dessous annonce trente secondes (et la diapositive 3 confirme « Arrête-toi trente secondes… Trente vraies secondes »). Soit le rituel dure une minute, soit il dure trente secondes.

À faire : Sur la diapositive 1, supprimer la durée du sous-titre pour ne laisser que « reconnaître ta part » (la durée reste annoncée en diapositive 3 et dans la légende), ou, si l'on préfère garder la mention, écrire le titre « La pause de crédit » et conserver « reconnaître ta part — trente secondes ».

**semaine-13 · 4-jeudi-fiche-la-minute-de-credit** — diapositive 4 · *francais*

> Le verbe « compter » revient trois fois en quatre lignes, dont deux fois à deux lignes d'écart dans le corps du texte, avec en plus deux sens différents (« ça compte » = avoir de la valeur ; « celle qui compte l'ordinaire » = dénombrer).

À faire : Remplacer la seule troisième occurrence, en gardant le titre et « ça compte » intacts : « La fierté réservée aux exploits meurt de faim — celle qui accueille l'ordinaire nourrit tous les jours. » (« reconnaît » convient aussi ; l'antithèse meurt de faim / nourrit est préservée).

**semaine-13 · 5-vendredi-bd-un-non-d-une-seconde** — diapositive 3 · *forme-de-bulle*

> Les deux queues sont démesurées et filiformes : chacune est plus longue que la bulle n'est haute (environ 230 px pour celle de gauche, 360 px pour celle de droite) et se réduit très vite à un trait unique, alors que le contour des bulles est épais et régulier. Les deux bords de la queue de gauche n'ont pas la même épaisseur, le droit étant nettement plus gras que le gauche. Sur les autres cases (1, 2, 4) les queues sont de courts triangles bien proportionnés : celle-ci détonne.

À faire : Redessiner les deux queues de la diapositive 3 en courts triangles larges — base sur le bord inférieur de la bulle, longueur d'environ un tiers de la hauteur de la bulle, comme sur les cases 1, 2 et 4 — avec un contour continu de la même épaisseur que celui de la bulle sur les deux bords.

**semaine-13 · 5-vendredi-bd-un-non-d-une-seconde** — diapositive 4 · *francais*

> La bulle de pensée et le bandeau du narrateur disent deux fois la même chose, avec la même locution « même pas » à quelques lignes d'écart : l'information est donnée, puis redonnée. Le bandeau pourrait se contenter de la première phrase, ou dire autre chose que ce que la pensée vient d'énoncer.

À faire : Supprimer la seconde ligne du bandeau « IL N'EST MÊME PAS CONTRARIÉ. » et, si l'on veut garder deux lignes, la remplacer par une phrase qui apporte l'information manquante plutôt que l'écho, par exemple « ELLE Y AVAIT PENSÉ PENDANT TROIS SEMAINES. »

**semaine-13 · 5-vendredi-bd-un-non-d-une-seconde** — diapositive 0 · *francais*

> Légende de la publication (fichier legende.txt, hors diapositives). Deux points : la même proposition passe de l'imparfait au futur pour le même personnage (« n'attendait », « posait », puis « il ira »), ce qui déraille ; et « tout l'entraînement avant » est elliptique — il faudrait « tout l'entraînement d'avant » ou « toute la préparation en amont ».

À faire : Dans legende.txt ligne 2, écrire : « …pas le refus lui-même, mais tout l'entraînement d'avant. Et la plupart du temps, l'autre n'attend même pas de justification — il pose une question, c'est tout, et il ira demander ailleurs sans drame ni rancune. » (présent partout, et « d'avant » — ou « toute la préparation en amont » — à la place de « avant »).

**semaine-13 · 6-samedi-illustre-meteo-interieure** — diapositive 2 · *francais*

> « souvent » revient trois fois sur la diapositive, dont deux fois à une ligne d'écart dans le même bloc, avec en plus la structure « il y a souvent » répétée à l'identique dans les deux phrases qui se suivent. L'une des deux occurrences peut sauter (« Derrière l'angoisse, il y a le besoin qu'on te rassure. »).

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json ligne 3054 (et dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-30-meteo-interieure.md ligne 45), remplacer « Et derrière l’angoisse, il y a souvent le besoin qu’on te rassure. » par « Et derrière l’angoisse, le besoin qu’on te rassure. », puis régénérer la diapositive 02 — l’ellipse supprime d’un coup le « souvent » et le « il y a » répétés tout en gardant le parallélisme et la nuance portée par la première phrase.

**semaine-13 · 6-samedi-illustre-meteo-interieure** — diapositive 3 · *francais*

> Deux répétitions dans un paragraphe de trois lignes : « juste » y est employé deux fois avec deux sens différents (l'adjectif « le mot juste », puis l'adverbe « il faut juste plus de temps »), et « forte » deux fois à une ligne d'écart (« moins forte », « reste forte »).

À faire : Remplacer la fin du paragraphe par « Et si elle reste forte, c'est normal : il lui faut simplement plus de temps. », pour libérer « juste » et le réserver à « le mot juste ».

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 3 · *autre*

> Rupture de continuité vestimentaire : le héros porte un t-shirt vert olive sur cette diapositive alors qu'il porte le même t-shirt bleu-gris sur les diapositives 1, 2, 4 et 5, pour une scène qui se déroule dans la même soirée.

À faire : Régénérer la diapositive 03 en donnant au héros le même t-shirt bleu-gris que sur les diapositives 01, 02, 04 et 05 (teinte approximative RVB 112, 119, 129), sans rien changer d'autre à la scène ni aux textes.

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 1 · *autre*

> Césure malheureuse dans le bandeau du narrateur : la première phrase se termine par un mot seul sur la deuxième ligne. Raccourcir la phrase ou élargir le bandeau.

À faire : Raccourcir la première phrase du bandeau pour qu'elle tienne sur une seule ligne : remplacer « IL RENTRE CHEZ LUI, IL N’Y A PERSONNE D’AUTRE CE SOIR. » par « IL RENTRE CHEZ LUI, PERSONNE D’AUTRE CE SOIR. » (45 caractères, contre les 48 qui tiennent actuellement sur la ligne 1).

**semaine-14 · 2-mardi-bd-calme-impossible-a-savourer** — diapositive 4 · *autre*

> Même défaut de retour à la ligne dans le bandeau du narrateur : un seul mot reste sur la deuxième ligne.

À faire : Forcer le retour à la ligne après « IL SOUPIRE » pour obtenir deux lignes équilibrées : « ACCOUDÉ À LA FENÊTRE, IL SOUPIRE / POUR LA DEUXIÈME FOIS. », la phrase « SES ÉPAULES COMMENCENT ENFIN À REDESCENDRE. » restant sur sa propre ligne.

**semaine-14 · 4-jeudi-illustre-expiration-longue** — diapositive 0 · *francais*

> Légende (pas une diapositive) : « geste » répété à une phrase d'écart, et la tournure « peu de gestes agissent aussi vite sur toi » est bancale (« agir vite sur quelqu'un » se dit mal ; la diapositive 4 emploie la formule juste : « Presque rien d'autre ne calme ton corps aussi vite »).

À faire : Dans legende.txt (ligne 2), remplacer « et peu de gestes agissent aussi vite sur toi » par « et presque rien d'autre ne calme ton corps aussi vite », ce qui supprime la répétition de « geste » et reprend la formule juste de la diapositive 4.

**semaine-14 · 6-samedi-bd-atelier-en-fait-ca-va-pas** — diapositive 3 · *forme-de-bulle*

> La bulle du haut porte une queue alors qu'elle est empilée au-dessus d'une seconde bulle du même personnage : cette queue n'a pas de pointe, elle est coupée par le bord supérieur de la bulle du dessous.

À faire : Supprimer entièrement la queue de la bulle du haut « EN FAIT NON, ÇA VA PAS DU TOUT. » pour en faire un simple rectangle à coins arrondis, contour fermé, et ne laisser la queue que sur la bulle du bas « J'AI PEUR DE DEVOIR FERMER L'ATELIER EN JANVIER. », qui pointe déjà correctement vers le potier.

**semaine-14 · 6-samedi-bd-atelier-en-fait-ca-va-pas** — diapositive 4 · *forme-de-bulle*

> Même défaut que sur la diapositive 3 : la queue de la bulle supérieure de l'apprentie se termine derrière la bulle empilée en dessous, contour ouvert et pointe invisible.

À faire : Supprimer la queue de la bulle « JE SAVAIS PAS QUE TU EN ÉTAIS LÀ. » (deux bulles empilées du même personnage : seule celle du bas doit en porter une) ; à défaut, la raccourcir pour qu'elle se termine en pointe fermée dans l'espace de fond libre au-dessus de la bulle du dessous.

**semaine-15 · 1-lundi-illustre-message-sans-reponse** — diapositive 1 · *francais*

> Répétition du mot « autre » dans le sous-titre, à deux mots d'écart : « pendant que l'autre fait autre chose ». La phrase se lit mal à voix haute. Variante possible : « pendant que l'autre est simplement ailleurs » ou « pendant que l'autre vit sa journée ».

À faire : Remplacer le sous-titre par « Ce que ta tête invente pendant que l’autre vit sa journée » — dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/contenus.json (ligne 1329, champ « sousTitre ») et dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-illustre/prompts/post-13-message-sans-reponse.md (ligne 3), puis régénérer la diapositive 01 pour Instagram et TikTok.

**semaine-15 · 1-lundi-illustre-message-sans-reponse** — diapositive 5 · *autre*

> La phrase de citation affirme l'inverse de ce que dit la légende de la publication. Ici : « Un silence ne dit rien du tout. » Dans la légende : « Parfois, c'est vrai, un silence veut dire quelque chose ». L'affirmation absolue de la diapositive est aussi plus fragile que le propos du carrousel, qui porte sur ce que le silence ne dit pas de toi. Une formulation du type « Un silence ne dit rien de toi » lèverait la contradiction.

À faire : Dans la diapositive 5, remplacer « Un silence ne dit rien du tout. » par « Un silence ne dit rien de toi. », le reste de la citation restant inchangé.

**semaine-15 · 2-mardi-fiche-comprendre-surprise** — diapositive 3 · *francais*

> Énumération bancale : le premier terme est accompagné de sa condition, les deux suivants sont nus. « en joie si c'est une bonne nouvelle, en peur, en colère » — le lecteur attend « en peur si… , en colère si… » et reste en suspens. Soit on donne la condition aux trois, soit on n'en donne à aucun : « en joie, en peur ou en colère, selon ce qui arrive ».

À faire : Remplacer « en joie si c'est une bonne nouvelle, en peur, en colère » par une énumération homogène : soit « en joie si c'est une bonne nouvelle, en peur si c'est une menace, en colère si c'est une injustice », soit, en version courte, « en joie, en peur ou en colère, selon ce qui arrive ».

**semaine-15 · 3-mercredi-bd-telephone-dans-le-noir** — diapositive 5 · *autre*

> Même problème de césure dans le bandeau du narrateur : la première phrase déborde d'un mot et laisse « NUIT. » seul, centré, sur la deuxième ligne. Le bandeau se lit en trois lignes dont une quasi vide, juste au-dessus de la troisième ligne pleine.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json, raccourcir la première phrase du champ « narrateur » de cette diapositive pour qu'elle tienne sur une ligne : remplacer « ELLE ATTEND UNE RÉPONSE QUI NE VIENDRA PAS CETTE NUIT. / SON CORPS RÉAGIT COMME S’IL Y AVAIT UN DANGER. » par « ELLE ATTEND UNE RÉPONSE QUI NE VIENDRA PAS. / SON CORPS RÉAGIT COMME S’IL Y AVAIT UN DANGER. », puis régénérer la diapositive 05.

**semaine-15 · 4-jeudi-illustre-boule-au-ventre-lundi** — diapositive 6 · *francais*

> « À quel moment exact la boule se serre ? » : ce n’est pas la boule qui se serre, c’est le ventre. Une boule arrive, se forme, s’installe. La légende du post utilise d’ailleurs le bon verbe (« note l’heure exacte où la boule arrive ») et la diapositive 1 dit bien « TON VENTRE SE SERRE ». Écrire « À quel moment exact la boule arrive ? » ou « À quel moment exact ton ventre se serre ? ».

À faire : Remplacer le sous-titre de la diapositive 6 par « À quel moment exact la boule arrive ? » (formulation identique à celle de la légende).

**semaine-15 · 6-samedi-bd-quarante-longueurs** — diapositive 3 · *francais*

> « LA NAGEUSE PLUS ÂGÉE » est une tournure bancale : en français, un comparatif employé ainsi, sans complément, demande l’article du superlatif ou une virgule. Écrire « LA NAGEUSE LA PLUS ÂGÉE » ou « L’AUTRE NAGEUSE, PLUS ÂGÉE, NE CHANGE PAS DE SUJET ».

À faire : Dans le bandeau du narrateur de la diapositive 3, remplacer « LA NAGEUSE PLUS ÂGÉE NE CHANGE PAS DE SUJET » par « LA NAGEUSE LA PLUS ÂGÉE NE CHANGE PAS DE SUJET » (ou, plus proche du ton du reste de la série, « L'AUTRE NAGEUSE NE CHANGE PAS DE SUJET »).

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 2 · *autre*

> Le décompte des vêtements recule d'une diapositive à l'autre : la diapositive 1 annonce déjà « TROISIÈME HAUT ESSAYÉ », et la diapositive 2 revient au deuxième. Le lecteur qui fait défiler passe de trois à deux, puis de nouveau à trois en diapositive 3.

À faire : Dans /Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd/contenus.json, posts[20].titre, remplacer « 7 H 10.|TROISIÈME HAUT ESSAYÉ. AUCUN NE VA. » par « 7 H 10.|PREMIER HAUT ESSAYÉ. ÇA NE VA PAS. », puis régénérer la diapositive 01 — les bandeaux des diapos 2 (« deuxième pull ») et 3 (« trois hauts ») restent inchangés, le décompte devient 1 → 2 → trois.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 3 · *autre*

> Deux types de bulles pour la même personne seule dans sa chambre : la bulle du haut est une bulle de dialogue (capitales, queue triangulaire), celle du bas une bulle de pensée (minuscules, chaîne de ronds). Les diapositives 1, 2 et 5 n'utilisent que des bulles de pensée.

À faire : Transformer la bulle du haut en bulle de pensée pour la rendre cohérente avec les diapositives 1, 2 et 5 : passer le texte en minuscules (« Allez, il faut que j'y aille maintenant. ») et remplacer la queue triangulaire pointue par la chaîne de trois petits ronds descendant vers la tête du personnage.

**semaine-16 · 4-jeudi-bd-miroir-du-matin** — diapositive 3 · *forme-de-bulle*

> La chaîne de la bulle de pensée est minuscule et posée sur les cheveux du personnage, au lieu de s'arrêter à distance de la tête comme sur les diapositives 1, 2 et 5.

À faire : Redessiner la chaîne de pensée de la diapositive 03 au même gabarit que les 01, 02 et 05 — trois ronds cernés de noir, d'environ 21, 15 et 9 px de diamètre, décroissants — et la déplacer sous le bord bas de la bulle dans le fond de fenêtre libre (vers x 250-340, y 630-730) pour qu'elle descende vers la tête en s'arrêtant à distance des cheveux, au lieu de reposer dessus.

**semaine-16 · 6-samedi-fiche-emotion-ou-humeur** — diapositive 0 · *francais*

> Dans legende.txt (ligne des hashtags), le mot-dièse « #émotions » est écrit deux fois, au début et à la fin de la même ligne.

À faire : Dans legende.txt ligne 7, supprimer le « #émotions » final (celui de fin de ligne) et le remplacer par un mot-dièse encore absent, par exemple « #introspection », pour garder huit hashtags distincts.

**semaine-17 · 1-lundi-bd-besoin-de-silence-pas-de-toi-en-moins** — diapositive 1 · *placement-bulle*

> La queue de la bulle « NON, PAS CE SOIR, J'AI PAS ENVIE. » part vers le bas, dans le ventre de celui qui parle, alors que sa tête est juste au-dessus de la bulle.

À faire : Déplacer la queue de la bulle « NON, PAS CE SOIR, J'AI PAS ENVIE. » du bord inférieur vers le bord supérieur du cadre, légèrement à droite du centre (vers x≈300), en la faisant pointer vers le haut en direction du menton et de la bouche de l'homme aux cheveux blancs, comme le fait déjà la bulle de droite.

**semaine-17 · 3-mercredi-fiche-la-meteo-interieure** — diapositive 3 · *francais*

> Point 3 : « Le besoin pointe l'action » est une tournure bancale (pointer quelque chose = le désigner du doigt, pas l'indiquer), et « besoin » est répété deux lignes plus haut dans le titre du point.

À faire : Remplacer « Le besoin pointe l’action. » par « Le besoin indique l’action. » (ou, pour garder la métaphore de la boussole, « Le besoin pointe vers l’action. ») — dans l'image 03 et à la ligne 661 de /Users/cavalier/Dev/Site Emotion/reseaux-sociaux/contenus.py, puis régénérer la diapositive.

## Ce qui demande de régénérer une illustration

Les crédits nanobanana sont épuisés ; ces défauts viennent du générateur d'images et
ne se réparent pas à la composition. Ils rejoignent les neuf illustrations déjà en
attente, listées dans `reseaux-sociaux-bd/REPRENDRE.md`.
