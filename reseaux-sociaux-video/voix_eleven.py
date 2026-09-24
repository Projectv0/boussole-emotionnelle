#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La voix off par ElevenLabs — celle qu'on entend sur les vidéos de référence.

    python3 voix_eleven.py --voix               # liste les voix françaises du compte, avec un extrait
    python3 voix_eleven.py --essai <voice_id>   # lit une phrase d'essai dans voix/essai-<id>.mp3

Le générateur l'appelle lui-même pour chaque script (voir generateur.py).

LA CLÉ. Elle se range dans ~/.config/boussole/elevenlabs.cle — un fichier lisible par toi
seul, hors du dépôt. Ce script la lit ; il ne l'affiche jamais, ne l'écrit nulle part,
ne l'envoie qu'à api.elevenlabs.io. Pour la poser, dans le Terminal :

    mkdir -p ~/.config/boussole
    printf '%s' 'COLLE_TA_CLÉ_ICI' > ~/.config/boussole/elevenlabs.cle
    chmod 600 ~/.config/boussole/elevenlabs.cle

L'INSTANT DE CHAQUE MOT. ElevenLabs rend, avec l'audio, le moment où chaque caractère
est prononcé ; on en tire celui de chaque mot, dans le même format que voix.swift —
le générateur ne voit pas la différence entre les deux voix.
"""
import base64, json, os, subprocess, sys, urllib.request, urllib.error

CLE_FICHIER = os.path.expanduser("~/.config/boussole/elevenlabs.cle")
API = "https://api.elevenlabs.io/v1"
MODELE = "eleven_multilingual_v2"

def cle():
    c = os.environ.get("ELEVENLABS_API_KEY", "")
    if not c and os.path.exists(CLE_FICHIER):
        c = open(CLE_FICHIER, encoding="utf-8").read().strip()
    return c or None

def appel(chemin, corps=None, methode=None):
    req = urllib.request.Request(API + chemin, data=json.dumps(corps).encode("utf-8") if corps is not None else None,
                                 headers={"xi-api-key": cle(), "Content-Type": "application/json", "Accept": "application/json"},
                                 method=methode or ("POST" if corps is not None else "GET"))
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise SystemExit(f"ElevenLabs {e.code} sur {chemin} : {detail}")

def voix_francaises():
    """Les voix du compte parlant français (les voix multilingues le parlent toutes)."""
    v = appel("/voices").get("voices", [])
    out = []
    for x in v:
        lab = x.get("labels") or {}
        out.append({"id": x["voice_id"], "nom": x["name"], "genre": lab.get("gender", "?"),
                    "accent": lab.get("accent", "?"), "langue": lab.get("language", "?"),
                    "description": lab.get("description", ""), "extrait": x.get("preview_url")})
    return out

def synthetiser(texte, voice_id, sortie_mp3, sortie_json, stabilite=0.5, style=0.25):
    """Écrit l'audio et le JSON des instants de mots. Rend les données JSON."""
    rep = appel(f"/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128", {
        "text": texte, "model_id": MODELE,
        "voice_settings": {"stability": stabilite, "similarity_boost": 0.8, "style": style, "use_speaker_boost": True},
    })
    open(sortie_mp3, "wb").write(base64.b64decode(rep["audio_base64"]))
    al = rep.get("alignment") or rep.get("normalized_alignment")
    chars, debuts, fins = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    rendu = "".join(chars)
    # Les caractères rendus doivent être ceux du texte envoyé ; sinon on se cale
    # par recherche, mot à mot, sur ce qui a été rendu.
    import re
    mots = []
    curseur = 0
    for m in re.finditer(r"[^\s]+", texte):
        mot, pos = m.group(0), m.start()
        if rendu == texte:
            t = debuts[pos]
        else:
            i = rendu.find(mot, curseur)
            if i < 0: i = curseur
            t = debuts[min(i, len(debuts) - 1)]; curseur = i + len(mot)
        mots.append({"mot": mot, "debut": pos, "longueur": len(mot), "t": round(float(t), 3)})
    for k in range(1, len(mots)):                       # jamais en arrière
        if mots[k]["t"] < mots[k - 1]["t"]: mots[k]["t"] = mots[k - 1]["t"]
    duree = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", sortie_mp3],
                                 capture_output=True, text=True).stdout.strip() or fins[-1])
    d = {"voix": f"elevenlabs:{voice_id}", "duree": duree, "fin": round(float(fins[-1]) + 0.5, 3), "texte": texte, "mots": mots}
    json.dump(d, open(sortie_json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return d

if __name__ == "__main__":
    if not cle():
        raise SystemExit("Pas de clé : voir en tête de ce fichier comment la poser (jamais dans le dépôt).")
    if "--voix" in sys.argv:
        for v in voix_francaises():
            print(f"  {v['id']}  {v['nom']:<18} {v['genre']:<8} {v['accent']:<12} {v['langue']:<6} {v['description'][:40]}")
            if v["extrait"]: print(f"      extrait : {v['extrait']}")
    elif "--essai" in sys.argv:
        vid = sys.argv[sys.argv.index("--essai") + 1]
        ici = os.path.dirname(os.path.abspath(__file__)); os.makedirs(os.path.join(ici, "voix"), exist_ok=True)
        phrase = ("Tu réponds « ça va » dix fois par jour. Et tu sais très bien que c'est faux. "
                  "Il y a deux mille ans, Sénèque rapportait que les sages appelaient la colère une courte folie.")
        d = synthetiser(phrase, vid, os.path.join(ici, "voix", f"essai-{vid}.mp3"), os.path.join(ici, "voix", f"essai-{vid}.json"))
        print(f"voix/essai-{vid}.mp3 · {d['duree']:.1f} s · {len(d['mots'])} mots datés")
    else:
        print(__doc__)
