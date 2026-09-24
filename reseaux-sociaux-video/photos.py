#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Des photos qui collent au thème de chaque vidéo.

    python3 photos.py            # les vingt thèmes
    python3 photos.py 02 10      # ceux-là

Pour chaque script, ses mots-clés (« images » dans scripts.py) sont cherchés dans
une banque d'images, et une trentaine de photos en format paysage sont rangées
dans photos/<id>/, avec photos/<id>.json qui dit d'où vient chacune et ce que sa
licence demande.

Deux sources :

  · Pexels — des photos de banque, libres d'usage commercial, sans attribution
    obligatoire (licence Pexels). C'est la bonne source. Il faut une clé, gratuite,
    rangée dans ~/.config/boussole/pexels.cle — jamais dans le dépôt :

        mkdir -p ~/.config/boussole
        printf '%s' 'COLLE_TA_CLÉ_ICI' > ~/.config/boussole/pexels.cle
        chmod 600 ~/.config/boussole/pexels.cle

  · Openverse — sans clé, mais 200 requêtes par jour et des photos de Flickr très
    inégales. Sert de dépannage. On n'y prend que du CC0 / domaine public (rien à
    créditer) et du CC BY : dans ce dernier cas le crédit est obligatoire, et le
    générateur l'écrit dans la légende.
"""
import json, os, sys, time, urllib.parse, urllib.request
from io import BytesIO
from PIL import Image
from scripts import SCRIPTS

ICI = os.path.dirname(os.path.abspath(__file__))
def ici(*p): return os.path.join(ICI, *p)
PAR_VIDEO = 30
CLE_PEXELS = os.path.expanduser("~/.config/boussole/pexels.cle")
UA = "boussole-emotionnelle.fr (atelier video, contact@boussole-emotionnelle.fr)"
import re
ANIMAUX = re.compile(r"\b(cat|kitten|dog|puppy|bird|horse|cow|sheep|lion|tiger|monkey|animal|child|children|kid|boy|girl|baby|toddler|soldier|military|army|skeleton|skull|person|people|man|men|woman|women|human|face|portrait|couple|family|crowd|hand|hands|arm|finger|model|businessman|businesswoman|worker|team|smiling|standing|sitting|wearing|holding|walking|selfie|silhouette|swimmer|swimming|duck|goose|geese|swan|deer|fox|wolf|bear|squirrel|rabbit|insect|butterfly|hummingbird|fish|seagull|gull|pigeon|eagle|owl)s?\b", re.I)

def cle_pexels():
    c = os.environ.get("PEXELS_API_KEY", "")
    if not c and os.path.exists(CLE_PEXELS): c = open(CLE_PEXELS, encoding="utf-8").read().strip()
    return c or None

def lire_json(url, entetes):
    req = urllib.request.Request(url, headers=entetes)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))

def telecharger(url, chemin, entetes=None):
    """Enregistre si c'est un paysage d'au moins 1 000 px de large ; rend (w, h) ou None."""
    req = urllib.request.Request(url, headers=entetes or {"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        octets = r.read()
    try:
        im = Image.open(BytesIO(octets)); im.load()
    except Exception:
        return None
    w, h = im.size
    if w < 1000 or w <= h * 1.1: return None
    if im.mode in ("RGBA", "LA", "P") and (im.mode == "P" and "transparency" in im.info or im.mode != "P"):
        return None                                   # un détourage sur fond transparent, pas une photo
    from PIL import ImageStat
    if max(ImageStat.Stat(im.convert("RGB").resize((64, 36))).stddev) < 18:
        return None                                   # presque unie : un aplat, un logo, une pancarte
    if w > 2000:
        im = im.resize((2000, round(h * 2000 / w)), Image.LANCZOS)
    im.convert("RGB").save(chemin, "JPEG", quality=88)
    return im.size

def pexels(mots, besoin):
    """Photos Pexels, paysage, par mot-clé ; rend des fiches {url, credit…}."""
    out, vus = [], set()
    for mot in mots:
        if len(out) >= besoin: break
        q = urllib.parse.urlencode({"query": mot, "orientation": "landscape", "size": "medium", "per_page": 15})
        try:
            d = lire_json(f"https://api.pexels.com/v1/search?{q}", {"Authorization": cle_pexels(), "User-Agent": UA})
        except Exception as e:
            print(f"    pexels/{mot}: {e}"); continue
        for p in d.get("photos", []):
            if p["id"] in vus: continue
            vus.add(p["id"])
            if ANIMAUX.search(p.get("alt") or ""): continue     # un chat qui bâille n'illustre pas la fatigue
            out.append({"id": f"pexels-{p['id']}", "url": p["src"]["large2x"], "source": p["url"], "alt": p.get("alt", ""),
                        "auteur": p.get("photographer", ""), "licence": "Pexels (usage libre, sans attribution)",
                        "credit": "", "mot": mot})
        time.sleep(0.3)
    return out

def openverse(mots, besoin):
    out, vus = [], set()
    for mot in mots:
        if len(out) >= besoin: break
        q = urllib.parse.urlencode({"q": mot, "license": "cc0,pdm,by", "aspect_ratio": "wide",
                                    "page_size": 20, "mature": "false"})
        try:
            d = lire_json(f"https://api.openverse.org/v1/images/?{q}", {"User-Agent": UA})
        except Exception as e:
            print(f"    openverse/{mot}: {e}"); continue
        for r in d.get("results", []):
            if r["id"] in vus or (r.get("width") or 0) < 1000: continue
            vus.add(r["id"])
            lic = r.get("license", "")
            credit = "" if lic in ("cc0", "pdm") else f"{r.get('creator') or 'auteur inconnu'} ({r.get('source')}, CC {lic.upper()} {r.get('license_version','')})".strip()
            out.append({"id": f"openverse-{r['id']}", "url": r["url"], "source": r.get("foreign_landing_url"),
                        "auteur": r.get("creator") or "", "licence": f"CC {lic.upper()}", "credit": credit, "mot": mot})
        time.sleep(3.2)     # 20 requêtes par minute, pas plus
    return out

def collecter(script):
    ident = script["id"]; dossier = ici("photos", ident); os.makedirs(dossier, exist_ok=True)
    manif = ici("photos", f"{ident}.json")
    fiches = json.load(open(manif, encoding="utf-8")) if os.path.exists(manif) else []
    if len(fiches) >= PAR_VIDEO:
        print(f"  {ident}: déjà {len(fiches)} photos"); return
    source = "pexels" if cle_pexels() else "openverse"
    candidats = (pexels if source == "pexels" else openverse)(script["images"], PAR_VIDEO * 2)
    deja = {f["id"] for f in fiches}
    for c in candidats:
        if len(fiches) >= PAR_VIDEO: break
        if c["id"] in deja: continue
        chemin = os.path.join(dossier, f"{c['id']}.jpg")
        try:
            taille = telecharger(c["url"], chemin)
        except Exception:
            continue
        if not taille: continue
        c["fichier"] = f"{c['id']}.jpg"; c["taille"] = list(taille)
        fiches.append(c); deja.add(c["id"])
        time.sleep(0.2)
    tmp = manif + ".tmp"
    json.dump(fiches, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); os.replace(tmp, manif)
    print(f"  {ident}: {len(fiches)} photos ({source})")

if __name__ == "__main__":
    args = sys.argv[1:]
    for s in SCRIPTS:
        if args and not any(s["id"].startswith(a) for a in args): continue
        collecter(s)
