#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cale une voix humaine sur son texte : à quel instant chaque mot est dit.

    python3 aligner.py <enregistrement.wav> <texte.txt> <sortie.json>

Avec la voix de synthèse, le synthétiseur nous disait lui-même quand il
prononçait chaque mot. Avec une vraie voix, il faut l'écouter : Whisper (le
modèle de reconnaissance d'OpenAI, ici dans sa version pour puce Apple) transcrit
l'enregistrement avec l'instant de chaque mot, puis on recolle cette
transcription sur le texte qu'on connaît déjà — c'est lui qui fait foi, la
transcription ne sert qu'à dater.

Sortie : le même JSON que voix.swift, pour que le générateur ne voie pas la
différence. Les mots que Whisper a manqués (il en manque toujours quelques-uns)
reçoivent un instant interpolé entre leurs voisins.
"""
import difflib, json, re, sys, unicodedata

MODELE = "mlx-community/whisper-medium-mlx"     # ~1,5 Go, téléchargé une fois

def normaliser(mot):
    """Un mot rendu comparable : minuscules, sans accents ni ponctuation, apostrophes unifiées."""
    m = unicodedata.normalize("NFD", mot.lower())
    m = "".join(c for c in m if unicodedata.category(c) != "Mn")
    m = m.replace("’", "'").replace("œ", "oe")
    return re.sub(r"[^a-z0-9']", "", m)

def jetons_texte(texte):
    """Les mots du texte avec leur position (offset de caractère), comme voix.swift les rapporte."""
    return [(m.group(0), m.start()) for m in re.finditer(r"[^\s]+", texte)]

def transcrire(chemin):
    import mlx_whisper
    r = mlx_whisper.transcribe(chemin, path_or_hf_repo=MODELE, language="fr",
                               word_timestamps=True, condition_on_previous_text=False)
    mots = []
    for seg in r.get("segments", []):
        for w in seg.get("words", []):
            mots.append((w["word"].strip(), float(w["start"]), float(w["end"])))
    return mots

def aligner(texte, entendus):
    """Rend, pour chaque mot du texte, l'instant où il est dit (ou None si inconnu)."""
    script = jetons_texte(texte)
    a = [normaliser(m) for m, _ in script]
    b = [normaliser(m) for m, _, _ in entendus]
    # On ignore les jetons vides (ponctuation seule) sans perdre l'alignement des indices.
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    instants = [None] * len(script)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                instants[i1 + k] = entendus[j1 + k][1]
        elif tag == "replace" and (i2 - i1) == (j2 - j1):
            # même nombre de mots des deux côtés : Whisper a mal entendu, le rythme est bon
            for k in range(i2 - i1):
                instants[i1 + k] = entendus[j1 + k][1]
    # interpolation des trous, monotone
    n = len(instants)
    connus = [k for k in range(n) if instants[k] is not None]
    if not connus:
        raise SystemExit("aucun mot reconnu : l'enregistrement correspond-il au texte ?")
    for k in range(n):
        if instants[k] is None:
            avant = max((j for j in connus if j < k), default=None)
            apres = min((j for j in connus if j > k), default=None)
            if avant is None:
                instants[k] = max(0.0, instants[apres] - 0.35 * (apres - k))
            elif apres is None:
                instants[k] = instants[avant] + 0.35 * (k - avant)
            else:
                instants[k] = instants[avant] + (instants[apres] - instants[avant]) * (k - avant) / (apres - avant)
    # jamais en arrière
    for k in range(1, n):
        if instants[k] < instants[k - 1]: instants[k] = instants[k - 1]
    return script, instants, len(connus)

if __name__ == "__main__":
    audio, txt, sortie = sys.argv[1:4]
    texte = open(txt, encoding="utf-8").read().strip()
    entendus = transcrire(audio)
    script, instants, reconnus = aligner(texte, entendus)
    fin = max(e for _, _, e in entendus) if entendus else instants[-1] + 1
    import subprocess
    duree = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                  "-of", "csv=p=0", audio], capture_output=True, text=True).stdout.strip() or fin)
    mots = [{"mot": m, "debut": pos, "longueur": len(m), "t": round(t, 3)} for (m, pos), t in zip(script, instants)]
    json.dump({"voix": "humaine", "duree": duree, "fin": round(fin + 0.6, 3), "texte": texte,
               "mots": mots, "reconnus": reconnus, "total": len(script)},
              open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{duree:.1f} s · {reconnus}/{len(script)} mots reconnus, les autres interpolés")
