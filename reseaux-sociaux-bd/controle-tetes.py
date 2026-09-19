#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifie les positions de tête relevées à la main, en les montrant.

    python3 controle-tetes.py            toutes les positions manuelles
    python3 controle-tetes.py --toutes   y compris celles du détecteur

Écrit des planches de vignettes dans controle/ : chaque vignette est découpée
AUTOUR de la position déclarée, avec un cercle rouge en son centre. Si le cercle
n'est pas sur un visage, la position est fausse — c'est tout ce qu'il y a à voir.

Une position fausse ne se remarque pas dans le JSON, et pas davantage sur le
carrousel monté : la queue de bulle part simplement vers un coin de mur, et on
croit à un défaut de dessin. Six des vingt-quatre relevés faits à l'œil sans ce
contrôle étaient dans le vide.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assembleur as A
from PIL import Image, ImageDraw

SORTIE = os.path.join(A.BASE, "controle")
T = 220          # côté d'une vignette
PAR_RANG = 6


def positions(toutes):
    """Les têtes à contrôler : (image, index, position en fractions du panneau)."""
    out = []
    for nom, vs in sorted(A.TETES_MANUELLES.items()):
        out += [(nom, i, v, "relevé") for i, v in enumerate(vs)]
    if toutes:
        for nom, vs in sorted(A.VISAGES.items()):
            src = A.source(nom)
            if not vs or src is None:
                continue
            im, (cg, ch, _, _), (ow, oh) = src
            for i, v in enumerate(vs):
                out.append((nom, i, {"x": (v["x"] * ow - cg) / im.width,
                                     "y": (v["y"] * oh - ch) / im.height,
                                     "h": v["h"] * oh / im.height}, "détecté"))
    return out


def principal(toutes=False):
    A.format_actif("instagram")
    items = positions(toutes)
    os.makedirs(SORTIE, exist_ok=True)
    f = A.F(A.CONDENSE, 20, A.LOURD)
    par_planche = PAR_RANG * 3
    for k in range(0, len(items), par_planche):
        bloc = items[k:k + par_planche]
        rangs = (len(bloc) + PAR_RANG - 1) // PAR_RANG
        planche = Image.new("RGB", (T * PAR_RANG, T * rangs), (20, 18, 16))
        for j, (nom, idx, v, origine) in enumerate(bloc):
            src = A.source(nom)
            if src is None:
                continue
            im = src[0]
            cx, cy = v["x"] * im.width, v["y"] * im.height
            r = max(v["h"] * im.height, 90) * 1.3
            p = im.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r)))
            p = p.resize((T, T), Image.LANCZOS)
            d = ImageDraw.Draw(p)
            d.ellipse([T / 2 - 7, T / 2 - 7, T / 2 + 7, T / 2 + 7],
                      outline=(255, 40, 40), width=3)
            plusieurs = len(A.TETES_MANUELLES.get(nom, [])) > 1
            et = nom[:24] + ("·%d" % idx if plusieurs else "")
            d.rectangle([0, T - 26, A.larg(et, f) + 10, T], fill=(20, 18, 16))
            d.text((5, T - 25), et, font=f, fill=(255, 230, 120))
            planche.paste(p, ((j % PAR_RANG) * T, (j // PAR_RANG) * T))
        planche.save(os.path.join(SORTIE, "tetes-%02d.jpg" % (k // par_planche + 1)),
                     quality=90)
    print(f"{len(items)} positions · {(len(items) + par_planche - 1) // par_planche} "
          f"planches dans controle/ — le cercle rouge doit être sur un visage")


if __name__ == "__main__":
    principal("--toutes" in sys.argv)
