#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose les carrousels illustrés : illustrations Nano Banana + typographie.

    python3 assembleur.py            tous les posts
    python3 assembleur.py 3 7 12     seulement ces posts

Lit contenus.json, va chercher les images dans illustrations/, écrit dans sortie/.
Une illustration absente laisse un cadre pointillé avec son identifiant : on peut
composer un carrousel incomplet pour juger la mise en page avant de tout générer.
"""
import json, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageStat

BASE = os.path.dirname(os.path.abspath(__file__))
ILLUS = os.path.join(BASE, "illustrations")
SORTIE = os.path.join(BASE, "sortie")

W, H = 1080, 1350
MARGE = 78

CREME = (247, 243, 236)
ENCRE = (43, 38, 34)
TERRE = (184, 74, 49)
SAUGE = (63, 130, 113)
GRIS = (110, 103, 121)
TRAIT = (223, 214, 200)
BLANC = (253, 251, 246)

SERIF = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
SANS = "/System/Library/Fonts/Avenir Next.ttc"
IT, SB = 2, 4                 # Baskerville : italique, semi-gras
REG, MED, DEMI, HEAVY = 7, 5, 2, 8   # Avenir Next

_f = {}
def F(chemin, taille, idx):
    cle = (chemin, int(taille), idx)
    if cle not in _f:
        _f[cle] = ImageFont.truetype(chemin, int(taille), index=idx)
    return _f[cle]

_m = ImageDraw.Draw(Image.new("RGB", (8, 8)))
def larg(t, f):
    return _m.textlength(t, font=f)

def nbsp(t):
    """espaces insécables avant la ponctuation haute et dans les guillemets"""
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

def ecrire(d, t, x, y, f, col, maxw, il=1.3, align="centre"):
    for l in couper(t, f, maxw):
        w = larg(l, f)
        px = x - w / 2 if align == "centre" else (x - w if align == "droite" else x)
        d.text((px, y), l, font=f, fill=col)
        y += int(f.size * il)
    return y

# ————— fond —————
def fond():
    img = Image.new("RGB", (W, H), CREME)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for x, y, r, col, a in [(120, 150, 520, (184, 74, 49), .05),
                            (W - 80, 520, 560, (233, 182, 142), .07),
                            (W // 2, H - 90, 620, (63, 130, 113), .05)]:
        for i in range(22, 0, -1):
            rr = int(r * i / 22)
            d.ellipse([x - rr, y - rr, x + rr, y + rr],
                      fill=col + (int(255 * a * (1 - i / 22) * .55),))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

# ————— illustrations —————
def recaler_fond(im):
    """Aligne le fond clair de l'illustration sur le crème exact de la page.

    Nano Banana rend un crème légèrement plus froid d'une image à l'autre : sans ce
    recalage, chaque vignette se voit comme un rectangle posé sur la page au lieu de
    flotter. Le décalage est appliqué à pleine force sur les tons clairs et s'éteint
    sur les tons sombres, pour ne pas ternir les visages ni les traits de crayon.
    Aucun effet si les quatre coins ne s'accordent pas sur un fond uni et clair.
    """
    b = max(4, im.width // 20)
    coins = [im.crop((0, 0, b, b)), im.crop((im.width - b, 0, im.width, b)),
             im.crop((0, im.height - b, b, im.height)),
             im.crop((im.width - b, im.height - b, im.width, im.height))]
    moy = [ImageStat.Stat(c).mean for c in coins]
    for c in range(3):
        v = [m[c] for m in moy]
        if min(v) < 215 or max(v) - min(v) > 14:
            return im
    ecart = [CREME[c] - sum(m[c] for m in moy) / 4 for c in range(3)]
    if max(abs(e) for e in ecart) < 1.5:
        return im
    table = []
    for c in range(3):
        table += [max(0, min(255, round(i + ecart[c] * (i / 255) ** .5))) for i in range(256)]
    return im.point(table)

_cache = {}
def vignette(nom, taille, ronde=False):
    """charge illustrations/<nom>.png|jpg, recadre au carré, fond crème fondu"""
    cle = (nom, taille, ronde)
    if cle in _cache:
        return _cache[cle]
    chemin = None
    for ext in (".png", ".jpg", ".jpeg", ".webp"):
        p = os.path.join(ILLUS, nom + ext)
        if os.path.exists(p):
            chemin = p; break
    if chemin is None:
        _cache[cle] = None
        return None
    im = recaler_fond(Image.open(chemin).convert("RGB"))
    c = min(im.size)
    im = im.crop(((im.width - c) // 2, (im.height - c) // 2,
                  (im.width + c) // 2, (im.height + c) // 2)).resize((taille, taille), Image.LANCZOS)
    m = Image.new("L", (taille, taille), 255)
    if ronde:
        m = Image.new("L", (taille, taille), 0)
        ImageDraw.Draw(m).ellipse([0, 0, taille - 1, taille - 1], fill=255)
    else:
        # bords fondus dans le crème : la vignette flotte, comme la référence
        b = int(taille * .08)
        m = Image.new("L", (taille, taille), 0)
        ImageDraw.Draw(m).rounded_rectangle([b // 2, b // 2, taille - 1 - b // 2, taille - 1 - b // 2],
                                            radius=int(taille * .06), fill=255)
        m = m.filter(ImageFilter.GaussianBlur(b * .55))
    im.putalpha(m)
    _cache[cle] = im
    return im

def poser_illu(img, nom, x, y, taille, ronde=False):
    v = vignette(nom, taille, ronde)
    if v is not None:
        img.paste(v, (int(x), int(y)), v)
        return True
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([x, y, x + taille, y + taille], radius=int(taille * .06),
                        outline=(205, 193, 176), width=3)
    f = F(SANS, max(15, taille // 14), MED)
    ecrire(d, "à générer\n" + nom, x + taille / 2, y + taille / 2 - taille // 12, f, (170, 158, 145), taille - 20, 1.35)
    return False

def bulle(img, texte, x, y, maxw, pointe="gauche"):
    """bulle de dialogue dessinée proprement — jamais générée par l'IA"""
    d = ImageDraw.Draw(img)
    f = F(SANS, 27, MED)
    lignes = couper(texte, f, maxw - 44)
    w = max(larg(l, f) for l in lignes) + 44
    h = len(lignes) * 36 + 30
    d.rounded_rectangle([x, y, x + w, y + h], radius=20, fill=BLANC, outline=TRAIT, width=2)
    px = x + 32 if pointe == "gauche" else x + w - 52
    d.polygon([(px, y + h - 2), (px + 20, y + h - 2), (px + 6, y + h + 16)], fill=BLANC)
    d.line([(px, y + h - 1), (px + 6, y + h + 16), (px + 20, y + h - 1)], fill=TRAIT, width=2)
    yy = y + 15
    for l in lignes:
        d.text((x + 22, yy), l, font=f, fill=ENCRE)
        yy += 36
    return h

# ————— titre de couverture, mot-clé en terracotta —————
def mesurer_titre(titre, taille, maxw):
    f = F(SANS, taille, HEAVY)
    n, cour = 1, ""
    for mot in nbsp(titre).upper().split(" "):
        essai = (cour + " " + mot).strip()
        if cour and larg(essai, f) > maxw:
            n += 1; cour = mot
        else:
            cour = essai
    return n

def titre_couverture(img, titre, accents, y, taille=86, maxLignes=None):
    d = ImageDraw.Draw(img)
    if maxLignes:
        while taille > 46 and mesurer_titre(titre, taille, W - 2 * MARGE) > maxLignes:
            taille -= 4
    f = F(SANS, taille, HEAVY)
    mots_accent = set()
    for a in (accents or "").split():
        mots_accent.add(a.strip(",.;:!?«»").upper())
    maxw = W - 2 * MARGE
    lignes, cour = [], []
    for mot in nbsp(titre).upper().split(" "):
        essai = cour + [mot]
        if cour and larg(" ".join(essai), f) > maxw:
            lignes.append(cour); cour = [mot]
        else:
            cour = essai
    lignes.append(cour)
    for ligne in lignes:
        total = larg(" ".join(ligne), f)
        x = (W - total) / 2
        for mot in ligne:
            col = TERRE if mot.strip(",.;:!?«» ") in mots_accent else ENCRE
            d.text((x, y), mot, font=f, fill=col)
            x += larg(mot + " ", f)
        y += int(taille * 1.12)
    return y

# ————— gabarits —————
def slide_couverture(post):
    img = fond()
    d = ImageDraw.Draw(img)
    items = post["slides"][0]["items"] if post["slides"] and post["slides"][0]["gabarit"] == "couverture" else []
    n = max(1, min(4, len(items)))
    y = titre_couverture(img, post["titre"], post.get("titreAccent", ""), 138, 88, maxLignes=3)
    if post.get("sousTitre"):
        y = ecrire(d, post["sousTitre"], W / 2, y + 22, F(SANS, 37, MED), GRIS, W - 2 * MARGE - 40, 1.32)
    dispo = H - y - 130
    if n <= 2:
        t = int(min(dispo - 30, (W - 2 * MARGE - 40) / max(1, n)))
        ecart = 40
        x0 = (W - (t * n + ecart * (n - 1))) / 2
        y0 = y + (dispo - t) / 2
        for k, it in enumerate(items[:n]):
            poser_illu(img, it.get("illustration", f"p{post['numero']:02d}-c{k+1}"), x0 + k * (t + ecart), y0, t)
    else:
        cols = 2
        t = int(min((dispo - 26) / 2, (W - 2 * MARGE - 34) / 2))
        ecart = 34
        nb = min(4, n)
        rangs = (nb + 1) // 2
        y0 = y + (dispo - (t * rangs + 26 * (rangs - 1))) / 2
        for k, it in enumerate(items[:4]):
            r, c = divmod(k, cols)
            surRang = min(cols, nb - r * cols)          # dernière rangée parfois incomplète
            x0 = (W - (t * surRang + ecart * (surRang - 1))) / 2
            poser_illu(img, it.get("illustration", f"p{post['numero']:02d}-c{k+1}"),
                       x0 + c * (t + ecart), y0 + r * (t + 26), t)
    pied(img)
    return img

def slide_grille(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 62, maxLignes=2) + 22
    items = s["items"][:6]
    cols = 2
    rangs = (len(items) + cols - 1) // cols
    dispo = H - y - 150
    hcase = dispo / rangs
    t = int(min(hcase * .52, (W - 2 * MARGE - 60) / cols * .78))
    for k, it in enumerate(items):
        r, c = divmod(k, cols)
        cx = MARGE + (W - 2 * MARGE) * (c + .5) / cols
        cy = y + r * hcase
        poser_illu(img, it.get("illustration", ""), cx - t / 2, cy, t)
        yy = cy + t + 14
        yy = ecrire(d, it["etiquette"], cx, yy, F(SANS, 38, DEMI), TERRE, (W - 2 * MARGE) / cols - 20, 1.2)
        ecrire(d, it["texte"], cx, yy + 6, F(SANS, 30, REG), GRIS, (W - 2 * MARGE) / cols - 16, 1.34)
    pied(img)
    return img

def slide_liste(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 62, maxLignes=2) + 30
    items = s["items"][:5]
    dispo = H - y - 150
    hcase = min(dispo / len(items), 300)
    y += min((dispo - hcase * len(items)) / 2, 70)
    t = int(min(hcase * .88, 255))
    for it in items:
        poser_illu(img, it.get("illustration", ""), MARGE, y + (hcase - t) / 2, t)
        xt = MARGE + t + 38
        maxw = W - MARGE - xt
        bloc = 40 * 1.18 + 32 * 1.34 * len(couper(it["texte"], F(SANS, 32, REG), maxw))
        yy = y + (hcase - bloc) / 2
        yy = ecrire(d, it["etiquette"], xt, yy, F(SANS, 40, DEMI), TERRE, maxw, 1.18, "gauche")
        ecrire(d, it["texte"], xt, yy + 6, F(SANS, 32, REG), GRIS, maxw, 1.34, "gauche")
        y += hcase
    pied(img)
    return img

def slide_duo(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 60, maxLignes=2) + 24
    g, dr = (s["items"] + s["items"])[:2]
    colw = (W - 2 * MARGE - 46) / 2
    dispo = H - y - 140
    fe, ft = F(SANS, 44, HEAVY), F(SANS, 32, REG)
    nEtq = max(len(couper(it["etiquette"], fe, colw)) for it in (g, dr))
    nTxt = max(len(couper(it["texte"], ft, colw - 10)) for it in (g, dr))
    hTexte = nEtq * 44 * 1.18 + 16 + 36 + nTxt * 32 * 1.4
    t = int(min(colw * .96, dispo - hTexte))
    y0 = y + (dispo - (hTexte + t)) / 2
    d.line([(W / 2, y0), (W / 2, y0 + hTexte + t)], fill=TRAIT, width=2)
    for k, it in enumerate((g, dr)):
        cx = MARGE + colw / 2 + k * (colw + 46)
        yy = ecrire(d, it["etiquette"], cx, y0, fe, TERRE if k == 0 else SAUGE, colw, 1.18)
        yy = y0 + nEtq * 44 * 1.18
        poser_illu(img, it.get("illustration", ""), cx - t / 2, yy + 16, t)
        ecrire(d, it["texte"], cx, yy + t + 36, ft, GRIS, colw - 10, 1.4)
    pied(img)
    return img

def slide_avant_apres(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 60, maxLignes=2) + 26
    items = s["items"][:2]
    dispo = H - y - 150
    hcase = min(dispo / max(1, len(items)), 430)
    y += min((dispo - hcase * len(items)) / 2, 70)
    for k, it in enumerate(items):
        t = int(min(hcase * .72, 290))
        yy = y + k * hcase
        poser_illu(img, it.get("illustration", ""), MARGE, yy + (hcase - t) / 2, t)
        xt = MARGE + t + 40
        maxw = W - MARGE - xt
        f = F(SANS, 26, DEMI)
        etq = (it["etiquette"] or "").upper()
        d.rounded_rectangle([xt, yy + (hcase - t) / 2, xt + larg(etq, f) + 34, yy + (hcase - t) / 2 + 46],
                            radius=23, fill=(TERRE if k == 0 else SAUGE))
        d.text((xt + 17, yy + (hcase - t) / 2 + 10), etq, font=f, fill=BLANC)
        ecrire(d, it["texte"], xt, yy + (hcase - t) / 2 + 68, F(SANS, 34, REG), ENCRE, maxw, 1.38, "gauche")
        if it.get("bulle"):
            bulle(img, it["bulle"], xt, yy + (hcase - t) / 2 + 68 + 34 * 1.38 * len(couper(it["texte"], F(SANS, 34, REG), maxw)) + 16, min(maxw, 380))
    pied(img)
    return img

def slide_etapes(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 60, maxLignes=2) + 30
    items = s["items"][:4]
    dispo = H - y - 150
    hcase = min(dispo / len(items), 330)
    y += min((dispo - hcase * len(items)) / 2, 70)
    t = int(min(hcase * .82, 250))
    for k, it in enumerate(items):
        yy = y + k * hcase + (hcase - t) / 2 - 10
        dia = 60
        d.ellipse([MARGE, yy + t / 2 - dia / 2, MARGE + dia, yy + t / 2 + dia / 2], fill=(236, 214, 205))
        num = str(k + 1)
        fn = F(SERIF, 36, SB)
        d.text((MARGE + (dia - larg(num, fn)) / 2, yy + t / 2 - 24), num, font=fn, fill=TERRE)
        xi = MARGE + dia + 24
        poser_illu(img, it.get("illustration", ""), xi, yy, t)
        xt = xi + t + 30
        maxw = W - MARGE - xt
        fe, ft = F(SANS, 38, DEMI), F(SANS, 31, REG)
        hbloc = 38 * 1.2 * len(couper(it["etiquette"], fe, maxw)) + 6 + 31 * 1.36 * len(couper(it["texte"], ft, maxw))
        yt = yy + (t - hbloc) / 2
        yt = ecrire(d, it["etiquette"], xt, yt, fe, ENCRE, maxw, 1.2, "gauche")
        ecrire(d, it["texte"], xt, yt + 6, ft, GRIS, maxw, 1.36, "gauche")
        if k < len(items) - 1:
            d.line([(MARGE, y + (k + 1) * hcase - 16), (W - MARGE, y + (k + 1) * hcase - 16)], fill=TRAIT, width=1)
    pied(img)
    return img

def slide_remplace(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 128
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 60, maxLignes=2) + 30
    items = s["items"][:3]
    dispo = H - y - 150
    hcase = min(dispo / len(items), 380)
    y += max(0, (dispo - hcase * len(items)) / 2)
    fav, fap, fno = F(SERIF, 34, IT), F(SERIF, 37, SB), F(SANS, 26, REG)
    for k, it in enumerate(items):
        yy = y + k * hcase
        t = int(min(hcase * .72, 250))
        poser_illu(img, it.get("illustration", ""), W - MARGE - t, yy + (hcase - t) / 2 - 8, t)
        maxw = W - 2 * MARGE - t - 44
        note = (it.get("note") or "").strip()
        nav = len(couper("« " + it["etiquette"] + " »", fav, maxw))
        nap = len(couper("« " + it["texte"] + " »", fap, maxw))
        nno = len(couper(note, fno, maxw)) if note else 0
        hbloc = 30 + nav * 34 * 1.26 + 44 + nap * 37 * 1.26 + (14 + nno * 26 * 1.34 if note else 0)
        yt = yy + (hcase - hbloc) / 2
        d.text((MARGE, yt), "AU LIEU DE", font=F(SANS, 23, DEMI), fill=GRIS)
        yt = ecrire(d, "« " + it["etiquette"] + " »", MARGE, yt + 30, fav, GRIS, maxw, 1.26, "gauche")
        d.text((MARGE, yt + 14), "DIS PLUTÔT", font=F(SANS, 23, DEMI), fill=TERRE)
        yt = ecrire(d, "« " + it["texte"] + " »", MARGE, yt + 44, fap, ENCRE, maxw, 1.26, "gauche")
        if note:
            ecrire(d, note, MARGE, yt + 14, fno, GRIS, maxw, 1.34, "gauche")
        if k < len(items) - 1:
            d.line([(MARGE, yy + hcase - 16), (W - MARGE, yy + hcase - 16)], fill=TRAIT, width=1)
    pied(img)
    return img

def slide_grand(post, s):
    img = fond()
    d = ImageDraw.Draw(img)
    it = s["items"][0]
    y = 130
    if s.get("titre"):
        y = titre_couverture(img, s["titre"], post.get("titreAccent", ""), y, 62, maxLignes=2) + 20
    t = 560
    poser_illu(img, it.get("illustration", ""), (W - t) / 2, y, t)
    yy = y + t + 34
    yy = ecrire(d, it["etiquette"], W / 2, yy, F(SANS, 46, DEMI), TERRE, W - 2 * MARGE, 1.2)
    yy = ecrire(d, it["texte"], W / 2, yy + 12, F(SANS, 34, REG), GRIS, W - 2 * MARGE - 40, 1.4)
    if it.get("bulle"):
        bulle(img, it["bulle"], MARGE + 40, yy + 24, 420)
    pied(img)
    return img

def slide_phrase(post):
    img = fond()
    d = ImageDraw.Draw(img)
    f = F(SERIF, 72, IT)
    lignes = couper(post["phraseFinale"], f, W - 2 * MARGE - 40)
    y = (H - len(lignes) * 72 * 1.3) / 2 - 40
    for l in lignes:
        d.text(((W - larg(l, f)) / 2, y), l, font=f, fill=TERRE)
        y += int(72 * 1.3)
    d.line([(W / 2 - 60, y + 30), (W / 2 + 60, y + 30)], fill=TRAIT, width=2)
    pied(img)
    return img

def slide_appel(post):
    img = fond()
    d = ImageDraw.Draw(img)
    y = 330
    f = F(SERIF, 96, IT)
    d.text(((W - larg("Et toi ?", f)) / 2, y), "Et toi ?", font=f, fill=ENCRE)
    y += 150
    y = ecrire(d, post["question"], W / 2, y, F(SANS, 46, DEMI), ENCRE, W - 2 * MARGE - 40, 1.32)
    y = ecrire(d, "Le test de la Boussole émotionnelle : 14 émotions, une note sur 10 pour chacune, "
                  "et une analyse personnalisée à la fin.",
               W / 2, y + 34, F(SANS, 33, REG), GRIS, W - 2 * MARGE - 60, 1.42)
    t = "boussole-emotionnelle.fr"
    f = F(SANS, 44, DEMI)
    w = larg(t, f)
    d.rounded_rectangle([(W - w) / 2 - 54, y + 60, (W + w) / 2 + 54, y + 156], radius=48, fill=SAUGE)
    d.text(((W - w) / 2, y + 87), t, font=f, fill=BLANC)
    return img

def pied(img):
    d = ImageDraw.Draw(img)
    f = F(SANS, 26, MED)
    t = "boussole-emotionnelle.fr"
    d.text(((W - larg(t, f)) / 2, H - 78), t, font=f, fill=SAUGE)

GABARITS = {
    "grille": slide_grille, "liste": slide_liste, "duo": slide_duo,
    "avant-apres": slide_avant_apres, "etapes": slide_etapes,
    "remplace": slide_remplace, "grand": slide_grand,
}

def composer(post):
    dossier = os.path.join(SORTIE, f"{post['numero']:02d}-{post['slug']}")
    os.makedirs(dossier, exist_ok=True)
    slides = [slide_couverture(post)]
    for s in post["slides"]:
        if s["gabarit"] == "couverture":
            continue
        slides.append(GABARITS.get(s["gabarit"], slide_grand)(post, s))
    slides.append(slide_phrase(post))
    slides.append(slide_appel(post))
    for i, im in enumerate(slides, 1):
        im.save(os.path.join(dossier, f"{i:02d}.jpg"), quality=92)
    # légende
    txt = (f"=== LÉGENDE ===\n{post['legende']}\n\n"
           f"Le test complet est sur boussole-emotionnelle.fr (lien en bio) : 14 émotions, "
           f"une note sur 10 pour chacune.\n\n"
           f"=== HASHTAGS ===\n{post['hashtags']}\n\n"
           f"=== PUBLIER ===\nInstagram : carrousel, les {len(slides)} images dans l’ordre.\n"
           f"TikTok : mode Photo, mêmes images, ajouter un son doux en tendance.\n")
    if post.get("lienGuide"):
        txt += f"\nArticle lié : boussole-emotionnelle.fr/guide/{post['lienGuide']}\n"
    open(os.path.join(dossier, "legende.txt"), "w", encoding="utf-8").write(txt)
    return dossier, len(slides)

def principal():
    posts = json.load(open(os.path.join(BASE, "contenus.json"), encoding="utf-8"))["posts"]
    voulus = [int(a) for a in sys.argv[1:] if a.isdigit()]
    if voulus:
        posts = [p for p in posts if p["numero"] in voulus]
    manquantes, total = [], 0
    for p in posts:
        for s in p["slides"]:
            for it in s["items"]:
                nom = it.get("illustration")
                if nom and vignette(nom, 64) is None:
                    manquantes.append(nom)
        dossier, n = composer(p)
        total += n
        print(f"  {p['numero']:02d} · {p['titre'][:52]:54} {n} diapositives")
    print(f"\n{len(posts)} posts · {total} images composées dans sortie/")
    if manquantes:
        u = sorted(set(manquantes))
        print(f"⚠️  {len(u)} illustrations manquantes (cadres pointillés en attendant) :")
        for m in u[:12]:
            print("   ·", m)
        if len(u) > 12:
            print(f"   … et {len(u) - 12} autres")
    else:
        print("✓ toutes les illustrations sont présentes")

if __name__ == "__main__":
    principal()
