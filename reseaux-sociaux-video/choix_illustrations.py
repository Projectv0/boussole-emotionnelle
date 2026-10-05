# -*- coding: utf-8 -*-
"""Les illustrations nanobanana choisies pour chaque phrase, dans l'ordre.

Une image par phrase posée sur fond d'image : la liste commence à la première phrase
après l'accroche sur fond noir, et s'arrête à l'avant-dernière (la dernière, « Fais le
test », garde l'image de la phrase d'avant sous la page de fin).

« I: » = reseaux-sociaux-illustre/illustrations (crayon et aquarelle, carré)
« B: » = reseaux-sociaux-bd/illustrations       (bande dessinée, portrait)

Chaque image n'est utilisée qu'une fois sur les vingt vidéos. Le catalogue complet,
avec la description de chaque image, est dans illustrations/catalogue.json.
"""

CHOIX = {
    "01-ca-va": [
        "B:table-diner-verre-leve",            # Darwin : l'émotion s'écrit sur le visage
        "B:table-diner-rire-decale",           # avant même qu'on décide de la montrer
        "B:lavabo-compte-a-rebours",           # les sourcils, la mâchoire, le souffle
        "B:table-voisine-question-douce",      # ce que tu ne dis pas se voit quand même
        "I:bureau-pause",                      # cette semaine, compte doucement
        "B:table-porte-qui-se-referme",        # combien de fois tu as répondu « ça va »
        "I:anniversaire-sourire-poli",         # ce n'est pas de la politesse
        "I:couv-tendresse-avalee",             # une émotion qui n'a pas trouvé son mot
        "I:cover-message-envoyer",             # elle attend qu'on la nomme
        "I:table-ecoute",                      # seize situations, quatorze émotions
        "I:samedi-libre",                      # et la place qu'elles occupent chez toi
    ],
    "02-colere": [
        "I:salon-tendu",                       # Sénèque : une courte folie
        "I:dispute-cuisine",                   # une tempête qui passe
        "I:irritabilite-cuisine",              # qu'on peut apprendre à voir venir
        "I:couv-colere-table",                 # un signal avant d'éclater
        "I:machoire-serree",                   # la mâchoire qui se serre
        "I:sarcasme-repas",                    # la phrase qu'on prépare au lieu d'écouter
        "I:couv-machoire-serree",              # ce signal, tu l'as déjà
        "I:porte-claquee",                     # le voir avant la porte
        "I:escalier-souffle",                  # une affaire d'entraînement
        "I:marche-trottoir",
        "I:retour-table",
    ],
    "03-ruminer": [
        "I:carnet-sur-les-genoux",             # un empereur écrivait, pour lui seul
        "I:honte-question-reunion",            # ce n'est pas elle qui te trouble
        "I:proces-rejoue",                     # c'est le jugement que tu portes
        "I:souvenir-canape",                   # il s'appelait Marc Aurèle
        "I:rejeu-nuit",                        # le reste, c'est toi qui l'ajoutes
        "I:tri-demain-matin",                  # sépare ce qui a été dit
        "I:relecture-tard",                    # de ce que tu as entendu
        "I:carnet-cuisine",                    # écris les deux
        "I:pensees-en-boucle",                 # la deuxième te tient éveillé
        "I:muret-dehors",
        "I:fauteuil-relache",
    ],
    "04-dimanche-soir": [
        "B:liste-dimanche-table-cuisine",      # un professeur écrivait chaque jour
        "B:liste-dimanche-stylo-suspendu",     # il s'appelait Alain
        "B:liste-dimanche-quatre-lignes-de-plus",  # humeur et volonté
        "B:salon-dimanche-lumiere-qui-baisse", # ce qui descend le dimanche soir
        "I:dimanche-soir",                     # une humeur, elle vient toute seule
        "I:sac-prepare",                       # ce que tu en fais
        "I:dimanche-soir-cuisine",             # dimanche prochain, regarde bien
        "B:cuisine-lundi-cafe-intact",         # toute la semaine, ou une seule chose
        "B:cuisine-lundi-ventre-serre",        # que tu n'as pas encore nommée
        "B:rue-matin-sac-epaule",              # ce n'est jamais toute la semaine
        "B:salon-dimanche-lampe-allumee",
        "B:liste-dimanche-interrupteur",
    ],
    "05-jalousie-couple": [
        "B:canape-rire-au-telephone",          # un moraliste écrivait que la jalousie
        "B:canape-tasse-immobile",             # se nourrit dans les doutes
        "B:canape-epaule-abandon",             # elle s'éteint avec la certitude
        "B:canape-telephone-retourne",         # il s'appelait La Rochefoucauld
        "I:telephone-retourne",                # pas de ce que tu sais
        "I:verification-nocturne",             # de ce que tu ne sais pas
        "I:fenetre-seule",                     # de quoi as-tu peur ?
        "I:salle-de-bain-nuit",                # pas de qui, de quoi
        "I:cafe-sourire-fige",                 # d'être remplacé ?
        "I:voiture-enquete",                   # ce n'est pas l'autre qui te répondra
        "I:miroir-gorge",                      # c'est toi
        "I:canape-aveu",
        "I:voiture-aveu",
    ],
    "06-message-vu": [
        "B:canape-soir-telephone-lu",          # nous souffrons plus souvent
        "B:canape-defilement-nocturne",        # en imagination qu'en réalité
        "B:cuisine-nuit-message-hesitant",     # le silence non plus
        "I:couv-message-relu",                 # c'est toi qui les as écrites
        "I:relire-son-message",                # écris ce que tu crois
        "I:question-posee",                    # puis écris ce que tu sais
        "B:salon-samedi-canape-telephone-retourne",  # compare les deux colonnes
        "I:attente-calme",                     # c'est une attente
        "B:cafe-matin-retrouvailles",          # sans lui inventer une histoire
        "B:cafe-tasse-reposee",
        "I:question-simple",
    ],
    "07-parler-en-reunion": [
        "B:salle-reunion-accord-general",      # Montaigne : ce dont il avait le plus peur
        "B:reunion-stylo-suspendu",            # la peur elle-même
        "B:reunion-regard-vers-la-porte",      # la peur de la chose
        "I:silence-reunion",                   # ce n'est pas la réunion qui te bloque
        "I:reunion-silencieuse",               # le silence après ta phrase, un regard
        "B:reunion-fin-chaises-repoussees",    # aucun des deux n'est arrivé
        "I:gorge-couloir",                     # ta gorge se serre-t-elle
        "I:avant-la-reunion",                  # ou avant de parler ?
        "I:escalier-avant-presentation",       # une peur qui a pris de l'avance
        "I:dix-secondes-escalier",
        "B:couloir-apres-reunion-dossier-contre-soi",
    ],
    "08-surprise": [
        "I:cadeau-genoux",                     # Descartes classait les passions
        "I:velo-qui-surgit",                   # pas la joie, pas la peur
        "I:atelier-admiration",                # l'admiration
        "I:porte-qui-claque",                  # la surprise est une porte
        "I:message-pour-rien",                 # ce qui entre après
        "I:bonjour-regard",                    # mais la porte, c'est elle
        "I:feu-rouge-freinage",                # la prochaine fois que quelque chose t'arrive
        "I:cafe-bonne-nouvelle",               # ce qui suit la seconde de surprise
        "B:atelier-la-phrase-qui-sort",        # la même émotion, ou une différente ?
        "I:vingt-secondes-parking",            # ce que tu attends du monde
        "I:couv-vapeur-couloir",
        "I:rire-qui-fait-lever-la-tete",
    ],
    "09-pleurer": [
        "I:cuisine-chanson",                   # un psychologue a retourné la question
        "I:quai-metro-larmes",                 # on croit qu'on pleure parce qu'on est triste
        "I:voiture-chanson",                   # triste parce qu'on pleure
        "I:larmes-retenues-escalier",          # le corps d'abord
        "I:supermarche-fige",                  # pas de la pub
        "I:epaule-plus-basse",                 # un corps qui était plein
        "I:larmes-cuisine",                    # qui a trouvé une sortie
        "I:jardin-vague",                      # ne cherche pas ce qui vient d'arriver
        "I:pile-de-dossiers",                  # ce qui s'accumule depuis des jours
        "I:couv-larmes-voiture",               # seulement la goutte
        "I:confier-deux-tasses",
        "I:cafe-chaleur",
    ],
    "10-trois-heures": [
        "I:lit-trois-heures",                  # un philosophe danois appelait l'angoisse
        "I:nuit-plafond",                      # le vertige de la liberté
        "I:reveil-nuit",                       # il s'appelait Kierkegaard
        "B:lit-plafond-deux-heures",           # tu n'as rien à faire
        "B:cuisine-verre-d-eau-minuit",        # rien pour tenir la pensée
        "I:boucle-scenario",                   # elle regarde le vide
        "I:scenarios",                         # ce n'est pas le problème qui te réveille
        "B:canape-plafond-une-heure-du-matin", # l'espace qu'il trouve à cette heure-là
        "I:carnet-dix-minutes",                # note-le sur un papier
        "I:bord-du-lit-soir",                  # un endroit où être
        "I:assise-pieds-au-sol",               # qui ne soit pas ta tête
        "B:balcon-matin-appel-lance",
        "I:souffle-fenetre",
    ],
    "11-imposteur": [
        "B:open-space-felicitation-publique",  # un ancien esclave devenu philosophe
        "B:bureau-chaise-recul-epaules",       # ce qui dépend de toi
        "B:bureau-main-sur-la-nuque",          # il s'appelait Épictète
        "I:nimporte-qui",                      # ton travail dépend de toi
        "I:couv-compliment-esquive",           # leur verdict ne dépend pas de toi
        "I:merite-rendu-equipe",               # la deuxième colonne
        "I:ce-netait-rien",                    # fais l'inventaire
        "I:chance-invoquee",                   # ce que tu as fait
        "B:machine-a-cafe-seul-gobelet",       # la liste est plus longue que la voix
        "B:fenetre-bureau-reflet-sourire",     # elle l'est toujours
        "I:couv-victoire-discrete",
        "I:couv-nouvelle-rangee",
    ],
    "12-dire-non": [
        "B:palier-il-sonne-encore",            # Aristote : une émotion juste
        "B:palier-les-trois-arguments",        # la bonne personne, au bon moment
        "B:palier-le-non",                     # dire non n'est pas une faute
        "I:non-court",                         # une émotion qui a trouvé sa bonne adresse
        "I:demande-couloir",                   # ce n'est pas le non qui fait mal
        "I:oui-automatique",                   # l'idée que l'autre va moins t'aimer
        "I:non-alternative",                   # la dernière fois qu'on t'a dit non
        "B:palier-rien-ne-seffondre",          # tu as juste réorganisé ta journée
        "I:non-au-telephone",                  # c'est ce qu'il fera aussi
        "B:palier-elle-referme-la-porte",
        "I:non-differe",
    ],
    "13-amitie": [
        "I:canape-fou-rire",                   # Aristote distinguait trois amitiés
        "I:table-rires",                       # l'utilité, le plaisir
        "I:rire-dehors",                       # ce qu'on est, au fond
        "I:appart-visite",                     # elles finissent quand leur raison finit
        "I:eclaircie-sur-un-banc",             # la troisième, non
        "I:cles-appartement",                  # quand le contexte change
        "B:supermarche-rayon-rencontre",       # l'amitié du contexte
        "B:supermarche-au-revoir-rapide",      # ce qui te manque : la personne
        "B:cuisine-ranger-courses-arret",      # ou l'époque où vous étiez ensemble
        "B:cuisine-fenetre-soir-nommer",       # la réponse change ce que tu dois faire
        "B:cafe-deux-ans-sans-se-voir",
        "B:trottoir-devant-le-cafe",
    ],
    "14-rupture": [
        "I:cote-du-lit",                       # il le couvre de cristaux
        "I:attente-cafe",                      # une branche couverte de diamants
        "I:chaise-vide",                       # la cristallisation
        "I:deux-tasses",                       # elle n'existe pas tout à fait
        "I:relire-la-nuit",                    # c'est toi qui les as posés
        "I:lettre-sous-la-lampe",              # écris trois choses qui t'agaçaient
        "I:projets-ranges",                    # si tu n'en trouves aucune
        "I:dos-a-moitie-tourne",               # tu regardes encore la branche
        "I:mettre-en-sourdine",
        "I:marche-du-matin",
    ],
    "15-reconnaissance": [
        "I:open-space-applaudissements",       # Épicure séparait
        "I:envie-reconnaissance",              # les désirs naturels des désirs vains
        "I:salle-pause-felicitations",         # qu'aucune quantité ne remplit
        "I:efforts-invisibles",                # le besoin d'être vu est naturel
        "I:frontiere-reunion",                 # que ce soit lui, devant tout le monde
        "I:classement-ecran",                  # le désir qui ne se remplit pas
        "I:bureau-merci",                      # qui a vu ce que tu as fait ?
        "I:openspace-compliment",              # n'importe qui
        "I:machine-a-cafe",                    # il y a presque toujours quelqu'un
        "I:fier-de-quelquun-dautre",
        "I:propose-la-suite",
    ],
    "16-fatigue": [
        "B:fatigue-samedi-bord-du-lit",        # Pascal : tout le malheur des hommes
        "B:fatigue-canape-tasse-froide",       # rester en repos dans une chambre
        "B:fatigue-fenetre-il-fait-beau",      # ce n'est pas ce que tu fais
        "I:avant-canape-eteint",               # c'est ce que tu fuis
        "I:priorites-qui-changent",            # l'écran qu'on rallume
        "I:fatigue-bus",                       # fuir demande de l'énergie
        "B:calme-soir-assis-trop-droit",       # dix minutes, sans rien
        "B:calme-soir-fenetre-ouverte",        # note ce qui remonte
        "B:fatigue-mains-sur-les-genoux",      # c'est ça qui te fatigue
        "B:calme-soir-assis-par-terre",
        "B:calme-soir-poser-les-cles",          # (chez toi : il rentre et pose ses clés)
    ],
    "17-telephone": [
        "B:telephone-noir-lueur-sur-le-visage",  # une philosophe écrivait que l'attention
        "I:banc-parc-attention",               # la plus pure forme de la générosité
        "B:telephone-noir-pouce-immobile",     # elle s'appelait Simone Weil
        "I:ecran-retour",                      # ce que tu as de plus précieux
        "I:ecran-a-table",                     # un écran qui n'a rien à te dire
        "B:telephone-noir-troisieme-relecture",  # une émotion qui cherche une sortie
        "I:bus-ecran",                         # l'ennui, l'attente
        "I:main-qui-s-arrete",                 # arrête ta main une seconde
        "B:telephone-noir-face-contre-le-matelas",  # qu'est-ce que je ne veux pas ressentir ?
        "B:telephone-noir-plafond-une-heure",  # la réponse vient vite
        "I:chaussures-enlevees",
        "I:couv-musique-linge",
    ],
    "18-parents": [
        "B:salon-papa-la-meme-histoire",       # Montaigne : la plus grande chose du monde
        "B:salon-papa-troisieme-fois",         # savoir être à soi
        "B:dimanche-regard-qui-hesite",        # en regardant son propre âge
        "B:cuisine-bocal-qui-resiste",         # ce qui se serre quand tu les vois vieillir
        "I:tendresse-porte",                   # de l'amour qui découvre qu'il a une durée
        "B:voiture-devant-la-maison",          # on ne le règle pas, on le regarde
        "B:dimanche-manteau-et-plat",          # pose une question
        "I:cafe-du-matin",                     # sur eux, sur avant toi
        "I:cafe-fierte",                       # donne-lui celui-là
        "B:entree-manteau-le-depart",
        "B:dimanche-porte-entrouverte",
    ],
    "19-gratitude": [
        "B:coloc-soupe-a-la-porte",            # la plus grande des vertus
        "B:coloc-elle-pose-le-bol",            # la mère de toutes les autres
        "B:coloc-le-reflexe-desole",           # le merci a duré une seconde
        "B:coloc-le-mot-qui-change",           # ce qui reste quand tu y repenses
        "B:coloc-la-soupe-tiede",              # la plupart n'y repensent jamais
        "I:merci-recu",                        # une chose que quelqu'un a faite pour toi
        "I:cafe-merci",                        # une seule
        "I:banc-parc-merci",                   # c'est difficile
        "I:cuisine-courses",                   # tu ne les comptes pas
        "I:etagere-outils",
        "I:fin-de-repas",
    ],
    "20-ne-plus-rien-ressentir": [
        "I:bougies-visage-fixe",               # Spinoza : la joie est un passage
        "I:cuisine-musique-plate",             # plus grande, plus petite
        "I:invitation-sans-elan",              # des passages, des mouvements
        "I:arret-de-bus-sans-agacement",       # sentir, c'est bouger
        "I:chambre-immobile",                  # ce n'est pas la paix, c'est l'arrêt
        "I:rideaux-tires",                     # quelque chose a fait trop mal
        "I:matin-lourd",                       # tout a été baissé d'un coup
        "I:fenetre-fin-d-apres-midi",          # la dernière fois que tu as senti
        "I:tete-ailleurs",                     # ce qui s'est passé juste après
        "I:canape-annulation",                 # c'est là que ça s'est éteint
        "I:laptop-referme",
        "I:bus-jour-calme",
    ],
}
