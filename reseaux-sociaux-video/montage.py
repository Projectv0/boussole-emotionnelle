#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le montage : les mots au rythme d'une voix off, des images qui bougent, des transitions.

Le générateur décide quoi montrer (les phrases, les images, la fin) ; ce module décide
quand et comment, image par image, à 30 images par seconde :

  · LE RYTHME. Sans voix, chaque mot apparaît à l'instant où une voix off le dirait :
    un mot long prend plus de temps qu'un mot court, une virgule fait respirer, un
    point marque un vrai temps. Quand une phrase est dite en entier, elle reste le
    temps de finir de la lire, puis la suivante arrive. Le tout est accéléré pour que
    chaque vidéo dure 50 s (DUREE_VISEE) : environ 160 mots par minute, le débit d'une
    voix off. Avec une voix (SANS_VOIX = False), ce sont les instants de la voix.
  · LES MOTS. Chacun arrive en fondu, en remontant de quelques pixels ; les mots en
    couleur arrivent un peu plus gros et se posent. La phrase d'avant s'efface quand
    la suivante commence.
  · LES IMAGES. Chaque image bouge lentement pendant qu'on lit : elle avance, recule,
    ou glisse d'un côté — vers les visages quand il y en a.
  · LES TRANSITIONS. L'image change au moment exact où la phrase change, par un fondu,
    une poussée latérale, un zoom ou un flou, en alternance.
  · LA FIN. Le bandeau monte du bas, la question se pose mot à mot.

Les images sont rendues en mémoire et envoyées directement à ffmpeg.
"""
import math, os, random, re, subprocess
from PIL import Image, ImageDraw, ImageFilter
import generateur as G

L, H, FPS = G.L, G.H, G.FPS
NOIR, BLANC = G.NOIR, G.BLANC

# — le rythme d'une voix off posée —
DUREE_VISEE = 50.0          # chaque vidéo dure 50 s : le rythme ci-dessous est accéléré d'autant
                            # (de ~130 à ~160 mots par minute, le débit d'une voix off)
DEBUT = 0.5                 # le noir avant le premier mot
TENUE = 0.75                # une phrase dite en entier reste ce temps-là avant la suivante
TENUE_ACCROCHE = 1.15       # un peu plus pour les trois phrases de l'accroche, sur fond noir
FIN = 4.5                   # la page de fin reste ce temps-là
PAUSES = {",": 0.24, ";": 0.32, ":": 0.32, ".": 0.42, "!": 0.42, "?": 0.42, "…": 0.45}
PAUSE_LIGNE = 0.12          # le petit souffle d'un « / »

# — les effets —
APPARITION = 0.18           # un mot met ce temps à apparaître
EFFACEMENT = 0.20           # la phrase d'avant s'efface en ce temps-là
TRANSITION = 0.55           # durée d'un changement d'image
MONTEE_BANDEAU = 0.55
TRANSITIONS = ["fondu", "glisse", "zoom", "flou"]
MOUVEMENTS = ["avant", "gauche", "arriere", "droite"]

def lisse(p):          # accélère puis ralentit
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, p)))

def sortie_douce(p):   # démarre vite, se pose
    p = max(0.0, min(1.0, p))
    return 1 - (1 - p) ** 3

# ————————————————————————— le rythme —————————————————————————

def syllabes(mot):
    """Le nombre de syllabes d'un mot français, à une près : les groupes de voyelles,
    moins le « e » muet final (« porte », « portes »)."""
    m = mot.lower().replace("’", "")
    n = len(re.findall(r"[aeiouyàâäéèêëîïôöùûüœæ]+", m))
    if n > 1 and re.search(r"[^aeiouyàâäéèêëîïôöùûüœæ]es?$", m):
        n -= 1
    return max(1, n)

def duree_mot(mot):
    return 0.10 + 0.17 * syllabes(mot)

def dire(groupe, debut):
    """Les instants où chaque mot affiché d'un groupe est dit, et la fin de la parole."""
    lignes, ponctuations = G.lignes_affichees(groupe, avec_ponctuation=True)
    instants, t, dernier = [], debut, None
    for mots, ponct in zip(lignes, ponctuations):
        for k, ((mot, _), signes) in enumerate(zip(mots, ponct)):
            instants.append(t)
            pause = max([PAUSES.get(c, 0) for c in signes] + [PAUSE_LIGNE if k == len(mots) - 1 else 0])
            t += duree_mot(mot) + pause
            dernier = (instants[-1], mot)
    fin_parole = dernier[0] + duree_mot(dernier[1]) if dernier else debut
    return instants, fin_parole

def chronologie(groupes, visee=None):
    """[{debut, mots: [instants]}] pour chaque groupe, et la durée totale.

    Avec « visee », tout le texte est accéléré dans la même proportion — les mots, les
    pauses, les tenues — pour que la vidéo dure ce temps-là ; jamais ralenti."""
    visee = DUREE_VISEE if visee is None else visee
    out, t = [], DEBUT
    for k, g in enumerate(groupes):
        instants, fin = dire(g, t)
        out.append({"debut": t, "mots": instants})
        t = fin + (TENUE_ACCROCHE if k < 3 else TENUE)
    duree = out[-1]["debut"] + FIN
    if visee and duree > visee:
        f = (visee - FIN - DEBUT) / (duree - FIN - DEBUT)
        acc = lambda x: DEBUT + (x - DEBUT) * f
        out = [{"debut": acc(g["debut"]), "mots": [acc(m) for m in g["mots"]]} for g in out]
        duree = out[-1]["debut"] + FIN
    return out, duree

def chronologie_voix(groupes, voix):
    """Avec une voix : chaque mot affiché prend l'instant où la voix le dit. Les mots
    de la voix sans lettre (un « ? » isolé) sont sautés ; si les deux listes ne
    s'accordent pas, on revient au rythme calculé."""
    dits = [m["t"] for m in voix["mots"] if re.search(r"\w", m["mot"])]
    affiches = [len([w for l in G.lignes_affichees(g) for w in l]) for g in groupes]
    if sum(affiches) != len(dits):
        print(f"    (voix : {len(dits)} mots dits pour {sum(affiches)} affichés — rythme calculé à la place)")
        return chronologie(groupes)
    out, i = [], 0
    for n in affiches:
        out.append({"debut": dits[i], "mots": dits[i:i + n]}); i += n
    return out, min(voix["duree"], voix.get("fin", voix["duree"])) + G.SORTIE_FINALE

# ————————————————————————— les mots —————————————————————————

_sprites = {}
def sprite(mot, couleur, f):
    """Un mot prêt à poser — contour noir, ombre portée — et le décalage de son origine."""
    cle = (mot, couleur, f.size)
    if cle not in _sprites:
        l, t, r, b = f.getbbox(mot, stroke_width=3)
        m = 8
        im = Image.new("RGBA", (int(r - l) + 2 * m + 4, int(b - t) + 2 * m + 5), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        ox, oy = m - l, m - t
        d.text((ox + 3, oy + 4), mot, font=f, fill=(0, 0, 0, 170))
        d.text((ox, oy), mot, font=f, fill=(couleur or BLANC) + (255,), stroke_width=3, stroke_fill=NOIR)
        _sprites[cle] = (im, int(ox), int(oy))
    return _sprites[cle]

def mots_places(places):
    """Chaque mot d'un groupe disposé : [(sprite, x, y, en_couleur)], dans l'ordre de lecture."""
    out = []
    for x, y, w, grande, f, espace, mots in places:
        for mot, couleur in mots:
            im, ox, oy = sprite(mot, couleur, f)
            out.append((im, int(x) - ox, int(y) - oy, couleur is not None))
            x += f.getlength(mot) + espace
    return out

def avec_opacite(im, a):
    if a >= 0.999: return im
    im = im.copy()
    im.putalpha(im.getchannel("A").point(lambda v: int(v * a)))
    return im

def poser_mots(cadre, mots, instants, t, opacite=1.0):
    """Pose sur le cadre les mots déjà dits à l'instant t, le dernier en train d'apparaître."""
    for (im, x, y, couleur), a in zip(mots, instants):
        if t < a: break
        p = (t - a) / APPARITION
        if p >= 1:
            s = avec_opacite(im, opacite)
            cadre.paste(s, (x, y), s)
            continue
        e = sortie_douce(p)
        s = im
        dx = dy = 0
        if couleur:                             # le mot en couleur arrive plus gros et se pose
            k = 1.28 - 0.28 * e
            s = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.BILINEAR)
            dx, dy = (im.width - s.width) // 2, (im.height - s.height) // 2
        dy += round(12 * (1 - e))
        s = avec_opacite(s, e * opacite)
        cadre.paste(s, (x + dx, y + dy), s)

def poser_ombre(cadre, masque, a):
    """Le voile sombre derrière le texte, à l'opacité a."""
    if masque is None or a <= 0.01: return
    if a < 0.999:
        masque = masque.point(lambda v: int(v * a))
    cadre.paste(NOIR, (0, 0, L, H), masque)

# ————————————————————————— les images —————————————————————————

def cadre_mobile(plan, t):
    """L'image d'un plan à l'instant t, avec son mouvement lent."""
    base = plan["image"]
    u = lisse((t - plan["debut"]) / max(0.1, plan["fin"] + TRANSITION - plan["debut"]))
    fx, fy = plan["foyer"]
    mvt = plan["mouvement"]
    if mvt == "avant":      z, cx, cy = 1.0 + 0.075 * u, fx, fy
    elif mvt == "arriere":  z, cx, cy = 1.075 - 0.075 * u, fx, fy
    elif mvt == "gauche":   z, cx, cy = 1.065, fx + 0.028 - 0.056 * u, fy
    else:                   z, cx, cy = 1.065, fx - 0.028 + 0.056 * u, fy
    return zoomer(base, z, cx, cy)

def zoomer(im, z, cx=0.5, cy=0.5):
    if abs(z - 1) < 1e-3: return im
    w, h = L / z, H / z
    x0 = min(max(cx * L - w / 2, 0), L - w); y0 = min(max(cy * H - h / 2, 0), H - h)
    return im.transform((L, H), Image.EXTENT, (x0, y0, x0 + w, y0 + h), Image.BILINEAR)

def transition(a, b, p, genre, sens):
    """Le passage de l'image a à l'image b, p allant de 0 à 1."""
    e = lisse(p)
    if genre == "glisse":
        out = Image.new("RGB", (L, H))
        out.paste(a, (int(-sens * L * e), 0)); out.paste(b, (int(sens * L * (1 - e)), 0))
        return out
    if genre == "zoom":
        return Image.blend(zoomer(a, 1 + 0.30 * e), zoomer(b, 1.18 - 0.18 * e), e)
    if genre == "flou":
        r = 9 * math.sin(math.pi * p)
        if r > 0.6:
            a, b = a.filter(ImageFilter.GaussianBlur(r)), b.filter(ImageFilter.GaussianBlur(r))
        return Image.blend(a, b, e)
    return Image.blend(a, b, e)

# ————————————————————————— le montage —————————————————————————

def preparer(script, chrono, duree, fonds, visages_par_fond):
    """Tout ce qui ne dépend pas de l'instant : les plans, les mots placés, les voiles."""
    groupes, noir = script["groupes"], script["noir"]
    alea = random.Random(script["id"])
    genres = TRANSITIONS[:]; alea.shuffle(genres)
    mvts = MOUVEMENTS[:]; alea.shuffle(mvts)
    plans = []
    for j, g in enumerate(range(noir, len(groupes) - 1)):
        visages = visages_par_fond[j]
        if visages:
            fx = sum((c[0] + c[2]) / 2 for c, _ in visages) / len(visages) / L
            fy = sum((c[1] + c[3]) / 2 for c, _ in visages) / len(visages) / H
        else:
            fx, fy = 0.5, 0.45
        fin = chrono[g + 1]["debut"] if g + 2 < len(groupes) else duree
        plans.append({"debut": chrono[g]["debut"], "fin": fin, "image": fonds[j], "foyer": (fx, fy),
                      "mouvement": mvts[j % len(mvts)],
                      "transition": "fondu" if j == 0 else genres[j % len(genres)],
                      "sens": 1 if j % 2 else -1})
    textes = []
    for g, grp in enumerate(groupes[:-1]):
        sur_noir = g < noir
        visages = None if sur_noir or not G.ILLUSTRATIONS else visages_par_fond[g - noir]
        places = G.placer_groupe(grp, g, noir=sur_noir, eviter=visages)
        masque = G.ombre_douce(G.emprise(places)) if (visages is not None and places) else None
        textes.append({"mots": mots_places(places), "instants": chrono[g]["mots"],
                       "debut": chrono[g]["debut"], "fin": chrono[g + 1]["debut"], "masque": masque})
    # la fin : la question, mot à mot, et le bandeau
    dernier = chrono[-1]["debut"]
    visages_fin = visages_par_fond[-1] if G.ILLUSTRATIONS else None
    lignes, boite = G.placer_question(visages_fin)
    f = G.police(50)
    places = [(x, y, 0, True, f, 14, mots) for x, y, mots in lignes]
    instants, t = [], dernier + 0.45            # « ET · TOI, · OÙ · EN · ES-TU · ? », au même rythme
    for mot, _ in lignes[0][2] + lignes[1][2]:
        instants.append(t)
        nu = mot.strip(",?")
        t += (duree_mot(nu) if nu else 0.05) + max([PAUSES.get(c, 0) for c in mot] + [0])
    fin = {"debut": dernier, "mots": mots_places(places), "instants": instants,
           "masque": G.ombre_douce(boite) if G.ILLUSTRATIONS else None, "bandeau": G.couche_bandeau()}
    return plans, textes, fin

def image_au_temps(t, plans, textes, fin):
    # le fond
    plan = None
    for j, p in enumerate(plans):
        if p["debut"] <= t + 1e-9: plan = j
    if plan is None:
        cadre = Image.new("RGB", (L, H), NOIR)
    else:
        p = plans[plan]
        cadre = cadre_mobile(p, t)
        if t < p["debut"] + TRANSITION:
            avant = cadre_mobile(plans[plan - 1], t) if plan > 0 else Image.new("RGB", (L, H), NOIR)
            cadre = transition(avant, cadre, (t - p["debut"]) / TRANSITION, p["transition"], p["sens"])
    # le texte : la phrase en cours, et celle d'avant qui s'efface
    for k, tx in enumerate(textes):
        if tx["debut"] <= t < tx["fin"]:
            poser_ombre(cadre, tx["masque"], sortie_douce((t - tx["debut"]) / 0.25))
            poser_mots(cadre, tx["mots"], tx["instants"], t)
        elif tx["fin"] <= t < tx["fin"] + EFFACEMENT:
            a = 1 - (t - tx["fin"]) / EFFACEMENT
            poser_ombre(cadre, tx["masque"], a)
            poser_mots(cadre, tx["mots"], tx["instants"], t, opacite=a)
    # la fin
    if t >= fin["debut"]:
        dt = t - fin["debut"]
        poser_ombre(cadre, fin["masque"], sortie_douce((dt - 0.35) / 0.3))
        poser_mots(cadre, fin["mots"], fin["instants"], t)
        y = H - G.HAUT_BANDEAU + round((G.HAUT_BANDEAU + 10) * (1 - sortie_douce(dt / MONTEE_BANDEAU)))
        cadre.paste(fin["bandeau"], (0, y), fin["bandeau"])
    return cadre

def monter(script, fonds, visages_par_fond, sortie, musique, voix=None, apercu=None):
    """Rend la vidéo dans « sortie ». apercu : un dossier où poser, au lieu de la vidéo,
    une image par phrase (le moment où elle est entière) et la page de fin."""
    groupes = script["groupes"]
    chrono, duree = chronologie_voix(groupes, voix[1]) if voix else chronologie(groupes)
    plans, textes, fin = preparer(script, chrono, duree, fonds, visages_par_fond)
    if apercu:
        os.makedirs(apercu, exist_ok=True)
        for vieux in os.listdir(apercu):
            if vieux.endswith(".png"): os.remove(os.path.join(apercu, vieux))
        moments = [tx["fin"] - 0.05 for tx in textes] + [duree - 0.1]
        for k, t in enumerate(moments):
            image_au_temps(t, plans, textes, fin).save(os.path.join(apercu, f"{k:03d}.png"))
        return duree, len(moments)
    fondu = max(duree - 3.0, 0)
    if voix is None:
        filtre = (f"[1:a]aresample=44100,atrim=0:{duree:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.5,"
                  f"afade=t=out:st={fondu:.3f}:d=3,volume=0.55[a]")
        entrees = ["-i", musique]
    else:
        filtre = (f"[2:a]aresample=44100,atrim=0:{duree:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.2,"
                  f"afade=t=out:st={fondu:.3f}:d=3,volume=0.16[m];"
                  f"[1:a]aresample=44100,atrim=0:{duree:.3f},apad=whole_dur={duree:.3f}[v];"
                  f"[v][m]amix=inputs=2:duration=first:normalize=0[a]")
        entrees = ["-i", voix[0], "-i", musique]
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{L}x{H}",
           "-framerate", str(FPS), "-i", "-", *entrees, "-filter_complex", filtre,
           "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "44100",
           "-t", f"{duree:.3f}", "-movflags", "+faststart", sortie]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        for n in range(int(math.ceil(duree * FPS))):
            proc.stdin.write(image_au_temps(n / FPS, plans, textes, fin).tobytes())
        proc.stdin.close()
    except BrokenPipeError:
        pass
    err = proc.stderr.read().decode("utf-8", "replace")
    if proc.wait() != 0:
        raise SystemExit(f"ffmpeg a échoué pour {script['id']} :\n{err[-1500:]}")
    return duree, None
