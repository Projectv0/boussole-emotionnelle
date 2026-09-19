#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose les carrousels « scène vécue » : illustration pleine page + bulles + narrateur.

    python3 assembleur.py            tous les posts
    python3 assembleur.py 3 7 12     seulement ceux-là

Lit contenus.json, va chercher les images dans illustrations/, écrit dans sortie/
un dossier par post avec instagram/ (1080×1350), tiktok/ (1080×1920) et legende.txt.

Contrairement au dossier reseaux-sociaux-illustre/, l'illustration occupe ici toute la
page : les bulles et le narrateur se posent dessus. C'est l'assembleur qui les dessine,
en vrai français — on ne les demande jamais au générateur d'images, qui déforme les mots.
"""
import itertools, json, math, os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
ILLUS = os.path.join(BASE, "illustrations")
SORTIE = os.path.join(BASE, "sortie")

FORMATS = {
    "instagram": dict(W=1080, H=1350, ECH=1.00, HAUT=120, BAS=120),
    "tiktok":    dict(W=1080, H=1920, ECH=1.12, HAUT=260, BAS=300),
}
W, H, ECH, HAUT, BAS = 1080, 1350, 1.00, 120, 120

def format_actif(nom):
    global W, H, ECH, HAUT, BAS, _cache
    f = FORMATS[nom]
    W, H, ECH, HAUT, BAS = f["W"], f["H"], f["ECH"], f["HAUT"], f["BAS"]
    _cache = {}

def E(n):
    return int(n * ECH)

CREME = (247, 242, 233)
ENCRE = (26, 22, 20)
TERRE = (192, 78, 42)
BLANC = (255, 253, 249)
OMBRE = (26, 22, 20)

CONDENSE = "/System/Library/Fonts/Avenir Next Condensed.ttc"
SANS = "/System/Library/Fonts/Avenir Next.ttc"
LOURD, DEMI, MOYEN, REG = 8, 2, 5, 7      # Avenir Next Condensed
S_REG, S_DEMI = 7, 2                       # Avenir Next

_f = {}
def F(chemin, taille, idx):
    t = int(taille * ECH)
    cle = (chemin, t, idx)
    if cle not in _f:
        _f[cle] = ImageFont.truetype(chemin, t, index=idx)
    return _f[cle]

_m = ImageDraw.Draw(Image.new("RGB", (8, 8)))
def larg(t, f):
    return _m.textlength(t, font=f)

def nbsp(t):
    for p in ("?", "!", ":", ";", "»"):
        t = t.replace(" " + p, " " + p)
    return t.replace("« ", "« ")

def couper(t, f, maxw):
    lignes = []
    for para in nbsp(t).split("\n"):
        cour = ""
        for mot in para.split(" "):
            essai = (cour + " " + mot).strip()
            if not cour or larg(essai, f) <= maxw:
                cour = essai
            else:
                lignes.append(cour); cour = mot
        lignes.append(cour)
    return lignes

# ————— illustrations —————
def chemin_illustration(nom):
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = os.path.join(ILLUS, nom + ext)
        if os.path.exists(p):
            return p
    return None

def _bord_dessine(sombres, unies, moyennes, limite):
    """Où s'arrête la marge, en partant d'un bord : juste après le liseré du cadre.

    Le cadre que le générateur dessine a une signature précise : une marge claire
    d'une seule teinte, un trait sombre fin, puis le dessin. Les trois conditions
    comptent — sans la marge claire, toutes les scènes de nuit passaient pour
    encadrées, et un tiers de l'image y perdait sa tête.
    """
    for i in range(3, limite):
        # on s'arrête trois lignes avant le trait : celle qui le précède est un
        # dégradé d'anticrénelage, jamais parfaitement unie.
        m = max(3, i - 3)
        if sombres[i] <= .80 or not all(unies[:m]) or min(moyennes[:m]) < 150:
            continue
        j = i
        while j < limite and sombres[j] > .55:
            j += 1
        if j - i > 14 or j + 8 >= limite:       # un trait fin, pas une zone sombre
            return 0
        if all(unies[j:j + 8]):                 # du dessin doit commencer après
            return 0
        return j
    return 0

# Les rognages décidés à la main, quand la détection ne peut pas trancher.
# Une bande d'aplat en haut du panneau est presque toujours la zone calme voulue,
# celle où se posent les bulles : on ne la rogne pas. Sauf quand c'est visiblement
# une barre noire posée sur la scène, avec une arête franche et une couleur
# étrangère au décor — ce qui n'arrive qu'ici, sur cent cinquante illustrations.
A_ROGNER = {"calme-soir-fenetre-ouverte": (0.0, 0.28, 1.0, 1.0)}

_source = {}
def source(nom):
    """L'illustration, débarrassée du cadre que le générateur dessine parfois.

    Cinq images sur cent cinquante portent un liseré noir et une marge crème autour
    du dessin. Les bulles se posaient dans cette marge, détachées de la scène, et la
    queue mourait sur le trait du cadre sans jamais rejoindre une tête. On rogne donc
    jusqu'à l'intérieur du panneau. Le rognage est mémorisé : visages() doit appliquer
    exactement le même, sinon les têtes sont décalées d'autant.
    """
    if nom in _source:
        return _source[nom]
    chemin = chemin_illustration(nom or "")
    if chemin is None:
        _source[nom] = None
        return None
    im = Image.open(chemin).convert("RGB")
    g = im.convert("L")
    px = g.load()
    w, h = g.size
    def bande(indices, taille, horizontale):
        sombres, unies, moyennes = [], [], []
        for k in indices:
            vals = [px[j, k] if horizontale else px[k, j] for j in range(0, taille, 3)]
            sombres.append(sum(1 for v in vals if v < 90) / len(vals))
            mo = sum(vals) / len(vals)
            moyennes.append(mo)
            unies.append((sum((v - mo) ** 2 for v in vals) / len(vals)) ** .5 < 6)
        return sombres, unies, moyennes
    lim_v, lim_h = int(h * .35), int(w * .35)
    haut = _bord_dessine(*bande(range(lim_v), w, True), lim_v)
    bas = _bord_dessine(*bande(range(h - 1, h - lim_v - 1, -1), w, True), lim_v)
    gauche = _bord_dessine(*bande(range(lim_h), h, False), lim_h)
    droite = _bord_dessine(*bande(range(w - 1, w - lim_h - 1, -1), h, False), lim_h)
    boite = (gauche, haut, w - droite, h - bas)
    main = A_ROGNER.get(nom)
    if main:
        boite = (max(boite[0], int(w * main[0])), max(boite[1], int(h * main[1])),
                 min(boite[2], int(w * main[2])), min(boite[3], int(h * main[3])))
    if boite != (0, 0, w, h):
        im = im.crop(boite)
    _source[nom] = (im, boite, (w, h))
    return _source[nom]

def tetes_du_panneau(nom):
    """Les têtes en fractions du panneau, d'où qu'elles viennent.

    file/visages.json est relatif au fichier d'origine, file/tetes-manuelles.json au
    panneau : on ramène tout à la même échelle avant de s'en servir.
    """
    src = source(nom)
    if src is None:
        return []
    im, (cg, ch, _, _), (ow, oh) = src
    brutes = VISAGES.get(nom or "", [])
    if brutes:
        return [{"x": (v["x"] * ow - cg) / im.width, "y": (v["y"] * oh - ch) / im.height,
                 "l": v["l"] * ow / im.width, "h": v["h"] * oh / im.height} for v in brutes]
    return list(TETES_MANUELLES.get(nom or "", []))

def cadrage(nom):
    """Le recadrage « cover » : dimensions après agrandissement, et le coin rogné.

    Le décalage horizontal était toujours centré, ce qui tranchait un personnage
    assis au bord du panneau — on ne voyait plus qu'une demi-joue sans œil. On le
    glisse maintenant du minimum nécessaire pour que toutes les têtes tiennent.
    """
    src = source(nom)
    if src is None:
        return None
    im = src[0]
    r = max(W / im.width, H / im.height)
    nw, nh = max(W, int(im.width * r)), max(H, int(im.height * r))
    # on garde le haut de l'image : c'est là que se trouvent les visages
    dy = min((nh - H) // 2, int(nh * .12))
    dx = (nw - W) // 2
    tetes = tetes_du_panneau(nom)
    if tetes and nw > W:
        gauche = min((t["x"] - t["l"] * .7) * nw for t in tetes)
        droite = max((t["x"] + t["l"] * .7) * nw for t in tetes)
        bas, haut = droite - W + E(12), gauche - E(12)
        if bas <= haut:                      # tout tient : on ne bouge qu'au besoin
            dx = int(min(max(dx, bas), haut))
        dx = max(0, min(dx, nw - W))
    return im, nw, nh, dx, dy

_cache = {}
def illustration(nom):
    """Charge illustrations/<nom>.*, recadre pour remplir la page sans déformer."""
    cle = (nom, W, H)
    if cle in _cache:
        return _cache[cle]
    c = cadrage(nom)
    if c is None:
        _cache[cle] = None
        return None
    im, nw, nh, dx, dy = c
    im = im.resize((nw, nh), Image.LANCZOS).crop((dx, dy, dx + W, dy + H))
    _cache[cle] = im
    return im

def fond_manquant(nom):
    """Page de secours quand l'illustration n'est pas encore générée."""
    img = Image.new("RGB", (W, H), CREME)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([40, 40, W - 40, H - 40], radius=28, outline=(205, 190, 172), width=4)
    f = F(CONDENSE, 46, DEMI)
    d.text(((W - larg(nom, f)) / 2, H / 2 - 30), nom, font=f, fill=(150, 135, 120))
    g = F(CONDENSE, 32, REG)
    t = "à générer"
    d.text(((W - larg(t, g)) / 2, H / 2 + 34), t, font=g, fill=(170, 155, 140))
    return img

# ————— bulles —————
ZONES = {   # (ancre x en fraction de W, ancre y en fraction de H, alignement)
    "hg": (.06, .07, "gauche"), "hd": (.94, .07, "droite"),
    "mg": (.06, .34, "gauche"), "md": (.94, .34, "droite"),
    "bg": (.06, .60, "gauche"), "bd": (.94, .60, "droite"),
}

# ————— vers qui la queue pointe —————
# Les visages sont détectés une fois pour toutes sur les illustrations d'origine
# (voir `detecter-visages.sh`) et rangés dans file/visages.json, en coordonnées
# normalisées, origine en haut à gauche.
#
# Avant, la queue visait une ancre fixe — le quart ou les trois quarts de la largeur.
# Sur une illustration où le personnage est au centre, ou décalé, elle pointait donc
# à côté de lui. Elle vise maintenant sa tête.
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", "visages.json"),
              encoding="utf-8") as _fv:
        VISAGES = json.load(_fv)
except FileNotFoundError:
    VISAGES = {}

# Vision est entraîné sur des photos : il ne voit rien sur vingt-quatre illustrations,
# personnages de trois quarts, de dos ou en contre-jour. Leurs têtes sont relevées à
# l'œil dans ce fichier, en fractions du panneau — donc après rognage du cadre.
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "file", "tetes-manuelles.json"), encoding="utf-8") as _fm:
        TETES_MANUELLES = {k: v for k, v in json.load(_fm).items() if not k.startswith("_")}
except FileNotFoundError:
    TETES_MANUELLES = {}

# Position de repli quand aucun visage n'a été détecté sur l'illustration.
TETES = {"gauche": (.27, .52), "droite": (.73, .52)}

def visages(nom):
    """Les têtes, en pixels du cadre composé, triées de gauche à droite."""
    tetes = tetes_du_panneau(nom)
    c = cadrage(nom)
    if not tetes or c is None:
        return []
    _, nw, nh, dx, dy = c
    out = [{"x": t["x"] * nw - dx, "y": t["y"] * nh - dy,
            "l": t["l"] * nw, "h": t["h"] * nh} for t in tetes]
    return sorted(out, key=lambda v: v["x"])

# Quand elle vaut une liste, chaque bulle y dépose sa géométrie : de quoi contrôler
# après coup qu'aucune ne couvre un visage. Voir controle-bulles.py.
CONTROLE = None

def attribuer_tetes(bulles, faces):
    """À chaque bulle, la tête qu'elle désigne — choisie par proximité.

    Une diapositive a au plus deux locuteurs, un par côté : on attribue donc une
    tête par côté, et toutes les bulles d'un même côté la partagent. Attribuer une
    tête par bulle envoyait la deuxième bulle d'un même personnage — sa pensée —
    vers le visage d'en face.
    """
    if not faces or not bulles:
        return [None] * len(bulles)
    cotes = [ZONES.get(b["zone"], ZONES["hg"])[2] for b in bulles]
    presents = [c for c in ("gauche", "droite") if c in cotes]
    reps = {"gauche": W * .25, "droite": W * .75}
    k = min(len(faces), len(presents))
    meilleur = None
    for gs in itertools.combinations(range(len(presents)), k):
        for fs in itertools.permutations(range(len(faces)), k):
            cout = sum(abs(reps[presents[g]] - faces[f]["x"]) for g, f in zip(gs, fs))
            if meilleur is None or cout < meilleur[0]:
                meilleur = (cout, dict(zip(gs, fs)))
    # Une tête franchement du mauvais côté n'est pas celle qui parle : c'est le
    # cas quand le détecteur n'a vu que l'interlocuteur, ou qu'il a pris un reflet
    # pour un visage. On préfère alors l'ancre de repli, du bon côté.
    seuil = W * .42
    choix = {}
    for gi, fi in meilleur[1].items():
        c = presents[gi]
        if abs(reps[c] - faces[fi]["x"]) < seuil:
            choix[c] = faces[fi]
    return [choix.get(c) for c in cotes]

def _aire_commune(r, autre):
    return (max(0, min(r[2], autre[2]) - max(r[0], autre[0]))
            * max(0, min(r[3], autre[3]) - max(r[1], autre[1])))

def _chevauche(r, autre, marge=0):
    return (r[0] < autre[2] + marge and r[2] > autre[0] - marge
            and r[1] < autre[3] + marge and r[3] > autre[1] - marge)

def _boite_visage(v):
    """Le visage un peu élargi : cheveux au-dessus, menton en dessous."""
    return (v["x"] - v["l"] * .55, v["y"] - v["h"] * .75,
            v["x"] + v["l"] * .55, v["y"] + v["h"] * .70)

def plancher_lecture(prec, g):
    """Hauteur minimale de `g` pour qu'elle se lise après `prec`.

    En bande dessinée, l'œil prend la bulle la plus haute en premier, et à hauteur
    égale celle de gauche. Les bulles de `contenus.json` sont dans l'ordre où on
    les prononce : une réplique qui répond depuis la gauche doit donc descendre,
    sinon elle se lit avant la question. Deux bulles à la même hauteur, la première
    à droite : on lisait la réponse avant la question sur vingt-six diapositives.

    De gauche à droite, rien à faire — la même ligne se lit déjà dans le bon sens.
    """
    if prec is None:
        return None
    cx_p = prec["x"] + prec["bw"] / 2
    cx_g = g["x"] + g["bw"] / 2
    if cx_g > cx_p + E(20):
        return prec["y"] - E(10)
    return prec["y"] + max(E(60), int(prec["bh"] * .55))

def poser_bulles(img, bulles, nom_illu, depuis=0, texte_narrateur=""):
    """Pose toutes les bulles d'une diapositive : dans l'ordre de lecture, têtes
    visées, et rien ni sur un visage ni sur le bandeau du narrateur."""
    limite = min(H - E(120), haut_du_narrateur(texte_narrateur) - E(16))
    faces = visages(nom_illu)
    tetes = attribuer_tetes(bulles, faces)
    boites = [_boite_visage(v) for v in faces]
    occupe = []
    prec = None
    for b, cible in zip(bulles, tetes):
        genre = b.get("type", "dit")
        g = mesurer_bulle(b["texte"], genre, b["zone"], depuis)
        plafond = limite - g["bh"]              # au-dessus du bandeau du narrateur
        pl = plancher_lecture(prec, g)
        bas = max(depuis + E(10), pl if pl is not None else 0)
        bas = min(bas, plafond)                 # le cadre l'emporte sur le décalage
        # La zone fixe tombait parfois pile sur une figure. On glisse alors la bulle
        # à la verticale, sans jamais remonter au-dessus de la bulle précédente.
        depart = max(bas, g["y"])
        obstacles = occupe + boites
        essais, pose = [], None
        for d in (0, E(80), -E(70), E(170), -E(150), E(260), -E(230), E(350), E(440)):
            y = min(max(bas, depart + d), plafond)
            for dx in (0, -E(60), E(60), -E(130), E(130)):
                x = min(max(E(18), g["x"] + dx), W - g["bw"] - E(18))
                # elle glisse, mais sans changer de moitié : une bulle qui traverse
                # le cadre se met à désigner l'autre personnage.
                milieu = x + g["bw"] / 2
                if (milieu > W * .56) if g["align"] == "gauche" else (milieu < W * .44):
                    continue
                r = (x, y, x + g["bw"], y + g["bh"])
                if not any(_chevauche(r, o, E(14)) for o in obstacles):
                    pose = (x, y); break
                essais.append((sum(_aire_commune(r, o) for o in obstacles), len(essais), x, y))
            if pose:
                break
        if pose:
            g["x"], g["y"] = pose
        else:
            # Aucune position libre — un gros plan où le visage occupe tout le cadre.
            # On prend alors celle qui en couvre le moins, plutôt que de laisser la
            # bulle à sa place de repos, c'est-à-dire en plein sur la figure.
            _, _, g["x"], g["y"] = min(essais)
        r = (g["x"], g["y"], g["x"] + g["bw"], g["y"] + g["bh"])
        bulle(img, g, genre, cible, voisines=list(occupe))
        occupe.append(r)
        prec = g

def _sortie_du_cadre(x, y, bw, bh, vers_x, vers_y):
    """Où la queue perce le cadre de la bulle, en allant vers (vers_x, vers_y)."""
    cx, cy = x + bw / 2, y + bh / 2
    dx, dy = vers_x - cx, vers_y - cy
    if not dx and not dy:
        return cx, y + bh, "bas"
    ts = []
    if dx > 0: ts.append(((x + bw - cx) / dx, "droite"))
    if dx < 0: ts.append(((x - cx) / dx, "gauche"))
    if dy > 0: ts.append(((y + bh - cy) / dy, "bas"))
    if dy < 0: ts.append(((y - cy) / dy, "haut"))
    t, cote = min(ts)
    px, py = cx + dx * t, cy + dy * t
    # on écarte des coins, sinon la queue naît sur l'arrondi et se décolle du cadre
    m = E(34)
    if cote in ("bas", "haut"):
        px = min(max(px, x + m), x + bw - m)
    else:
        py = min(max(py, y + m), y + bh - m)
    return px, py, cote

def mesurer_bulle(texte, genre, zone, depuis=0):
    """Taille et place de repos d'une bulle, avant d'éviter les visages."""
    fx, fy, align = ZONES.get(zone, ZONES["hg"])
    f = F(CONDENSE, 38, DEMI)
    lignes = couper(texte.upper() if genre == "dit" else texte, f, int(W * .40))
    lh = int(f.size * 1.16)
    pad = E(22)
    bw = max(larg(l, f) for l in lignes) + pad * 2
    bh = len(lignes) * lh + pad * 2 - E(6)

    x = int(W * fx) if align == "gauche" else int(W * fx) - bw
    # « depuis » réserve le haut de la page : sur la diapositive de titre, les bulles
    # se posaient par-dessus le titre. Les zones glissent alors sous lui.
    y = depuis + int((H - depuis) * fy)
    x = max(E(18), min(x, W - bw - E(18)))
    y = max(depuis + E(10), min(y, H - bh - E(120)))
    return dict(x=x, y=y, bw=int(bw), bh=bh, lignes=lignes, f=f, lh=lh, pad=pad,
                align=align, zone=zone, texte=texte, depuis=depuis)

def _arret_avant(bx, by, ux, uy, longueur, boites, marge):
    """Raccourcit la queue pour qu'elle s'arrête avant d'entrer dans une de ces boîtes.

    Sert deux fois : devant la tête visée, pour que la pointe ne touche pas le visage ;
    et devant une bulle voisine, car deux bulles empilées du même côté visent la même
    tête et la queue de celle du haut traversait celle du bas.
    """
    for x0, y0, x1, y1 in boites:
        ts = []
        for p, d, a, b in ((bx, ux, x0, x1), (by, uy, y0, y1)):
            if d == 0:
                if not (a <= p <= b):
                    ts = None; break
                ts.append((-1e9, 1e9))
            else:
                t0, t1 = (a - p) / d, (b - p) / d
                ts.append((min(t0, t1), max(t0, t1)))
        if ts is None:
            continue
        deb, fin = max(ts[0][0], ts[1][0]), min(ts[0][1], ts[1][1])
        if deb <= fin and fin > 0:
            longueur = min(longueur, max(0, deb - marge))
    return longueur

def bulle(img, g, genre, cible=None, voisines=()):
    """Dessine une bulle de dialogue ou de pensée, sa queue pointée vers celui qui parle.

    Le texte est écrit ici, en français, par l'assembleur : jamais par le générateur
    d'images, qui déforme systématiquement les mots.
    """
    x, y, bw, bh = g["x"], g["y"], g["bw"], g["bh"]
    lignes, f, lh, pad, align = g["lignes"], g["f"], g["lh"], g["pad"], g["align"]
    d = ImageDraw.Draw(img)

    if CONTROLE is not None:
        CONTROLE.append({"zone": g["zone"], "rect": (x, y, x + bw, y + bh), "cible": cible,
                         "texte": g["texte"]})

    # ombre portée douce, pour détacher la bulle de l'illustration
    ombre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ombre).rounded_rectangle([x + 5, y + 6, x + bw + 5, y + bh + 6],
                                            radius=E(26), fill=(26, 22, 20, 60))
    img.paste(Image.alpha_composite(img.convert("RGBA"), ombre.filter(
        ImageFilter.GaussianBlur(7))).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)

    d.rounded_rectangle([x, y, x + bw, y + bh], radius=E(26), fill=BLANC,
                        outline=ENCRE, width=E(4))

    # La queue pointe vers la tête de celui qui parle. Quand le visage a été détecté on
    # vise sa tête réelle ; sinon on retombe sur l'ancre approximative du côté.
    if cible:
        tete_x, tete_y, tete_h = cible["x"], cible["y"], cible["h"]
    else:
        tx, ty_t = TETES[align]
        tete_x, tete_y = W * tx, max(y + bh + E(150), H * ty_t)
        tete_h = E(180)

    base_x, base_y, _ = _sortie_du_cadre(x, y, bw, bh, tete_x, tete_y)
    vx, vy = tete_x - base_x, tete_y - base_y
    dist = math.hypot(vx, vy) or 1.0
    ux, uy = vx / dist, vy / dist
    # Elle tend vers la tête et s'arrête net devant : une queue qui touche le visage
    # se lit comme un trait de crayon en travers de la figure, et trois ronds blancs
    # posés sur une chevelure se voient de loin. On s'arrête sur la boîte de la tête
    # plutôt que sur une marge calculée depuis son centre : quand le détecteur
    # surestime la taille d'une tête, cette marge mangeait toute la queue.
    boite = _boite_visage(cible) if cible else (tete_x - E(90), tete_y - E(110),
                                               tete_x + E(90), tete_y + E(110))
    mini = E(42) if genre != "dit" else E(28)   # trois ronds ont besoin d'un peu de course
    # Le plafond était à 130 px : la queue s'arrêtait en plein mur, laissant parfois
    # deux cents pixels de vide entre sa pointe et le personnage. Elle peut aller plus
    # loin sans risque, puisque _arret_avant la stoppe net devant la boîte de la tête.
    longueur = max(mini, _arret_avant(base_x, base_y, ux, uy, E(240), [boite], E(34)))
    # Deux bulles du même personnage, empilées du même côté : la queue de celle du
    # haut butait dans celle du bas et s'y terminait en moignon tronqué. Dès qu'une
    # voisine la raccourcit, on la supprime — c'est celle du bas qui désigne la tête.
    # On teste contre les voisines élargies de la demi-largeur de la queue : le rayon
    # passait à côté de la boîte alors que le triangle, lui, mordait dedans.
    larges = [(a - E(20), b - E(20), c + E(20), e + E(20)) for a, b, c, e in voisines]
    if _arret_avant(base_x, base_y, ux, uy, longueur, larges, E(18)) < longueur - E(2):
        return _texte_bulle(d, g)
    pointe_x, pointe_y = base_x + ux * longueur, base_y + uy * longueur

    if genre == "dit":
        demi = E(15)
        # la base est un segment posé sur le cadre, perpendiculaire à la direction
        px, py = -uy * demi, ux * demi
        a = (base_x + px, base_y + py)
        b = (base_x - px, base_y - py)
        d.polygon([a, b, (pointe_x, pointe_y)], fill=BLANC)
        # on efface le trait du cadre sous la base, pour souder la queue à la bulle
        d.line([(a[0] - ux * E(2), a[1] - uy * E(2)),
                (b[0] - ux * E(2), b[1] - uy * E(2))], fill=BLANC, width=E(7))
        # puis les deux flancs, à l'épaisseur du cadre : dessinés par polygon(outline),
        # ils ne faisaient qu'un pixel contre quatre, et la queue ressemblait à une
        # rayure sur le mur plutôt qu'à un appendice de la bulle.
        d.line([a, (pointe_x, pointe_y), b], fill=ENCRE, width=E(4), joint="curve")
    else:
        # Chaîne de ronds orientée vers la tête. Toujours trois : un rond isolé ne se
        # lit plus comme une pensée. Leur rayon est plafonné par l'écart entre eux,
        # sinon ils se chevauchaient en un pâté blanc collé sous la bulle.
        # Elle reste courte : plus longue, elle descend sur les cheveux, et trois ronds
        # blancs percés dans un crâne se voient de loin.
        pas = longueur / 3.4
        for i, r in enumerate((E(10), E(7), E(5))):
            r = max(E(3), min(r, pas * .45))
            t = (i + 1) * pas
            cx, cy = base_x + ux * t, base_y + uy * t
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANC, outline=ENCRE,
                      width=max(2, E(3)))

    _texte_bulle(d, g)

def _texte_bulle(d, g):
    """Le texte, centré dans la bulle.

    Il était ferré vers le bord extérieur du cadre : une dernière ligne courte
    collait à une paroi en laissant un blanc de la moitié de la bulle en face.
    En bande dessinée, le texte d'une bulle se centre.
    """
    ty = g["y"] + g["pad"] - E(3)
    for l in g["lignes"]:
        d.text((g["x"] + (g["bw"] - larg(l, g["f"])) / 2, ty), l, font=g["f"], fill=ENCRE)
        ty += g["lh"]

def _bandeau_narrateur(texte):
    """Les lignes et la taille du bandeau, avant de le dessiner.

    Mesuré à part parce que les bulles ont besoin de savoir où il commence : elles
    descendent maintenant pour respecter l'ordre de lecture, et sans ça rien ne les
    empêcherait de finir dessus.
    """
    f = F(CONDENSE, 34, LOURD)
    # Un « / » dans le texte du narrateur marque une coupure voulue entre deux
    # phrases : il était rendu tel quel, au milieu du bandeau. On le traduit en
    # retour à la ligne, et couper() respecte déjà les sauts de ligne.
    lignes = couper(re.sub(r"\s*/\s*", "\n", texte).upper(), f, int(W * .74))
    lh = int(f.size * 1.2)
    pad = E(20)
    bw = max(larg(l, f) for l in lignes) + pad * 2
    bh = len(lignes) * lh + pad * 2 - E(8)
    return f, lignes, lh, pad, int(bw), bh

def haut_du_narrateur(texte):
    """Le bord haut du bandeau, ou le bas du cadre s'il n'y a pas de narrateur."""
    if not texte:
        return H
    return H - BAS - _bandeau_narrateur(texte)[5]

def narrateur(img, texte, bas=True):
    """La phrase du narrateur : capitales, bandeau sombre, posée en bas de l'image."""
    if not texte:
        return
    d = ImageDraw.Draw(img)
    f, lignes, lh, pad, bw, bh = _bandeau_narrateur(texte)
    x = int((W - bw) / 2)
    y = H - BAS - bh if bas else int(H * .07)
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=E(14), fill=ENCRE)
    ty = y + pad - E(4)
    for l in lignes:
        d.text((x + (bw - larg(l, f)) / 2, ty), l, font=f, fill=CREME)
        ty += lh

# ————— diapositives —————
def voile_haut(img, hauteur, force=1.6):
    """Dégradé crème du haut vers le bas, pour asseoir le titre sur l'illustration.

    `force` retarde la disparition du crème. Sur les trois scènes où un personnage
    est cadré très haut, le titre lui passait sur le front ; un voile plus couvrant
    le transforme en bandeau franc, ce qui se lit et se regarde mieux qu'un texte
    posé sur une figure.
    """
    v = Image.new("L", (1, hauteur))
    for i in range(hauteur):
        t = i / max(1, hauteur - 1)
        v.putpixel((0, i), int(255 * max(0, 1 - t ** force)))
    masque = v.resize((W, hauteur))
    creme = Image.new("RGB", (W, hauteur), CREME)
    haut = img.crop((0, 0, W, hauteur))
    img.paste(Image.composite(creme, haut, masque), (0, 0))

def slide_titre(post):
    img = illustration(post["slides"][0]["illustration"]) or fond_manquant(post["slides"][0]["illustration"])
    img = img.copy()
    lignes = [l.strip() for l in post["titre"].split("|") if l.strip()]
    taille = 82
    f = F(CONDENSE, taille, LOURD)
    while taille > 46 and any(larg(l.upper(), F(CONDENSE, taille, LOURD)) > W - E(110) for l in lignes):
        taille -= 3
        f = F(CONDENSE, taille, LOURD)
    lh = int(f.size * 1.08)
    bas_titre = HAUT + lh * len(lignes)
    sur_une_tete = any(y0 < bas_titre and y1 > HAUT
                       for y0, y1 in ((_boite_visage(v)[1], _boite_visage(v)[3])
                                      for v in visages(post["slides"][0].get("illustration"))))
    voile_haut(img, bas_titre + E(90), 3.0 if sur_une_tete else 1.6)
    d = ImageDraw.Draw(img)
    y = HAUT
    for i, l in enumerate(lignes):
        t = l.upper()
        col = ENCRE if i == 0 else TERRE if l.endswith("?") else ENCRE
        d.text(((W - larg(t, f)) / 2, y), t, font=f, fill=col)
        y += lh
    sous_titre = y + E(40)
    poser_bulles(img, post["slides"][0].get("bulles", []),
                 post["slides"][0].get("illustration"), depuis=sous_titre,
                 texte_narrateur=post["slides"][0].get("narrateur", ""))
    narrateur(img, post["slides"][0].get("narrateur", ""))
    return img

def slide_scene(s):
    img = illustration(s["illustration"]) or fond_manquant(s["illustration"])
    img = img.copy()
    poser_bulles(img, s.get("bulles", []), s.get("illustration"),
                 texte_narrateur=s.get("narrateur", ""))
    narrateur(img, s.get("narrateur", ""))
    return img

def slide_revelation(post):
    """La bascule : texte sur crème, sans illustration — on respire avant la chute."""
    img = Image.new("RGB", (W, H), CREME)
    d = ImageDraw.Draw(img)
    f = F(CONDENSE, 56, DEMI)
    maxw = W - E(160)
    lignes = couper(post["revelation"], f, maxw)
    lh = int(f.size * 1.3)
    y = (H - len(lignes) * lh) / 2 - E(40)
    for l in lignes:
        d.text(((W - larg(l, f)) / 2, y), l, font=f, fill=ENCRE)
        y += lh
    d.line([(W / 2 - E(50), y + E(40)), (W / 2 + E(50), y + E(40))], fill=TERRE, width=E(4))
    pied(img)
    return img

def slide_appel(post):
    img = Image.new("RGB", (W, H), CREME)
    d = ImageDraw.Draw(img)
    f = F(CONDENSE, 62, LOURD)
    # La question est mesurée en capitales, pas en minuscules : mesurer avant de
    # passer en majuscules faisait déborder la ligne, les capitales étant plus larges.
    lignes = couper(post["question"].upper(), f, W - E(150))
    while len(lignes) > 3 and f.size > E(40):
        f = F(CONDENSE, int(f.size / ECH) - 4, LOURD)
        lignes = couper(post["question"].upper(), f, W - E(150))
    lh = int(f.size * 1.16)
    y = int(H * .30)
    for l in lignes:
        d.text(((W - larg(l, f)) / 2, y), l, font=f, fill=ENCRE)
        y += lh
    g = F(SANS, 30, S_REG)
    sous = ("Le test de la Boussole émotionnelle : 14 émotions, une note sur 10 pour "
            "chacune, et une analyse personnalisée.")
    y += E(34)
    for l in couper(sous, g, W - E(190)):
        d.text(((W - larg(l, g)) / 2, y), l, font=g, fill=(110, 100, 92))
        y += int(g.size * 1.42)
    t = "boussole-emotionnelle.fr"
    fb = F(CONDENSE, 44, DEMI)
    w = larg(t, fb)
    d.rounded_rectangle([(W - w) / 2 - E(44), y + E(46), (W + w) / 2 + E(44), y + E(46) + E(86)],
                        radius=E(44), fill=TERRE)
    d.text(((W - w) / 2, y + E(68)), t, font=fb, fill=CREME)
    return img

def pied(img):
    d = ImageDraw.Draw(img)
    f = F(SANS, 24, S_DEMI)
    t = "boussole-emotionnelle.fr"
    d.text(((W - larg(t, f)) / 2, H - BAS + E(16)), t, font=f, fill=TERRE)

# ————— assemblage —————
def diapositives(post):
    slides = [slide_titre(post)]
    for s in post["slides"][1:]:
        slides.append(slide_scene(s))
    slides.append(slide_revelation(post))
    slides.append(slide_appel(post))
    return slides

def legende(post, n):
    txt = (f"=== LÉGENDE (TikTok et Instagram) ===\n{post['legende']}\n\n"
           f"Le test complet est sur boussole-emotionnelle.fr (lien en bio) : 14 émotions, "
           f"une note sur 10 pour chacune.\n\n"
           f"=== HASHTAGS ===\n{post['hashtags']}\n\n"
           f"=== CÔTÉ TIKTOK ===\nPublier en mode Photo (les {n} images du dossier tiktok/ "
           f"dans l'ordre), et choisir un son doux dans les tendances.\n\n"
           f"=== CÔTÉ INSTAGRAM ===\nPublier en carrousel avec les {n} images du dossier "
           f"instagram/ (format 4:5), dans l'ordre.\n\n"
           f"=== À DÉCLARER ===\nLes illustrations sont générées par IA : cocher « contenu "
           f"généré par IA » à la publication, comme le fait le compte de référence.\n")
    if post.get("lienGuide"):
        txt += f"\nArticle lié : boussole-emotionnelle.fr/guide/{post['lienGuide']}\n"
    return txt

def composer(post):
    dossier = os.path.join(SORTIE, f"{post['numero']:02d}-{post['slug']}")
    n = 0
    for nom in ("instagram", "tiktok"):
        format_actif(nom)
        sous = os.path.join(dossier, nom)
        os.makedirs(sous, exist_ok=True)
        slides = diapositives(post)
        n = len(slides)
        for i, im in enumerate(slides, 1):
            im.save(os.path.join(sous, f"{i:02d}.jpg"), quality=92)
    format_actif("instagram")
    open(os.path.join(dossier, "legende.txt"), "w", encoding="utf-8").write(legende(post, n))
    return dossier, n

def principal():
    data = json.load(open(os.path.join(BASE, "contenus.json"), encoding="utf-8"))
    posts = data["posts"]
    voulus = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if voulus:
        posts = [p for p in posts if p["numero"] in voulus]
    manquantes, total = [], 0
    for p in posts:
        for s in p["slides"]:
            nom = s.get("illustration") or ""
            if not nom or illustration(nom) is None:
                manquantes.append(nom or f"(sans identifiant) post {p['numero']:02d}")
        _, n = composer(p)
        total += n
        print(f"  {p['numero']:02d} · {p['titre'].replace('|', ' ')[:54]:56} {n} diapositives")
    print(f"\n{len(posts)} posts · {total} images composées dans sortie/")
    if manquantes:
        u = sorted(set(manquantes))
        print(f"⚠️  {len(u)} illustrations manquantes :")
        for m in u[:12]:
            print("   ·", m)
        if len(u) > 12:
            print(f"   … et {len(u) - 12} autres")
    else:
        print("✓ toutes les illustrations sont présentes")

if __name__ == "__main__":
    principal()
