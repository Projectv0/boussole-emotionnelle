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
_cache = {}
def illustration(nom):
    """Charge illustrations/<nom>.*, recadre pour remplir la page sans déformer."""
    cle = (nom, W, H)
    if cle in _cache:
        return _cache[cle]
    chemin = None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = os.path.join(ILLUS, nom + ext)
        if os.path.exists(p):
            chemin = p; break
    if chemin is None:
        _cache[cle] = None
        return None
    im = Image.open(chemin).convert("RGB")
    # recadrage « cover » : on remplit, on rogne ce qui dépasse, on garde le haut
    # de l'image car c'est là que se trouvent les visages.
    r = max(W / im.width, H / im.height)
    im = im.resize((max(W, int(im.width * r)), max(H, int(im.height * r))), Image.LANCZOS)
    x = (im.width - W) // 2
    y = min((im.height - H) // 2, int(im.height * .12))
    im = im.crop((x, y, x + W, y + H))
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

# Position de repli quand aucun visage n'a été détecté sur l'illustration.
TETES = {"gauche": (.27, .52), "droite": (.73, .52)}

def visages(nom):
    """Les visages de l'illustration, en pixels du cadre composé, triés de gauche à droite.

    Reprend exactement le recadrage « cover » de illustration() : sans ça les
    coordonnées seraient justes sur l'image d'origine et fausses sur la page.
    """
    bruts = VISAGES.get(nom or "", [])
    if not bruts:
        return []
    chemin = None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = os.path.join(ILLUS, nom + ext)
        if os.path.exists(p):
            chemin = p; break
    if chemin is None:
        return []
    with Image.open(chemin) as im:
        iw, ih = im.size
    r = max(W / iw, H / ih)
    nw, nh = max(W, int(iw * r)), max(H, int(ih * r))
    dx, dy = (nw - W) // 2, min((nh - H) // 2, int(nh * .12))
    out = [{"x": v["x"] * nw - dx, "y": v["y"] * nh - dy,
            "l": v["l"] * nw, "h": v["h"] * nh} for v in bruts]
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

def _chevauche(r, autre, marge=0):
    return (r[0] < autre[2] + marge and r[2] > autre[0] - marge
            and r[1] < autre[3] + marge and r[3] > autre[1] - marge)

def _boite_visage(v):
    """Le visage un peu élargi : cheveux au-dessus, menton en dessous."""
    return (v["x"] - v["l"] * .55, v["y"] - v["h"] * .75,
            v["x"] + v["l"] * .55, v["y"] + v["h"] * .70)

def poser_bulles(img, bulles, nom_illu, depuis=0):
    """Pose toutes les bulles d'une diapositive : têtes visées, et rien sur un visage."""
    faces = visages(nom_illu)
    tetes = attribuer_tetes(bulles, faces)
    boites = [_boite_visage(v) for v in faces]
    occupe = []
    for b, cible in zip(bulles, tetes):
        genre = b.get("type", "dit")
        g = mesurer_bulle(b["texte"], genre, b["zone"], depuis)
        # La zone fixe tombait parfois pile sur une figure. On glisse alors la bulle
        # à la verticale, d'abord vers le haut, jusqu'à dégager le visage.
        for dy in (0, -E(70), E(80), -E(150), E(170), -E(230), E(250)):
            y = max(depuis + E(10), min(g["y"] + dy, H - g["bh"] - E(120)))
            r = (g["x"], y, g["x"] + g["bw"], y + g["bh"])
            if not any(_chevauche(r, o, E(14)) for o in occupe + boites):
                g["y"] = y
                break
        r = (g["x"], g["y"], g["x"] + g["bw"], g["y"] + g["bh"])
        bulle(img, g, genre, cible, voisines=list(occupe))
        occupe.append(r)

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

def _avant_la_voisine(bx, by, ux, uy, longueur, voisines):
    """Raccourcit la queue pour qu'elle n'entre pas dans une bulle voisine.

    Deux bulles empilées du même côté visent la même tête : sans ça, la queue de
    celle du haut traversait celle du bas.
    """
    for x0, y0, x1, y1 in voisines:
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
            longueur = min(longueur, max(0, deb - E(18)))
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
    # elle tend vers la tête mais s'arrête avant : une queue qui touche le visage
    # se lit comme un trait de crayon en travers de la figure.
    # tete_h est la hauteur du visage seul : les cheveux montent bien au-dessus,
    # d'où la marge large. Trois ronds blancs posés sur une chevelure se voient
    # de loin, et c'est exactement ce qu'ils faisaient.
    longueur = max(E(30), min(dist - (tete_h * .95 + E(30)), E(130)))
    longueur = _avant_la_voisine(base_x, base_y, ux, uy, longueur, voisines)
    if longueur < E(14):
        return _texte_bulle(d, g)
    pointe_x, pointe_y = base_x + ux * longueur, base_y + uy * longueur

    if genre == "dit":
        demi = E(15)
        # la base est un segment posé sur le cadre, perpendiculaire à la direction
        px, py = -uy * demi, ux * demi
        d.polygon([(base_x + px, base_y + py), (base_x - px, base_y - py),
                   (pointe_x, pointe_y)], fill=BLANC, outline=ENCRE)
        # on recouvre le trait du cadre sous la base pour souder la queue à la bulle
        d.line([(base_x + px - ux * E(2), base_y + py - uy * E(2)),
                (base_x - px - ux * E(2), base_y - py - uy * E(2))], fill=BLANC, width=E(7))
    else:
        # Chaîne de ronds courte et orientée vers la tête : plus longue, elle descendait
        # sur les cheveux et les visages, et trois ronds blancs percés dans un crâne se
        # voient de loin.
        for t, r in ((.28, E(10)), (.60, E(7)), (.90, E(5))):
            cx = base_x + (pointe_x - base_x) * t
            cy = base_y + (pointe_y - base_y) * t
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANC, outline=ENCRE, width=E(3))

    _texte_bulle(d, g)

def _texte_bulle(d, g):
    ty = g["y"] + g["pad"] - E(3)
    for l in g["lignes"]:
        lx = (g["x"] + g["pad"] if g["align"] == "gauche"
              else g["x"] + g["bw"] - g["pad"] - larg(l, g["f"]))
        d.text((lx, ty), l, font=g["f"], fill=ENCRE)
        ty += g["lh"]

def narrateur(img, texte, bas=True):
    """La phrase du narrateur : capitales, bandeau sombre, posée en bas de l'image."""
    if not texte:
        return
    d = ImageDraw.Draw(img)
    f = F(CONDENSE, 34, LOURD)
    maxw = int(W * .74)
    # Un « / » dans le texte du narrateur marque une coupure voulue entre deux
    # phrases : il était rendu tel quel, au milieu du bandeau. On le traduit en
    # retour à la ligne, et couper() respecte déjà les sauts de ligne.
    texte = re.sub(r"\s*/\s*", "\n", texte)
    lignes = couper(texte.upper(), f, maxw)
    lh = int(f.size * 1.2)
    tw = max(larg(l, f) for l in lignes)
    pad = E(20)
    bw, bh = tw + pad * 2, len(lignes) * lh + pad * 2 - E(8)
    x = int((W - bw) / 2)
    y = H - BAS - bh if bas else int(H * .07)
    d.rounded_rectangle([x, y, x + bw, y + bh], radius=E(14), fill=ENCRE)
    ty = y + pad - E(4)
    for l in lignes:
        d.text((x + (bw - larg(l, f)) / 2, ty), l, font=f, fill=CREME)
        ty += lh

# ————— diapositives —————
def voile_haut(img, hauteur):
    """Dégradé crème du haut vers le bas, pour asseoir le titre sur l'illustration."""
    v = Image.new("L", (1, hauteur))
    for i in range(hauteur):
        t = i / max(1, hauteur - 1)
        v.putpixel((0, i), int(255 * max(0, 1 - t ** 1.6)))
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
    voile_haut(img, HAUT + lh * len(lignes) + E(90))
    d = ImageDraw.Draw(img)
    y = HAUT
    for i, l in enumerate(lignes):
        t = l.upper()
        col = ENCRE if i == 0 else TERRE if l.endswith("?") else ENCRE
        d.text(((W - larg(t, f)) / 2, y), t, font=f, fill=col)
        y += lh
    sous_titre = y + E(40)
    poser_bulles(img, post["slides"][0].get("bulles", []),
                 post["slides"][0].get("illustration"), depuis=sous_titre)
    narrateur(img, post["slides"][0].get("narrateur", ""))
    return img

def slide_scene(s):
    img = illustration(s["illustration"]) or fond_manquant(s["illustration"])
    img = img.copy()
    poser_bulles(img, s.get("bulles", []), s.get("illustration"))
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
