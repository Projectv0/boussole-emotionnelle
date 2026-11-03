# -*- coding: utf-8 -*-
"""Les 13 semaines de contenus — 3 posts par semaine.

Trois séries qui reviennent chaque semaine :
  · lundi    « Comprendre »            — une émotion expliquée
  · mercredi « Deux mots, deux choses » — une distinction qui change la lecture
  · vendredi « La pratique du vendredi » — un geste concret à tester

Chaque post : couverture et diapositive finale générées automatiquement ;
ici, seulement les diapositives du milieu, la légende et les hashtags.
"""

BASE_TAGS = "#émotions #psychologie #développementpersonnel #bienêtre #connaissancedesoi #santémentale"

def T(k, t, c, vign=None):
    d = dict(k=k, t=t, c=c)
    if vign: d["vign"] = vign
    return ("texte", d)

def D(t, a, b, note):
    return ("duo", dict(t=t, a=a, b=b, note=note))

def E(k, t, etapes):
    return ("etapes", dict(k=k, t=t, e=etapes))

def P(serie, n, slug, titre, sous, slides, question, legende, tags, emo=None, emos=None):
    return dict(serie=serie, n=n, slug=slug, titre=titre, sous=sous, slides=slides,
                question=question, legende=legende, tags=f"{BASE_TAGS} {tags}",
                emo=emo, emos=emos)

SEMAINES = [

# ————————————————————— SEMAINE 1 — l'alarme intérieure —————————————————————
[
P("comprendre", 1, "comprendre-anxiete", "L’anxiété",
  "quand ton cerveau imagine le pire un peu trop vite",
  [
   T("À QUOI ELLE SERT", "Elle t’aide à prévoir ce qui vient",
     "Quand tu ne sais pas ce qui va se passer, ton cerveau imagine les scénarios possibles. Et si je rate mon train ? Et si la réunion se passe mal ? À petite dose, cette inquiétude est utile : elle te pousse à réviser, à prévoir et à partir en avance."),
   T("QUAND ELLE COÛTE", "Quand elle tourne en boucle",
     "L’anxiété utile mène à une décision, puis elle s’arrête. L’anxiété qui épuise ne s’arrête jamais : elle repasse les mêmes scénarios sans rien décider. Ton corps se prépare alors à des dangers qui n’arriveront pas, et il se fatigue."),
   T("LE PIÈGE", "Éviter rend l’alarme plus forte",
     "Éviter une situation qui t’inquiète te soulage tout de suite. Mais ton cerveau en tire une conclusion : le danger était réel. La fois suivante, l’alarme sonne encore plus fort. C’est le mécanisme le plus important à connaître."),
  ],
  "Et toi, quelle place l’anxiété prend-elle dans ta vie en ce moment ?",
  "L’anxiété n’est pas un défaut. C’est un système d’alerte qui imagine l’avenir pour te protéger, et qui s’emballe parfois. Voici comment elle fonctionne, et le piège qui l’entretient.",
  "#anxiété #stress", emo="anxiete"),

P("distinction", 1, "peur-ou-anxiete", "Peur ou anxiété ?",
  "les deux te protègent, mais pas du même danger",
  [
   T("LA PREMIÈRE", "La peur",
     "Elle réagit à un danger présent et bien réel : la voiture qui déboule, le bruit dans la nuit. Elle arrive tout de suite, elle est intense, et elle retombe quand le danger passe.", vign="peur"),
   T("LA SECONDE", "L’anxiété",
     "Elle réagit à un danger futur et flou, celui des « et si ». Rien ne te menace ici et maintenant : c’est ton imagination qui tourne. Elle peut durer des heures ou des jours, sans jamais retomber.", vign="anxiete"),
   D("Ce qui les distingue",
     "La peur répond au présent. Elle se calme quand le danger passe.",
     "L’anxiété répond à un futur imaginé. Elle ne rencontre jamais son danger.",
     "C’est pour cela qu’on ne calme pas une anxiété comme on rassure une peur. Il n’y a rien à fuir, seulement un scénario à ralentir."),
  ],
  "Chez toi, laquelle des deux parle le plus fort ?",
  "On les confond tout le temps. Pourtant, la peur et l’anxiété ne répondent pas au même danger, et ne se traversent pas de la même façon.",
  "#anxiété #peur", emos=["peur", "anxiete"]),

P("pratique", 1, "respiration-expiration-longue", "La respiration\nà expiration longue",
  "trois minutes suffisent à calmer ton corps",
  [
   T("POURQUOI ÇA MARCHE", "L’expiration est un frein",
     "Quand tu expires plus longtemps que tu inspires, tu actives la partie du système nerveux qui ralentit le cœur. Ce n’est pas une astuce de magazine. C’est le moyen le plus direct dont ton corps dispose pour se calmer."),
   E("COMMENT FAIRE", "Fais-le pas à pas",
     [("Inspire sur 4 temps", "par le nez, sans forcer."),
      ("Expire sur 6 temps", "par la bouche, comme si tu soufflais sur une bougie sans l’éteindre."),
      ("Continue 3 minutes", "l’effet arrive vers la deuxième minute, pas avant. Tiens jusque-là.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Entraîne-toi les jours calmes",
     "Un corps entraîné redescend beaucoup plus vite les jours difficiles. Trois minutes chaque jour tranquille valent mieux que dix minutes en pleine tempête."),
  ],
  "Envie de savoir d’où tu pars, avant de commencer ?",
  "Trois minutes, aucun matériel. La respiration à expiration longue est le geste le plus direct pour calmer un corps en alerte. Voici comment la faire, et le détail que presque tout le monde rate.",
  "#respiration #anxiété", emo="serenite"),
],

# ————————————————————— SEMAINE 2 — la force qui défend —————————————————————
[
P("comprendre", 2, "comprendre-colere", "La colère",
  "elle défend tes limites",
  [
   T("À QUOI ELLE SERT", "Elle garde ce qui compte",
     "La colère monte quand quelqu’un franchit une de tes limites ou piétine une valeur qui compte pour toi : une injustice, un manque de respect, une promesse trahie. Elle ne cherche pas le conflit. Elle défend ton territoire."),
   T("DANS LE CORPS", "Elle arrive avant la pensée",
     "La chaleur monte, les mâchoires se serrent, les bras se chargent d’énergie. Ton corps réagit avant que ta raison ait compris quoi que ce soit. C’est pour cela qu’on dit parfois des choses qu’on regrette : la pensée arrive en retard."),
   T("LE PIÈGE", "Une colère enterrée ne meurt pas",
     "Quand tu t’interdis de l’exprimer, elle ressort ailleurs : en rancune, en sarcasme, en fatigue ou en tension. Une colère écoutée à temps fait moins de dégâts qu’une colère enterrée."),
  ],
  "Et toi, ta colère prend-elle trop de place, ou pas assez ?",
  "La colère n’est pas le contraire de la gentillesse. Elle défend tes limites. Le problème n’est presque jamais de la ressentir, mais ce qu’on en fait, ou ce qu’on en tait.",
  "#colère #limites", emo="colere"),

P("distinction", 2, "colere-ou-agressivite", "Colère ou agressivité ?",
  "l’une est une émotion, l’autre est un comportement",
  [
   T("LA PREMIÈRE", "La colère",
     "C’est un signal intérieur qui te dit qu’une limite importante vient d’être franchie. Tu peux la ressentir très fort sans blesser personne. Ressentir n’a jamais fait de mal à qui que ce soit.", vign="colere"),
   T("LA SECONDE", "L’agressivité",
     "C’est un comportement : on attaque, on humilie, on casse. Elle peut venir de la colère, mais aussi de la peur, de la honte ou de l’habitude. On peut même être agressif sans être en colère du tout.", vign="colere"),
   D("Ce qui les distingue",
     "La colère se ressent. Comme signal, elle est toujours légitime.",
     "L’agressivité se choisit. Comme réponse, elle se discute toujours.",
     "Interdire la colère ne rend pas plus doux, cela rend muet. Et ce qu’on tait finit par déborder ailleurs, souvent sur les mauvaises personnes."),
  ],
  "On t’a appris à écouter ta colère, ou à la taire ?",
  "Quand on dit « calme-toi », on confond deux choses : l’émotion et le comportement. On peut être très en colère et rester respectueux. On peut aussi être très calme et profondément blessant.",
  "#colère #communication", emos=["colere", "degout"]),

P("pratique", 2, "la-pause-annoncee", "La pause annoncée",
  "tu sors de la pièce sans abîmer le lien",
  [
   T("POURQUOI ÇA MARCHE", "Sous l’adrénaline, on n’écoute plus",
     "Quand la colère dépasse un certain seuil, ton corps passe en mode combat. Tu ne peux plus écouter, nuancer ni choisir tes mots. Continuer la discussion à ce moment-là, c’est essayer de se faire comprendre en pleine tempête."),
   E("COMMENT FAIRE", "Procède en trois gestes",
     [("Annonce ton départ", "dis par exemple : « Je suis trop en colère pour parler. Je reviens dans vingt minutes. »"),
      ("Pars vraiment", "marche, bouge, respire. L’adrénaline met du temps à redescendre. Ne prépare pas ta réplique."),
      ("Reviens vraiment", "c’est la moitié la plus importante. Revenir prouve que la pause n’était pas une fuite.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Annoncer protège l’autre",
     "Partir sans un mot, c’est comme claquer une porte : l’autre reste seul avec le silence. Annoncer la pause transforme le même geste en promesse. Tu te calmes parce que la suite compte pour toi."),
  ],
  "Envie de voir ce que ta colère raconte de toi ?",
  "Le conseil « respire et compte jusqu’à dix » ne suffit pas toujours. Quand la colère monte vraiment, voici ce qui marche : trois gestes, dont un que presque tout le monde oublie.",
  "#colère #couple", emo="colere"),
],

# ————————————————————— SEMAINE 3 — le regard des autres —————————————————————
[
P("comprendre", 3, "comprendre-honte", "La honte",
  "quand tu voudrais disparaître sous terre",
  [
   T("À QUOI ELLE SERT", "Elle protège ta place dans le groupe",
     "La honte apparaît sous un regard, réel ou imaginé. À l’origine, elle servait à t’éviter l’exclusion, à une époque où être rejeté du groupe pouvait te coûter la vie. Elle te rend attentif aux autres."),
   T("COMMENT ELLE PARLE", "Elle dit « toujours » et « jamais »",
     "La honte ne dit pas « j’ai raté ça ». Elle dit « je suis nul », « c’est toujours pareil ». Elle transforme un moment raté en jugement sur toute ta personne. C’est sa signature, et c’est aussi son mensonge."),
   T("LE PIÈGE", "Elle se nourrit du secret",
     "Plus tu caches ce qui te fait honte, plus cela grossit dans le noir. Le souvenir revient intact des années après, avec la même grimace. Ce qui reste secret garde toute sa force."),
  ],
  "Et toi, quelle place prend la honte chez toi ?",
  "C’est l’émotion qui se voit le plus, et celle qu’on cache le mieux. La honte transforme un moment raté en jugement sur toute la personne. Voici comment elle s’y prend.",
  "#honte #estimedesoi", emo="honte"),

P("distinction", 3, "honte-ou-culpabilite", "Honte ou culpabilité ?",
  "deux mots que l’on confond tous les jours",
  [
   T("LA PREMIÈRE", "La culpabilité",
     "Elle dit : « j’ai mal agi ». Elle porte sur un acte précis, situé dans le temps, et un acte se répare. Tu peux t’excuser, corriger, faire autrement la prochaine fois.", vign="culpabilite"),
   T("LA SECONDE", "La honte",
     "Elle dit : « je suis mauvais ». Elle porte sur toute la personne. Et une personne entière ne se répare pas, alors elle se cache.", vign="honte"),
   D("Ce qui les distingue",
     "La culpabilité te pousse vers l’autre, pour réparer et t’excuser.",
     "La honte t’éloigne de l’autre : tu te caches, tu évites, tu te tais.",
     "La force du ressenti ne mesure pas la faute. On peut avoir honte sans avoir rien fait de mal, et blesser quelqu’un sans ressentir grand-chose."),
  ],
  "Chez toi, laquelle des deux parle le plus fort ?",
  "« Je suis mauvais » et « j’ai mal agi » se ressemblent, mais ce sont deux mondes. C’est la distinction la plus éclairante de toute la vie émotionnelle, et on la confond tous les jours.",
  "#honte #culpabilité", emos=["honte", "culpabilite"]),

P("pratique", 3, "le-secret-desserre", "Le secret desserré",
  "le raconter à une seule personne sûre",
  [
   T("POURQUOI ÇA MARCHE", "La honte vit dans le noir",
     "Elle grossit tant qu’elle reste secrète. Elle perd presque toujours de sa force au moment où tu la racontes à quelqu’un qui écoute sans juger. Non parce que l’autre te pardonne, mais parce que le monstre, sorti de la nuit, retrouve sa vraie taille."),
   E("COMMENT FAIRE", "Vas-y doucement, c’est la règle",
     [("Choisis UNE personne sûre", "quelqu’un qui a déjà su écouter sans juger ni répéter. Pas la plus proche, la plus sûre."),
      ("Raconte le moment précis", "dis les faits et ce que tu as ressenti, sans te défendre et sans t’accuser davantage."),
      ("Observe la suite", "souvent, la scène qui te faisait grimacer depuis des années devient simplement une histoire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Commence petit",
     "Ne commence pas par la plus grande honte de ta vie. Essaie avec une petite. Vérifie que parler te soulage avant d’y amener le reste."),
  ],
  "Envie de savoir quelle place la honte occupe chez toi ?",
  "La honte a une propriété étrange : elle survit des années dans le secret, puis elle fond souvent en quelques minutes de parole. Voici comment t’en servir, avec prudence.",
  "#honte #vulnérabilité", emo="honte"),
],

# ————————————————————— SEMAINE 4 — réparer sans ruminer —————————————————————
[
P("comprendre", 4, "comprendre-culpabilite", "La culpabilité",
  "c’est un signal, pas un verdict",
  [
   T("À QUOI ELLE SERT", "Elle protège tes liens",
     "La culpabilité te pince quand tu penses avoir mal agi envers quelqu’un, ou contre tes propres valeurs. Elle a une fonction précieuse : elle te pousse à réparer. Sans elle, aucune relation ne durerait longtemps."),
   T("SA LIMITE", "Elle se déclenche trop souvent",
     "Elle sonne aussi pour ce qui ne dépendait pas de toi : un choix impossible, la fatigue d’un proche, le hasard. Le pincement n’est pas une preuve de faute. C’est une alarme, et une alarme se vérifie."),
   T("LE PIÈGE", "Souffrir n’est pas payer",
     "Ruminer donne l’impression de payer sa dette : « au moins, je m’en veux ». Mais s’en vouloir ne répare rien et n’a jamais soulagé la personne blessée. C’est un paiement symbolique, versé à personne."),
  ],
  "Et toi, quelle place la culpabilité prend-elle chez toi ?",
  "La culpabilité est là pour protéger tes liens, pas pour te juger. Le problème commence quand s’en vouloir remplace le fait de réparer. Voici comment elle fonctionne, et où elle déraille.",
  "#culpabilité #relations", emo="culpabilite"),

P("distinction", 4, "ruminer-ou-reparer", "Ruminer ou réparer ?",
  "tu peux tourner en rond, ou agir",
  [
   T("LA PREMIÈRE", "Ruminer",
     "Tu repasses la scène en boucle, surtout la nuit. Tu refais le dialogue, tu t’accuses, tu recommences. Cela ressemble à de la conscience morale, mais rien n’en sort et personne n’en profite.", vign="culpabilite"),
   T("LA SECONDE", "Réparer",
     "Tu fais une excuse claire, un geste concret, ou tu changes de comportement. C’est plus inconfortable sur le moment, car il faut se montrer. Mais cela referme vraiment ce qui a été ouvert.", vign="amour"),
   D("Ce qui les distingue",
     "La rumination regarde le passé, en boucle, seule dans ta tête.",
     "La réparation regarde le lien, une fois, dans le monde réel.",
     "Pose-toi une question simple : est-ce que ce que je fais profite à la personne concernée ? Si la réponse est non depuis des semaines, ce n’est plus de la conscience, c’est une boucle."),
  ],
  "Ta culpabilité répare, ou elle tourne ?",
  "S’en vouloir pendant des semaines semble moral. Pourtant, ruminer ne profite à personne, pas même à la personne blessée. Voici la différence entre tourner en rond et réparer.",
  "#culpabilité #rumination", emos=["culpabilite", "tristesse"]),

P("pratique", 4, "la-reparation-en-une-phrase", "La réparation\nen une phrase",
  "s’excuser vraiment, sans « mais »",
  [
   T("POURQUOI ÇA MARCHE", "Une vraie excuse ne se défend pas",
     "La plupart des excuses échouent parce qu’elles cherchent à se justifier : « je suis désolé, mais j’étais fatigué ». Le « mais » annule tout ce qui précède. Une excuse qui répare reconnaît l’acte, nomme son effet et propose une suite."),
   E("COMMENT FAIRE", "La phrase a trois morceaux",
     [("Nomme l’acte", "« J’ai annulé au dernier moment. » Dis les faits, sans chercher d’excuses."),
      ("Nomme l’effet", "« Je pense que ça t’a laissé seul·e face au problème. » Montre que tu as vu l’autre."),
      ("Propose", "« La prochaine fois, je préviens la veille. Est-ce que je peux rattraper ça ? »")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Supprime le « mais »",
     "Relis ton excuse. Si elle contient un « mais », coupe la phrase juste avant. Tes explications pourront venir plus tard, si l’autre les demande. La réparation passe d’abord."),
  ],
  "Envie de voir où ta culpabilité se place, parmi tes 14 émotions ?",
  "« Désolé, mais » n’est pas une excuse, c’est une façon de se défendre. Voici comment construire une excuse qui répare vraiment, en une phrase et trois morceaux.",
  "#excuses #relations", emo="culpabilite"),
],

# ————————————————————— SEMAINE 5 — la perte et la douceur —————————————————————
[
P("comprendre", 5, "comprendre-tristesse", "La tristesse",
  "elle te ralentit pour digérer une perte",
  [
   T("À QUOI ELLE SERT", "Elle digère la perte",
     "La tristesse ralentit tout : ton énergie, tes envies, tes pensées. Ce n’est pas une panne. C’est le programme qui te permet d’intégrer une perte : une personne, mais aussi un projet, une illusion, une image de toi."),
   T("SON LANGAGE", "Les larmes appellent la douceur",
     "Pleurer devant quelqu’un déclenche chez lui un réflexe de soin. Ce réflexe est inscrit en nous. La tristesse est une émotion qui réclame les autres, juste au moment où on a envie de s’isoler."),
   T("SA FORME", "Elle vient par vagues",
     "La tristesse saine monte, te submerge, puis redescend. Entre deux vagues, il y a des éclaircies. Tu peux rire le matin et pleurer le soir. Ce n’est pas de l’instabilité, c’est son mouvement normal."),
  ],
  "Et toi, quelle place la tristesse prend-elle chez toi en ce moment ?",
  "La tristesse n’est ni une faiblesse ni une panne. C’est le programme qui digère les pertes, même les petites qu’on ne s’avoue pas. Voici comment elle travaille.",
  "#tristesse #deuil", emo="tristesse"),

P("distinction", 5, "tristesse-ou-depression", "Tristesse ou dépression ?",
  "une vague, ou un poids qui dure",
  [
   T("LA PREMIÈRE", "La tristesse",
     "Elle est liée à une perte que tu peux nommer. Elle bouge : il y a des vagues, des éclaircies, des moments où le plaisir revient. Elle se partage, et en parler soulage. Elle finit par se déposer.", vign="tristesse"),
   T("LA SECONDE", "La dépression",
     "Ce n’est pas une émotion, c’est un état qui dure des semaines. Tout devient gris, même ce qu’on aimait. Le plaisir s’éteint, le corps pèse, et un « secoue-toi » n’y change rien.", vign="anxiete"),
   D("Ce qui les distingue",
     "La tristesse est une vague. Elle monte, elle passe, elle laisse des éclaircies.",
     "La dépression est un poids continu, sans éclaircie, semaine après semaine.",
     "Si le gris dure depuis plus de deux semaines sans un seul moment de plaisir, ce n’est plus une question de volonté. C’est le moment d’en parler à un médecin ou à un psy."),
  ],
  "Chez toi, est-ce une vague qui passe, ou un fond gris qui s’installe ?",
  "Confondre les deux fait des dégâts dans les deux sens. Soit on dramatise une tristesse normale, soit on banalise un état qui mérite de l’aide. Voici la différence qui compte.",
  "#tristesse #dépression", emos=["tristesse", "serenite"]),

P("pratique", 5, "laisser-passer-la-vague", "Laisser passer\nla vague",
  "tu ressens dix minutes, sans ruminer",
  [
   T("POURQUOI ÇA MARCHE", "Ressentir n’est pas ruminer",
     "Ce qui épuise, ce n’est pas la tristesse. C’est l’histoire qu’on se raconte autour, en boucle. Laisser la vague traverser ton corps sans relancer le film dans ta tête prend dix minutes. La boucle, elle, peut durer des semaines."),
   E("COMMENT FAIRE", "Fais-le pas à pas",
     [("Pose-toi dix minutes", "trouve un endroit calme, sans téléphone. Tu ne vas rien résoudre, juste ressentir."),
      ("Descends dans le corps", "où est la tristesse ? Gorge, poitrine, ventre ? Reste avec la sensation, pas avec l’histoire."),
      ("Laisse monter ce qui monte", "des larmes, un soupir, ou rien du tout : tout est bon. La vague sait quoi faire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Quand le film redémarre",
     "« Pourquoi il a dit ça, j’aurais dû, si seulement » : c’est la rumination qui revient. Chaque fois, ramène doucement ton attention vers la sensation dans ton corps. Dix fois s’il le faut. C’est cela, l’exercice."),
  ],
  "Envie de savoir quelle place ta tristesse occupe vraiment ?",
  "Pleurer dix minutes coûte moins cher que ruminer pendant trois semaines. Voici comment laisser passer une vague de tristesse, sans t’y noyer et sans la fuir.",
  "#tristesse #lâcherprise", emo="tristesse"),
],

# ————————————————————— SEMAINE 6 — l'envie de l'autre —————————————————————
[
P("comprendre", 6, "comprendre-jalousie", "La jalousie",
  "elle montre ce que tu veux vraiment",
  [
   T("À QUOI ELLE SERT", "Elle dit ce que tu désires",
     "Le pincement devant la réussite ou le bonheur d’un autre est un radar. Il pointe exactement ce que tu désires, ou ce que tu crains de perdre. L’information est précieuse. Ce qui empoisonne, c’est la boucle qui suit."),
   T("OÙ ELLE S’EMBALLE", "La comparaison est truquée",
     "Sur les réseaux, tu compares ton intérieur, doutes compris, à la vitrine des autres. C’est un match perdu d’avance, que tu rejoues cent fois par jour. Ton radar s’affole sur de fausses informations."),
   T("LE PIÈGE", "Vérifier soulage une minute",
     "Contrôler, scruter, regarder encore : cela soulage une minute et nourrit l’obsession pendant une heure. Plus tu vérifies, plus le doute grandit. C’est le moteur sans fin de la jalousie."),
  ],
  "Et toi, quelle place prend la jalousie chez toi ?",
  "On en a honte, donc on n’en parle jamais. Pourtant, la jalousie fonctionne comme un radar mal réglé : elle pointe ce que tu désires vraiment. Voici comment la lire.",
  "#jalousie #comparaison", emo="jalousie"),

P("distinction", 6, "jalousie-ou-envie", "Jalousie ou envie ?",
  "l’une se joue à trois, l’autre à deux",
  [
   T("LA PREMIÈRE", "La jalousie",
     "Elle se joue à trois : toi, quelqu’un que tu aimes, et la menace d’une autre personne. C’est la peur de perdre un lien qui compte. Elle se nourrit d’insécurité.", vign="jalousie"),
   T("LA SECONDE", "L’envie",
     "Elle se joue à deux : toi, et quelqu’un qui a ce que tu voudrais avoir. Un poste, un talent, une vie. Ce n’est pas une menace, c’est un désir qui n’a pas encore dit son nom.", vign="fierte"),
   D("Ce qui les distingue",
     "La jalousie a peur de perdre ce qu’elle a : elle protège un lien.",
     "L’envie veut obtenir ce qu’elle n’a pas : elle indique une direction.",
     "Chaque émotion appelle sa réponse. La jalousie se travaille dans la relation, l’envie se transforme en projet. Les confondre, c’est se tromper de chantier."),
  ],
  "Chez toi, cela se joue plutôt à trois, ou à deux ?",
  "On dit « jaloux » pour tout. Pourtant, craindre de perdre son couple et vouloir la carrière d’un autre n’ont rien à voir, et ne se traitent pas de la même façon.",
  "#jalousie #envie", emos=["jalousie", "amour"]),

P("pratique", 6, "traduire-le-pincement", "Traduire\nle pincement",
  "tu transformes l’envie en direction",
  [
   T("POURQUOI ÇA MARCHE", "L’envie est un désir masqué",
     "Le pincement devant la réussite d’un autre contient une information exacte sur ce que tu veux. Tant qu’il reste une gêne, il empoisonne. Une fois traduit en mots, il devient une boussole, la tienne."),
   E("COMMENT FAIRE", "Dès que ça pince",
     [("Attrape-le au vol", "quelqu’un publie, ton ventre se serre. Au lieu de faire défiler plus vite, arrête-toi deux secondes."),
      ("Complète la phrase", "« ce que ça dit de MON désir, c’est… » et finis-la. Parle de ce que tu veux, pas de ce que l’autre a."),
      ("Trouve le premier pas", "prends dix minutes, pas plus : un message, une recherche, une inscription. Le désir devient un chemin.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Allège la source",
     "Repère le compte, l’application ou la conversation qui pique le plus, et coupe-le pendant sept jours. Pas pour fuir, mais pour vérifier à quel point le pincement s’apaise quand tu arrêtes de le nourrir."),
  ],
  "Tu veux voir ce que ton envie essaie de te dire ?",
  "Le pincement que tu sens devant la vie des autres n’est pas un vilain défaut. C’est un désir qui n’a pas encore dit son nom. Voici comment le traduire, en trois gestes.",
  "#envie #objectifs", emo="jalousie"),
],

# ————————————————————— SEMAINE 7 — ce qui fait du bien —————————————————————
[
P("comprendre", 7, "comprendre-joie", "La joie",
  "elle te dit que quelque chose te fait du bien",
  [
   T("À QUOI ELLE SERT", "Elle repère ce qui te fait du bien",
     "La joie dit : « ça, c’est bon, reviens-y ». Elle ouvre le champ : tu as envie de partager, de créer, d’oser. Là où la peur rétrécit ton horizon, la joie l’élargit. C’est une émotion qui construit."),
   T("SA FRAGILITÉ", "Elle ne survit pas à l’inattention",
     "La joie est discrète : elle passe vite, et l’habitude l’use. Ce qui t’émerveillait il y a un an est devenu invisible. Non parce que c’est moins bien, mais parce que tu as cessé de le regarder."),
   T("LE PIÈGE", "Tu la remets à plus tard",
     "« Je profiterai quand j’aurai fini. » Mais la ligne d’arrivée recule à chaque objectif atteint. La joie ne se met pas de côté : elle se prend au passage, ou elle se perd."),
  ],
  "Et toi, quelle place la joie prend-elle chez toi en ce moment ?",
  "La joie n’est pas un luxe réservé au jour où tout ira bien. C’est un signal, et il s’éteint quand on cesse de le regarder. Voici comment elle fonctionne, et pourquoi elle s’use.",
  "#joie #gratitude", emo="joie"),

P("distinction", 7, "joie-ou-bonheur", "Joie ou bonheur ?",
  "l’une passe, l’autre dure",
  [
   T("LA PREMIÈRE", "La joie",
     "C’est un instant : un fou rire, une bonne nouvelle, un rayon de soleil sur la table. Elle a un lieu, une heure, une intensité, puis elle passe. C’est sa nature, pas un défaut.", vign="joie"),
   T("LA SECONDE", "Le bonheur",
     "C’est une moyenne : le sentiment, sur la durée, que ta vie te convient à peu près. Il est fait de mille choses, dont beaucoup de moments parfaitement ordinaires.", vign="serenite"),
   D("Ce qui les distingue",
     "La joie, c’est la météo : elle change dix fois par jour, et c’est normal.",
     "Le bonheur, c’est le climat : il se mesure sur des saisons, pas sur des heures.",
     "Courir après « le bonheur » comme après un état permanent fait rater les vraies joies qui passent. C’est vouloir le climat parfait en refusant la pluie."),
  ],
  "Tu attends le climat parfait, ou tu prends la météo du jour ?",
  "« Être heureux » met une pression étrange : celle d’un état permanent qui n’existe pas. La joie, elle, existe bel et bien, dix fois par jour, à condition de la voir passer.",
  "#joie #bonheur", emos=["joie", "serenite"]),

P("pratique", 7, "la-joie-notee", "La joie notée",
  "vingt secondes pour qu’elle laisse une trace",
  [
   T("POURQUOI ÇA MARCHE", "La mémoire garde ce qu’on repasse",
     "Ton cerveau archive en priorité ce qui est menaçant, c’est son travail. Les joies, elles, s’évaporent en quelques heures si on ne les repasse pas. Vingt secondes à les revivre suffisent pour les faire entrer dans la mémoire longue."),
   E("COMMENT FAIRE", "Fais-le chaque soir",
     [("Retrouve UNE joie du jour", "même minuscule : un échange, une belle lumière, une chose qui a marché. Il y en a toujours une."),
      ("Revis-la vingt secondes", "ferme les yeux : retrouve le lieu, ce que tu voyais, ce que ça faisait dans ton corps."),
      ("Note-la en une ligne", "trois mots suffisent. C’est le geste d’écrire qui grave.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "La précision fait la différence",
     "« Bonne journée » ne grave rien. « Le café en terrasse au soleil, à 8 h, avant que la ville se réveille » : cela, la mémoire le garde. Plus c’est précis, plus ça compte."),
  ],
  "Tu veux voir où ta joie se classe parmi tes 14 émotions ?",
  "Les mauvais moments se gravent tout seuls. Les bons demandent vingt secondes d’aide. Voici le geste du soir qui rééquilibre ta mémoire.",
  "#joie #rituel", emo="joie"),
],

# ————————————————————— SEMAINE 8 — les liens —————————————————————
[
P("comprendre", 8, "comprendre-amour", "L’amour",
  "il pousse à prendre soin",
  [
   T("À QUOI IL SERT", "Il attache, au bon sens du terme",
     "L’amour et la tendresse te poussent vers l’autre : tu cherches sa proximité, tu le protèges, tu en prends soin. C’est le ciment de tout ce qui compte, le couple, la famille, les amitiés. Aimer, c’est faire."),
   T("SES VISAGES", "Il prend trois formes différentes",
     "La passion du début, l’attachement qui rassure, la tendresse du quotidien : ce sont trois formes du même élan. Elles ne se remplacent pas, elles se suivent et se mélangent. Aucune n’est « plus vraie » que les autres."),
   T("LE PIÈGE", "Il s’use en silence",
     "On croit que l’amour « va de soi », et il devient invisible, jamais dit, jamais montré. L’habitude rend l’ordinaire transparent. Ce qu’on ne nourrit plus finit par manquer d’air."),
  ],
  "Quelle place l’amour et la tendresse prennent-ils chez toi ?",
  "L’amour n’est pas seulement un sentiment. C’est un élan vers l’autre, et comme tout élan, il s’entretient. Voici ses trois visages, et la façon dont il s’use sans bruit.",
  "#amour #tendresse", emo="amour"),

P("distinction", 8, "passion-ou-tendresse", "Passion ou tendresse ?",
  "l’une flambe, l’autre dure",
  [
   T("LA PREMIÈRE", "La passion",
     "C’est le feu du début : une obsession douce, le cœur qui s’emballe, l’autre partout dans tes pensées. Dans le corps, cet état ne dure pas, et heureusement. Personne ne tiendrait dix ans ainsi.", vign="amour"),
   T("LA SECONDE", "La tendresse",
     "C’est la braise qui dure : la main sur l’épaule, le café préparé sans qu’on le demande, la présence tranquille. Elle est moins spectaculaire, mais c’est elle qui chauffe la maison.", vign="serenite"),
   D("Ce qui les distingue",
     "La passion est un état d’exception : intense, brûlant et provisoire.",
     "La tendresse est un climat : discret, durable, et entretenu par les gestes.",
     "Passer de l’une à l’autre n’est pas la mort de l’amour, c’est son installation. Beaucoup de couples se quittent en croyant perdre ce qui était simplement en train de changer de forme."),
  ],
  "Tu sais reconnaître l’amour quand il baisse la voix ?",
  "« Ce n’est plus comme avant. » Non, et ce n’est pas censé l’être. La passion et la tendresse sont deux âges du même amour. Les confondre, c’est prendre un changement de forme pour une fin.",
  "#couple #amour", emos=["amour", "serenite"]),

P("pratique", 8, "la-question-qui-rapproche", "La question\nqui rapproche",
  "tu aimes dans la langue de l’autre",
  [
   T("POURQUOI ÇA MARCHE", "On aime dans sa langue à soi",
     "Tu montres ton amour comme on te l’a appris : des services, des mots, des cadeaux, du temps ou des gestes. L’autre fait pareil, mais pas forcément dans la même langue. Deux personnes peuvent s’aimer fort et se rater totalement."),
   E("COMMENT FAIRE", "Prends dix minutes pour en parler",
     [("Pose la question", "« Qu’est-ce qui te fait vraiment te sentir aimé·e ? Un moment précis où tu l’as senti ? »"),
      ("Écoute sans corriger", "la réponse peut te surprendre. C’est le signe qu’elle t’apprend quelque chose."),
      ("Fais ÇA cette semaine", "fais sa version de l’amour, pas la tienne. Même si elle te semble moins parlante.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Réponds aussi",
     "Dis ta propre langue, sinon l’autre continue de te deviner. Commence par « moi, c’est quand tu… » et finis la phrase. C’est la plus utile de la semaine."),
  ],
  "Envie de voir quelle place l’amour occupe chez toi ?",
  "Deux personnes peuvent s’aimer sincèrement et se rater tous les jours, parce qu’elles ne montrent pas leur amour de la même façon. Une question de dix minutes règle beaucoup de malentendus.",
  "#couple #communication", emo="amour"),
],

# ————————————————————— SEMAINE 9 — la reconnaissance —————————————————————
[
P("comprendre", 9, "comprendre-gratitude", "La gratitude",
  "ce merci intérieur te recharge",
  [
   T("À QUOI ELLE SERT", "Elle voit ce qui t’est donné",
     "La gratitude déplace ton attention : du manque vers ce qui est là, de ce qui rate vers ce qui tient. Ce n’est pas de la naïveté. C’est une correction du réflexe qui ne voit que les problèmes."),
   T("SON ENNEMIE", "On s’habitue à tout",
     "Tout ce qui est stable devient invisible : le toit, la santé, la personne fiable à côté de toi. Ton cerveau ne retient que ce qui est nouveau ou menaçant. La gratitude est l’effort de revoir ce qui n’a pas bougé."),
   T("LE PIÈGE", "Quand elle fait taire",
     "« Je n’ai pas le droit de me plaindre, d’autres ont pire. » Cela, ce n’est pas de la gratitude, c’est un bâillon. La vraie gratitude peut vivre à côté de la colère ou de la tristesse. Elle n’efface rien, elle complète."),
  ],
  "Et toi, quelle place la gratitude prend-elle chez toi ?",
  "Ce n’est ni de la politesse ni de la pensée positive. La gratitude corrige un cerveau qui ne voit que ce qui manque. Voici comment elle marche, et la fausse version qu’il vaut mieux éviter.",
  "#gratitude #mindset", emo="gratitude"),

P("distinction", 9, "gratitude-ou-dette", "Gratitude ou dette ?",
  "l’une relie, l’autre pèse",
  [
   T("LA PREMIÈRE", "La gratitude",
     "Elle dit : « ça compte pour moi ». Elle accueille ce qu’elle reçoit, le savoure, et donne envie de rendre, librement, sans obligation. Elle allège celui qui la ressent et touche celui qui la reçoit.", vign="gratitude"),
   T("LA SECONDE", "La dette",
     "Elle dit : « je te dois ». Elle transforme le cadeau en créance : il faudra rembourser, s’acquitter, être quitte. Elle pèse, et parfois elle pousse même à éviter la personne qui a aidé.", vign="culpabilite"),
   D("Ce qui les distingue",
     "La gratitude relie : elle donne envie de rendre, sans compter.",
     "La dette fait les comptes : elle oblige à rembourser, pour être quitte.",
     "Si recevoir t’est difficile, c’est peut-être que tout arrive chez toi étiqueté « dette ». Recevoir sans rembourser tout de suite, c’est laisser à l’autre le plaisir d’avoir donné."),
  ],
  "Tu sais recevoir, ou tu rembourses tout de suite ?",
  "Certaines personnes ne savent pas recevoir un service ou un compliment sans rendre la pareille dans l’heure. Ce n’est pas de la politesse. C’est la dette qui a pris la place de la gratitude.",
  "#gratitude #recevoir", emos=["gratitude", "culpabilite"]),

P("pratique", 9, "les-trois-du-soir", "Les trois du soir",
  "avec le « parce que » qui change tout",
  [
   T("POURQUOI ÇA MARCHE", "Tu revois l’invisible",
     "Noter trois bonnes choses chaque soir réentraîne ton attention à voir ce qui tient, et pas seulement ce qui rate. L’exercice est connu. Ce qui le rend efficace, c’est un détail que presque tout le monde saute."),
   E("COMMENT FAIRE", "Écris trois lignes le soir",
     [("Note trois choses du jour", "petites de préférence, comme le message d’un ami, un repas réussi, dix minutes de calme."),
      ("Ajoute « parce que »", "à chacune. « Parce que je me suis senti·e attendu·e. » C’est le « parce que » qui grave."),
      ("Varie les sources", "des personnes, des moments, des choses de toi, et pas trois fois la même source.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Le « parce que » est l’exercice",
     "Sans lui, la liste devient mécanique en une semaine : « famille, santé, café ». Le « parce que » t’oblige à retrouver l’effet réel sur toi. C’est là que ton attention se rééduque."),
  ],
  "Envie de mesurer ta gratitude, et tes 13 autres émotions ?",
  "L’exercice des « trois bonnes choses » est célèbre, et souvent mal fait. Deux mots le transforment : « parce que ». Voici la version qui fonctionne.",
  "#gratitude #journaling", emo="gratitude"),
],

# ————————————————————— SEMAINE 10 — la valeur de soi —————————————————————
[
P("comprendre", 10, "comprendre-fierte", "La fierté",
  "elle récompense ton effort",
  [
   T("À QUOI ELLE SERT", "Elle change l’effort en confiance",
     "La fierté récompense un effort fidèle à tes valeurs : tes épaules se redressent, tu as envie de raconter. C’est elle qui transforme tes réussites en confiance durable, à condition que tu la ressentes."),
   T("CE QUI LA VOLE", "La barre monte toujours",
     "Tu atteins un objectif, la barre monte, tu te dis « c’était normal », et tu passes au suivant. À force, plus rien n’est jamais une réussite, juste le minimum. On peut accomplir énormément sans rien savourer."),
   T("LE PIÈGE", "Ta valeur dépend de tes résultats",
     "Si ta valeur ne tient qu’à tes résultats, chaque échec devient un jugement sur toi. La fierté saine dit « j’ai bien fait », et non « je vaux quelque chose aujourd’hui, on verra demain »."),
  ],
  "Et toi, t’autorises-tu à ressentir de la fierté, ou presque jamais ?",
  "Il y a des gens qui réussissent tout et ne savourent rien. La fierté est un carburant, mais la course aux objectifs la vole à chaque fois. Voici comment cela se passe.",
  "#fierté #confianceensoi", emo="fierte"),

P("distinction", 10, "fierte-ou-arrogance", "Fierté ou arrogance ?",
  "l’une savoure, l’autre écrase",
  [
   T("LA PREMIÈRE", "La fierté",
     "Elle savoure SA part : « j’ai travaillé, ça a abouti, ça me fait du bien ». Elle n’a besoin d’écraser personne. Elle peut même se réjouir des réussites des autres. Elle se suffit à elle-même.", vign="fierte"),
   T("LA SECONDE", "L’arrogance",
     "Elle se compare : « je suis au-dessus ». Elle a besoin d’un public, d’un classement, de quelqu’un en dessous. Souvent, c’est une insécurité qui a enfilé un costume.", vign="degout"),
   D("Ce qui les distingue",
     "La fierté se nourrit de l’effort accompli : elle regarde son chemin.",
     "L’arrogance se nourrit de la comparaison : elle regarde les autres, de haut.",
     "La peur de l’arrogance empêche beaucoup de gens de savourer leurs réussites. Mais refuser toute fierté ne rend pas humble, cela laisse juste affamé."),
  ],
  "Tu t’autorises à être fier·e, ou tu t’en méfies ?",
  "Beaucoup de gens s’interdisent la fierté de peur de devenir arrogants. Ils se trompent de cible : ce sont deux mécanismes opposés. L’un regarde son chemin, l’autre regarde les autres de haut.",
  "#fierté #humilité", emos=["fierte", "gratitude"]),

P("pratique", 10, "la-minute-de-credit", "La minute\nde crédit",
  "tu reconnais ta part",
  [
   T("POURQUOI ÇA MARCHE", "Elle arrête la course",
     "Ton cerveau classe une réussite comme « normale » à la seconde où elle arrive, puis il file vers l’objectif suivant. La minute de crédit t’oblige à t’arrêter. C’est le péage qui empêche la course de tout emporter."),
   E("COMMENT FAIRE", "Quand tu finis une tâche",
     [("Arrête-toi trente secondes", "avant le dossier suivant. Prends trente vraies secondes."),
      ("Nomme TA part", "dis-toi « c’est moi qui ai préparé, relancé, tenu ». Pas la chance, pas l’équipe seule : ta part exacte."),
      ("Laisse la chaleur venir", "épaules, poitrine : la fierté est physique. Donne-lui le temps d’arriver.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Compte aussi les jours moyens",
     "Traverser une journée difficile, dire non, demander de l’aide : tout cela compte. La fierté réservée aux exploits meurt de faim. Celle qui accueille l’ordinaire te nourrit tous les jours."),
  ],
  "Envie de voir où ta fierté se situe, sur 10 ?",
  "Tu finis une tâche, tu passes à la suivante, et rien n’est jamais assez ? Cette course te vole ta fierté à chaque tour. Voici la pause de trente secondes qui te la rend.",
  "#fierté #accomplissement", emo="fierte"),
],

# ————————————————————— SEMAINE 11 — le calme —————————————————————
[
P("comprendre", 11, "comprendre-serenite", "La sérénité",
  "personne ne la remarque jamais",
  [
   T("À QUOI ELLE SERT", "Elle te permet de récupérer",
     "La sérénité, c’est ton système au repos : le corps répare, l’esprit prend du recul, les décisions se posent. Ce n’est pas « rien ». C’est l’état de fond où tout le reste se recharge."),
   T("POURQUOI ON LA RATE", "Elle n’émet aucun signal",
     "La peur crie, la colère chauffe, la joie pétille. La sérénité, elle, ne fait rien. Sans signal, elle n’attire pas l’attention. Tu peux vivre des heures sereines sans jamais les remarquer, et te croire « vide »."),
   T("LE PIÈGE", "Tu remplis chaque creux",
     "Dans une file d’attente, un trajet, deux minutes de creux, le téléphone sort tout seul. À force de remplir chaque petit vide, le calme n’a plus un seul endroit où exister. Ce n’est pas le stress qui manque de place, c’est lui."),
  ],
  "Et toi, quelle place la sérénité prend-elle chez toi, pour de vrai ?",
  "C’est l’émotion la plus sous-estimée : elle ne crie pas, ne pétille pas, ne prévient pas. On la vit sans la voir, et on la perd sans s’en apercevoir. Voici pourquoi.",
  "#sérénité #calme", emo="serenite"),

P("distinction", 11, "serenite-ou-indifference", "Sérénité ou indifférence ?",
  "l’une ressent, l’autre non",
  [
   T("LA PREMIÈRE", "La sérénité",
     "Elle ressent tout, mais rien ne la renverse. Elle est présente, disponible, touchée par ce qui arrive, sans être emportée. C’est un calme habité, le contraire de l’absence.", vign="serenite"),
   T("LA SECONDE", "L’indifférence",
     "Elle ne ressent plus rien. Elle est coupée, anesthésiée, elle dit « peu importe ». De loin, on dirait du calme. Mais c’est un débranchement, souvent le signe d’une fatigue émotionnelle profonde.", vign="degout"),
   D("Ce qui les distingue",
     "La sérénité reste reliée : elle sent, elle répond, elle reste douce.",
     "L’indifférence est débranchée : elle ne sent plus rien, même le bon.",
     "Sois honnête : les bonnes nouvelles te font-elles encore quelque chose ? La sérénité laisse passer la joie. L’indifférence bloque tout, et c’est un signal à prendre au sérieux."),
  ],
  "Ton calme est-il habité, ou débranché ?",
  "« Je suis calme » peut vouloir dire deux choses opposées : un système apaisé, ou un système débranché. La différence tient en une question. Est-ce que le bon passe encore ?",
  "#calme #burnout", emos=["serenite", "tristesse"]),

P("pratique", 11, "le-sas-de-transition", "Le sas\nde transition",
  "trois respirations entre deux moments",
  [
   T("POURQUOI ÇA MARCHE", "Les tensions s’empilent",
     "Sans transition, tu entres dans ta soirée avec la réunion encore sur les épaules, et dans ta réunion avec le trajet encore dans les nerfs. Chaque activité déborde sur la suivante, et le fond de tension monte toute la journée."),
   E("COMMENT FAIRE", "Quand tu changes d’activité",
     [("Repère tes frontières", "la voiture avant d’entrer, la porte du bureau, la fin d’un appel. Ce sont les sas naturels de ta journée."),
      ("Respire lentement trois fois", "rien de plus. Tu fermes ce qui vient de se passer, tu ouvres ce qui commence."),
      ("Nomme le passage", "dis-toi « fin du travail, début de la maison ». Une phrase intérieure suffit, elle marque la frontière.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Commence par le sas du soir",
     "Si tu n’en installes qu’un, mets-le entre le travail et la maison. C’est celui qui protège les personnes que tu aimes d’une journée qu’elles n’ont pas vécue."),
  ],
  "Envie de mesurer ton niveau de calme réel ?",
  "Ce n’est pas la journée qui épuise, c’est l’empilement : chaque activité déborde sur la suivante. Trois respirations placées aux bons endroits changent le goût d’une journée entière.",
  "#calme #routine", emo="serenite"),
],

# ————————————————————— SEMAINE 12 — l'inattendu —————————————————————
[
P("comprendre", 12, "comprendre-surprise", "La surprise",
  "elle remet ton attention à zéro",
  [
   T("À QUOI ELLE SERT", "Elle met à jour tes prévisions",
     "Ton cerveau prévoit en permanence la seconde qui suit. Quand la réalité contredit sa prévision, tes sourcils se lèvent, ta bouche s’ouvre, tout s’arrête. C’est la surprise : une correction d’urgence de ta carte du monde."),
   T("SA NATURE", "C’est un carrefour",
     "La surprise ne dure qu’un instant, puis elle se transforme en joie, en peur ou en colère, selon ce qui arrive. Elle n’est ni agréable ni désagréable. Elle est le carrefour, pas la destination."),
   T("QUAND ELLE MARQUE", "Une grosse surprise se digère",
     "Une énorme surprise, c’est une certitude centrale qui casse, sur une personne, sur toi, sur la vie. Ce qui suit, le temps de digérer et le besoin d’en reparler sans arrêt, n’est pas de la faiblesse. C’est ta carte du monde qui se reconstruit."),
  ],
  "Et toi, quelle place prend la surprise chez toi ?",
  "C’est l’émotion la plus courte, une seconde à peine, et l’une des plus importantes. Elle te signale que ta carte du monde vient de se tromper. Voici ce qui se joue dans cette seconde.",
  "#surprise #cerveau", emo="surprise"),

P("distinction", 12, "surprise-ou-sursaut", "Surprise ou sursaut ?",
  "l’une pense, l’autre bondit",
  [
   T("LE PREMIER", "Le sursaut",
     "Une porte claque, et ton corps a bondi avant toute pensée. C’est un réflexe de protection, inscrit dans le corps. Il ne dit rien de toi, sinon que ton alarme corporelle fonctionne.", vign="peur"),
   T("LA SECONDE", "La surprise",
     "Elle, c’est l’esprit qui réagit : une information contredit ce que tu croyais. Elle peut arriver sans aucun bruit. Une phrase dans une conversation calme peut être la plus grosse surprise de l’année.", vign="surprise"),
   D("Ce qui les distingue",
     "Le sursaut est un réflexe du corps : une seconde, rien à comprendre.",
     "La surprise est une mise à jour de l’esprit : elle a un sens, et des suites.",
     "Sursauter facilement ne veut pas dire « être peureux ». C’est un seuil d’alarme réglé bas, souvent par la fatigue ou une période de tension. C’est un signal, pas un trait de caractère."),
  ],
  "Comment est réglé ton seuil d’alarme, ces temps-ci ?",
  "Tu sursautes pour un rien en ce moment ? Ce n’est pas de la peur. C’est souvent un signe de fatigue ou de tension accumulée. La différence entre le sursaut et la surprise explique pourquoi.",
  "#surprise #stress", emos=["surprise", "peur"]),

P("pratique", 12, "la-seconde-de-suspension", "La seconde\nde suspension",
  "tu la prends avant de réagir",
  [
   T("POURQUOI ÇA MARCHE", "Tout se décide à cet instant",
     "Après une surprise, la première interprétation prend toute la place : « c’est une catastrophe », « il l’a fait exprès ». Or ce moment est un carrefour. La direction que tu prends dans la première seconde décide de l’heure qui suit."),
   E("COMMENT FAIRE", "Quand l’imprévu tombe",
     [("Prends une seconde, respire", "avant le premier mot. C’est court, et c’est immense."),
      ("Nomme l’imprévu", "« je n’avais pas prévu ça ». Ni bien ni mal pour l’instant, juste inattendu."),
      ("Choisis la question", "« qu’est-ce que ça change, concrètement ? », plutôt que « c’est une catastrophe ».")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Entraîne-toi sur les petits imprévus",
     "Un train annulé, un plan qui tombe à l’eau : ce sont des occasions de t’entraîner sans risque. Le réflexe construit sur les petites surprises sera là pour les grandes."),
  ],
  "Envie de voir comment tu réagis à l’inattendu ?",
  "Entre l’imprévu et ta réaction, il existe une seconde, et tout se joue dedans. Voici comment l’agrandir, en t’entraînant sur les petits imprévus du quotidien.",
  "#imprévu #résilience", emo="surprise"),
],

# ————————————————————— SEMAINE 13 — la boussole entière —————————————————————
[
P("comprendre", 13, "comprendre-degout", "Le dégoût",
  "il écarte ce qui pourrait te nuire",
  [
   T("À QUOI IL SERT", "Il rejette avant d’analyser",
     "Le dégoût est ton système de rejet. Devant une nourriture avariée ou une odeur suspecte, la grimace arrive avant la pensée. À l’échelle de l’espèce, ce réflexe a sauvé des milliers de vies."),
   T("SA VERSION MORALE", "Il s’étend aux actes",
     "Le même circuit s’active pour les comportements : la trahison, la cruauté ou l’injustice nous « écœurent ». Ton dégoût moral dessine tes valeurs en creux. Dis-moi ce qui te dégoûte, et je te dirai ce qui compte pour toi."),
   T("LE PIÈGE", "Il déshumanise plus vite que tout",
     "Dirigé contre des personnes ou des groupes, le dégoût devient l’émotion la plus dangereuse qui soit : il transforme des gens en choses. Quand il vise quelqu’un plutôt qu’un acte, méfie-toi, toujours."),
  ],
  "Et toi, quelle place prend le dégoût chez toi ?",
  "C’est l’émotion dont on ne parle jamais, et l’une des plus puissantes. Elle protège ton corps, elle dessine tes valeurs, et elle peut déshumaniser plus vite que toutes les autres. Voici son portrait.",
  "#dégoût #valeurs", emo="degout"),

P("distinction", 13, "emotion-ou-humeur", "Émotion ou humeur ?",
  "l’une réagit, l’autre colore tout",
  [
   T("LA PREMIÈRE", "L’émotion",
     "Elle a un déclencheur, un début et une fin : cette phrase m’a mis en colère, cette nouvelle m’a réjoui. Elle a une date et elle raconte quelque chose de précis. C’est un message.", vign="colere"),
   T("LA SECONDE", "L’humeur",
     "Elle n’a pas de cause claire. On se lève « gris » ou « léger », et cela colore tout : les mêmes événements paraissent lourds un jour, anodins le lendemain. C’est le fond de l’air intérieur.", vign="tristesse"),
   D("Ce qui les distingue",
     "L’émotion est une réaction : elle répond à quelque chose, puis elle passe.",
     "L’humeur est un climat : sommeil, fatigue, saison, hormones, tout y contribue.",
     "Les distinguer est utile : on ne « résout » pas une humeur en cherchant un coupable. Un jour gris ne signifie pas que ta vie va mal. Parfois, il signifie juste que tu as mal dormi."),
  ],
  "Aujourd’hui, est-ce une émotion qui te parle, ou une humeur qui te colore ?",
  "« Pourquoi je me sens comme ça ? » Parfois, il n’y a pas de pourquoi : c’est une humeur, pas une émotion. Savoir les distinguer évite de chercher des coupables aux jours gris.",
  "#humeur #introspection", emos=["joie", "tristesse"]),

P("pratique", 13, "la-meteo-interieure", "La météo\nintérieure",
  "une minute par jour peut tout changer",
  [
   T("POURQUOI ÇA MARCHE", "Nommer, c’est apaiser",
     "Une émotion que tu as nommée devient une chose que tu peux observer, au lieu d’un brouillard qui déborde. C’est la différence entre « je me sens mal » et « je sens de la honte, parce que je me suis exposé ». La seconde phrase ouvre une porte."),
   E("COMMENT FAIRE", "Cela te prend une minute",
     [("Qu’est-ce qui domine ?", "là, maintenant : plutôt anxiété, joie, colère ou fatigue ? Un mot suffit."),
      ("Où, dans le corps ?", "gorge, poitrine, ventre, mâchoires ? L’émotion a toujours une adresse dans le corps."),
      ("Quel besoin derrière ?", "être rassuré·e, reconnu·e, tranquille, relié·e ? Le besoin te montre quoi faire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Le mot juste compte",
     "« Stressé » est un mot fourre-tout. Anxieux, débordé, vexé, déçu, impatient : plus le mot est juste, plus l’émotion devient facile à manier. Le vocabulaire est un vrai outil pour s’apaiser."),
  ],
  "Et si tu faisais le point sur tes 14 émotions ?",
  "Le geste le plus utile de toute la vie émotionnelle tient en une minute : nommer ce qui se passe en toi. Voici la version en trois questions. C’est la porte d’entrée de tout le reste.",
  "#météointérieure #pleineconscience", emo="joie"),
],
]

# vérification rapide à l'import
assert len(SEMAINES) == 13, f"{len(SEMAINES)} semaines au lieu de 13"
for i, s in enumerate(SEMAINES, 1):
    assert len(s) == 3, f"semaine {i} : {len(s)} posts au lieu de 3"
    series = [p["serie"] for p in s]
    assert series == ["comprendre", "distinction", "pratique"], f"semaine {i} : ordre {series}"
