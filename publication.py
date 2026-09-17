#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monte le dossier de publication à partir des deux studios.

    python3 publication.py

Les 39 posts typographiques (reseaux-sociaux/) et les 30 carrousels illustrés
(reseaux-sociaux-illustre/) sont réunis en 13 semaines de cinq à six publications,
rangées dans l'ordre des jours et prêtes à poster sans réfléchir :

    publication/
      PLAN.md
      semaine-01/
        1-lundi-.../      instagram/  tiktok/  legende.txt
        2-mardi-.../      instagram/  tiktok/  legende.txt
        ...

Le chiffre en tête de chaque dossier force le bon ordre dans le Finder : « jeudi »
passe avant « lundi » en alphabétique, ce qui rendrait la semaine illisible.

Le calendrier vit dans calendrier.json : quel carrousel illustré tombe quel jour de
quelle semaine. Les posts typographiques gardent leur lundi, mercredi et vendredi.
"""
import json, os, shutil, sys

BASE = os.path.dirname(os.path.abspath(__file__))
TYPO = os.path.join(BASE, "reseaux-sociaux")
ILLU = os.path.join(BASE, "reseaux-sociaux-illustre", "sortie")
CIBLE = os.path.join(BASE, "publication")

RANG = {"lundi": 1, "mardi": 2, "mercredi": 3, "jeudi": 4, "vendredi": 5, "samedi": 6}


def copier(source, dest):
    """Copie un post complet (instagram/, tiktok/, legende.txt)."""
    os.makedirs(dest, exist_ok=True)
    for sous in ("instagram", "tiktok"):
        s = os.path.join(source, sous)
        if not os.path.isdir(s):
            raise SystemExit(f"manquant : {s}")
        d = os.path.join(dest, sous)
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(s, d)
    shutil.copy2(os.path.join(source, "legende.txt"), os.path.join(dest, "legende.txt"))
    return len([f for f in os.listdir(os.path.join(dest, "instagram")) if f.endswith(".jpg")])


def plan(cal, illus, compte):
    """Écrit publication/PLAN.md — le seul document à ouvrir pour publier."""
    L = ["# Plan de publication — 13 semaines, 69 publications",
         "",
         "Deux formats de carrousel en alternance, un jour sur deux :",
         "",
         "| | Jours | Ce que c'est |",
         "|---|---|---|",
         "| **Typographique** | lundi, mercredi, vendredi | texte et pictogrammes, les trois séries "
         "numérotées (Comprendre, Deux mots deux choses, La pratique du vendredi) |",
         "| **Illustré** | mardi, jeudi, et samedi 4 semaines sur 13 | personnages dessinés, "
         "scènes du quotidien |",
         "",
         "Chaque semaine tourne autour d'une émotion, et les deux formats l'éclairent autrement : "
         "le typographique explique et distingue, l'illustré met une scène vécue dessus.",
         "",
         "## Publier une journée (2-3 minutes)",
         "",
         "Ouvre le dossier du jour. Il contient tout, rien à préparer.",
         "",
         "**TikTok** : ➕ → mode Photo → glisser les images de `tiktok/` **dans l'ordre 01, 02, 03…** "
         "→ coller la légende depuis `legende.txt` → choisir un son doux dans les tendances "
         "(lo-fi, piano). Le son compte : TikTok pousse les photos qui utilisent un son en tendance.",
         "",
         "**Instagram** : ➕ Publication → sélection multiple des images de `instagram/` dans l'ordre "
         "→ coller la même légende → publier. Une story de relais le jour même aide beaucoup.",
         "",
         "Les dossiers sont numérotés de 1 à 6 dans l'ordre des jours : sans ce chiffre, le Finder "
         "classerait « jeudi » avant « lundi ».",
         "",
         "## Les réglages à faire une seule fois",
         "",
         "- **Lien en bio** sur les deux comptes : `https://boussole-emotionnelle.fr` — toutes les "
         "légendes y renvoient sans pouvoir cliquer dans le texte.",
         "- Heures conseillées : 12 h-13 h ou 19 h-21 h. La régularité compte plus que l'heure parfaite.",
         "- Réponds aux commentaires dans la première demi-heure : c'est le signal d'engagement le plus fort.",
         "- Ne supprime pas un post qui démarre lentement — les carrousels TikTok remontent parfois "
         "après plusieurs jours.",
         "- Épingle en profil le post qui marche le mieux, après deux ou trois semaines.",
         ""]

    for sem in cal["semaines"]:
        L += [f"## Semaine {sem['numero']:02d} — {sem.get('emotion', '')}", ""]
        if sem.get("justification"):
            L += [f"*{sem['justification']}*", ""]
        L += ["| Jour | Format | Dossier | Diapos |", "|---|---|---|---|"]
        for e in sem["publications"]:
            if e["type"] == "typographique":
                nom, titre = f"{RANG[e['jour']]}-{e['slug']}", e["slug"]
            else:
                p = illus[e["numero"]]
                nom = f"{RANG[e['jour']]}-{e['jour']}-{p['slug']}"
                titre = p["titre"][0] + p["titre"][1:].lower()
            fmt = "typographique" if e["type"] == "typographique" else "**illustré**"
            L.append(f"| {e['jour']} | {fmt} | `{nom}` | {compte.get(nom + str(sem['numero']), '')} |")
        L.append("")

    L += ["## Après ces treize semaines", "",
          "Le rythme d'un jour sur deux entre les deux formats est fait pour tenir : si tu veux "
          "ralentir, garde le lundi, le mercredi et le vendredi et publie les illustrés un jour "
          "sur deux seulement. Tu tiendras alors près de six mois avec le même dossier.",
          ""]
    open(os.path.join(CIBLE, "PLAN.md"), "w", encoding="utf-8").write("\n".join(L))


def principal():
    cal = json.load(open(os.path.join(BASE, "calendrier.json"), encoding="utf-8"))
    illus = {p["numero"]: p for p in
             json.load(open(os.path.join(BASE, "reseaux-sociaux-illustre", "contenus.json"),
                            encoding="utf-8"))["posts"]}
    shutil.rmtree(CIBLE, ignore_errors=True)
    os.makedirs(CIBLE, exist_ok=True)

    total_posts = total_images = 0
    compte = {}
    for sem in cal["semaines"]:
        n = sem["numero"]
        dossier_sem = os.path.join(CIBLE, f"semaine-{n:02d}")
        for entree in sem["publications"]:
            jour, kind = entree["jour"], entree["type"]
            if kind == "typographique":
                source = os.path.join(TYPO, f"semaine-{n:02d}", entree["slug"])
                nom = f"{RANG[jour]}-{entree['slug']}"
            else:
                p = illus[entree["numero"]]
                source = os.path.join(ILLU, f"{p['numero']:02d}-{p['slug']}")
                nom = f"{RANG[jour]}-{jour}-{p['slug']}"
            k = copier(source, os.path.join(dossier_sem, nom))
            compte[nom + str(n)] = k
            total_images += k
            total_posts += 1

    plan(cal, illus, compte)
    print(f"{total_posts} publications · {total_images} diapositives × 2 formats "
          f"= {total_images * 2} images dans publication/")
    return total_posts, total_images


if __name__ == "__main__":
    principal()
