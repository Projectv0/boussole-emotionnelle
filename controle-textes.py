#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contrôle mécanique de tous les textes publiés, avant de composer les images.

    python3 controle-textes.py

Trois choses qu'une relecture humaine ne voit pas, et qui se voient à l'écran :

**Un caractère que la police n'a pas.** Il sort en carré barré d'un point
d'interrogation, et la phrase perd son mot. Une flèche « → » est passée ainsi
jusque dans le dossier de publication : Avenir Next ne l'a pas.

**L'apostrophe droite.** Une série l'employait partout (784 fois) quand les deux
autres n'employaient que la courbe. Dans un même fil, le mélange se voit.

**L'espace manquante avant la ponctuation haute.** Les assembleurs la transforment
en espace insécable, mais encore faut-il qu'elle soit là.

Ne remplace pas une relecture : ce script ne juge ni le sens ni le style. Pour
l'orthographe, voir orthographe.swift, qui passe les mêmes textes au correcteur
français de macOS.
"""
import importlib.util, json, os, re, sys
from PIL import ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
POLICES = ["/System/Library/Fonts/Avenir Next Condensed.ttc",
           "/System/Library/Fonts/Avenir Next.ttc"]

# Tout ce qui n'est pas destiné au lecteur : identifiants d'images, gabarits,
# prompts en anglais, clés d'émotion.
EXCLUS = {"illustration", "gabarit", "prompt", "fiche", "zone", "type", "numero",
          "slug", "lienGuide", "ids", "idx", "col", "maxw", "taille", "vign",
          "serif", "sans", "espace", "accent", "n", "h", "img", "hashtags",
          "emo", "emos", "emotions"}


def textes():
    """Tous les blocs de texte publiés, avec d'où ils viennent."""
    blocs = []

    def parcours(src, o):
        if isinstance(o, str):
            if o.strip() and any(c.isalpha() for c in o):
                blocs.append((src, o))
        elif isinstance(o, dict):
            for k, v in o.items():
                if k not in EXCLUS:
                    parcours(f"{src}/{k}", v)
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                parcours(f"{src}[{i}]", v)

    spec = importlib.util.spec_from_file_location(
        "contenus_typo", os.path.join(BASE, "reseaux-sociaux", "contenus.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for semaine in mod.SEMAINES:
        for p in semaine:
            parcours("fiche/" + p["slug"], {k: v for k, v in p.items() if k not in EXCLUS})

    for dossier, lab in (("reseaux-sociaux-illustre", "illustre"),
                         ("reseaux-sociaux-bd", "bd")):
        d = json.load(open(os.path.join(BASE, dossier, "contenus.json"), encoding="utf-8"))
        for p in d["posts"]:
            parcours(f"{lab}/{p['numero']:0>2}-{p['slug']}",
                     {k: v for k, v in p.items() if k not in EXCLUS})
    return blocs


def sans_glyphe():
    """Les caractères qu'au moins une des deux polices ne sait pas dessiner.

    Un glyphe absent sort au dessin du caractère « .notdef » — le même carré barré
    pour tous. On le repère en comparant l'image obtenue à celle d'un caractère
    forcément absent, pris dans la zone à usage privé d'Unicode. C'est plus sûr que
    de lire la table de la police, que PIL n'expose pas.
    """
    polices = [ImageFont.truetype(c, 52, index=0) for c in POLICES]
    temoins = [bytes(f.getmask("\ue000")) for f in polices]
    absents = {}
    for src, t in textes():
        for ch in set(t):
            if ch.isspace() or ch in absents:
                continue
            for f, temoin in zip(polices, temoins):
                if bytes(f.getmask(ch)) == temoin:
                    absents[ch] = src
                    break
    return absents


def principal():
    blocs = textes()
    soucis = []

    for ch, src in sorted(sans_glyphe().items()):
        soucis.append(f"caractère sans glyphe {ch!r} (U+{ord(ch):04X}) — {src}")

    for src, t in blocs:
        for m in re.finditer(r"\w'", t):
            soucis.append(f"apostrophe droite — {src} : …{t[max(0,m.start()-24):m.end()+24]}…")
            break
        for m in re.finditer(r"[^\s  0-9][?!;:»]", t):
            soucis.append(f"espace manquante avant « {m.group()[-1]} » — {src} : "
                          f"…{t[max(0,m.start()-24):m.end()+24]}…")
            break

    print(f"{len(blocs)} blocs de texte publiés · "
          f"{sum(len(t) for _, t in blocs)} caractères")
    if not soucis:
        print("✓ rien à signaler")
        return 0
    for s in soucis:
        print("  ✗ " + " ".join(s.split()))
    return 1


if __name__ == "__main__":
    sys.exit(principal())
