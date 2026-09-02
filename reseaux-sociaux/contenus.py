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
  "le simulateur d’avenir qui tourne un peu trop bien",
  [
   T("À QUOI ELLE SERT", "Anticiper pour te protéger",
     "Face à l’incertitude, ton cerveau déroule les scénarios possibles : « et si je rate mon train ? », « et si la réunion tourne mal ? ». À dose utile, elle te fait réviser, prévoir, arriver en avance."),
   T("QUAND ELLE COÛTE", "Une décision… ou une boucle",
     "L’anxiété utile débouche sur une action. L’anxiété épuisante tourne sans jamais atterrir — et le corps paie la facture de dangers qui n’arriveront pas : tension, sommeil léger, fatigue de fond."),
   T("LE PIÈGE", "L’évitement renforce l’alarme",
     "Éviter soulage tout de suite. Mais ton cerveau en conclut que le danger était réel — et la prochaine fois, l’alarme sonne plus fort. C’est le mécanisme le plus important à connaître."),
  ],
  "Quelle place l’anxiété occupe-t-elle chez toi, en ce moment ?",
  "L’anxiété n’est pas un défaut de fabrication : c’est un système d’anticipation qui tourne un peu trop bien. Voici comment elle fonctionne — et le piège qui l’entretient.",
  "#anxiété #stress", emo="anxiete"),

P("distinction", 1, "peur-ou-anxiete", "Peur ou anxiété ?",
  "les deux protègent — mais pas du même danger",
  [
   T("LA PREMIÈRE", "La peur",
     "Elle réagit à un danger présent et identifiable : la voiture qui déboule, le bruit dans la nuit. Elle est immédiate, intense, et elle retombe quand le danger passe.", vign="peur"),
   T("LA SECONDE", "L’anxiété",
     "Elle réagit à un danger futur et flou : « et si… ». Rien ne menace ici et maintenant — c’est la simulation qui tourne. Elle peut durer des heures, des jours, sans jamais retomber.", vign="anxiete"),
   D("D’où la différence",
     "La peur répond au présent. Elle se calme quand le danger passe.",
     "L’anxiété répond à un futur imaginé. Elle ne rencontre jamais son danger.",
     "C’est pour ça qu’on ne raisonne pas une anxiété comme on rassure une peur : il n’y a rien à fuir — juste une simulation à ralentir."),
  ],
  "Et chez toi, laquelle des deux parle le plus fort ?",
  "On les confond tout le temps. Pourtant peur et anxiété ne répondent pas au même danger — et ne se traversent pas de la même façon.",
  "#anxiété #peur", emos=["peur", "anxiete"]),

P("pratique", 1, "respiration-expiration-longue", "La respiration\nà expiration longue",
  "trois minutes pour actionner le frein du corps",
  [
   T("POURQUOI ÇA MARCHE", "L’expiration est un frein",
     "Quand tu expires plus longtemps que tu n’inspires, tu actives la branche du système nerveux qui ralentit le cœur. Ce n’est pas une astuce de magazine : c’est l’interrupteur physiologique le plus direct dont tu disposes."),
   E("COMMENT FAIRE", "Le geste, pas à pas",
     [("Inspire sur 4 temps", "par le nez, sans forcer."),
      ("Expire sur 6 temps", "par la bouche, comme si tu soufflais sur une bougie sans l’éteindre."),
      ("Continue 3 minutes", "l’effet arrive vers la deuxième minute — pas avant. Tiens jusque-là.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Entraîne-toi les jours calmes",
     "Un système entraîné redescend beaucoup plus vite les jours difficiles. Trois minutes par jour tranquille valent mieux que dix minutes en pleine tempête."),
  ],
  "Envie de savoir d’où tu pars, avant de commencer ?",
  "Trois minutes, aucun matériel : la respiration à expiration longue est le geste le plus direct pour calmer un corps en alerte. Voici comment la faire — et le détail que presque tout le monde rate.",
  "#respiration #anxiété", emo="serenite"),
],

# ————————————————————— SEMAINE 2 — la force qui défend —————————————————————
[
P("comprendre", 2, "comprendre-colere", "La colère",
  "le gardien de tes frontières",
  [
   T("À QUOI ELLE SERT", "Défendre ce qui compte",
     "La colère se lève quand une limite ou une valeur importante est franchie : une injustice, un manque de respect, une promesse trahie. Elle ne cherche pas le conflit — elle défend un territoire."),
   T("DANS LE CORPS", "Plus rapide que la pensée",
     "Chaleur qui monte, mâchoires serrées, énergie dans les bras : le corps s’alerte avant que la raison n’ait analysé quoi que ce soit. C’est pour ça qu’on dit des choses qu’on regrette — la pensée arrive en retard."),
   T("LE PIÈGE", "La colère enterrée ne meurt pas",
     "Interdite d’expression, elle suinte : rancune, sarcasme, fatigue, tension qui sort ailleurs. Une colère écoutée à temps coûte toujours moins cher qu’une colère enterrée."),
  ],
  "Quelle place la colère occupe-t-elle chez toi — trop, ou pas assez ?",
  "La colère n’est pas le contraire de la gentillesse : c’est un gardien de frontières. Le problème n’est presque jamais de la ressentir — c’est ce qu’on en fait, ou ce qu’on en tait.",
  "#colère #limites", emo="colere"),

P("distinction", 2, "colere-ou-agressivite", "Colère ou agressivité ?",
  "l’une est une émotion, l’autre un comportement",
  [
   T("LA PREMIÈRE", "La colère",
     "C’est un signal intérieur : quelque chose d’important vient d’être franchi. On peut la ressentir intensément… et ne blesser personne. Ressentir n’a jamais fait de mal à quiconque.", vign="colere"),
   T("LA SECONDE", "L’agressivité",
     "C’est un comportement : attaquer, humilier, casser. Elle peut venir de la colère — mais aussi de la peur, de la honte, de l’habitude. Et on peut être agressif sans même être en colère.", vign="colere"),
   D("D’où la différence",
     "La colère se ressent. Elle est toujours légitime comme signal.",
     "L’agressivité se choisit. Elle est toujours discutable comme réponse.",
     "Interdire la colère ne rend pas doux — ça rend muet. Et ce qui est tu finit par déborder ailleurs, souvent sur les mauvaises personnes."),
  ],
  "Et toi, on t’a appris à écouter ta colère — ou à la taire ?",
  "« Calme-toi » confond deux choses : l’émotion et le comportement. On peut être très en colère et parfaitement respectueux. On peut être très calme et profondément blessant.",
  "#colère #communication", emos=["colere", "degout"]),

P("pratique", 2, "la-pause-annoncee", "La pause annoncée",
  "sortir de la pièce sans abîmer le lien",
  [
   T("POURQUOI ÇA MARCHE", "Sous adrénaline, on ne négocie rien",
     "Quand la colère dépasse un certain seuil, le corps est en mode combat : impossible d’écouter, de nuancer, de choisir ses mots. Continuer la discussion à ce moment-là, c’est plaider sa cause en pleine tempête."),
   E("COMMENT FAIRE", "Trois gestes, dans l’ordre",
     [("Annonce, ne claque pas", "« Je suis trop en colère pour parler correctement. Je reviens dans vingt minutes. »"),
      ("Pars vraiment", "marche, bouge, souffle — l’adrénaline met du temps à redescendre. Ne rumine pas ta réplique."),
      ("Reviens vraiment", "c’est la moitié qui compte : revenir prouve que la pause n’était pas une fuite.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "L’annonce protège l’autre",
     "Partir sans un mot, c’est une porte qui claque — l’autre reste seul avec le silence. Annoncer la pause transforme le même geste en promesse : je me calme parce que la suite m’importe."),
  ],
  "Envie de voir ce que ta colère raconte de toi ?",
  "Le conseil « respire et compte jusqu’à dix » ne suffit pas toujours. Quand ça monte vraiment, voici la version qui marche — en trois gestes, dont un que presque tout le monde oublie.",
  "#colère #couple", emo="colere"),
],

# ————————————————————— SEMAINE 3 — le regard des autres —————————————————————
[
P("comprendre", 3, "comprendre-honte", "La honte",
  "l’émotion qui donne envie de disparaître",
  [
   T("À QUOI ELLE SERT", "Rester acceptable aux yeux du groupe",
     "La honte apparaît sous un regard — réel ou imaginé. Sa fonction d’origine : t’éviter l’exclusion, à une époque où être rejeté du groupe était un danger de mort. Elle te rend attentif aux autres."),
   T("COMMENT ELLE PARLE", "En « toujours » et en « jamais »",
     "La honte ne dit pas « j’ai raté ça » mais « je suis nul », « toujours pareil », « pathétique ». Elle transforme un moment en verdict sur la personne entière. C’est sa signature — et son mensonge."),
   T("LE PIÈGE", "Elle se nourrit du secret",
     "Plus on cache ce qui fait honte, plus il grossit dans le noir. Le souvenir revient intact des années après, avec la même grimace. Ce qui reste secret reste puissant."),
  ],
  "Quelle place la honte occupe-t-elle chez toi ?",
  "C’est l’émotion qui se voit le plus — et celle qu’on cache le mieux. La honte transforme un moment raté en verdict sur toute la personne. Voici comment elle s’y prend.",
  "#honte #estimedesoi", emo="honte"),

P("distinction", 3, "honte-ou-culpabilite", "Honte ou culpabilité ?",
  "la distinction la plus utile de toutes",
  [
   T("LA PREMIÈRE", "La culpabilité",
     "Elle dit : « j’ai mal agi ». Elle porte sur un acte, situé dans le temps — donc réparable. On peut s’excuser, corriger, faire autrement la prochaine fois.", vign="culpabilite"),
   T("LA SECONDE", "La honte",
     "Elle dit : « je suis mauvais ». Elle porte sur la personne entière. Et une personne entière, ça ne se répare pas — ça se cache.", vign="honte"),
   D("D’où la différence",
     "La culpabilité pousse vers l’autre : réparer, s’excuser, recoudre.",
     "La honte pousse loin de l’autre : disparaître, éviter, se taire.",
     "L’intensité du ressenti ne mesure pas la faute : on peut avoir honte sans avoir rien fait de mal, et blesser quelqu’un sans ressentir grand-chose."),
  ],
  "Et chez toi, laquelle des deux parle le plus fort ?",
  "« Je suis mauvais » et « j’ai mal agi » : sept mots d’écart, deux mondes. C’est la distinction la plus éclairante de toute la vie émotionnelle — et on la confond tous les jours.",
  "#honte #culpabilité", emos=["honte", "culpabilite"]),

P("pratique", 3, "le-secret-desserre", "Le secret desserré",
  "raconter à une seule personne sûre",
  [
   T("POURQUOI ÇA MARCHE", "La honte vit dans le noir",
     "Elle grossit tant qu’elle reste secrète — et perd presque toujours de sa force au moment précis où elle est dite à quelqu’un qui écoute sans juger. Pas parce que l’autre absout : parce que le monstre, sorti de la nuit, retrouve sa taille réelle."),
   E("COMMENT FAIRE", "Avec précaution — c’est le principe",
     [("Choisis UNE personne sûre", "quelqu’un qui a déjà su écouter sans juger ni répéter. Pas la plus proche : la plus sûre."),
      ("Raconte le moment précis", "les faits, ce que tu as ressenti — sans plaidoirie, sans te charger davantage."),
      ("Observe l’après", "souvent, la scène qui te faisait grimacer depuis des années devient simplement… une histoire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Commence petit",
     "N’ouvre pas par la plus grande honte de ta vie. Essaie avec une petite — vérifie que la lumière fonctionne avant d’y amener le reste."),
  ],
  "Envie de savoir quelle place la honte occupe chez toi ?",
  "La honte a une propriété étrange : elle survit des années dans le secret, et fond souvent en quelques minutes de parole. Voici comment t’en servir — prudemment.",
  "#honte #vulnérabilité", emo="honte"),
],

# ————————————————————— SEMAINE 4 — réparer sans ruminer —————————————————————
[
P("comprendre", 4, "comprendre-culpabilite", "La culpabilité",
  "un signal — jamais un verdict",
  [
   T("À QUOI ELLE SERT", "Protéger tes liens",
     "La culpabilité pince quand tu penses avoir mal agi envers quelqu’un ou envers tes propres valeurs. Sa fonction est précieuse : elle pousse à réparer. Sans elle, aucune relation ne survivrait longtemps."),
   T("SA LIMITE", "Elle se déclenche trop large",
     "Elle sonne aussi pour ce qui ne dépendait pas de toi : le choix impossible, la fatigue d’un proche, le hasard. Le pincement n’est pas une preuve. C’est une alarme — et les alarmes se vérifient."),
   T("LE PIÈGE", "Souffrir n’est pas payer",
     "La rumination donne l’impression de rembourser : « au moins, je m’en veux ». Mais s’en vouloir ne répare rien et n’a jamais soulagé personne — c’est un paiement symbolique, versé à personne."),
  ],
  "Quelle place la culpabilité occupe-t-elle chez toi ?",
  "Elle est là pour protéger tes liens — pas pour te juger. Le problème commence quand s’en vouloir remplace réparer. Voici comment la culpabilité fonctionne, et où elle déraille.",
  "#culpabilité #relations", emo="culpabilite"),

P("distinction", 4, "ruminer-ou-reparer", "Ruminer ou réparer ?",
  "deux réponses au même pincement",
  [
   T("LA PREMIÈRE", "Ruminer",
     "Repasser la scène en boucle, la nuit surtout. Se refaire le dialogue, s’accuser, recommencer. Ça ressemble à de la conscience morale — mais rien n’en sort, et personne n’en bénéficie.", vign="culpabilite"),
   T("LA SECONDE", "Réparer",
     "Une excuse claire, un geste concret, un comportement qui change. C’est plus inconfortable sur le moment — il faut se montrer — mais ça referme réellement ce qui a été ouvert.", vign="amour"),
   D("D’où la différence",
     "La rumination regarde le passé, en boucle, seule dans ta tête.",
     "La réparation regarde le lien, une fois, dans le monde réel.",
     "Test simple : est-ce que ce que je fais là profite à la personne concernée ? Si la réponse est non depuis des semaines, ce n’est plus de la conscience — c’est une boucle."),
  ],
  "Et toi, ta culpabilité répare — ou elle tourne ?",
  "S’en vouloir pendant des semaines semble moral. Pourtant la rumination ne bénéficie à personne — pas même à la personne blessée. Voici la différence entre tourner et réparer.",
  "#culpabilité #rumination", emos=["culpabilite", "tristesse"]),

P("pratique", 4, "la-reparation-en-une-phrase", "La réparation\nen une phrase",
  "s’excuser vraiment — sans « mais »",
  [
   T("POURQUOI ÇA MARCHE", "Une vraie excuse referme",
     "La plupart des excuses échouent parce qu’elles plaident : « je suis désolé, mais j’étais fatigué ». Le « mais » annule tout ce qui précède. Une excuse qui répare reconnaît, nomme l’effet, et propose — c’est tout."),
   E("COMMENT FAIRE", "La phrase en trois morceaux",
     [("Nomme l’acte", "« J’ai annulé au dernier moment. » Les faits, sans les circonstances atténuantes."),
      ("Nomme l’effet", "« Je pense que ça t’a laissé seul·e face au problème. » Montre que tu as vu l’autre."),
      ("Propose", "« La prochaine fois je préviens la veille. Est-ce que je peux rattraper ça ? »")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Supprime le « mais »",
     "Relis ton excuse : si elle contient « mais », coupe la phrase juste avant. Les explications pourront venir plus tard, si l’autre les demande. D’abord, la réparation."),
  ],
  "Envie de voir où ta culpabilité se place, parmi tes 14 émotions ?",
  "« Désolé, mais… » n’est pas une excuse — c’est une plaidoirie. Voici la structure d’une excuse qui répare vraiment, en une phrase et trois morceaux.",
  "#excuses #relations", emo="culpabilite"),
],

# ————————————————————— SEMAINE 5 — la perte et la douceur —————————————————————
[
P("comprendre", 5, "comprendre-tristesse", "La tristesse",
  "le ralentisseur qui digère les pertes",
  [
   T("À QUOI ELLE SERT", "Digérer ce qui est perdu",
     "La tristesse ralentit tout — énergie, envies, pensées. Ce n’est pas une panne : c’est le programme qui permet d’intégrer une perte. Une personne, mais aussi un projet, une illusion, une image de soi."),
   T("SON LANGAGE", "Les larmes appellent la douceur",
     "Pleurer devant quelqu’un déclenche chez lui un réflexe de soin — c’est câblé. La tristesse est une émotion qui demande les autres, précisément au moment où on a envie de s’isoler."),
   T("SA FORME", "Des vagues, pas une pente",
     "La tristesse saine monte, submerge, puis redescend — et entre deux vagues, il y a des éclaircies. On peut rire le matin et pleurer le soir : ce n’est pas de l’instabilité, c’est le mouvement normal."),
  ],
  "Quelle place la tristesse occupe-t-elle chez toi, en ce moment ?",
  "La tristesse n’est pas une faiblesse ni une panne : c’est le programme qui digère les pertes — même les petites qu’on ne s’avoue pas. Voici comment elle travaille.",
  "#tristesse #deuil", emo="tristesse"),

P("distinction", 5, "tristesse-ou-depression", "Tristesse ou dépression ?",
  "une vague — ou une chape qui dure",
  [
   T("LA PREMIÈRE", "La tristesse",
     "Elle est liée à une perte identifiable. Elle bouge : des vagues, des éclaircies, des moments où le plaisir revient. Elle se partage — en parler soulage. Et elle finit par se déposer.", vign="tristesse"),
   T("LA SECONDE", "La dépression",
     "Ce n’est pas une émotion — c’est un état qui dure des semaines. Tout devient gris, même ce qu’on aimait. Le plaisir s’éteint, le corps pèse, et « secoue-toi » n’a aucune prise dessus.", vign="anxiete"),
   D("D’où la différence",
     "La tristesse est une vague : elle monte, elle passe, elle laisse des éclaircies.",
     "La dépression est une chape : continue, sans éclaircie, semaine après semaine.",
     "Si le gris dure depuis plus de deux semaines sans un seul moment de plaisir, ce n’est plus une histoire de volonté : c’est le moment d’en parler à un médecin ou un psy. Le 3114 écoute gratuitement, 24 h/24."),
  ],
  "Et chez toi, c’est une vague qui passe — ou un fond qui s’installe ?",
  "Confondre les deux fait des dégâts dans les deux sens : on dramatise une tristesse normale, ou on banalise une vraie dépression. Voici les trois différences qui comptent.",
  "#tristesse #dépression", emos=["tristesse", "serenite"]),

P("pratique", 5, "laisser-passer-la-vague", "Laisser passer\nla vague",
  "dix minutes pour ressentir sans ruminer",
  [
   T("POURQUOI ÇA MARCHE", "Ressentir n’est pas ruminer",
     "Ce qui épuise n’est pas la tristesse — c’est l’histoire qu’on se raconte autour, en boucle. Laisser la vague traverser le corps sans relancer le film mental prend dix minutes. La boucle, elle, peut durer des semaines."),
   E("COMMENT FAIRE", "Le geste, pas à pas",
     [("Pose-toi dix minutes", "un endroit calme, sans téléphone. Tu ne vas rien résoudre — juste ressentir."),
      ("Descends dans le corps", "où est la tristesse ? Gorge, poitrine, ventre ? Reste avec la sensation, pas avec l’histoire."),
      ("Laisse monter ce qui monte", "des larmes, un soupir, rien du tout — tout est bon. La vague sait quoi faire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Quand le film redémarre",
     "« Pourquoi il a dit ça, j’aurais dû, si seulement » — c’est la rumination qui revient. Chaque fois, ramène doucement l’attention à la sensation physique. Dix fois s’il faut. C’est ça, l’exercice."),
  ],
  "Envie de savoir quelle place ta tristesse occupe vraiment ?",
  "Pleurer dix minutes coûte moins cher que ruminer trois semaines. Voici comment laisser passer une vague de tristesse — sans t’y noyer et sans la fuir.",
  "#tristesse #lâcherprise", emo="tristesse"),
],

# ————————————————————— SEMAINE 6 — l'envie de l'autre —————————————————————
[
P("comprendre", 6, "comprendre-jalousie", "La jalousie",
  "le radar qui montre ce que tu veux",
  [
   T("À QUOI ELLE SERT", "Pointer tes désirs et tes peurs",
     "Le pincement devant la réussite ou le bonheur d’un autre est un radar : il pointe exactement ce que tu désires — ou ce que tu crains de perdre. L’information est précieuse. C’est la boucle qui empoisonne."),
   T("SON TERRAIN DE JEU", "La comparaison truquée",
     "Sur les réseaux, tu compares ton intérieur — doutes compris — à la vitrine des autres. Un match perdu d’avance, rejoué cent fois par jour. Le radar s’affole sur des données fausses."),
   T("LE PIÈGE", "Vérifier calme une minute",
     "Contrôler, scruter, re-regarder : ça soulage une minute et ça nourrit l’obsession une heure. Plus on vérifie, plus le doute grandit — c’est le mouvement perpétuel de la jalousie."),
  ],
  "Quelle place la jalousie occupe-t-elle chez toi ?",
  "On en a honte, donc on n’en parle jamais. Pourtant la jalousie est un radar — mal réglé, mais un radar : elle pointe ce que tu désires vraiment. Voici comment la lire.",
  "#jalousie #comparaison", emo="jalousie"),

P("distinction", 6, "jalousie-ou-envie", "Jalousie ou envie ?",
  "un triangle — ou un duo",
  [
   T("LA PREMIÈRE", "La jalousie",
     "Elle se joue à trois : toi, quelqu’un que tu aimes, et la menace d’un tiers. C’est la peur de perdre un lien qui compte. Son carburant : l’insécurité.", vign="jalousie"),
   T("LA SECONDE", "L’envie",
     "Elle se joue à deux : toi, et quelqu’un qui a ce que tu voudrais. Un poste, un talent, une vie. Ce n’est pas une menace — c’est un désir qui n’a pas encore dit son nom.", vign="fierte"),
   D("D’où la différence",
     "La jalousie a peur de perdre ce qu’elle a : elle protège un lien.",
     "L’envie veut obtenir ce qu’elle n’a pas : elle révèle une direction.",
     "Deux émotions, deux réponses : la jalousie se travaille dans la relation — l’envie se traduit en projet. Les confondre, c’est se tromper de chantier."),
  ],
  "Et chez toi, c’est plutôt le triangle — ou le duo ?",
  "On dit « jaloux » pour tout. Pourtant craindre de perdre son couple et vouloir la carrière d’un autre n’ont rien à voir — et ne se traitent pas pareil.",
  "#jalousie #envie", emos=["jalousie", "amour"]),

P("pratique", 6, "traduire-le-pincement", "Traduire\nle pincement",
  "transformer l’envie en direction",
  [
   T("POURQUOI ÇA MARCHE", "L’envie est un désir masqué",
     "Le pincement devant la réussite d’un autre contient une information exacte sur ce que tu veux. Tant qu’il reste une gêne, il empoisonne. Traduit en mots, il devient une boussole — la tienne."),
   E("COMMENT FAIRE", "À chaque pincement",
     [("Attrape-le au vol", "quelqu’un poste, ton ventre se serre. Au lieu de scroller plus vite : arrête-toi deux secondes."),
      ("Complète la phrase", "« Ce que ça dit de MON désir : … ». Pas de ce que l’autre a — de ce que toi tu veux."),
      ("Trouve le premier pas", "dix minutes, pas plus : un message, une recherche, une inscription. Le désir devient trajectoire.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Allège la source",
     "Repère le compte, l’appli ou la conversation qui pique le plus — et coupe-le sept jours. Pas pour fuir : pour vérifier à quel point le radar s’apaise quand on cesse de le suralimenter."),
  ],
  "Envie de voir ce que ton envie essaie de te dire ?",
  "Le pincement devant la vie des autres n’est pas un vilain défaut : c’est un désir qui n’a pas encore dit son nom. Voici comment le traduire — en trois gestes.",
  "#envie #objectifs", emo="jalousie"),
],

# ————————————————————— SEMAINE 7 — ce qui fait du bien —————————————————————
[
P("comprendre", 7, "comprendre-joie", "La joie",
  "le signal que quelque chose te fait du bien",
  [
   T("À QUOI ELLE SERT", "Marquer ce qui est bon pour toi",
     "La joie dit « ça, c’est bon — reviens-y ». Et elle élargit : envie de partager, de créer, d’oser. Là où la peur rétrécit le champ, la joie l’ouvre. C’est une émotion qui construit."),
   T("SA FRAGILITÉ", "Elle ne survit pas à l’inattention",
     "La joie est discrète : elle passe vite, et l’habitude l’érode. Ce qui t’émerveillait il y a un an est devenu invisible — non parce que c’est moins bien, mais parce que tu as cessé de le regarder."),
   T("LE PIÈGE", "La reporter à plus tard",
     "« Je profiterai quand j’aurai fini » — et la ligne d’arrivée recule à chaque objectif atteint. La joie ne se stocke pas : elle se prend au passage, ou elle se perd."),
  ],
  "Quelle place la joie occupe-t-elle chez toi, en ce moment ?",
  "La joie n’est pas un luxe pour quand tout ira bien : c’est un signal — et il s’éteint quand on cesse de le regarder. Voici comment elle fonctionne, et pourquoi elle s’use.",
  "#joie #gratitude", emo="joie"),

P("distinction", 7, "joie-ou-bonheur", "Joie ou bonheur ?",
  "la météo — ou le climat",
  [
   T("LA PREMIÈRE", "La joie",
     "C’est un instant : un fou rire, une bonne nouvelle, un rayon de soleil sur la table. Elle est datée, localisée, intense — et elle passe. C’est sa nature, pas un défaut.", vign="joie"),
   T("LA SECONDE", "Le bonheur",
     "C’est une moyenne : le sentiment, sur la durée, que ta vie te convient à peu près. Il est fait de mille choses — dont beaucoup de moments parfaitement ordinaires.", vign="serenite"),
   D("D’où la différence",
     "La joie est la météo : elle change dix fois par jour, et c’est normal.",
     "Le bonheur est le climat : il se mesure sur des saisons, pas sur des heures.",
     "Chasser « le bonheur » comme un état permanent fait rater les joies réelles qui passent — c’est chercher le climat parfait en refusant la pluie."),
  ],
  "Et toi, tu attends le climat parfait — ou tu prends la météo du jour ?",
  "« Être heureux » met une pression étrange : celle d’un état permanent qui n’existe pas. La joie, elle, existe — dix fois par jour, à condition de la voir passer.",
  "#joie #bonheur", emos=["joie", "serenite"]),

P("pratique", 7, "la-joie-notee", "La joie notée",
  "vingt secondes pour qu’elle laisse une trace",
  [
   T("POURQUOI ÇA MARCHE", "La mémoire garde ce qu’on repasse",
     "Ton cerveau archive en priorité ce qui est menaçant — c’est son travail. Les joies, elles, s’évaporent en quelques heures si on ne les repasse pas. Vingt secondes de relecture suffisent à les faire entrer en mémoire longue."),
   E("COMMENT FAIRE", "Chaque soir",
     [("Retrouve UNE joie du jour", "même minuscule : un échange, une lumière, un truc qui a marché. Il y en a toujours une."),
      ("Revis-la vingt secondes", "ferme les yeux : où c’était, ce que tu voyais, ce que ça faisait dans le corps."),
      ("Note-la en une ligne", "trois mots suffisent. C’est l’acte d’écrire qui grave.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "La précision fait tout",
     "« Bonne journée » ne grave rien. « Le café en terrasse au soleil, à 8 h, avant que la ville se réveille » — ça, la mémoire le garde. Plus c’est précis, plus ça compte."),
  ],
  "Curieux·se de voir où ta joie se classe, sur tes 14 émotions ?",
  "Les mauvais moments se gravent tout seuls — les bons demandent vingt secondes d’aide. Voici le geste du soir qui rééquilibre la mémoire.",
  "#joie #rituel", emo="joie"),
],

# ————————————————————— SEMAINE 8 — les liens —————————————————————
[
P("comprendre", 8, "comprendre-amour", "L’amour",
  "l’élan de prendre soin",
  [
   T("À QUOI IL SERT", "Attacher — au bon sens du terme",
     "L’amour et la tendresse poussent vers l’autre : proximité, protection, soin. C’est le ciment de tout ce qui compte — couple, famille, amitiés. Une émotion tournée vers le geste : aimer, c’est faire."),
   T("SES VISAGES", "Passion, attachement, tendresse",
     "Le feu du début, la sécurité de la durée, la douceur du quotidien : trois formes du même élan. Elles ne se remplacent pas — elles se succèdent et se mélangent. Aucune n’est « plus vraie » que les autres."),
   T("LE PIÈGE", "Il s’use en silence",
     "On croit que l’amour « va de soi » — et il devient invisible, jamais dit, jamais montré. L’habitude rend l’ordinaire transparent : ce qu’on ne nourrit plus finit par manquer d’air."),
  ],
  "Quelle place l’amour et la tendresse occupent-ils chez toi ?",
  "L’amour n’est pas qu’un sentiment : c’est un élan vers l’autre — et comme tout élan, il s’entretient. Voici ses trois visages, et la façon dont il s’use sans bruit.",
  "#amour #tendresse", emo="amour"),

P("distinction", 8, "passion-ou-tendresse", "Passion ou tendresse ?",
  "le feu — ou la braise",
  [
   T("LA PREMIÈRE", "La passion",
     "Le feu du début : obsession douce, cœur qui s’emballe, l’autre partout dans les pensées. Chimiquement, ça ne dure pas — et heureusement : personne ne survivrait à dix ans de ça.", vign="amour"),
   T("LA SECONDE", "La tendresse",
     "La braise de la durée : la main sur l’épaule, le café préparé sans qu’on demande, la présence tranquille. Moins spectaculaire — mais c’est elle qui chauffe la maison.", vign="serenite"),
   D("D’où la différence",
     "La passion est un état d’exception : intense, brûlant, provisoire.",
     "La tendresse est un climat : discret, durable, entretenu par les gestes.",
     "Le passage de l’une à l’autre n’est pas la mort de l’amour — c’est son installation. Beaucoup de couples se quittent en croyant perdre ce qui était juste en train de changer de forme."),
  ],
  "Et toi, tu sais reconnaître l’amour quand il baisse la voix ?",
  "« Ce n’est plus comme avant » — non, et ce n’est pas censé l’être. La passion et la tendresse sont deux âges du même amour. Les confondre fait prendre une mutation pour une fin.",
  "#couple #amour", emos=["amour", "serenite"]),

P("pratique", 8, "la-question-qui-rapproche", "La question\nqui rapproche",
  "aimer dans la langue de l’autre",
  [
   T("POURQUOI ÇA MARCHE", "On aime dans sa langue à soi",
     "Tu montres ton amour comme on te l’a appris : des services, des mots, des cadeaux, du temps, des gestes. L’autre aussi — mais pas forcément la même. Deux personnes peuvent s’aimer fort et se rater complètement."),
   E("COMMENT FAIRE", "Une conversation de dix minutes",
     [("Pose la question", "« Qu’est-ce qui te fait vraiment te sentir aimé·e ? Un moment précis où tu l’as senti ? »"),
      ("Écoute sans corriger", "la réponse peut te surprendre — c’est le signe qu’elle t’apprend quelque chose."),
      ("Fais ÇA cette semaine", "pas ta version à toi de l’amour : la sienne. Même si ça te semble moins « parlant ».")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Réponds aussi",
     "Dis ta propre langue — sinon l’autre continue de te deviner. « Moi, c’est quand tu… » : la phrase la plus rentable de la semaine."),
  ],
  "Envie de voir la place que l’amour occupe dans ton paysage ?",
  "Deux personnes peuvent s’aimer sincèrement et se rater tous les jours — parce qu’elles ne parlent pas la même langue d’amour. Une question de dix minutes règle beaucoup de malentendus.",
  "#couple #communication", emo="amour"),
],

# ————————————————————— SEMAINE 9 — la reconnaissance —————————————————————
[
P("comprendre", 9, "comprendre-gratitude", "La gratitude",
  "le merci intérieur qui recharge",
  [
   T("À QUOI ELLE SERT", "Mesurer ce qui t’est donné",
     "La gratitude est un déplacement d’attention : du manquant vers le présent, de ce qui rate vers ce qui tient. Ce n’est pas de la naïveté — c’est un correctif au biais qui ne voit que les problèmes."),
   T("SON ENNEMIE", "L’habituation",
     "Tout ce qui est stable devient invisible : le toit, la santé, la personne fiable à côté de toi. Le cerveau n’archive que le nouveau et le menaçant. La gratitude est l’effort de re-voir ce qui n’a pas bougé."),
   T("LE PIÈGE", "La gratitude-écran",
     "« Je n’ai pas le droit de me plaindre, d’autres ont pire » — ça, ce n’est pas de la gratitude : c’est un bâillon. La vraie gratitude coexiste avec la colère ou la tristesse. Elle n’efface rien : elle complète."),
  ],
  "Quelle place la gratitude occupe-t-elle chez toi ?",
  "Ce n’est ni de la politesse ni de la pensée positive : la gratitude est un correctif au cerveau qui ne voit que ce qui manque. Voici comment elle marche — et sa contrefaçon à éviter.",
  "#gratitude #mindset", emo="gratitude"),

P("distinction", 9, "gratitude-ou-dette", "Gratitude ou dette ?",
  "un cadeau — ou une facture",
  [
   T("LA PREMIÈRE", "La gratitude",
     "« Ça compte pour moi. » Elle reçoit ce qui est donné, le savoure, et donne envie de rendre — librement, sans obligation. Elle allège celui qui la ressent et touche celui qui la reçoit.", vign="gratitude"),
   T("LA SECONDE", "La dette",
     "« Je te dois. » Elle transforme le cadeau en créance : il faudra rembourser, s’acquitter, être quitte. Elle pèse — et parfois elle fait même éviter la personne qui a aidé.", vign="culpabilite"),
   D("D’où la différence",
     "La gratitude relie : elle donne envie de rendre, sans compter.",
     "La dette comptabilise : elle oblige à rembourser, pour être quitte.",
     "Si recevoir t’est difficile, c’est peut-être que tout arrive chez toi étiqueté « dette ». Recevoir sans rembourser tout de suite, c’est laisser l’autre avoir le plaisir d’avoir donné."),
  ],
  "Et toi, tu sais recevoir — ou tu rembourses tout de suite ?",
  "Certaines personnes ne savent pas recevoir un service ou un compliment sans rendre la pareille dans l’heure. Ce n’est pas de la politesse — c’est la dette qui a pris la place de la gratitude.",
  "#gratitude #recevoir", emos=["gratitude", "culpabilite"]),

P("pratique", 9, "les-trois-du-soir", "Les trois du soir",
  "avec le « parce que » qui fait tout",
  [
   T("POURQUOI ÇA MARCHE", "Re-voir l’invisible",
     "Noter trois bonnes choses chaque soir réentraîne l’attention à voir ce qui tient — pas seulement ce qui rate. L’exercice est connu ; ce qui le rend efficace, c’est un détail que presque tout le monde saute."),
   E("COMMENT FAIRE", "Trois lignes avant de dormir",
     [("Note trois choses du jour", "petites de préférence : le message d’un ami, un repas réussi, dix minutes de calme."),
      ("Ajoute « parce que… »", "à chacune. « … parce que je me suis senti·e attendu·e. » C’est le parce que qui grave."),
      ("Varie les registres", "des personnes, des moments, des choses de toi — pas trois fois la même source.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Le « parce que » est l’exercice",
     "Sans lui, la liste devient mécanique en une semaine : « famille, santé, café ». Le « parce que » force à retrouver l’effet réel sur toi — c’est là que l’attention se rééduque."),
  ],
  "Envie de mesurer ta gratitude — et les 13 autres ?",
  "L’exercice des « trois bonnes choses » est célèbre — et souvent mal fait. Un seul mot le transforme : « parce que ». Voici la version qui fonctionne.",
  "#gratitude #journaling", emo="gratitude"),
],

# ————————————————————— SEMAINE 10 — la valeur de soi —————————————————————
[
P("comprendre", 10, "comprendre-fierte", "La fierté",
  "la chaleur qui suit l’effort",
  [
   T("À QUOI ELLE SERT", "Transformer l’effort en confiance",
     "La fierté récompense un effort aligné avec tes valeurs : épaules qui se redressent, envie de raconter. C’est elle qui convertit les réussites en confiance durable — à condition d’être ressentie."),
   T("LE MÉCANISME QUI LA VOLE", "Le tapis roulant",
     "Objectif atteint → la barre monte → « c’était normal » → objectif suivant. À force, plus rien n’est jamais une réussite : juste le minimum. On peut accomplir énormément sans avoir rien savouré."),
   T("LE PIÈGE", "La valeur suspendue à la performance",
     "Si ta valeur ne tient que par les résultats, chaque échec devient un verdict sur toi. La fierté saine dit « j’ai bien fait » — pas « je vaux quelque chose aujourd’hui, on verra demain »."),
  ],
  "Quelle place la fierté occupe-t-elle chez toi — assez, ou jamais ?",
  "Il y a des gens qui réussissent tout et ne savourent rien. La fierté est un carburant — mais le tapis roulant des objectifs la vole systématiquement. Voici comment.",
  "#fierté #confianceensoi", emo="fierte"),

P("distinction", 10, "fierte-ou-arrogance", "Fierté ou arrogance ?",
  "se hausser — ou rabaisser",
  [
   T("LA PREMIÈRE", "La fierté",
     "Elle savoure SA part : « j’ai travaillé, ça a abouti, ça me fait du bien ». Elle n’a besoin d’écraser personne — elle peut même célébrer les réussites des autres. Elle se suffit.", vign="fierte"),
   T("LA SECONDE", "L’arrogance",
     "Elle se mesure : « je suis au-dessus ». Elle a besoin d’un public, d’un classement, de quelqu’un en dessous. Souvent, c’est une insécurité qui a mis un costume.", vign="degout"),
   D("D’où la différence",
     "La fierté se nourrit de l’effort accompli : elle regarde son chemin.",
     "L’arrogance se nourrit de la comparaison : elle regarde les autres, de haut.",
     "C’est la peur de l’arrogance qui empêche tant de gens de savourer leurs réussites. Mais refuser toute fierté ne rend pas humble — ça rend juste affamé."),
  ],
  "Et toi, tu t’autorises à être fier·e — ou tu t’en méfies ?",
  "Beaucoup de gens s’interdisent la fierté de peur de devenir arrogants. Erreur de cible : ce sont deux mécanismes opposés. L’un regarde son chemin, l’autre regarde les autres de haut.",
  "#fierté #humilité", emos=["fierte", "gratitude"]),

P("pratique", 10, "la-minute-de-credit", "La minute\nde crédit",
  "reconnaître ta part — trente secondes",
  [
   T("POURQUOI ÇA MARCHE", "Contre le tapis roulant",
     "Le cerveau classe les réussites en « normal » à la seconde où elles arrivent — et file à l’objectif suivant. La minute de crédit force l’arrêt : c’est le péage qui empêche le tapis roulant de tout emporter."),
   E("COMMENT FAIRE", "Après chaque tâche finie",
     [("Arrête-toi trente secondes", "avant d’ouvrir le dossier suivant. Trente vraies secondes."),
      ("Nomme TA part", "« c’est moi qui ai préparé, relancé, tenu ». Pas la chance, pas l’équipe seule : ta part exacte."),
      ("Laisse la chaleur venir", "épaules, poitrine — la fierté est physique. Donne-lui le temps d’arriver.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Compte aussi les jours moyens",
     "Tenu une journée difficile, dit non, demandé de l’aide : ça compte. La fierté réservée aux exploits meurt de faim — celle qui compte l’ordinaire nourrit tous les jours."),
  ],
  "Envie de voir où ta fierté se situe, sur 10 ?",
  "Tu finis un truc, tu passes au suivant, et rien n’est jamais assez ? Le tapis roulant vole ta fierté à chaque tour. Voici le péage de trente secondes qui la récupère.",
  "#fierté #accomplissement", emo="fierte"),
],

# ————————————————————— SEMAINE 11 — le calme —————————————————————
[
P("comprendre", 11, "comprendre-serenite", "La sérénité",
  "l’état que personne ne remarque",
  [
   T("À QUOI ELLE SERT", "Récupérer, digérer, choisir",
     "La sérénité, c’est le système apaisé : le corps répare, l’esprit prend du recul, les décisions se posent. Ce n’est pas « rien » — c’est l’état de fond où tout le reste se recharge."),
   T("POURQUOI ON LA RATE", "Elle n’émet aucun signal",
     "La peur crie, la colère chauffe, la joie pétille — la sérénité, elle, ne fait rien. Aucun signal, donc aucune attention. On peut vivre des heures sereines sans jamais les remarquer, et se croire « vide »."),
   T("LE PIÈGE", "Les interstices remplis",
     "File d’attente, trajet, deux minutes de creux : le téléphone sort tout seul. À force de remplir chaque interstice, le calme n’a plus un seul endroit où exister. Ce n’est pas le stress qui manque de place — c’est lui."),
  ],
  "Quelle place la sérénité occupe-t-elle chez toi — pour de vrai ?",
  "C’est l’émotion la plus sous-cotée : elle ne crie pas, ne pétille pas, ne prévient pas. On la vit sans la voir — et on la perd sans s’en apercevoir. Voici pourquoi.",
  "#sérénité #calme", emo="serenite"),

P("distinction", 11, "serenite-ou-indifference", "Sérénité ou indifférence ?",
  "posé — ou coupé",
  [
   T("LA PREMIÈRE", "La sérénité",
     "Elle ressent tout — mais rien ne la secoue. Présente, disponible, touchée par ce qui arrive, sans être renversée. C’est un calme habité : le contraire de l’absence.", vign="serenite"),
   T("LA SECONDE", "L’indifférence",
     "Elle ne ressent plus. Coupée, anesthésiée, « peu importe ». Ça ressemble à du calme vu de loin — mais c’est un débranchement, souvent le signe d’une fatigue émotionnelle profonde.", vign="degout"),
   D("D’où la différence",
     "La sérénité est connectée : elle sent, elle répond, elle reste douce.",
     "L’indifférence est débranchée : elle ne sent plus rien — même le bon.",
     "Test honnête : les bonnes nouvelles te font-elles encore quelque chose ? La sérénité laisse passer la joie. L’indifférence bloque tout — c’est un signal à prendre au sérieux."),
  ],
  "Et ton calme à toi — habité, ou débranché ?",
  "« Je suis calme » peut vouloir dire deux choses opposées : un système apaisé, ou un système débranché. La différence tient en une question — est-ce que le bon passe encore ?",
  "#calme #burnout", emos=["serenite", "tristesse"]),

P("pratique", 11, "le-sas-de-transition", "Le sas\nde transition",
  "trois respirations entre deux vies",
  [
   T("POURQUOI ÇA MARCHE", "Les tensions s’empilent",
     "Sans transition, tu entres dans ta soirée avec la réunion encore sur les épaules, dans ta réunion avec le trajet dans les nerfs. Chaque activité déborde sur la suivante — et le fond de tension monte toute la journée."),
   E("COMMENT FAIRE", "Aux moments charnières",
     [("Repère tes frontières", "la voiture avant d’entrer, la porte du bureau, la fin d’un appel : les sas naturels de ta journée."),
      ("Trois respirations lentes", "juste ça. Tu fermes ce qui vient de se passer, tu ouvres ce qui commence."),
      ("Nomme le passage", "« fin du travail, début de la maison ». Une phrase intérieure suffit — elle signe la frontière.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Le sas du soir d’abord",
     "Si tu n’en installes qu’un, mets-le entre le travail et la maison : c’est celui qui protège les personnes que tu aimes de la journée qu’elles n’ont pas vécue."),
  ],
  "Envie de mesurer ton niveau de calme réel ?",
  "Ce n’est pas la journée qui épuise — c’est l’empilement : chaque activité qui déborde sur la suivante. Trois respirations aux bons endroits changent la texture d’une journée entière.",
  "#calme #routine", emo="serenite"),
],

# ————————————————————— SEMAINE 12 — l'inattendu —————————————————————
[
P("comprendre", 12, "comprendre-surprise", "La surprise",
  "la remise à zéro de l’attention",
  [
   T("À QUOI ELLE SERT", "Mettre à jour tes prédictions",
     "Ton cerveau prédit en permanence la seconde suivante. Quand la réalité contredit la prédiction — sourcils levés, bouche ouverte, tout s’arrête — c’est la surprise : une mise à jour d’urgence du modèle."),
   T("SA NATURE", "Un carrefour neutre",
     "La surprise ne dure qu’un instant, puis elle se transforme : en joie si c’est une bonne nouvelle, en peur, en colère. Elle n’est ni agréable ni désagréable — c’est l’aiguillage, pas la destination."),
   T("QUAND ELLE MARQUE", "La facture d’apprentissage",
     "Une énorme surprise, c’est une prédiction centrale qui casse — sur une personne, sur soi, sur la vie. Ce qui suit (le temps de digérer, d’en reparler sans arrêt) n’est pas de la faiblesse : c’est le modèle qui se reconstruit."),
  ],
  "Quelle place la surprise occupe-t-elle chez toi ?",
  "C’est l’émotion la plus courte — une seconde à peine — et l’une des plus importantes : elle signale que ta carte du monde vient de se tromper. Voici ce qui se joue dans cette seconde.",
  "#surprise #cerveau", emo="surprise"),

P("distinction", 12, "surprise-ou-sursaut", "Surprise ou sursaut ?",
  "l’esprit — ou le réflexe",
  [
   T("LE PREMIER", "Le sursaut",
     "Un claquement de porte, et le corps a bondi avant toute pensée : c’est un réflexe de protection, pur câblage. Il ne dit rien de toi — sinon que ton alarme corporelle fonctionne.", vign="peur"),
   T("LA SECONDE", "La surprise",
     "Elle, c’est l’esprit : une information qui contredit ce que tu croyais. Elle peut arriver sans aucun bruit — une phrase dans une conversation calme peut être la plus grosse surprise de l’année.", vign="surprise"),
   D("D’où la différence",
     "Le sursaut est un réflexe du corps : une seconde, aucun contenu.",
     "La surprise est une mise à jour de l’esprit : elle a un contenu, et des suites.",
     "Sursauter facilement n’est pas « être peureux » — c’est un seuil d’alarme réglé bas, souvent par la fatigue ou une période de tension. Ça se lit comme un indicateur, pas comme un trait."),
  ],
  "Et toi, ton seuil d’alarme est réglé comment, ces temps-ci ?",
  "Tu sursautes pour un rien en ce moment ? Ce n’est pas de la peur — c’est souvent un indicateur de fatigue ou de tension accumulée. La différence entre sursaut et surprise explique pourquoi.",
  "#surprise #stress", emos=["surprise", "peur"]),

P("pratique", 12, "la-seconde-de-suspension", "La seconde\nde suspension",
  "entre l’imprévu et ta réaction",
  [
   T("POURQUOI ÇA MARCHE", "L’aiguillage se joue là",
     "Après une surprise, la première interprétation prend toute la place : « c’est une catastrophe », « il l’a fait exprès ». Or c’est un carrefour — et la direction prise dans la première seconde décide de l’heure qui suit."),
   E("COMMENT FAIRE", "Quand l’imprévu tombe",
     [("Une seconde, une respiration", "avant le premier mot. C’est court — et c’est immense."),
      ("Nomme ce qui casse", "« je n’avais pas prévu ça ». Pas encore bien ou mal : juste inattendu."),
      ("Choisis la question", "« qu’est-ce que ça change, concrètement ? » — au lieu de « c’est une catastrophe »." )]),
   T("LE DÉTAIL QUI CHANGE TOUT", "Entraîne-toi sur les petits imprévus",
     "Le train annulé, le plan qui tombe à l’eau : des occasions d’entraînement gratuites. Le réflexe construit sur les petites surprises sera là pour les grandes."),
  ],
  "Envie de voir comment tu réagis à l’inattendu ?",
  "Entre l’imprévu et ta réaction, il existe une seconde — et tout se joue dedans. Voici comment l’agrandir, en t’entraînant sur les imprévus qui ne coûtent rien.",
  "#imprévu #résilience", emo="surprise"),
],

# ————————————————————— SEMAINE 13 — la boussole entière —————————————————————
[
P("comprendre", 13, "comprendre-degout", "Le dégoût",
  "le gardien qui écarte ce qui nuit",
  [
   T("À QUOI IL SERT", "Rejeter avant d’analyser",
     "Le dégoût est ton système de rejet : nourriture avariée, odeur suspecte — la grimace arrive avant la pensée, et elle t’a sauvé la vie des milliers de fois à l’échelle de l’espèce."),
   T("SON EXTENSION", "Le dégoût moral",
     "Le même circuit s’active pour les comportements : la trahison, la cruauté, l’injustice « écœurent ». Ton dégoût moral dessine tes valeurs en creux — dis-moi ce qui te dégoûte, je te dirai ce qui t’est sacré."),
   T("LE PIÈGE", "Il déshumanise plus vite que tout",
     "Dirigé contre des personnes ou des groupes, le dégoût est l’émotion la plus dangereuse qui soit : il transforme des gens en choses. Quand il vise quelqu’un plutôt qu’un acte — méfiance, toujours."),
  ],
  "Quelle place le dégoût occupe-t-il chez toi ?",
  "C’est l’émotion dont on ne parle jamais — et l’une des plus puissantes : elle protège ton corps, dessine tes valeurs… et peut déshumaniser plus vite que toutes les autres. Portrait.",
  "#dégoût #valeurs", emo="degout"),

P("distinction", 13, "emotion-ou-humeur", "Émotion ou humeur ?",
  "la réaction — ou le fond de l’air",
  [
   T("LA PREMIÈRE", "L’émotion",
     "Elle a un déclencheur, un début, une fin : cette phrase m’a mis en colère, cette nouvelle m’a réjoui. Elle est datée et elle raconte quelque chose de précis — c’est un message.", vign="colere"),
   T("LA SECONDE", "L’humeur",
     "Elle n’a pas de cause claire : on se lève « gris » ou « léger », et ça colore tout — les mêmes événements paraissent lourds un jour, anodins le lendemain. C’est le fond de l’air intérieur.", vign="tristesse"),
   D("D’où la différence",
     "L’émotion est une réaction : elle répond à quelque chose, puis elle passe.",
     "L’humeur est un climat : sommeil, fatigue, saison, hormones — tout y contribue.",
     "L’intérêt de les distinguer : on ne « résout » pas une humeur en cherchant un coupable. Un jour gris ne signifie pas que ta vie va mal — parfois, il signifie juste que tu as mal dormi."),
  ],
  "Et aujourd’hui — c’est une émotion qui te parle, ou une humeur qui te colore ?",
  "« Pourquoi je me sens comme ça ? » — parfois il n’y a pas de pourquoi : c’est une humeur, pas une émotion. Savoir les distinguer évite de chercher des coupables aux jours gris.",
  "#humeur #émotions", emos=["joie", "tristesse"]),

P("pratique", 13, "la-meteo-interieure", "La météo\nintérieure",
  "une minute par jour pour tout changer",
  [
   T("POURQUOI ÇA MARCHE", "Nommer, c’est réguler",
     "Une émotion identifiée devient un objet qu’on peut observer — au lieu d’un brouillard qui déborde. C’est la différence entre « je me sens mal » et « je sens de la honte, parce que je me suis exposé ». La seconde ouvre une porte."),
   E("COMMENT FAIRE", "Une minute, où tu veux",
     [("Quelle est la dominante ?", "là, maintenant : plutôt anxiété, joie, colère, fatigue ? Un mot suffit."),
      ("Où, dans le corps ?", "gorge, poitrine, ventre, mâchoires — l’émotion a toujours une adresse physique."),
      ("Quel besoin dessous ?", "être rassuré·e, reconnu·e, tranquille, relié·e ? Le besoin pointe l’action.")]),
   T("LE DÉTAIL QUI CHANGE TOUT", "La précision du mot",
     "« Stressé » est un fourre-tout. Anxieux, débordé, vexé, déçu, impatient : plus le mot est juste, plus l’émotion devient maniable. Le vocabulaire est un outil de régulation."),
  ],
  "Et si tu faisais le point complet — les 14 d’un coup ?",
  "Le geste le plus rentable de toute la vie émotionnelle tient en une minute : nommer ce qui se passe. Voici la version en trois questions — la porte d’entrée de tout le reste.",
  "#météointérieure #pleineconscience", emo="joie"),
],
]

# vérification rapide à l'import
assert len(SEMAINES) == 13, f"{len(SEMAINES)} semaines au lieu de 13"
for i, s in enumerate(SEMAINES, 1):
    assert len(s) == 3, f"semaine {i} : {len(s)} posts au lieu de 3"
    series = [p["serie"] for p in s]
    assert series == ["comprendre", "distinction", "pratique"], f"semaine {i} : ordre {series}"
