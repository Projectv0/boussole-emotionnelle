#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique les vidéos, une par script, dans le style des références.

    python3 generateur.py                # les vingt
    python3 generateur.py 03 17          # celles-là seulement
    python3 generateur.py --apercu 03    # juste les images-clés, sans vidéo

Le style, tel qu'il a été lu dans les trois vidéos de référence :
  · paysage 16:9, une minute environ, 30 images par seconde ;
  · une accroche sur fond noir, les mots posés un par un, un mot en couleur ;
  · puis des photos assombries, sur le thème de la vidéo — une photo par phrase,
    la photo et le texte changent au même instant, jamais l'un sans l'autre ;
  · à la fin, le produit et un badge rouge « LIEN EN BIO ».

Ce qu'on assemble :
  scripts.py       les vingt textes, groupe de mots par groupe de mots
  photos/          les photos de chaque thème (voir photos.py)
  musiques/        Kevin MacLeod, CC BY — le crédit part dans la légende
  voix_eleven.py   la voix ElevenLabs (voix.swift, celle de macOS, en dernier recours)
  ../og.jpg        l'image du site, montrée à la fin comme « le produit »

Sortie : « ../Vidéos à publier/NN - Titre.mp4 », avec sa légende à côté.
Les fichiers de travail (voix, images-clés) vont dans .cache/, qu'on peut effacer.
"""
import hashlib, json, math, os, random, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scripts import SCRIPTS

ICI = os.path.dirname(os.path.abspath(__file__))
def ici(*p): return os.path.join(ICI, *p)
SORTIE = ici("..", "Vidéos à publier")
CACHE = ici(".cache")
for d in (SORTIE, os.path.join(CACHE, "voix"), os.path.join(CACHE, "images")): os.makedirs(d, exist_ok=True)

L, H, FPS = 1024, 576, 30
SANS_VOIX = True                 # pour l'instant : texte et musique seulement, le temps de lecture fait le rythme
VOIX = "Jacques"                 # la voix macOS, en dernier recours (quand SANS_VOIX passe à False)
VOIX_ELEVEN = ""                 # l'identifiant d'une voix ElevenLabs : voir voix_eleven.py --voix
POLICE = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
SORTIE_FINALE = 4.0          # le produit reste à l'écran après le dernier mot
SITE = "boussole-emotionnelle.fr"

BLANC, NOIR = (255, 255, 255), (0, 0, 0)
COULEURS = {"*": (245, 208, 0), "!": (224, 48, 48), "+": (46, 204, 113)}   # jaune, rouge, vert
ROUGE_BADGE = (196, 22, 22)

PRODUIT = Image.open(ici("..", "og.jpg")).convert("RGB")

# ————————————————————————— le texte —————————————————————————

def narration(groupes):
    """Ce que la voix lit : les groupes bout à bout, sans les marques, avec la ponctuation."""
    morceaux = []
    for g in groupes:
        s = re.sub(r"[*!+]", "", g).replace(" / ", " ").replace("/", " ")
        morceaux.append(re.sub(r"\s+", " ", s).strip())
    return " ".join(morceaux)

def lignes_affichees(groupe):
    """Les lignes à l'écran : [[(mot, couleur|None), …], …], en capitales, sans ponctuation.

    Une marque peut couvrir plusieurs mots — « *ça va* » — : on découpe la ligne en
    tronçons colorés ou non, puis chaque tronçon en mots."""
    lignes = []
    for ligne in groupe.split("/"):
        mots = []
        for m in re.finditer(r"([*!+])(.+?)\1|([^*!+]+)", ligne):
            couleur = COULEURS[m.group(1)] if m.group(1) else None
            for jeton in (m.group(2) or m.group(3) or "").split():
                propre = re.sub(r"[.,:;!?«»\"()…]", "", jeton).strip().replace("'", "’")
                if propre:
                    mots.append((propre.upper(), couleur))
        if mots:
            lignes.append(mots)
    return lignes

# ————————————————————————— la voix —————————————————————————

def voix_eleven(ident, texte):
    """ElevenLabs : la voix des vidéos de référence, avec l'instant de chaque mot."""
    import voix_eleven as ve
    empreinte = hashlib.sha1(f"eleven|{VOIX_ELEVEN}|{ve.MODELE}|{texte}".encode("utf-8")).hexdigest()[:10]
    mp3, js = os.path.join(CACHE, "voix", f"{ident}.mp3"), os.path.join(CACHE, "voix", f"{ident}.json")
    if os.path.exists(js):
        d = json.load(open(js, encoding="utf-8"))
        if d.get("empreinte") == empreinte and os.path.exists(mp3):
            return mp3, d
    d = ve.synthetiser(texte, VOIX_ELEVEN, mp3, js)
    d["empreinte"] = empreinte
    json.dump(d, open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"    ElevenLabs : {d['duree']:.1f} s · {len(texte)} caractères")
    return mp3, d

def synthetiser(ident, texte):
    """Rend (chemin audio, données JSON) : ElevenLabs si une voix est choisie et la
    clé posée, sinon la synthèse macOS."""
    if VOIX_ELEVEN:
        import voix_eleven as ve
        if ve.cle(): return voix_eleven(ident, texte)
        print("    (voix ElevenLabs choisie mais pas de clé : voix macOS à la place)")
    empreinte = hashlib.sha1((VOIX + texte + open(ici("voix.swift"), encoding="utf-8").read()).encode("utf-8")).hexdigest()[:10]
    caf, js, txt = os.path.join(CACHE, "voix", f"{ident}.caf"), os.path.join(CACHE, "voix", f"{ident}.json"), os.path.join(CACHE, "voix", f"{ident}.txt")
    if os.path.exists(js):
        d = json.load(open(js, encoding="utf-8"))
        if d.get("empreinte") == empreinte and os.path.exists(caf):
            return caf, d
    open(txt, "w", encoding="utf-8").write(texte)
    r = subprocess.run(["swift", ici("voix.swift"), VOIX, txt, caf, js], capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(js):
        raise SystemExit(f"voix.swift a échoué pour {ident} :\n{r.stderr[-800:]}")
    d = json.load(open(js, encoding="utf-8"))
    d["empreinte"] = empreinte
    json.dump(d, open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return caf, d

def dater_groupes(groupes, texte, mots):
    """L'instant où chaque groupe apparaît : celui du premier de ses mots dans la voix.

    On retrouve chaque groupe par sa position dans le texte lu, puis on prend le
    premier mot daté qui tombe dans cette plage. Un groupe sans mot daté (ça
    n'arrive pas, mais) hérite d'un instant interpolé entre ses voisins."""
    debuts, curseur = [], 0
    for g in groupes:
        propre = narration([g])
        i = texte.index(propre, curseur)
        debuts.append((i, i + len(propre)))
        curseur = i + len(propre)
    instants = [None] * len(groupes)
    for m in mots:
        pos = m["debut"]
        for k, (a, b) in enumerate(debuts):
            if a <= pos < b:
                if instants[k] is None or m["t"] < instants[k]:
                    instants[k] = m["t"]
                break
    # interpolation des trous
    for k in range(len(instants)):
        if instants[k] is None:
            prev = next((instants[j] for j in range(k - 1, -1, -1) if instants[j] is not None), 0.0)
            nxt = next((instants[j] for j in range(k + 1, len(instants)) if instants[j] is not None), None)
            instants[k] = prev + 0.4 if nxt is None else (prev + nxt) / 2
    return instants

# ————————————————————————— les images —————————————————————————

def couvrir(im, l, h):
    """Recadre l'image pour remplir l × h sans déformer."""
    r = max(l / im.width, h / im.height)
    im = im.resize((max(l, round(im.width * r)), max(h, round(im.height * r))), Image.LANCZOS)
    x, y = (im.width - l) // 2, (im.height - h) // 2
    return im.crop((x, y, x + l, y + h))

_fonds = {}
def fond_tableau(fichier):
    """Le fond assombri et vignetté, comme dans les références. Mis en cache.
    « fichier » est un chemin relatif à l'atelier : tableaux/… ou photos/<id>/…"""
    if fichier in _fonds: return _fonds[fichier]
    im = couvrir(Image.open(ici(fichier)).convert("RGB"), L, H)
    # assombrissement uniforme, puis un vignettage doux
    im = Image.blend(im, Image.new("RGB", (L, H), NOIR), 0.42)
    masque = Image.new("L", (L, H), 0)
    d = ImageDraw.Draw(masque)
    d.ellipse((-L * 0.25, -H * 0.45, L * 1.25, H * 1.45), fill=255)
    masque = masque.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(im, Image.new("RGB", (L, H), NOIR), masque)
    _fonds[fichier] = im
    return im

_polices = {}
def police(taille):
    if taille not in _polices: _polices[taille] = ImageFont.truetype(POLICE, taille)
    return _polices[taille]

def largeur_ligne(mots, f, espace):
    return sum(f.getlength(m) for m, _ in mots) + espace * (len(mots) - 1)

def ecrire_ligne(d, x, y, mots, f, espace):
    """Écrit une ligne mot par mot, chacun dans sa couleur, avec contour et ombre."""
    for mot, couleur in mots:
        d.text((x + 3, y + 4), mot, font=f, fill=(0, 0, 0, 170))
        d.text((x, y), mot, font=f, fill=couleur or BLANC, stroke_width=3, stroke_fill=NOIR)
        x += f.getlength(mot) + espace

# Les emplacements du texte, loin du médaillon (centre bas). On les enchaîne dans
# un ordre fixe : les références bougent le texte d'un groupe à l'autre.
ANCRES = [("droite", 70), ("gauche", 300), ("droite", 220), ("gauche", 70), ("droite", 340), ("gauche", 180)]

def replier(mots, f, espace, largeur_max):
    """Coupe une ligne de mots en plusieurs si elle dépasse la largeur permise."""
    lignes, courante = [], []
    for mot in mots:
        essai = courante + [mot]
        if courante and largeur_ligne(essai, f, espace) > largeur_max:
            lignes.append(courante); courante = [mot]
        else:
            courante = essai
    if courante: lignes.append(courante)
    return lignes

def ecrire_groupe(im, groupe, rang, noir=False):
    lignes = lignes_affichees(groupe)
    if not lignes: return im
    d = ImageDraw.Draw(im, "RGBA")
    cote, y = ANCRES[rang % len(ANCRES)]
    if noir:
        # sur fond noir, les mots se posent en escalier depuis le coin
        cote, y = ("gauche", 150) if rang % 2 == 0 else ("droite", 120)
    marge = 64
    # la ligne large peut se replier ; les lignes étroites aussi, plus rarement
    rendu = []
    for k, mots in enumerate(lignes):
        grande = (k == 0)
        f = police(50 if grande else 30)
        espace = 14 if grande else 9
        for morceau in replier(mots, f, espace, L - 2 * marge - 40):
            rendu.append((grande, f, espace, morceau))
    for k, (grande, f, espace, mots) in enumerate(rendu):
        w = largeur_ligne(mots, f, espace)
        decal = k * 34            # l'escalier des lignes suivantes
        x = (marge + decal) if cote == "gauche" else (L - marge - w - decal)
        x = max(24, min(x, L - 24 - w))
        ecrire_ligne(d, x, y, mots, f, espace)
        y += (58 if grande else 38)
    return im

def cadre_produit(fond):
    """La fin : le produit au centre, le nom du site, et le badge rouge."""
    im = fond.convert("RGBA")
    d = ImageDraw.Draw(im, "RGBA")
    # le visuel du site, encadré et ombré
    pl = 470; prod = PRODUIT.resize((pl, round(PRODUIT.height * pl / PRODUIT.width)), Image.LANCZOS)
    px, py = 64, 92
    ombre = Image.new("RGBA", (prod.width + 60, prod.height + 60), (0, 0, 0, 0))
    ImageDraw.Draw(ombre).rectangle((30, 40, prod.width + 30, prod.height + 40), fill=(0, 0, 0, 180))
    ombre = ombre.filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(ombre, (px - 30, py - 30))
    d.rectangle((px - 4, py - 4, px + prod.width + 4, py + prod.height + 4), fill=(248, 244, 236, 255))
    im.paste(prod, (px, py))
    # le texte, à droite
    d = ImageDraw.Draw(im, "RGBA")
    f1, f2, f3 = police(52), police(30), police(22)
    x = px + prod.width + 42
    ecrire_ligne(d, x, 128, [("FAIS", None), ("LE", None), ("TEST", COULEURS["*"])], f1, 14)
    ecrire_ligne(d, x, 200, [("SEIZE", None), ("SITUATIONS", None)], f2, 9)
    ecrire_ligne(d, x, 240, [("QUATORZE", None), ("ÉMOTIONS", None)], f2, 9)
    ecrire_ligne(d, x, 296, [(SITE.upper(), COULEURS["+"])], f3, 9)
    # le badge rouge
    fb = police(34); texte = "LIEN EN BIO"; tw = fb.getlength(texte)
    bx, by = x, 360
    d.rectangle((bx, by, bx + tw + 44, by + 62), fill=ROUGE_BADGE + (255,))
    d.text((bx + 22, by + 11), texte, font=fb, fill=BLANC)
    return im.convert("RGB")

# ————————————————————————— la ligne de temps —————————————————————————

_lum = {}
def luminance(fichier):
    """La clarté moyenne d'un tableau (0–255), calculée une fois sur une vignette."""
    if fichier not in _lum:
        im = Image.open(ici(fichier)).convert("L").resize((64, 36))
        _lum[fichier] = sum(im.getdata()) / (64 * 36)
    return _lum[fichier]

def photos_du_theme(ident):
    """Les photos collectées pour cette vidéo (photos.py), avec leurs crédits."""
    manif = ici("photos", f"{ident}.json")
    if not os.path.exists(manif): return []
    return [f for f in json.load(open(manif, encoding="utf-8"))
            if os.path.exists(ici("photos", ident, f["fichier"]))]

def tableaux_pour(ident, n):
    """n fonds distincts pour cette vidéo, tirés au sort de façon reproductible parmi
    les photos de son thème. Rend des chemins relatifs à l'atelier."""
    photos = photos_du_theme(ident)
    if len(photos) < 12:
        raise SystemExit(f"{ident} : pas assez de photos — lance d'abord  python3 photos.py {ident[:2]}")
    alea = random.Random(ident)
    pool = [os.path.join("photos", ident, f["fichier"]) for f in photos
            if luminance(os.path.join("photos", ident, f["fichier"])) >= 40]
    alea.shuffle(pool)
    if len(pool) < n: pool = pool * (n // max(len(pool), 1) + 1)
    return pool[:n]

def credits_photos(ident, fichiers):
    """Les crédits obligatoires (CC BY) des photos utilisées ; vide pour Pexels et le CC0."""
    par_fichier = {os.path.join("photos", ident, f["fichier"]): f for f in photos_du_theme(ident)}
    lignes = sorted({par_fichier[f]["credit"] for f in fichiers if f in par_fichier and par_fichier[f].get("credit")})
    return lignes

def instants_lecture(groupes):
    """Sans voix : chaque groupe reste le temps de se lire, posément.

    Une base pour poser le regard, puis un temps par mot ; les phrases très
    courtes ne clignotent pas, les longues ne s'éternisent pas. Les trois
    groupes de l'accroche, sur fond noir, prennent un peu plus de temps."""
    instants, t = [], 0.6
    for k, g in enumerate(groupes):
        mots = len(narration([g]).split())
        d = 1.1 + 0.30 * mots
        d = max(1.8, min(d, 4.6))
        if k < 3: d += 0.4
        instants.append(round(t, 3)); t += d
    return instants, round(t, 3)

def construire(script, apercu=False):
    ident = script["id"]
    groupes = script["groupes"]
    texte = narration(groupes)
    if SANS_VOIX:
        caf = None
        instants, fin_voix = instants_lecture(groupes)
    else:
        caf, voix = synthetiser(ident, texte)
        instants = dater_groupes(groupes, texte, voix["mots"])
        fin_voix = min(voix["duree"], voix.get("fin", voix["duree"]))
    duree = fin_voix + SORTIE_FINALE
    noir = script["noir"]

    # L'image ne change qu'avec le texte : une photo neuve à chaque phrase, posée à
    # l'instant exact où la phrase apparaît. Le dernier groupe (« Fais le test… »)
    # garde la photo de la phrase précédente sous le produit.
    cuts_tableaux = instants[noir:len(groupes) - 1]
    coupes = sorted(set([0.0] + instants + [duree]))
    # on écarte les coupes trop proches (moins d'une image) pour ne pas produire de durées nulles
    propres = [coupes[0]]
    for c in coupes[1:]:
        if c - propres[-1] >= 1 / FPS: propres.append(c)
    coupes = propres

    fichiers_tableaux = tableaux_pour(ident, len(cuts_tableaux))
    dossier = os.path.join(CACHE, "images", ident); os.makedirs(dossier, exist_ok=True)
    liste, cache = [], {}

    for k in range(len(coupes) - 1):
        t0, t1 = coupes[k], coupes[k + 1]
        # quel groupe est affiché ? le dernier dont l'instant est ≤ t0
        g = max((i for i, ti in enumerate(instants) if ti <= t0 + 1e-6), default=None)
        # quel tableau ? le dernier cut ≤ t0
        idx_tab = max((i for i, tc in enumerate(cuts_tableaux) if tc <= t0 + 1e-6), default=None)
        sur_noir = g is None or g < noir
        produit = g is not None and g >= len(groupes) - 1
        cle = ("noir" if sur_noir else fichiers_tableaux[idx_tab if idx_tab is not None else 0], g, produit)
        if cle not in cache:
            if sur_noir:
                im = Image.new("RGB", (L, H), NOIR)
                if g is not None: im = ecrire_groupe(im, groupes[g], g, noir=True)
            else:
                im = fond_tableau(cle[0]).copy()     # jamais écrire sur l'image en cache
                if produit:
                    im = cadre_produit(im)
                else:
                    im = ecrire_groupe(im, groupes[g], g)
            chemin = os.path.join(dossier, f"{len(cache):03d}.png")
            im.save(chemin, "PNG", compress_level=3)
            cache[cle] = chemin
        liste.append((cache[cle], t1 - t0))

    if apercu:
        print(f"  {ident} : {len(cache)} images-clés dans images/{ident}/ (durée {duree:.1f} s)")
        return

    # la liste pour ffmpeg (le dernier fichier est répété : c'est ce que le format exige)
    lst = os.path.join(dossier, "liste.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for chemin, d in liste:
            f.write(f"file '{chemin}'\nduration {d:.4f}\n")
        f.write(f"file '{liste[-1][0]}'\n")

    musique = ici("musiques", script["musique"])
    nom = f"{ident[:2]} - {script['titre']}"
    sortie = os.path.join(SORTIE, f"{nom}.mp4")
    fondu = max(duree - 3.0, 0)
    if caf is None:
        filtre = (f"[1:a]aresample=44100,atrim=0:{duree:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.5,"
                  f"afade=t=out:st={fondu:.3f}:d=3,volume=0.55[a]")
        entrees = ["-i", musique]
    else:
        # La voix sort du synthétiseur à basse cadence ; sans rééchantillonnage, amix
        # alignait la musique dessus et l'abîmait. Tout passe à 44,1 kHz d'abord.
        filtre = (f"[2:a]aresample=44100,atrim=0:{duree:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.2,"
                  f"afade=t=out:st={fondu:.3f}:d=3,volume=0.16[m];"
                  f"[1:a]aresample=44100,atrim=0:{duree:.3f},apad=whole_dur={duree:.3f}[v];"
                  f"[v][m]amix=inputs=2:duration=first:normalize=0[a]")
        entrees = ["-i", caf, "-i", musique]
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
           *entrees, "-filter_complex", filtre,
           "-map", "0:v", "-map", "[a]", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium",
           "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
           "-t", f"{duree:.3f}", "-movflags", "+faststart", sortie]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"ffmpeg a échoué pour {ident} :\n{r.stderr[-1500:]}")

    # la légende, avec le lien de l'article et le crédit musique (obligatoire, CC BY)
    titre_musique = script["musique"].replace(".mp3", "").replace("---", " - ").replace("-", " ")
    legende = (f"{script['legende']}\n\n"
               f"Pour aller plus loin : {SITE}/guide/{script['article']}.html\n"
               f"Le test : {SITE} (lien en bio)\n\n"
               f"#émotions #psychologie #{script['penseur'].lower().replace(' ', '').replace('é', 'e')} "
               f"#développementpersonnel #boussoleémotionnelle\n\n"
               f"Musique : « {titre_musique} » — Kevin MacLeod (incompetech.com), licence CC BY 4.0\n")
    creds = credits_photos(ident, fichiers_tableaux)
    legende += ("Photos : " + " · ".join(creds) + "\n") if creds else "Photos : Pexels\n"
    open(os.path.join(SORTIE, f"{nom} (légende).txt"), "w", encoding="utf-8").write(legende.replace("'", "’"))
    taille = os.path.getsize(sortie) / 1e6
    print(f"  {nom} : {duree:.1f} s · {taille:.1f} Mo")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apercu = "--apercu" in sys.argv
    choisis = [s for s in SCRIPTS if not args or any(s["id"].startswith(a) for a in args)]
    print(f"{len(choisis)} vidéo(s) → {SORTIE}")
    for s in choisis:
        construire(s, apercu=apercu)
