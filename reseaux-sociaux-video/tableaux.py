#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Va chercher des tableaux du domaine public pour les fonds des vidéos.

    python3 tableaux.py            # ~200 tableaux dans tableaux/, et tableaux.json

Deux musées qui publient leurs reproductions sous licence CC0 — libres de tout usage,
y compris commercial, sans attribution obligatoire :

  · The Metropolitan Museum of Art (New York), Open Access
  · The Art Institute of Chicago, Open Access

On ne garde que des PEINTURES, entre 1500 et 1900, en format paysage : le cadre
vidéo est en 16:9 et un portrait en hauteur devrait être massacré au recadrage.
Chaque fichier est noté dans tableaux.json avec son titre, son auteur, sa date, son
musée et l'adresse d'origine — pour pouvoir dire d'où vient chaque image.

Ce script est poli : une requête à la fois, une courte pause entre deux.
"""
import json, os, sys, time, urllib.parse, urllib.request
from io import BytesIO
from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.join(ICI, "tableaux")
MANIFESTE = os.path.join(ICI, "tableaux.json")
CIBLE = 220
os.makedirs(DOSSIER, exist_ok=True)

# Les scènes des originaux : foules, cours, banquets, batailles, salons, marchés.
TERMES = ["crowd", "court", "banquet", "feast", "battle", "procession", "market",
          "assembly", "coronation", "ball", "festival", "tribunal", "senate",
          "council", "audience", "ceremony", "wedding", "theater", "carnival",
          "triumph", "gathering", "harvest", "fair", "salon", "orator", "judgment",
          "supper", "siege", "cavalry", "landscape figures", "interior figures"]

UA = {"User-Agent": "boussole-emotionnelle.fr (atelier vidéo, usage éditorial)"}

def lire(url, binaire=False):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        d = r.read()
    return d if binaire else json.loads(d.decode("utf-8"))

def garder(image_bytes, chemin):
    """Enregistre si c'est un paysage d'au moins 900 px de large ; rend (w, h) ou None."""
    try:
        im = Image.open(BytesIO(image_bytes)); im.load()
    except Exception:
        return None
    w, h = im.size
    if w < 840 or w <= h * 1.05:
        return None
    im.convert("RGB").save(chemin, "JPEG", quality=88)
    return (w, h)

manifeste = json.load(open(MANIFESTE, encoding="utf-8")) if os.path.exists(MANIFESTE) else []
deja = {m["id"] for m in manifeste}
n = len(manifeste)
print(f"déjà {n} tableau(x) en place, cible {CIBLE}")

# ————— The Met —————
def met():
    global n
    for terme in TERMES:
        if n >= CIBLE: return
        q = urllib.parse.urlencode({"q": terme, "hasImages": "true", "isPublicDomain": "true", "medium": "Paintings"})
        try:
            ids = (lire(f"https://collectionapi.metmuseum.org/public/collection/v1/search?{q}").get("objectIDs") or [])[:40]
        except Exception as e:
            print(f"  met/{terme}: {e}")
            if "403" in str(e): print("  met : bloqué, on passe à l'AIC"); return
            continue
        pris = 0
        for oid in ids:
            cle = f"met-{oid}"
            if cle in deja or n >= CIBLE: continue
            try:
                o = lire(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{oid}")
            except Exception:
                continue
            time.sleep(0.6)
            if o.get("classification") != "Paintings" or not o.get("isPublicDomain"): continue
            if o.get("department") not in ("European Paintings", "The American Wing",
                                           "Robert Lehman Collection", "European Sculpture and Decorative Arts"): continue
            an = o.get("objectBeginDate") or 0
            if not (1500 <= an <= 1890): continue
            # La petite image (~1 400 px de large) suffit à un cadre de 1 024 px, et
            # demander la grande (4 000 px, 4 Mo) a valu un 403 au bout de vingt.
            url = o.get("primaryImageSmall") or o.get("primaryImage")
            if not url: continue
            try:
                taille = garder(lire(url, binaire=True), os.path.join(DOSSIER, f"{cle}.jpg"))
            except Exception:
                continue
            if not taille: continue
            manifeste.append({"id": cle, "fichier": f"{cle}.jpg", "titre": o.get("title"),
                              "auteur": o.get("artistDisplayName"), "date": o.get("objectDate"),
                              "musee": "The Metropolitan Museum of Art", "licence": "CC0 (Open Access)",
                              "source": o.get("objectURL"), "taille": taille})
            deja.add(cle); n += 1; pris += 1
        print(f"  met/{terme}: +{pris} (total {n})")
        json.dump(manifeste, open(MANIFESTE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ————— Art Institute of Chicago —————
def aic():
    global n
    for terme in TERMES:
        if n >= CIBLE: return
        # Le filtre « peinture » se fait côté serveur (artwork_type_id 1) : la simple
        # recherche par mot ramenait surtout des estampes et des sculptures.
        corps = json.dumps({
            "q": terme, "limit": 100,
            "fields": ["id", "title", "image_id", "date_start", "artist_title", "department_title"],
            "query": {"bool": {"must": [
                {"term": {"artwork_type_id": 1}},
                {"term": {"is_public_domain": True}},
                {"range": {"date_start": {"gte": 1500, "lte": 1890}}},
            ]}},
        }).encode("utf-8")
        try:
            req = urllib.request.Request("https://api.artic.edu/api/v1/artworks/search", data=corps,
                                         headers={**UA, "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = json.loads(r.read().decode("utf-8")).get("data") or []
        except Exception as e:
            print(f"  aic/{terme}: {e}"); continue
        pris = 0
        for a in data:
            cle = f"aic-{a['id']}"
            if cle in deja or n >= CIBLE: continue
            if not a.get("image_id"): continue
            if a.get("department_title") not in ("Painting and Sculpture of Europe", "Arts of the Americas"): continue
            url = f"https://www.artic.edu/iiif/2/{a['image_id']}/full/1686,/0/default.jpg"
            try:
                octets = lire(url, binaire=True)
            except Exception:
                try: octets = lire(url.replace("1686,", "843,"), binaire=True)
                except Exception: continue
            time.sleep(0.3)
            taille = garder(octets, os.path.join(DOSSIER, f"{cle}.jpg"))
            if not taille: continue
            manifeste.append({"id": cle, "fichier": f"{cle}.jpg", "titre": a.get("title"),
                              "auteur": a.get("artist_title"), "date": str(a.get("date_start")),
                              "musee": "The Art Institute of Chicago", "licence": "CC0 (Open Access)",
                              "source": f"https://www.artic.edu/artworks/{a['id']}", "taille": taille})
            deja.add(cle); n += 1; pris += 1
        print(f"  aic/{terme}: +{pris} (total {n})")
        json.dump(manifeste, open(MANIFESTE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

met()
aic()
json.dump(manifeste, open(MANIFESTE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\n{n} tableaux dans {DOSSIER}")
