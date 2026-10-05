#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique les vidéos, une par script, dans le style des références.

    python3 generateur.py                # les vingt
    python3 generateur.py 03 17          # celles-là seulement
    python3 generateur.py --apercu 03    # juste les images-clés, sans vidéo
    python3 generateur.py --illustrations        # les vingt, sur les illustrations nanobanana
    python3 generateur.py --illustrations 03     # (choix phrase par phrase : choix_illustrations.py)

Le style, tel qu'il a été lu dans les trois vidéos de référence :
  · paysage 4:3 (1024 × 768), 50 secondes, 30 images par seconde ;
  · une accroche sur fond noir, les mots posés un par un, un mot en couleur ;
  · puis des photos assombries, sur le thème de la vidéo — une photo par phrase,
    la photo et le texte changent au même instant, jamais l'un sans l'autre ;
  · les mots apparaissent au rythme d'une voix off, chaque image bouge lentement,
    et chaque changement de phrase passe par une transition (voir montage.py) ;
  · à la fin, la photo reste entière : une question dans le style des phrases,
    et un bandeau discret en bas — la boussole, le nom, l'adresse, « LIEN EN BIO ».

Ce qu'on assemble :
  scripts.py       les vingt textes, groupe de mots par groupe de mots
  photos/          les photos de chaque thème (voir photos.py)
  musiques/        Kevin MacLeod, CC BY — le crédit part dans la légende
  voix_eleven.py   la voix ElevenLabs (voix.swift, celle de macOS, en dernier recours)
  ../og.jpg        l'image du site, montrée à la fin comme « le produit »

Sortie : « ../Vidéos à publier/Photos/NN - Titre.mp4 », avec sa légende à côté — et, avec
--illustrations, « ../Vidéos à publier/Illustrations/ ».
Les fichiers de travail (voix, images-clés) vont dans .cache/, qu'on peut effacer.

Les illustrations sont des scènes avec des personnages : le cadrage se centre sur
les visages (repérés par ../reseaux-sociaux-bd/detecter-visages.swift), et chaque
phrase se pose à l'endroit du cadre où elle ne couvre aucun visage.
"""
import hashlib, json, math, os, random, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat
from scripts import SCRIPTS

ICI = os.path.dirname(os.path.abspath(__file__))
def ici(*p): return os.path.join(ICI, *p)
ILLUSTRATIONS = "--illustrations" in sys.argv     # fonds : illustrations nanobanana au lieu des photos Pexels
# un seul dossier, deux versions : « Vidéos à publier/Photos » et « Vidéos à publier/Illustrations »
SORTIE = ici("..", "Vidéos à publier", "Illustrations" if ILLUSTRATIONS else "Photos")
CACHE = ici(".cache")
IMAGES_CLES = os.path.join(CACHE, "images-illustrations" if ILLUSTRATIONS else "images")
for d in (SORTIE, os.path.join(CACHE, "voix"), IMAGES_CLES): os.makedirs(d, exist_ok=True)

L, H, FPS = 1024, 768, 30        # 4:3 ; tout le reste (texte, cadrages, fin) suit la hauteur
SANS_VOIX = True                 # pour l'instant : texte et musique seulement, le temps de lecture fait le rythme
VOIX = "Jacques"                 # la voix macOS, en dernier recours (quand SANS_VOIX passe à False)
VOIX_ELEVEN = ""                 # l'identifiant d'une voix ElevenLabs : voir voix_eleven.py --voix
POLICES = {"grasse": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
           "italique": "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
           "normale": "/System/Library/Fonts/Supplemental/Georgia.ttf"}
SORTIE_FINALE = 4.0          # la page de fin reste à l'écran après le dernier mot
SITE = "boussole-emotionnelle.fr"

BLANC, NOIR = (255, 255, 255), (0, 0, 0)
COULEURS = {"*": (245, 208, 0), "!": (224, 48, 48), "+": (46, 204, 113)}   # jaune, rouge, vert
CREME, ENCRE = (253, 248, 238), (38, 34, 30)                              # les tons du site

PRODUIT = Image.open(ici("..", "og.jpg")).convert("RGB")

# ————————————————————————— le texte —————————————————————————

def narration(groupes):
    """Ce que la voix lit : les groupes bout à bout, sans les marques, avec la ponctuation."""
    morceaux = []
    for g in groupes:
        s = re.sub(r"[*!+]", "", g).replace(" / ", " ").replace("/", " ")
        morceaux.append(re.sub(r"\s+", " ", s).strip())
    return " ".join(morceaux)

def lignes_affichees(groupe, avec_ponctuation=False):
    """Les lignes à l'écran : [[(mot, couleur|None), …], …], en capitales, sans ponctuation.

    Une marque peut couvrir plusieurs mots — « *ça va* » — : on découpe la ligne en
    tronçons colorés ou non, puis chaque tronçon en mots.

    Avec avec_ponctuation, rend aussi, ligne par ligne, la ponctuation qui suit chaque
    mot (« , », « . », « ? »…) : c'est elle qui fait respirer le rythme de lecture."""
    lignes, ponctuations = [], []
    for ligne in groupe.split("/"):
        mots, ponct = [], []
        for m in re.finditer(r"([*!+])(.+?)\1|([^*!+]+)", ligne):
            couleur = COULEURS[m.group(1)] if m.group(1) else None
            # « d'*humeur* » : l'élision reste collée au mot coloré, et prend sa couleur
            colle = bool(m.group(1)) and m.start() > 0 and ligne[m.start() - 1] in "'’" and bool(mots)
            for i, jeton in enumerate((m.group(2) or m.group(3) or "").split()):
                propre = re.sub(r"[.,:;!?«»\"()…]", "", jeton).strip().replace("'", "’")
                signes = "".join(c for c in jeton if c in ".,:;!?…")
                if not propre:                      # « ? » isolé, « . » après un mot coloré
                    if ponct: ponct[-1] += signes
                    continue
                if colle and i == 0:
                    propre = mots.pop()[0] + propre.upper(); ponct.pop()
                mots.append((propre.upper(), couleur)); ponct.append(signes)
        if mots:
            lignes.append(mots); ponctuations.append(ponct)
    return (lignes, ponctuations) if avec_ponctuation else lignes

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

# — les illustrations nanobanana —

DOSSIERS_ILLUS = {"I": ici("..", "reseaux-sociaux-illustre", "illustrations"),
                  "B": ici("..", "reseaux-sociaux-bd", "illustrations")}
VOILE_ILLUS = 0.30        # moins sombre que les photos : les illustrations sont claires, crème
_visages = None
def visages():
    """Les têtes de chaque illustration, en fractions de l'image d'origine."""
    global _visages
    if _visages is None:
        _visages = {}
        for f in (ici("illustrations", "visages-illustre.json"),
                  ici("..", "reseaux-sociaux-bd", "file", "visages.json")):
            if os.path.exists(f): _visages.update(json.load(open(f, encoding="utf-8")))
        # les têtes que le détecteur avait ratées : retrouvées sur l'image agrandie, ou relevées à l'œil
        f = ici("illustrations", "visages-complement.json")
        if os.path.exists(f):
            for nom, tetes in json.load(open(f, encoding="utf-8")).items():
                if not nom.startswith("_"): _visages[nom] = _visages.get(nom, []) + tetes
    return _visages

def rogner_bords(im, jeu="I", seuil=9):
    """La boîte utile d'une illustration : sans marge claire ni filet de cadre.

    Sur chaque bord : on mange la marge claire et unie (le papier crème des
    illustrations, jusqu'à 22 % ; le blanc pur hors du cadre des cases de BD,
    jusqu'à 12 %), puis le filet sombre du cadre s'il y en a un, puis un peu plus
    pour ne pas garder sa trace. Un mur uni à l'intérieur d'une case n'est pas
    une marge : il est trop sombre pour être pris pour du blanc, et c'est la
    place prévue pour le texte."""
    petit = im.convert("L").resize((240, round(240 * im.height / im.width)))
    w, h = petit.size
    clair, plafond = (246, 0.12) if jeu == "B" else (226, 0.22)
    def ligne(cote, n):
        return {"g": (n, 0, n + 1, h), "d": (w - n - 1, 0, w - n, h),
                "h": (0, n, w, n + 1), "b": (0, h - n - 1, w, h - n)}[cote]
    def mesure(cote, n):
        s = ImageStat.Stat(petit.crop(ligne(cote, n)))
        return s.mean[0], s.stddev[0]
    bords = {}
    for cote, dim in (("g", w), ("d", w), ("h", h), ("b", h)):
        n = 0
        while n < dim * plafond:
            m, s = mesure(cote, n)
            if s < seuil and m > clair: n += 1
            else: break
        k = n
        while k < n + dim * 0.03:                     # le filet du cadre
            m, s = mesure(cote, k)
            if m < 90 and s < 40: k += 1
            else: break
        bords[cote] = k + 2 if k else 0
    if jeu == "B":
        # Une case posée sur une marge colorée (sage, beige) garde son filet : on le
        # cherche directement — une ligne sombre, fine (2 % au plus), qui traverse
        # l'image presque entière, près du bord. En haut, on va plus loin : certaines
        # cases ont un bandeau crème fermé par un trait, vestige de la mise en page
        # des carrousels. Une bande sombre épaisse (une nuit, un mur dans l'ombre)
        # n'est pas un filet ; un bord de table non plus, il ne traverse pas tout.
        sombre = petit.point(lambda v: 255 if v < 110 else 0)
        def part(cote, n, a, b):
            boite = {"g": (n, a, n + 1, b), "d": (w - n - 1, a, w - n, b),
                     "h": (a, n, b, n + 1), "b": (a, h - n - 1, b, h - n)}[cote]
            return ImageStat.Stat(sombre.crop(boite)).mean[0] / 255
        def filet(cote, dim, loin, a, b):
            """Le bord intérieur du filet trouvé de ce côté, ou None."""
            n = bords[cote]
            while n < dim * loin:
                if max(part(cote, n, a, b), part(cote, n + 1, a, b)) > 0.75:
                    fin = n
                    while fin < dim * loin and max(part(cote, fin, a, b), part(cote, fin + 1, a, b)) > 0.75:
                        fin += 1
                    return fin + 2 if fin - n <= max(3, dim * 0.025) else None
                n += 1
            return None
        # le haut et le bas d'abord, sur toute la largeur…
        for cote, loin in (("h", 0.38), ("b", 0.08)):
            f_ = filet(cote, h, loin, 0, w)
            if f_: bords[cote] = f_
        # … puis les côtés, entre le haut et le bas de la case
        for cote in ("g", "d"):
            f_ = filet(cote, w, 0.08, bords["h"], h - bords["b"])
            if f_: bords[cote] = f_
    f = im.width / w
    return (round(bords["g"] * f), round(bords["h"] * f),
            round(im.width - bords["d"] * f), round(im.height - bords["b"] * f))

_fonds_illus = {}
def fond_illustration(code):
    """(fond L × H, têtes en pixels du cadre) pour une illustration « I:nom » ou « B:nom ».

    Le cadrage couvre tout le format, centré sur les visages : ils tombent vers les
    deux cinquièmes de la hauteur, sans couper le haut de la tête quand c'est possible."""
    if code in _fonds_illus: return _fonds_illus[code]
    jeu, nom = code.split(":", 1)
    im = Image.open(os.path.join(DOSSIERS_ILLUS[jeu], nom + ".jpg")).convert("RGB")
    W0, H0 = im.size
    x0, y0, x1, y1 = rogner_bords(im, jeu)
    im = im.crop((x0, y0, x1, y1))
    r = max(L / im.width, H / im.height)
    nw, nh = max(L, round(im.width * r)), max(H, round(im.height * r))
    im = im.resize((nw, nh), Image.LANCZOS)
    # La taille d'une tête déduite de la posture (et non du visage) est souvent
    # exagérée : on la ramène à une taille de tête plausible.
    tetes = [((t["x"] * W0 - x0) * r, (t["y"] * H0 - y0) * r,
              min(t["l"], 0.20 if t.get("posture") else 1) * W0 * r,
              min(t["h"], 0.15 if t.get("posture") else 1) * H0 * r)
             for t in visages().get(nom, [])]
    if tetes:
        cy = sum(t[1] for t in tetes) / len(tetes)
        haut = min(t[1] - t[3] * 1.15 for t in tetes)         # le sommet du crâne, cheveux compris
        # Les cases de BD ont été dessinées personnages en bas, mur vide au-dessus pour les
        # bulles : on garde ce mur, c'est la place du texte. Les illustrations carrées
        # ont les visages plus haut.
        cible = 0.56 if jeu == "B" else 0.40
        oy = min(cy - cible * H, haut - 0.05 * H)
        oy = max(oy, cy - 0.64 * H)                       # jamais le visage tout en bas
        ox = sum(t[0] for t in tetes) / len(tetes) - L / 2
    else:
        oy, ox = (nh - H) * 0.4, (nw - L) / 2
    oy = int(max(0, min(oy, nh - H))); ox = int(max(0, min(ox, nw - L)))
    im = im.crop((ox, oy, ox + L, oy + H))
    # Ce qu'il ne faut pas couvrir : le cœur du visage (les yeux, la bouche), jamais ;
    # autour, les cheveux et le menton, si possible.
    boites = [((cx - ox - tl * 0.5, cy - oy - th * 0.55, cx - ox + tl * 0.5, cy - oy + th * 0.5),
               (cx - ox - tl * 0.85, cy - oy - th * 0.95, cx - ox + tl * 0.85, cy - oy + th * 0.85))
              for cx, cy, tl, th in tetes]
    im = Image.blend(im, Image.new("RGB", (L, H), NOIR), VOILE_ILLUS)
    masque = Image.new("L", (L, H), 0)
    ImageDraw.Draw(masque).ellipse((-L * 0.25, -H * 0.45, L * 1.25, H * 1.45), fill=255)
    masque = masque.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(im, Image.new("RGB", (L, H), NOIR), masque)
    _fonds_illus[code] = (im, boites)
    return _fonds_illus[code]

_polices = {}
def police(taille, style="grasse"):
    cle = (style, taille)
    if cle not in _polices: _polices[cle] = ImageFont.truetype(POLICES[style], taille)
    return _polices[cle]

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
# (hauteurs dessinées pour 576 px de haut, ramenées à la hauteur réelle)
def _y(v): return round(v * H / 576)
ANCRES = [("droite", _y(70)), ("gauche", _y(300)), ("droite", _y(220)), ("gauche", _y(70)), ("droite", _y(340)), ("gauche", _y(180))]

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

def replier_equilibre(mots, f, espace, largeur_max):
    """Comme replier, avec le même nombre de lignes, mais des lignes de longueur
    voisine : « IL Y A DEUX MILLE ANS / SÉNÈQUE ÉCRIVAIT » plutôt qu'un mot seul
    qui pend sur la dernière ligne."""
    gloutonne = replier(mots, f, espace, largeur_max)
    n = len(gloutonne)
    if n < 2 or len(mots) > 16: return gloutonne
    from itertools import combinations
    meilleure, pire = gloutonne, max(largeur_ligne(l, f, espace) for l in gloutonne)
    for coupes in combinations(range(1, len(mots)), n - 1):
        bornes = (0,) + coupes + (len(mots),)
        lignes = [mots[bornes[i]:bornes[i + 1]] for i in range(n)]
        w = max(largeur_ligne(l, f, espace) for l in lignes)
        if w <= largeur_max and w < pire:
            meilleure, pire = lignes, w
    return meilleure

def disposer(lignes, cote, y, largeur_max, equilibre=False):
    """Où va chaque ligne : [(x, y, largeur, grande, police, espace, mots), …].

    La ligne large peut se replier ; les lignes étroites aussi, plus rarement. Les
    lignes suivantes descendent en escalier depuis le côté choisi."""
    marge, rendu = 64, []
    plier = replier_equilibre if equilibre else replier
    for k, mots in enumerate(lignes):
        grande = (k == 0)
        f, espace = police(50 if grande else 30), (14 if grande else 9)
        for morceau in plier(mots, f, espace, largeur_max):
            rendu.append((grande, f, espace, morceau))
    places = []
    for k, (grande, f, espace, mots) in enumerate(rendu):
        w = largeur_ligne(mots, f, espace)
        decal = k * 34            # l'escalier des lignes suivantes
        x = (marge + decal) if cote == "gauche" else (L - marge - w - decal)
        x = max(24, min(x, L - 24 - w))
        places.append((x, y, w, grande, f, espace, mots))
        y += (58 if grande else 38)
    return places

def emprise(places):
    """La boîte qu'occupe un groupe de lignes."""
    return (min(p[0] for p in places), places[0][1] - 4,
            max(p[0] + p[2] for p in places), places[-1][1] + (58 if places[-1][3] else 38))

def recouvrement(a, b):
    l = min(a[2], b[2]) - max(a[0], b[0]); h = min(a[3], b[3]) - max(a[1], b[1])
    return l * h if l > 0 and h > 0 else 0

def gene(boite, visages_ici):
    """Ce que coûte une boîte de texte posée là : couvrir des yeux pèse dix fois
    plus que couvrir des cheveux."""
    return sum(10 * recouvrement(boite, coeur) + recouvrement(boite, autour)
               for coeur, autour in visages_ici)

def placer_hors_visages(lignes, rang, eviter):
    """Parmi douze emplacements, celui où le texte couvre le moins de visage.

    À recouvrement égal (le plus souvent : aucun), on garde l'alternance gauche /
    droite et la hauteur prévues par ANCRES, pour que le texte continue de bouger
    d'une phrase à l'autre comme dans les références."""
    cote0, y0 = ANCRES[rang % len(ANCRES)]
    meilleur = None
    for largeur in (660, 520):                 # plus étroit si c'est le seul moyen d'éviter un visage
        for cote in ("gauche", "droite"):
            for y in range(40, H - 150, 70):
                places = disposer(lignes, cote, y, largeur, equilibre=True)
                boite = emprise(places)
                if boite[3] > H - 28: continue
                score = gene(boite, eviter) + (0 if cote == cote0 else 800) + abs(y - y0) * 3 + (0 if largeur == 660 else 1500)
                if meilleur is None or score < meilleur[0]:
                    meilleur = (score, places)
    return meilleur[1] if meilleur else disposer(lignes, cote0, y0, 660, equilibre=True)

def placer_groupe(groupe, rang, noir=False, eviter=None):
    """Où vont les lignes d'un groupe. « eviter » (les visages d'une illustration)
    déplace le texte hors des visages."""
    lignes = lignes_affichees(groupe)
    if not lignes: return []
    if eviter is not None:
        return placer_hors_visages(lignes, rang, eviter)
    cote, y = ANCRES[rang % len(ANCRES)]
    if noir:
        # sur fond noir, les mots se posent en escalier depuis le coin
        cote, y = ("gauche", _y(150)) if rang % 2 == 0 else ("droite", _y(120))
    return disposer(lignes, cote, y, L - 2 * 64 - 40)

def ombre_douce(boite):
    """Le voile sombre et flou posé derrière un texte sur fond clair : un masque L × H."""
    x0, y0, x1, y1 = boite
    ombre = Image.new("L", (L, H), 0)
    ImageDraw.Draw(ombre).rounded_rectangle((x0 - 26, y0 - 18, x1 + 26, y1 + 14), radius=30, fill=125)
    return ombre.filter(ImageFilter.GaussianBlur(26))

def ecrire_groupe(im, groupe, rang, noir=False, eviter=None):
    """Écrit un groupe d'un coup (images fixes). Sur une illustration, le texte
    évite les visages et une ombre douce le rend lisible sur un fond clair."""
    places = placer_groupe(groupe, rang, noir, eviter)
    if not places: return im
    if eviter is not None:
        im = Image.composite(Image.new("RGB", (L, H), NOIR), im, ombre_douce(emprise(places)))
    d = ImageDraw.Draw(im, "RGBA")
    for x, y, w, grande, f, espace, mots in places:
        ecrire_ligne(d, x, y, mots, f, espace)
    return im

def medaillon(diam, bord=3):
    """La boussole de og.jpg, découpée en rond sur son fond crème, avec un liseré."""
    src = PRODUIT.crop((50, 30, 610, 590)).resize((diam, diam), Image.LANCZOS)
    masque = Image.new("L", (diam, diam), 0)
    ImageDraw.Draw(masque).ellipse((0, 0, diam - 1, diam - 1), fill=255)
    rond = Image.new("RGBA", (diam, diam), (0, 0, 0, 0))
    rond.paste(src, (0, 0), masque)
    ImageDraw.Draw(rond).ellipse((0, 0, diam - 1, diam - 1), outline=CREME + (255,), width=bord)
    return rond

QUESTION = ([("ET", None), ("TOI,", None)],
            [("OÙ", None), ("EN", None), ("ES-TU", COULEURS["*"]), ("?", None)])
HAUT_BANDEAU = 150

def placer_question(eviter=None):
    """Les deux lignes de « ET TOI, / OÙ EN ES-TU ? » : [(x, y, mots), (x, y, mots)], et la
    boîte qu'elles occupent. Sur une illustration, la place la plus libre au-dessus du
    bandeau, à gauche ou à droite, plus ou moins haut."""
    f = police(50)
    w2 = largeur_ligne(QUESTION[1], f, 14)
    xa, ya = 96, _y(150)
    if eviter:
        meilleur = None
        for droite in (False, True):
            for y in range(40, H - HAUT_BANDEAU - 150, 40):
                a = (L - 96 - w2 - 34) if droite else 96
                boite = (a - 20, y - 10, a + 34 + w2 + 20, y + 64 + 70)
                score = gene(boite, eviter) + abs(y - _y(150)) * 3 + (600 if droite else 0)
                if meilleur is None or score < meilleur[0]:
                    meilleur = (score, a, y)
        _, xa, ya = meilleur
    xb, yb = xa + 34, ya + 64
    return [(xa, ya, QUESTION[0]), (xb, yb, QUESTION[1])], (xa, ya, xb + w2, yb + 56)

def couche_bandeau():
    """Le bandeau du bas, seul, sur fond transparent : L × HAUT_BANDEAU, RGBA.
    La boussole en médaillon, le nom du site en italique, l'adresse, et une
    étiquette jaune « LIEN EN BIO »."""
    im = Image.new("RGBA", (L, HAUT_BANDEAU), (12, 10, 10, 215))
    im.alpha_composite(medaillon(104), (60, 23))
    d = ImageDraw.Draw(im, "RGBA")
    x, haut = 196, H - HAUT_BANDEAU
    d.text((x, H - 128 - haut), "Boussole émotionnelle", font=police(34, "italique"), fill=CREME)
    d.text((x, H - 82 - haut), "Fais le test  ·  16 situations  ·  14 émotions", font=police(22, "normale"), fill=(215, 210, 200))
    d.text((x, H - 50 - haut), SITE, font=police(24), fill=COULEURS["+"])
    fb = police(26); texte = "LIEN EN BIO"; tw, th = fb.getlength(texte), fb.size
    cx, cy = L - 150, H - 75 - haut
    x0, y0, x1, y1 = cx - tw / 2 - 28, cy - th / 2 - 12, cx + tw / 2 + 28, cy + th / 2 + 12
    d.rounded_rectangle((x0, y0, x1, y1), radius=(y1 - y0) / 2, fill=COULEURS["*"] + (255,))
    d.text((cx - tw / 2, y0 + 12 - th * 0.12), texte, font=fb, fill=ENCRE)
    return im

def cadre_produit(fond, eviter=None):
    """La fin, d'un coup (image fixe) : l'image reste entière, la question dans le
    style des phrases, et le bandeau en bas."""
    lignes, boite = placer_question(eviter)
    if eviter:
        fond = Image.composite(Image.new("RGB", (L, H), NOIR), fond, ombre_douce(boite))
    im = fond.convert("RGBA")
    d = ImageDraw.Draw(im, "RGBA")
    for x, y, mots in lignes:
        ecrire_ligne(d, x, y, mots, police(50), 14)
    im.alpha_composite(couche_bandeau(), (0, H - HAUT_BANDEAU))
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

def construire(script, apercu=False):
    """Une vidéo : on choisit les fonds (une image par phrase posée sur image) et la
    voix s'il y en a une ; montage.py fait le reste — le rythme des mots, le
    mouvement des images, les transitions, la fin."""
    import montage
    ident = script["id"]
    groupes = script["groupes"]
    n = len(groupes) - script["noir"] - 1          # le dernier groupe garde l'image d'avant, sous la fin
    if ILLUSTRATIONS:
        from choix_illustrations import CHOIX
        fichiers_tableaux = CHOIX.get(ident, [])
        if len(fichiers_tableaux) != n:
            raise SystemExit(f"{ident} : {len(fichiers_tableaux)} illustrations choisies pour "
                             f"{n} phrases — voir choix_illustrations.py")
        fonds, visages_par_fond = zip(*(fond_illustration(c) for c in fichiers_tableaux))
    else:
        fichiers_tableaux = tableaux_pour(ident, n)
        fonds, visages_par_fond = [fond_tableau(f) for f in fichiers_tableaux], [[] for _ in range(n)]
    voix = None if SANS_VOIX else synthetiser(ident, narration(groupes))
    nom = f"{ident[:2]} - {script['titre']}"
    sortie = os.path.join(SORTIE, f"{nom}.mp4")
    duree, images = montage.monter(script, list(fonds), list(visages_par_fond), sortie,
                                   ici("musiques", script["musique"]), voix=voix,
                                   apercu=os.path.join(IMAGES_CLES, ident) if apercu else None)
    if apercu:
        print(f"  {ident} : {images} images de contrôle (durée {duree:.1f} s)")
        return duree
    ecrire_legende(script, fichiers_tableaux)
    print(f"  {nom} : {duree:.1f} s · {os.path.getsize(sortie) / 1e6:.1f} Mo", flush=True)
    return duree

def ecrire_legende(script, fichiers_tableaux=None):
    """La légende, avec le lien de l'article et le crédit musique (obligatoire, CC BY)."""
    import unicodedata
    ident = script["id"]
    nom = f"{ident[:2]} - {script['titre']}"
    titre_musique = script["musique"].replace(".mp3", "").replace("---", " - ").replace("-", " ")
    penseur = "".join(c for c in unicodedata.normalize("NFD", script["penseur"].lower())
                      if unicodedata.category(c) != "Mn" and c.isalnum())     # « Sénèque » → seneque
    legende = (f"{script['legende']}\n\n"
               f"Pour aller plus loin : {SITE}/guide/{script['article']}.html\n"
               f"Le test : {SITE} (lien en bio)\n\n"
               f"#émotions #psychologie #{penseur} "
               f"#développementpersonnel #boussoleémotionnelle\n\n"
               f"Musique : « {titre_musique} » — Kevin MacLeod (incompetech.com), licence CC BY 4.0\n")
    if not ILLUSTRATIONS:                      # nos propres illustrations : rien à créditer
        if fichiers_tableaux is None: fichiers_tableaux = []
        creds = credits_photos(ident, fichiers_tableaux)
        legende += ("Photos : " + " · ".join(creds) + "\n") if creds else "Photos : Pexels\n"
    open(os.path.join(SORTIE, f"{nom} (légende).txt"), "w", encoding="utf-8").write(legende.replace("'", "’"))

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apercu = "--apercu" in sys.argv
    choisis = [s for s in SCRIPTS if not args or any(s["id"].startswith(a) for a in args)]
    if "--legendes" in sys.argv:               # réécrire les légendes seulement, sans refaire les vidéos
        for s in choisis: ecrire_legende(s)
        print(f"{len(choisis)} légende(s) réécrite(s) → {SORTIE}")
        raise SystemExit
    print(f"{len(choisis)} vidéo(s) → {SORTIE}", flush=True)
    if apercu or len(choisis) == 1:
        for s in choisis:
            construire(s, apercu=apercu)
    else:
        # chaque vidéo se rend image par image : on en fait plusieurs à la fois
        import multiprocessing as mp
        with mp.get_context("fork").Pool(max(1, min(6, (os.cpu_count() or 2) - 2))) as pool:
            pool.map(construire, choisis, chunksize=1)
