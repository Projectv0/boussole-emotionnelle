#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les carrousels TikTok + Instagram de la Boussole émotionnelle.

    python3 generateur.py

Tout part de contenus.py (les 13 semaines) : modifier les textes là-bas,
relancer, et les dossiers semaine-XX sont entièrement recréés.
Chaque post produit : tiktok/ (1080×1920), instagram/ (1080×1350), legende.txt.
"""
import json, os, shutil, sys
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from contenus import SEMAINES

ASSETS = os.path.join(BASE, "assets")
EMOS = json.load(open(os.path.join(ASSETS, "emotions.json"), encoding="utf-8"))

SERIF = "/System/Library/Fonts/Supplemental/Baskerville.ttc"
SANS  = "/System/Library/Fonts/Avenir Next.ttc"
IT, SB = 2, 4          # Baskerville : Italique (affichage), SemiBold
REG, MED, DEMI = 7, 5, 2   # Avenir Next : Regular, Medium, Demi Bold

CREME = (248, 244, 236); ENCRE = (45, 40, 51); DOUX = (74, 68, 83)
MUTED = (110, 103, 121); SAGE = (63, 130, 113); LAV = (123, 111, 180)
BLANC = (253, 251, 246)

FORMATS = {
    "tiktok":    dict(W=1080, H=1920, haut=215, bas=265, marge=84, ech=1.00),
    "instagram": dict(W=1080, H=1350, haut=105, bas=150, marge=84, ech=0.86),
}

SERIES = {
    "comprendre":  dict(jour="lundi",    etiq="COMPRENDRE · ÉPISODE {n}/13"),
    "distinction": dict(jour="mercredi", etiq="DEUX MOTS, DEUX CHOSES · {n}/13"),
    "pratique":    dict(jour="vendredi", etiq="LA PRATIQUE DU VENDREDI · {n}/13"),
}

_fonts, _vign = {}, {}
def F(chemin, taille, idx):
    cle = (chemin, int(taille), idx)
    if cle not in _fonts:
        _fonts[cle] = ImageFont.truetype(chemin, int(taille), index=idx)
    return _fonts[cle]

def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def accent_de(post):
    ids = post.get("emos") or ([post["emo"]] if post.get("emo") else [])
    return hexrgb(EMOS[ids[0]]["color"]) if ids else SAGE

def vignette(id_, taille):
    cle = (id_, taille)
    if cle not in _vign:
        img = Image.open(os.path.join(ASSETS, f"{id_}.png")).convert("RGB")
        img = img.resize((taille, taille), Image.LANCZOS)
        m = Image.new("L", (taille, taille), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, taille - 1, taille - 1],
                                            radius=int(taille * .28), fill=255)
        img.putalpha(m)
        _vign[cle] = img
    return _vign[cle]

def fond(fmt, accent):
    W, H = fmt["W"], fmt["H"]
    img = Image.new("RGB", (W, H), CREME)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    halos = [(int(W * .12), int(H * .10), int(H * .38), accent, .13),
             (int(W * .95), int(H * .30), int(H * .40), (233, 182, 142), .17),
             (int(W * .50), int(H * .94), int(H * .42), SAGE, .12)]
    for x, y, r, col, a in halos:
        for i in range(26, 0, -1):
            rr = int(r * i / 26)
            d.ellipse([x - rr, y - rr, x + rr, y + rr],
                      fill=tuple(col) + (int(255 * a * (1 - i / 26) * .5),))
    return Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")

_mesure = ImageDraw.Draw(Image.new("RGB", (8, 8)))
def envelopper(txt, fnt, maxw):
    lignes = []
    for para in txt.split("\n"):
        cour = ""
        for mot in para.split(" "):
            t = (cour + " " + mot).strip()
            if not cour or _mesure.textlength(t, font=fnt) <= maxw:
                cour = t
            else:
                lignes.append(cour); cour = mot
        lignes.append(cour)
    return lignes

def nbsp(t):
    """espace insécable avant la ponctuation haute — jamais de « ? » orphelin"""
    for p in ("?", "!", ":", ";", "»"):
        t = t.replace(" " + p, " " + p)
    return t.replace("« ", "« ")

# ————— pose des blocs : une passe de mesure, une passe de dessin —————
def poser(fmt, blocs, f, img=None):
    W, ech = fmt["W"], fmt["ech"] * f
    d = ImageDraw.Draw(img) if img is not None else _mesure
    maxw_def = W - 2 * fmt["marge"]
    y = 0
    for b in blocs:
        typ, p = b[0], b[1]
        if typ == "espace":
            y += int(p["h"] * ech)
        elif typ == "vign":
            t = int(p["taille"] * ech)
            ids = p["ids"]; ecart = int(30 * ech)
            larg = t * len(ids) + ecart * (len(ids) - 1)
            x0 = (W - larg) // 2
            if img is not None:
                for k, idv in enumerate(ids):
                    v = vignette(idv, t)
                    img.paste(v, (x0 + k * (t + ecart), y), v)
            y += t
        elif typ in ("serif", "sans"):
            chemin = SERIF if typ == "serif" else SANS
            fnt = F(chemin, p["taille"] * ech, p["idx"])
            maxw = int(p.get("maxw", maxw_def))
            lh = p["taille"] * ech * p.get("il", 1.24)
            for l in envelopper(nbsp(p["txt"]), fnt, maxw):
                if img is not None:
                    w = d.textlength(l, font=fnt)
                    d.text(((W - w) / 2, y), l, font=fnt, fill=p["col"])
                y += int(lh)
        elif typ == "etape":
            dia = int(78 * ech)
            xC = fmt["marge"] + int(6 * ech)
            xT = xC + dia + int(34 * ech)
            maxw = W - fmt["marge"] - xT
            fT = F(SANS, 45 * ech, DEMI); fB = F(SANS, 41 * ech, REG)
            lT = envelopper(nbsp(p["gras"]), fT, maxw)
            lB = envelopper(nbsp(p["txt"]), fB, maxw)
            hT, hB = int(45 * ech * 1.22), int(41 * ech * 1.3)
            haut_bloc = len(lT) * hT + len(lB) * hB
            if img is not None:
                acc = p["accent"]
                pastel = tuple(int(c + (255 - c) * .82) for c in acc)
                d.ellipse([xC, y, xC + dia, y + dia], fill=pastel)
                fN = F(SERIF, 44 * ech, SB)
                num = str(p["n"])
                wN = d.textlength(num, font=fN)
                d.text((xC + (dia - wN) / 2, y + dia * .16), num, font=fN, fill=acc)
                yy = y
                for l in lT:
                    d.text((xT, yy), l, font=fT, fill=ENCRE); yy += hT
                for l in lB:
                    d.text((xT, yy), l, font=fB, fill=MUTED); yy += hB
            y += max(haut_bloc, dia) + int(36 * ech)
        elif typ == "pill":
            fnt = F(SANS, 50 * ech, DEMI)
            w = _mesure.textlength(p["txt"], font=fnt)
            h = int(112 * ech)
            if img is not None:
                x0, x1 = (W - w) / 2 - 62 * ech, (W + w) / 2 + 62 * ech
                d.rounded_rectangle([x0, y, x1, y + h], radius=h / 2, fill=SAGE)
                d.text(((W - w) / 2, y + int(28 * ech)), p["txt"], font=fnt, fill=BLANC)
            y += h
    return y

def rendre(fmt_nom, blocs, accent, chemin, avec_marque=True):
    fmt = FORMATS[fmt_nom]
    zone = fmt["H"] - fmt["haut"] - fmt["bas"]
    f = 1.0
    while f > 0.62:
        h = poser(fmt, blocs, f)
        if h <= zone:
            break
        f = round(f - 0.04, 2)
    y0 = fmt["haut"] + max(0, (zone - h) // 2)
    img = fond(fmt, accent)
    calque = Image.new("RGBA", (fmt["W"], fmt["H"]), (0, 0, 0, 0))
    poser(fmt, blocs, f, calque)
    img.paste(calque, (0, y0), calque)
    if avec_marque:
        d = ImageDraw.Draw(img)
        fm = F(SANS, 33 * fmt["ech"], MED)
        t = "boussole-emotionnelle.fr"
        w = d.textlength(t, font=fm)
        d.text(((fmt["W"] - w) / 2, fmt["H"] - fmt["bas"] + int(52 * fmt["ech"])),
               t, font=fm, fill=SAGE)
    img.save(chemin, quality=91)
    return f

# ————— assemblage des diapositives d'un post —————
def diapos_du(post):
    s = SERIES[post["serie"]]
    acc = accent_de(post)
    ids = post.get("emos") or ([post["emo"]] if post.get("emo") else [])
    out = []

    couv = [("sans", dict(txt=s["etiq"].format(n=post["n"]), taille=33, idx=DEMI, col=acc, il=1.1)),
            ("espace", dict(h=56))]
    if ids:
        couv.append(("vign", dict(ids=ids, taille=300 if len(ids) == 1 else 240)))
        couv.append(("espace", dict(h=64)))
    couv += [("serif", dict(txt=post["titre"], taille=118, idx=IT, col=ENCRE, il=1.08, maxw=880)),
             ("espace", dict(h=36)),
             ("sans", dict(txt=post["sous"], taille=46, idx=MED, col=MUTED, maxw=800, il=1.3))]
    out.append(couv)

    for typ, p in post["slides"]:
        if typ == "texte":
            bl = [("sans", dict(txt=p["k"], taille=33, idx=DEMI, col=p.get("accent", acc), il=1.1)),
                  ("espace", dict(h=44))]
            if p.get("vign"):
                bl += [("vign", dict(ids=[p["vign"]], taille=210)), ("espace", dict(h=48))]
            bl += [("serif", dict(txt=p["t"], taille=86, idx=IT, col=ENCRE, il=1.1, maxw=860)),
                   ("espace", dict(h=52)),
                   ("sans", dict(txt=p["c"], taille=46, idx=REG, col=DOUX, maxw=830, il=1.42))]
            out.append(bl)
        elif typ == "duo":
            bl = [("serif", dict(txt=p["t"], taille=88, idx=IT, col=ENCRE, il=1.1, maxw=860)),
                  ("espace", dict(h=76)),
                  ("sans", dict(txt=p["a"], taille=53, idx=DEMI, col=SAGE, maxw=780, il=1.3)),
                  ("espace", dict(h=44)),
                  ("sans", dict(txt=p["b"], taille=53, idx=DEMI, col=LAV, maxw=780, il=1.3)),
                  ("espace", dict(h=76)),
                  ("sans", dict(txt=p["note"], taille=44, idx=REG, col=MUTED, maxw=820, il=1.4))]
            out.append(bl)
        elif typ == "etapes":
            bl = [("sans", dict(txt=p["k"], taille=33, idx=DEMI, col=acc, il=1.1)),
                  ("espace", dict(h=40)),
                  ("serif", dict(txt=p["t"], taille=82, idx=IT, col=ENCRE, il=1.1, maxw=860)),
                  ("espace", dict(h=64))]
            for i, (gras, txt) in enumerate(p["e"]):
                bl.append(("etape", dict(n=i + 1, gras=gras, txt=txt, accent=acc)))
            out.append(bl)

    out.append([
        ("serif", dict(txt="Et toi ?", taille=124, idx=IT, col=ENCRE, il=1.05)),
        ("espace", dict(h=44)),
        ("sans", dict(txt=post["question"], taille=50, idx=DEMI, col=ENCRE, maxw=800, il=1.32)),
        ("espace", dict(h=52)),
        ("sans", dict(txt="Le test de la Boussole émotionnelle : 14 émotions passées en revue, "
                          "une note sur 10 pour chacune, une analyse personnalisée. "
                          "Rien n’est enregistré.", taille=43, idx=REG, col=MUTED, maxw=810, il=1.42)),
        ("espace", dict(h=88)),
        ("pill", dict(txt="boussole-emotionnelle.fr")),
    ])
    return out

LEGENDE_PIED = ("\n\nLe test complet est sur boussole-emotionnelle.fr (lien en bio) : "
                "14 émotions, une note sur 10 pour chacune. Rien n'est enregistré.")

def ecrire_legende(post, dossier):
    s = SERIES[post["serie"]]
    tags = post["tags"]
    txt = f"""=== LÉGENDE (TikTok et Instagram) ===
{post['legende']}{LEGENDE_PIED}

=== HASHTAGS ===
{tags}

=== CÔTÉ TIKTOK ===
Publier en mode Photo (les {2 + len(post['slides'])} images dans l'ordre), ajouter #apprendresurtiktok,
et choisir un son doux dans les tendances (lo-fi, piano, « calm aesthetic »).

=== CÔTÉ INSTAGRAM ===
Publier en carrousel avec les images du dossier instagram/ (format 4:5).
Répondre aux premiers commentaires dans la demi-heure aide beaucoup la portée.
"""
    open(os.path.join(dossier, "legende.txt"), "w", encoding="utf-8").write(txt)

def principal():
    total, avertis = 0, []
    for sem in sorted(os.listdir(BASE)):
        if sem.startswith("semaine-"):
            shutil.rmtree(os.path.join(BASE, sem))
    for si, semaine in enumerate(SEMAINES, 1):
        for post in semaine:
            s = SERIES[post["serie"]]
            dossier = os.path.join(BASE, f"semaine-{si:02d}",
                                   f"{s['jour']}-{post['slug']}")
            for fmt_nom in FORMATS:
                os.makedirs(os.path.join(dossier, fmt_nom), exist_ok=True)
            diapos = diapos_du(post)
            acc = accent_de(post)
            for di, blocs in enumerate(diapos, 1):
                for fmt_nom in FORMATS:
                    chemin = os.path.join(dossier, fmt_nom, f"{di:02d}.jpg")
                    marque = not any(bl[0] == "pill" for bl in blocs)
                    f = rendre(fmt_nom, blocs, acc, chemin, avec_marque=marque)
                    total += 1
                    if f < 0.80:
                        avertis.append(f"{sem_id(si, post)} diapo {di} ({fmt_nom}) réduit à {f}")
            ecrire_legende(post, dossier)
    print(f"{total} images générées pour {sum(len(s) for s in SEMAINES)} posts")
    if avertis:
        print("⚠️ textes trop longs :")
        for a in avertis:
            print("  ·", a)
    else:
        print("aucun texte n'a dû être réduit au-delà de 20 % ✓")

def sem_id(si, post):
    return f"s{si:02d}/{SERIES[post['serie']]['jour']}-{post['slug']}"

if __name__ == "__main__":
    principal()
