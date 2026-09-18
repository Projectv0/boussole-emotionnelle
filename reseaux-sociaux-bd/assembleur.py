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
import json, os, re, sys
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

def bulle(img, texte, zone, genre, depuis=0):
    """Dessine une bulle de dialogue ou de pensée, avec sa queue vers le centre bas.

    Le texte est écrit ici, en français, par l'assembleur : jamais par le générateur
    d'images, qui déforme systématiquement les mots.
    """
    d = ImageDraw.Draw(img)
    fx, fy, align = ZONES.get(zone, ZONES["hg"])
    f = F(CONDENSE, 38, DEMI)
    maxw = int(W * .40)
    lignes = couper(texte.upper() if genre == "dit" else texte, f, maxw)
    lh = int(f.size * 1.16)
    tw = max(larg(l, f) for l in lignes)
    pad = E(22)
    bw, bh = tw + pad * 2, len(lignes) * lh + pad * 2 - E(6)

    x = int(W * fx) if align == "gauche" else int(W * fx) - bw
    # « depuis » réserve le haut de la page : sur la diapositive de titre, les bulles
    # se posaient par-dessus le titre. Les zones glissent alors sous lui.
    utile = H - depuis
    y = depuis + int(utile * fy)
    x = max(E(18), min(x, W - bw - E(18)))
    y = max(depuis + E(10), min(y, H - bh - E(120)))

    # ombre portée douce, pour détacher la bulle de l'illustration
    ombre = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ombre).rounded_rectangle([x + 5, y + 6, x + bw + 5, y + bh + 6],
                                            radius=E(26), fill=(26, 22, 20, 60))
    img.paste(Image.alpha_composite(img.convert("RGBA"), ombre.filter(
        ImageFilter.GaussianBlur(7))).convert("RGB"), (0, 0))
    d = ImageDraw.Draw(img)

    d.rounded_rectangle([x, y, x + bw, y + bh], radius=E(26), fill=BLANC,
                        outline=ENCRE, width=E(4))

    # la queue part vers le bas, du côté du centre de l'image
    qx = x + bw - E(52) if align == "gauche" else x + E(52)
    if genre == "dit":
        vers = qx + (E(34) if align == "gauche" else -E(34))
        d.polygon([(qx, y + bh - E(4)), (qx + E(30), y + bh - E(4)), (vers, y + bh + E(34))],
                  fill=BLANC, outline=ENCRE)
        d.line([(qx + 2, y + bh - E(3)), (qx + E(28), y + bh - E(3))], fill=BLANC, width=E(5))
    else:
        # Chaîne de ronds volontairement courte : plus longue, elle descendait sur les
        # cheveux et les visages quand le générateur plaçait une tête plus haut que prévu,
        # et trois ronds blancs percés dans un crâne se voient de loin.
        for i, (dx, r) in enumerate(((0, E(10)), (E(18), E(7)), (E(32), E(5)))):
            cx = qx + (dx if align == "gauche" else -dx)
            cy = y + bh + E(11) + i * E(10)
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLANC, outline=ENCRE, width=E(3))

    ty = y + pad - E(3)
    for l in lignes:
        lx = x + pad if align == "gauche" else x + bw - pad - larg(l, f)
        d.text((lx, ty), l, font=f, fill=ENCRE)
        ty += lh

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
    for b in post["slides"][0].get("bulles", []):
        bulle(img, b["texte"], b["zone"], b.get("type", "dit"), depuis=sous_titre)
    narrateur(img, post["slides"][0].get("narrateur", ""))
    return img

def slide_scene(s):
    img = illustration(s["illustration"]) or fond_manquant(s["illustration"])
    img = img.copy()
    for b in s.get("bulles", []):
        bulle(img, b["texte"], b["zone"], b.get("type", "dit"))
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
