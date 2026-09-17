#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Régénère sitemap.xml depuis les fichiers réellement présents.

    python3 sitemap.py

La date de chaque page est celle de son dernier commit, pas une valeur saisie à la
main : le sitemap annonçait « 2026-09-01 » pour des articles modifiés depuis, ce qui
apprend aux moteurs à ne plus faire confiance aux dates. À relancer dans le même
commit que toute modification du site — le script le rappelle si l'index git a
changé après la génération.

Les pages légales et la page de remerciement restent hors du sitemap : elles portent
« noindex » et n'ont rien à faire dans un index de recherche.
"""
import glob, os, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://boussole-emotionnelle.fr"
HORS = {"merci.html", "apres-bascule.html"}


def date_du_dernier_commit(chemin):
    """Date ISO du dernier commit touchant ce fichier, ou la date du fichier."""
    r = subprocess.run(["git", "log", "-1", "--format=%cI", "--", chemin],
                       capture_output=True, text=True, cwd=BASE)
    iso = r.stdout.strip()[:10]
    if iso:
        return iso
    import datetime
    return datetime.date.fromtimestamp(os.path.getmtime(chemin)).isoformat()


def pages():
    """(url, chemin, priorité, fréquence) pour chaque page indexable."""
    out = [("/", "index.html", "1.0", "monthly"),
           ("/guide/", "guide/index.html", "0.9", "monthly")]
    for f in sorted(glob.glob(os.path.join(BASE, "guide", "*.html"))):
        nom = os.path.basename(f)
        if nom == "index.html" or nom in HORS:
            continue
        out.append((f"/guide/{nom}", f"guide/{nom}", "0.8", "monthly"))
    return out


def principal():
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, chemin, prio, freq in pages():
        lignes += ["  <url>",
                   f"    <loc>{SITE}{url}</loc>",
                   f"    <lastmod>{date_du_dernier_commit(chemin)}</lastmod>",
                   f"    <changefreq>{freq}</changefreq>",
                   f"    <priority>{prio}</priority>",
                   "  </url>"]
    lignes.append("</urlset>")
    open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(lignes) + "\n")

    modifies = subprocess.run(["git", "diff", "--name-only"], capture_output=True,
                              text=True, cwd=BASE).stdout.split()
    print(f"sitemap.xml écrit · {len(pages())} URL")
    aretenir = [m for m in modifies if m.endswith(".html") and m != "sitemap.xml"]
    if aretenir:
        print("⚠️  des pages sont modifiées mais pas encore commitées :",
              ", ".join(aretenir[:5]), "…" if len(aretenir) > 5 else "")
        print("    relance ce script après le commit pour que les dates soient justes.")


if __name__ == "__main__":
    principal()
