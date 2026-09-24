#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique les vidéos, une par script, dans le style des références.

    python3 generateur.py                # les vingt
    python3 generateur.py 03 17          # celles-là seulement
    python3 generateur.py --apercu 03    # juste les images-clés, sans vidéo

Le style, tel qu'il a été lu dans les trois vidéos de référence :
  · paysage 16:9, une minute environ, 30 images par seconde ;
  · une accroche sur fond noir, les mots posés un par un, un mot en couleur ;
  · puis un tableau de maître assombri, qui change toutes les deux secondes,
    un personnage fixe devant (ici le médaillon de la Boussole), et les mots
    qui apparaissent quand la voix les dit ;
  · à la fin, le produit et un badge rouge « LIEN EN BIO ».

Ce qu'on assemble :
  scripts.py       les vingt textes, groupe de mots par groupe de mots
  voix.swift       la voix de macOS, qui date chaque mot
  tableaux/        des peintures du domaine public (voir tableaux.py)
  musiques/        Kevin MacLeod, CC BY — le crédit part dans la légende
  medaillon.png    le personnage fixe
  ../og.jpg        l'image du site, montrée à la fin comme « le produit »

Sortie : sortie/<id>.mp4 et sortie/<id>.legende.txt.
"""
import hashlib, json, math, os, random, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from scripts import SCRIPTS

ICI = os.path.dirname(os.path.abspath(__file__))
def ici(*p): return os.path.join(ICI, *p)
for d in ("voix", "sortie", "images"): os.makedirs(ici(d), exist_ok=True)

L, H, FPS = 1024, 576, 30
VOIX = "Jacques"
POLICE = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
CADENCE_TABLEAU = 2.3        # secondes entre deux tableaux
SORTIE_FINALE = 4.0          # le produit reste à l'écran après le dernier mot
SITE = "boussole-emotionnelle.fr"

BLANC, NOIR = (255, 255, 255), (0, 0, 0)
COULEURS = {"*": (245, 208, 0), "!": (224, 48, 48), "+": (46, 204, 113)}   # jaune, rouge, vert
ROUGE_BADGE = (196, 22, 22)

MANIFESTE = json.load(open(ici("tableaux.json"), encoding="utf-8"))
MEDAILLON = Image.open(ici("medaillon.png")).convert("RGBA")
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
                propre = re.sub(r"[.,:;!?«»\"()…]", "", jeton).strip()
                if propre:
                    mots.append((propre.upper(), couleur))
        if mots:
            lignes.append(mots)
    return lignes

# ————————————————————————— la voix —————————————————————————

def enregistrement_humain(ident):
    """Le fichier déposé dans enregistrement/ pour cette vidéo, s'il existe."""
    for ext in ("m4a", "wav", "mp3", "aiff", "aif", "caf", "flac", "ogg"):
        p = ici("enregistrement", f"{ident}.{ext}")
        if os.path.exists(p): return p
    return None

def voix_humaine(ident, texte, source):
    """Une vraie voix : convertie en wav, puis calée mot à mot sur le texte par aligner.py."""
    st = os.stat(source)
    empreinte = hashlib.sha1(f"humaine|{texte}|{st.st_size}|{int(st.st_mtime)}".encode("utf-8")).hexdigest()[:10]
    wav, js, txt = ici("voix", f"{ident}.wav"), ici("voix", f"{ident}.json"), ici("voix", f"{ident}.txt")
    if os.path.exists(js):
        d = json.load(open(js, encoding="utf-8"))
        if d.get("empreinte") == empreinte and os.path.exists(wav):
            return wav, d
    open(txt, "w", encoding="utf-8").write(texte)
    # mono, 44,1 kHz, coupe-bas contre le souffle et le grondement, niveau normalisé
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", source, "-ac", "1", "-ar", "44100",
                        "-af", "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11", wav], capture_output=True, text=True)
    if r.returncode != 0: raise SystemExit(f"conversion de {source} : {r.stderr[-500:]}")
    r = subprocess.run([sys.executable, ici("aligner.py"), wav, txt, js], capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(js):
        raise SystemExit(f"aligner.py a échoué pour {ident} :\n{r.stdout[-400:]}\n{r.stderr[-800:]}")
    d = json.load(open(js, encoding="utf-8")); d["empreinte"] = empreinte
    json.dump(d, open(js, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"    voix humaine : {r.stdout.strip()}")
    return wav, d

def synthetiser(ident, texte):
    """Rend (chemin audio, données JSON) : la voix humaine si elle est là, sinon la synthèse."""
    source = enregistrement_humain(ident)
    if source: return voix_humaine(ident, texte, source)
    empreinte = hashlib.sha1((VOIX + texte + open(ici("voix.swift"), encoding="utf-8").read()).encode("utf-8")).hexdigest()[:10]
    caf, js, txt = ici("voix", f"{ident}.caf"), ici("voix", f"{ident}.json"), ici("voix", f"{ident}.txt")
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
    """Le tableau assombri et vignetté, comme dans les références. Mis en cache."""
    if fichier in _fonds: return _fonds[fichier]
    im = couvrir(Image.open(ici("tableaux", fichier)).convert("RGB"), L, H)
    # assombrissement uniforme, puis un vignettage doux
    im = Image.blend(im, Image.new("RGB", (L, H), NOIR), 0.42)
    masque = Image.new("L", (L, H), 0)
    d = ImageDraw.Draw(masque)
    d.ellipse((-L * 0.25, -H * 0.45, L * 1.25, H * 1.45), fill=255)
    masque = masque.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(im, Image.new("RGB", (L, H), NOIR), masque)
    _fonds[fichier] = im
    return im

MED_H = 300
_med = MEDAILLON.resize((round(MEDAILLON.width * MED_H / MEDAILLON.height), MED_H), Image.LANCZOS)
def poser_medaillon(im):
    im = im.convert("RGBA")
    im.alpha_composite(_med, ((L - _med.width) // 2, H - _med.height + 36))
    return im.convert("RGB")

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
ANCRES = [("droite", 70), ("gauche", 190), ("droite", 200), ("gauche", 70), ("droite", 120), ("gauche", 240)]

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
        f = police(56 if grande else 32)
        espace = 14 if grande else 9
        for morceau in replier(mots, f, espace, L - 2 * marge - 40):
            rendu.append((grande, f, espace, morceau))
    for k, (grande, f, espace, mots) in enumerate(rendu):
        w = largeur_ligne(mots, f, espace)
        decal = k * 34            # l'escalier des lignes suivantes
        x = (marge + decal) if cote == "gauche" else (L - marge - w - decal)
        x = max(24, min(x, L - 24 - w))
        ecrire_ligne(d, x, y, mots, f, espace)
        y += (64 if grande else 40)
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
        im = Image.open(ici("tableaux", fichier)).convert("L").resize((64, 36))
        _lum[fichier] = sum(im.getdata()) / (64 * 36)
    return _lum[fichier]

# Les références n'utilisent que des scènes à personnages : foules, cours, batailles.
# Une nature morte ou un tigre, même assombris, cassent l'illusion. On écarte sur le
# titre — c'est grossier, mais c'est ce que le manifeste sait dire.
HORS_STYLE = re.compile(r"still life|nature morte|flowers?|fruit|apples?|roses?|chrysanth|vase|"
                        r"tiger|lion|horse[s]? (in|at)|cattle|sheep|dog|cat\b|bird|"
                        r"landscape|cliff|coast|seascape|haystack|water lil|garden|"
                        r"self-portrait|portrait of|study|sketch", re.I)

def tableaux_pour(ident, n):
    """n tableaux distincts, tirés au sort de façon reproductible pour cette vidéo.
    Les toiles déjà très sombres sont écartées : assombries encore, elles ne
    donnaient plus qu'une bouillie brune. Les sujets hors style aussi."""
    alea = random.Random(ident)
    pool = [t for t in MANIFESTE
            if luminance(t["fichier"]) >= 62 and not HORS_STYLE.search(t.get("titre") or "")]
    alea.shuffle(pool)
    if len(pool) < n: pool = pool * (n // max(len(pool), 1) + 1)
    return [t["fichier"] for t in pool[:n]]

def construire(script, apercu=False):
    ident = script["id"]
    groupes = script["groupes"]
    texte = narration(groupes)
    caf, voix = synthetiser(ident, texte)
    instants = dater_groupes(groupes, texte, voix["mots"])
    fin_voix = min(voix["duree"], voix.get("fin", voix["duree"]))
    duree = fin_voix + SORTIE_FINALE
    noir = script["noir"]
    t_tableaux = instants[noir]                         # le premier tableau arrive avec ce groupe
    t_produit = instants[len(groupes) - 1]              # le dernier groupe : « Fais le test… »

    # Les instants où l'image change : chaque groupe, et un tableau toutes les 2,3 s.
    coupes = sorted(set([0.0] + instants + [t_produit, duree]))
    t = t_tableaux
    cuts_tableaux = []
    while t < t_produit:
        cuts_tableaux.append(t); t += CADENCE_TABLEAU
    coupes = sorted(set(coupes + cuts_tableaux))
    # on écarte les coupes trop proches (moins d'une image) pour ne pas produire de durées nulles
    propres = [coupes[0]]
    for c in coupes[1:]:
        if c - propres[-1] >= 1 / FPS: propres.append(c)
    coupes = propres

    fichiers_tableaux = tableaux_pour(ident, len(cuts_tableaux) + 1)
    dossier = ici("images", ident); os.makedirs(dossier, exist_ok=True)
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
                im = fond_tableau(cle[0])
                if produit:
                    im = cadre_produit(im)
                else:
                    im = poser_medaillon(im)
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
    sortie = ici("sortie", f"{ident}.mp4")
    fondu = max(duree - 3.0, 0)
    # La voix sort du synthétiseur à basse cadence ; sans rééchantillonnage, amix
    # alignait la musique dessus et l'abîmait. Tout passe à 44,1 kHz d'abord.
    filtre = (f"[2:a]aresample=44100,atrim=0:{duree:.3f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=1.2,"
              f"afade=t=out:st={fondu:.3f}:d=3,volume=0.16[m];"
              f"[1:a]aresample=44100,atrim=0:{duree:.3f},apad=whole_dur={duree:.3f}[v];"
              f"[v][m]amix=inputs=2:duration=first:normalize=0[a]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
           "-i", caf, "-i", musique, "-filter_complex", filtre,
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
               f"Musique : « {titre_musique} » — Kevin MacLeod (incompetech.com), licence CC BY 4.0\n"
               f"Tableaux : domaine public — The Metropolitan Museum of Art et The Art Institute of Chicago (CC0)\n")
    open(ici("sortie", f"{ident}.legende.txt"), "w", encoding="utf-8").write(legende)
    taille = os.path.getsize(sortie) / 1e6
    print(f"  {ident} : {duree:.1f} s · {len(cache)} images-clés · {taille:.1f} Mo")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apercu = "--apercu" in sys.argv
    choisis = [s for s in SCRIPTS if not args or any(s["id"].startswith(a) for a in args)]
    print(f"{len(choisis)} vidéo(s) · {len(MANIFESTE)} tableaux disponibles")
    for s in choisis:
        construire(s, apercu=apercu)
