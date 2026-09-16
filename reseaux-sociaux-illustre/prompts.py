#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les fiches de prompts Nano Banana, une par post.

    python3 prompts.py

Lit contenus.json, écrit prompts/post-XX-slug.md et prompts/TOUS-LES-PROMPTS.md.
Chaque prompt est complet : scène + expressions + suffixe de style. Copier-coller direct.
"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(BASE, "prompts")

SUFFIXE = (
    "Style: soft digital illustration, colored pencil and light watercolor texture, visible "
    "pencil linework, gentle grain, warm diffused lighting, no harsh shadows. Semi-realistic "
    "young adult characters with very expressive faces and carefully drawn hands, slightly "
    "stylized proportions. Cozy knitwear in muted tones: sage green, dusty rose, lavender, "
    "mustard, slate blue, cream, terracotta. Minimal setting suggested with just a few elements. "
    "Plain warm cream background #F7F3EC, no frame, no border, the vignette floats on the "
    "background. Square composition, characters framed from the waist up. NO text, NO letters, "
    "NO words, NO watermark, NO logo anywhere in the image. Not cartoon, not 3D, not "
    "photorealistic, not vector flat."
)

def fiche(post):
    L = [f"# Post {post['numero']:02d} — {post['titre']}",
         "",
         f"*{post.get('sousTitre', '')}*" if post.get("sousTitre") else "",
         "",
         f"**Émotions** : {', '.join(post.get('emotions', []))}  ",
         f"**Illustrations à générer** : voir ci-dessous  ",
         "**Où déposer** : `illustrations/` — le nom du fichier doit être EXACTEMENT celui indiqué.",
         "",
         "---",
         ""]
    n = 0
    for s in post["slides"]:
        for it in s["items"]:
            if not it.get("prompt"):
                continue
            n += 1
            nom = it.get("illustration") or f"p{post['numero']:02d}-{n:02d}"
            L += [f"## {n}. `{nom}.png`",
                  "",
                  f"> {it.get('etiquette') or s.get('titre') or 'couverture'}"
                  + (f" — {it['texte']}" if it.get("texte") and it.get("etiquette") else ""),
                  "",
                  "```",
                  it["prompt"].strip().rstrip(".") + ". " + SUFFIXE,
                  "```",
                  ""]
            if it.get("bulle"):
                L += [f"*(La bulle «&nbsp;{it['bulle']}&nbsp;» est dessinée par l'assembleur — "
                      "ne la demande pas à Nano Banana.)*", ""]
    L += ["---", "",
          "## Une fois les images générées",
          "",
          "```bash",
          f"python3 assembleur.py {post['numero']}",
          "```",
          "",
          f"Les diapositives et la légende arrivent dans `sortie/{post['numero']:02d}-{post['slug']}/`.",
          ""]
    return "\n".join(x for x in L if x is not None)

def principal():
    data = json.load(open(os.path.join(BASE, "contenus.json"), encoding="utf-8"))
    posts = data["posts"]
    os.makedirs(DOSSIER, exist_ok=True)
    for f in os.listdir(DOSSIER):
        if re.match(r"post-\d+", f) or f == "TOUS-LES-PROMPTS.md":
            os.remove(os.path.join(DOSSIER, f))
    total = 0
    tous = ["# Tous les prompts, dans l'ordre",
            "",
            "Chaque bloc est prêt à coller dans Nano Banana. Le nom de fichier attendu est en titre.",
            "Le suffixe de style est déjà inclus : **ne le modifie pas**, c'est lui qui assure la cohérence.",
            ""]
    for p in posts:
        nom = f"post-{p['numero']:02d}-{p['slug']}.md"
        open(os.path.join(DOSSIER, nom), "w", encoding="utf-8").write(fiche(p))
        n = sum(1 for s in p["slides"] for it in s["items"] if it.get("prompt"))
        total += n
        tous += [f"## Post {p['numero']:02d} — {p['titre']} ({n} illustrations)", ""]
        k = 0
        for s in p["slides"]:
            for it in s["items"]:
                if not it.get("prompt"):
                    continue
                k += 1
                cible = it.get("illustration") or f"p{p['numero']:02d}-{k:02d}"
                tous += [f"**`{cible}.png`**", "", "```",
                         it["prompt"].strip().rstrip(".") + ". " + SUFFIXE, "```", ""]
    open(os.path.join(DOSSIER, "TOUS-LES-PROMPTS.md"), "w", encoding="utf-8").write("\n".join(tous))
    print(f"{len(posts)} fiches écrites dans prompts/ · {total} prompts au total")
    print(f"moyenne : {total/len(posts):.1f} illustrations par post")

if __name__ == "__main__":
    principal()
