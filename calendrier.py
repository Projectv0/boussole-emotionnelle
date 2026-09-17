#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit et vérifie calendrier.json à partir d'une répartition des carrousels illustrés.

    python3 calendrier.py repartition.json

La répartition dit seulement, pour chaque semaine, quel carrousel illustré tombe le
mardi, le jeudi et le samedi. Ce script en fait le calendrier complet : il y remet les
posts typographiques à leur lundi, mercredi et vendredi, et il refuse d'écrire quoi que
ce soit si le compte ne tombe pas juste.

Les trois vérifications qui comptent — un carrousel oublié ou placé deux fois ne se voit
pas à l'œil dans un fichier de treize semaines, mais se voit tout de suite dans le dossier
de publication, une fois les images copiées.
"""
import json, os, sys, glob, re

BASE = os.path.dirname(os.path.abspath(__file__))
TYPO = os.path.join(BASE, "reseaux-sociaux")

EMOTIONS = {1: "l'anxiété et la peur", 2: "la colère", 3: "la honte", 4: "la culpabilité",
            5: "la tristesse", 6: "la jalousie et l'envie", 7: "la joie", 8: "l'amour",
            9: "la gratitude", 10: "la fierté", 11: "la sérénité", 12: "la surprise",
            13: "le dégoût"}


def posts_typo():
    """Les 39 posts typographiques, rangés par semaine et par jour."""
    par_semaine = {}
    for d in sorted(glob.glob(os.path.join(TYPO, "semaine-*", "*", ""))):
        n = int(re.search(r"semaine-(\d+)", d).group(1))
        slug = os.path.basename(d.rstrip("/"))
        par_semaine.setdefault(n, []).append({"jour": slug.split("-")[0], "slug": slug})
    return par_semaine


def verifier(rep, illus):
    """Renvoie la liste des erreurs. Vide = le calendrier est utilisable."""
    erreurs = []
    vus, places = {}, []
    for sem in rep["semaines"]:
        for cle in ("mardi", "jeudi", "samedi"):
            num = sem.get(cle)
            if num is None:
                continue
            places.append(num)
            if num in vus:
                erreurs.append(f"carrousel {num:02d} placé deux fois "
                               f"(semaine {vus[num]} et semaine {sem['numero']})")
            vus[num] = sem["numero"]
    manquants = sorted(set(illus) - set(places))
    if manquants:
        erreurs.append("carrousels jamais placés : " + ", ".join(f"{n:02d}" for n in manquants))
    inconnus = sorted(set(places) - set(illus))
    if inconnus:
        erreurs.append("numéros inexistants : " + ", ".join(str(n) for n in inconnus))
    if len(rep["semaines"]) != 13:
        erreurs.append(f"{len(rep['semaines'])} semaines au lieu de 13")
    samedis = sum(1 for s in rep["semaines"] if s.get("samedi") is not None)
    if samedis != 4:
        erreurs.append(f"{samedis} semaines avec un samedi au lieu de 4 "
                       f"(4 × 3 + 9 × 2 = 30 carrousels)")
    for sem in rep["semaines"]:
        if sem.get("mardi") is None or sem.get("jeudi") is None:
            erreurs.append(f"semaine {sem['numero']} : mardi ou jeudi vide")
    return erreurs


def principal():
    source = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "repartition.json")
    rep = json.load(open(source, encoding="utf-8"))
    illus = {p["numero"] for p in json.load(
        open(os.path.join(BASE, "reseaux-sociaux-illustre", "contenus.json"),
             encoding="utf-8"))["posts"]}

    erreurs = verifier(rep, illus)
    if erreurs:
        print("répartition refusée :")
        for e in erreurs:
            print("  ·", e)
        raise SystemExit(1)

    typo = posts_typo()
    semaines = []
    for sem in sorted(rep["semaines"], key=lambda s: s["numero"]):
        n = sem["numero"]
        pubs = [{"jour": p["jour"], "type": "typographique", "slug": p["slug"]}
                for p in typo[n]]
        for jour in ("mardi", "jeudi", "samedi"):
            if sem.get(jour) is not None:
                pubs.append({"jour": jour, "type": "illustre", "numero": sem[jour]})
        ordre = {"lundi": 1, "mardi": 2, "mercredi": 3, "jeudi": 4, "vendredi": 5, "samedi": 6}
        pubs.sort(key=lambda p: ordre[p["jour"]])
        semaines.append({"numero": n, "emotion": EMOTIONS[n],
                         "justification": sem.get("justification", ""),
                         "publications": pubs})

    cal = {"strategie": rep.get("strategie", ""), "semaines": semaines}
    json.dump(cal, open(os.path.join(BASE, "calendrier.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    total = sum(len(s["publications"]) for s in semaines)
    print(f"calendrier.json écrit · {len(semaines)} semaines · {total} publications "
          f"({sum(1 for s in semaines for p in s['publications'] if p['type'] == 'typographique')} "
          f"typographiques + "
          f"{sum(1 for s in semaines for p in s['publications'] if p['type'] == 'illustre')} illustrés)")


if __name__ == "__main__":
    principal()
