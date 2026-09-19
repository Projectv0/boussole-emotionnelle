#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monte le dossier de publication à partir des trois studios.

    python3 publication.py

Les 39 fiches typographiques (reseaux-sociaux/), les 30 carrousels illustrés
(reseaux-sociaux-illustre/) et les 30 scènes de bande dessinée (reseaux-sociaux-bd/)
sont réunis en 99 publications, six par semaine, du lundi au samedi :

    publication/
      LISEZMOI.md            comment publier, et les réglages à faire une seule fois
      PLAN.md                le calendrier des dix-sept semaines
      calendrier.csv         une ligne par publication, pour un tableur
      semaine-01/
        SEMAINE.md           les six posts de la semaine, légendes comprises
        1-lundi-fiche-.../     instagram/  tiktok/  legende.txt
        2-mardi-illustre-.../  instagram/  tiktok/  legende.txt
        3-mercredi-bd-.../     instagram/  tiktok/  legende.txt
        ...

Le chiffre en tête de chaque dossier force le bon ordre dans le Finder : « jeudi »
passe avant « lundi » en alphabétique, ce qui rendrait la semaine illisible.

**L'ordre des genres** n'est pas un tour de rôle fixe. Les trois séries n'ont pas la
même taille — 39, 30, 30 — et un tour de rôle strict les ferait finir à trois dates
différentes, les dernières semaines n'offrant plus qu'un seul genre. On les entrelace
donc proportionnellement : chacune revient à intervalle régulier et les trois
s'épuisent ensemble, à la semaine dix-sept.

**Le fil émotionnel** est tenu par les fiches, qui gardent leur ordre : treize
émotions, trois fiches chacune. Chaque carrousel se place ensuite près des fiches
dont il partage l'émotion, pour que la semaine parle d'une même chose sous trois
formes.
"""
import csv, json, os, re, shutil, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
TYPO = os.path.join(BASE, "reseaux-sociaux")
ILLU = os.path.join(BASE, "reseaux-sociaux-illustre")
BD = os.path.join(BASE, "reseaux-sociaux-bd")
CIBLE = os.path.join(BASE, "publication")

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
PAR_SEMAINE = 6

GENRES = {
    "fiche":    {"titre": "Fiche", "pluriel": "fiches", "source": TYPO,
                 "quoi": "texte et pictogrammes — comprendre, distinguer, pratiquer"},
    "illustre": {"titre": "Illustré", "pluriel": "illustrés", "source": os.path.join(ILLU, "sortie"),
                 "quoi": "personnages dessinés, une idée déroulée écran par écran"},
    "bd":       {"titre": "BD", "pluriel": "BD", "source": os.path.join(BD, "sortie"),
                 "quoi": "une scène vécue, bulles et narrateur, la chute à la fin"},
}

# Les émotions sont comparées sans accents, mais s'écrivent avec.
ACCENTUEES = {"anxiete": "anxiété", "colere": "colère", "culpabilite": "culpabilité",
              "fierte": "fierté", "serenite": "sérénité", "degout": "dégoût"}

def en_clair(emotions):
    return ", ".join(ACCENTUEES.get(e, e) for e in emotions[:3])

# Les treize semaines de fiches, et l'émotion que chacune traite. C'est la colonne
# vertébrale : les carrousels viennent s'y accrocher.
EMOTIONS = {
    1: ("l'anxiété et la peur", ["anxiete", "peur"]),
    2: ("la colère", ["colere"]),
    3: ("la honte", ["honte"]),
    4: ("la culpabilité", ["culpabilite"]),
    5: ("la tristesse", ["tristesse"]),
    6: ("la jalousie et l'envie", ["jalousie", "envie"]),
    7: ("la joie", ["joie"]),
    8: ("l'amour", ["amour"]),
    9: ("la gratitude", ["gratitude"]),
    10: ("la fierté", ["fierte"]),
    11: ("la sérénité", ["serenite"]),
    12: ("la surprise", ["surprise"]),
    13: ("le dégoût", ["degout"]),
}


def sans_accents(t):
    return "".join(c for c in unicodedata.normalize("NFD", t or "")
                   if unicodedata.category(c) != "Mn").lower().strip()


# ————— ce qu'on a à publier —————

def titres_des_fiches():
    """Le vrai titre de chaque fiche, lu dans le studio typographique.

    Sans ça, les tableaux affichaient le nom de dossier — « comprendre anxiete »,
    sans accents ni ponctuation.
    """
    import importlib.util
    chemin = os.path.join(TYPO, "contenus.py")
    spec = importlib.util.spec_from_file_location("contenus_typo", chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = {}
    for semaine in mod.SEMAINES:
        for p in semaine:
            titre = p.get("titre", "")
            if p.get("sous"):
                titre += " — " + p["sous"]
            out[p["slug"]] = titre
    return out


def fiches():
    """Les 39 fiches, dans l'ordre des semaines et des jours d'origine."""
    out = []
    titres = titres_des_fiches()
    rang = {"lundi": 1, "mercredi": 2, "vendredi": 3}
    for d in sorted(os.listdir(TYPO)):
        m = re.fullmatch(r"semaine-(\d+)", d)
        if not m:
            continue
        n = int(m.group(1))
        posts = [s for s in sorted(os.listdir(os.path.join(TYPO, d)))
                 if os.path.isdir(os.path.join(TYPO, d, s))]
        posts.sort(key=lambda s: rang.get(s.split("-")[0], 9))
        for slug in posts:
            # Le dossier d'origine porte son ancien jour de parution — « lundi-… ».
            # On le retire : le nouveau jour est déjà en tête du nom, et les deux se
            # contredisaient (« 4-jeudi-fiche-mercredi-peur-ou-anxiete »).
            court = slug.split("-", 1)[1] if slug.split("-")[0] in JOURS else slug
            out.append({"genre": "fiche", "slug": court,
                        "source": os.path.join(TYPO, d, slug),
                        "titre": titres.get(court, court.replace("-", " ")),
                        "emotions": EMOTIONS[n][1], "semaine_origine": n})
    return out


def carrousels(genre, dossier_json):
    """Les 30 carrousels d'une série, dans leur ordre éditorial."""
    posts = json.load(open(os.path.join(dossier_json, "contenus.json"),
                           encoding="utf-8"))["posts"]
    out = []
    for p in sorted(posts, key=lambda p: int(p["numero"])):
        n = int(p["numero"])
        out.append({"genre": genre, "slug": p["slug"],
                    "source": os.path.join(GENRES[genre]["source"], f"{n:02d}-{p['slug']}"),
                    "titre": " ".join(p["titre"].replace("|", " ").split()),
                    "emotions": [sans_accents(e) for e in p.get("emotions", [])],
                    "numero": n})
    return out


# ————— l'ordre de passage —————

def ordre_des_genres(compte):
    """Quel genre à quelle place, sur toute la série.

    Un tour de rôle strict (fiche, illustré, BD, fiche, illustré, BD…) épuiserait
    les deux séries de trente bien avant les trente-neuf fiches : les dernières
    semaines n'auraient plus qu'un seul genre. On prend donc à chaque tour celui qui
    est le plus en retard sur sa part, en refusant de répéter le précédent tant qu'un
    autre genre reste disponible.
    """
    reste = dict(compte)
    pose = {g: 0 for g in compte}
    out = []
    for _ in range(sum(compte.values())):
        libres = sorted((g for g in compte if reste[g]),
                        key=lambda g: (pose[g] / compte[g], -reste[g], g))
        g = libres[1] if len(libres) > 1 and out and libres[0] == out[-1] else libres[0]
        out.append(g)
        pose[g] += 1
        reste[g] -= 1
    return out


def affinite(post, cibles):
    """Ce que ce carrousel a de commun avec l'émotion en cours.

    3 si c'est son émotion principale, 2 pour la deuxième, 1 s'il l'aborde, 0 sinon.
    """
    for i, e in enumerate(post["emotions"][:3]):
        if e in cibles:
            return 3 - i
    return 0


def programme():
    """La liste des 99 publications, dans l'ordre de parution."""
    f, i, b = fiches(), carrousels("illustre", ILLU), carrousels("bd", BD)
    genres = ordre_des_genres({"fiche": len(f), "illustre": len(i), "bd": len(b)})

    # 1. les fiches occupent leurs places dans l'ordre : elles portent le fil.
    places = [None] * len(genres)
    suite = iter(f)
    for k, g in enumerate(genres):
        if g == "fiche":
            places[k] = next(suite)

    # 2. pour chaque place de carrousel, l'émotion de la fiche la plus proche.
    fiches_aux = [k for k, g in enumerate(genres) if g == "fiche"]
    def emotion_a(k):
        proche = min(fiches_aux, key=lambda j: (abs(j - k), j))
        return places[proche]["emotions"]

    # 3. on y pose le carrousel disponible qui parle le mieux de cette émotion — en
    #    gardant pour plus tard celui qui serait le seul à savoir parler d'une émotion
    #    encore à venir. Sans cette réserve, le seul carrousel sur le dégoût partait
    #    dès la quatrième semaine et la dernière n'avait plus rien qui colle.
    for g, pool in (("illustre", list(i)), ("bd", list(b))):
        miennes = [k for k, x in enumerate(genres) if x == g]
        for rang, k in enumerate(miennes):
            cibles = emotion_a(k)
            apres = [emotion_a(j) for j in miennes[rang + 1:]]
            def valeur(p):
                plus_tard = max((affinite(p, c) for c in apres), default=0)
                return (affinite(p, cibles), -plus_tard, -p["numero"])
            choix = max(pool, key=valeur)
            pool.remove(choix)
            places[k] = choix

    for k, p in enumerate(places):
        p["semaine"] = k // PAR_SEMAINE + 1
        p["jour"] = JOURS[k % PAR_SEMAINE]
        p["rang"] = k % PAR_SEMAINE + 1
        p["dossier"] = f"{p['rang']}-{p['jour']}-{p['genre']}-{p['slug']}"
    return places


# ————— le montage —————

def copier(source, dest):
    """Copie une publication complète : instagram/, tiktok/, legende.txt."""
    if not os.path.isdir(source):
        raise SystemExit(f"source manquante : {source}")
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


def legende_courte(chemin, limite=180):
    """Le début de la légende, pour la relire sans ouvrir le fichier.

    Le fichier est découpé en sections « === TITRE === » ; on ne garde que le corps
    de la première, celle de la légende elle-même.
    """
    corps, dedans = [], False
    for ligne in open(chemin, encoding="utf-8").read().splitlines():
        if ligne.startswith("==="):
            if dedans:
                break
            dedans = "LÉGENDE" in ligne
        elif dedans and ligne.strip():
            corps.append(ligne.strip())
    t = " ".join(" ".join(corps).split())
    return (t[:limite].rsplit(" ", 1)[0] + "…") if len(t) > limite else t


def titre_semaine(posts):
    """Les émotions dont parle la semaine, en clair."""
    vus = []
    for p in posts:
        for n, (libelle, cles) in EMOTIONS.items():
            if p["genre"] == "fiche" and p["emotions"] == cles and libelle not in vus:
                vus.append(libelle)
    return " puis ".join(vus) if vus else "les carrousels"


# ————— les documents du dossier —————

LISEZMOI = """# Publier — le mode d'emploi

Ce dossier contient **{posts} publications prêtes à poster**, six par semaine, du lundi
au samedi, sur **{semaines} semaines**. Rien à préparer, rien à retoucher : chaque
dossier de jour contient déjà les images aux deux formats et la légende.

## Les trois genres

| Genre | Dans le nom du dossier | Ce que c'est | Combien | Diapos |
|---|---|---|---|---|
{tableau_genres}

Ils alternent : **jamais deux publications du même genre deux jours de suite**, sur les
{posts} publications. Les trois séries n'ayant pas la même taille — {compte_genres} —,
elles ne se relaient pas à tour de rôle fixe mais à intervalle proportionnel, pour
finir ensemble à la semaine {semaines}.

## Publier une journée — deux minutes

Ouvre le dossier du jour. Il contient trois choses : `instagram/`, `tiktok/`,
`legende.txt`.

**TikTok** — ➕ puis mode Photo. Glisser les images de `tiktok/` **dans l'ordre 01, 02,
03…** Coller la légende depuis `legende.txt`. Choisir un son doux dans les tendances
(lo-fi, piano, « calm aesthetic »). Le son compte vraiment : TikTok pousse les
carrousels photo qui utilisent un son en tendance.

**Instagram** — ➕ Publication, sélection multiple des images de `instagram/` dans
l'ordre, la même légende, publier. Une story de relais le jour même aide beaucoup.

Les dossiers sont numérotés de 1 à 6 dans l'ordre des jours. Sans ce chiffre, le Finder
classerait « jeudi » avant « lundi » et la semaine deviendrait illisible.

## Les réglages à faire une seule fois

- **Lien en bio** sur les deux comptes : `https://boussole-emotionnelle.fr`. Toutes les
  légendes y renvoient, et aucune ne peut être cliquable dans le texte.
- **Heures** : 12 h-13 h ou 19 h-21 h. La régularité compte plus que l'heure parfaite.
- **Les trente premières minutes** : réponds aux commentaires. C'est le signal
  d'engagement le plus fort sur les deux plateformes.
- **Ne supprime jamais un post qui démarre lentement.** Les carrousels TikTok remontent
  parfois plusieurs jours après.
- **Épingle** en profil le post qui marche le mieux, après deux ou trois semaines.

## Si six par semaine devient trop

Ne saute pas des jours : **publie la même suite, trois par semaine au lieu de six.** La
semaine 01 devient alors deux semaines, et ainsi de suite. L'alternance reste intacte
puisque c'est le même ordre, et le dossier dure trente-trois semaines — huit mois.

Ne garde pas « le lundi, le mercredi et le vendredi » : en sautant un jour sur deux, on
retombe dix fois sur deux publications du même genre à la suite.

## Où retrouver les sources

Les images sont montées par trois studios séparés, qui restent en dehors de ce dossier :

- `reseaux-sociaux/` — les fiches typographiques
- `reseaux-sociaux-illustre/` — les carrousels illustrés
- `reseaux-sociaux-bd/` — les scènes de bande dessinée

Pour remonter ce dossier après une modification : `python3 publication.py`.
"""


def ecrire_lisezmoi(prog, semaines, diapos):
    lignes_g = []
    for g in ("fiche", "illustre", "bd"):
        n = [diapos[p["dossier"], p["semaine"]] for p in prog if p["genre"] == g]
        taille = f"{min(n)}" if min(n) == max(n) else f"{min(n)} à {max(n)}"
        lignes_g.append(f"| **{GENRES[g]['titre']}** | `-{g}-` | {GENRES[g]['quoi']} "
                        f"| {len(n)} | {taille} |")
    compte = ", ".join(f"{sum(1 for p in prog if p['genre'] == g)} {GENRES[g]['pluriel']}"
                       for g in ("fiche", "illustre", "bd"))
    open(os.path.join(CIBLE, "LISEZMOI.md"), "w", encoding="utf-8").write(
        LISEZMOI.format(posts=len(prog), semaines=semaines,
                        tableau_genres="\n".join(lignes_g), compte_genres=compte))


def ecrire_plan(prog, semaines, diapos):
    L = [f"# Plan de publication — {semaines} semaines, {len(prog)} publications", "",
         "Six publications par semaine, du lundi au samedi. Les trois genres alternent : "
         "jamais deux du même genre deux jours de suite.", "",
         "Le mode d'emploi est dans `LISEZMOI.md`. Ce document-ci n'est que le calendrier.", "",
         "| | Publications | Diapositives |", "|---|---|---|"]
    for g in ("fiche", "illustre", "bd"):
        n = sum(1 for p in prog if p["genre"] == g)
        d = sum(diapos[p["dossier"], p["semaine"]] for p in prog if p["genre"] == g)
        L.append(f"| **{GENRES[g]['titre']}** | {n} | {d} × 2 formats |")
    L += [f"| **Total** | **{len(prog)}** | **{sum(diapos.values())} × 2 = "
          f"{sum(diapos.values()) * 2} images** |", "",
          "Le fil est tenu par les fiches : treize émotions, trois fiches chacune, dans "
          "l'ordre. Chaque carrousel est posé près des fiches dont il partage l'émotion — "
          "la semaine parle d'une même chose sous trois formes.", ""]
    derniere = [p for p in prog if p["semaine"] == semaines]
    if len(derniere) < PAR_SEMAINE:
        L += [f"La dernière semaine est courte : il reste {len(derniere)} publications, "
              f"du {derniere[0]['jour']} au {derniere[-1]['jour']}.", ""]

    for s in range(1, semaines + 1):
        sem = [p for p in prog if p["semaine"] == s]
        L += [f"## Semaine {s:02d} — {titre_semaine(sem)}", "",
              "| Jour | Genre | Sujet | Dossier | Diapos |", "|---|---|---|---|---|"]
        for p in sem:
            L.append(f"| {p['jour']} | {GENRES[p['genre']]['titre']} | {p['titre']} "
                     f"| `{p['dossier']}` | {diapos[p['dossier'], s]} |")
        L.append("")
    open(os.path.join(CIBLE, "PLAN.md"), "w", encoding="utf-8").write("\n".join(L))


def ecrire_semaine(prog, s, diapos):
    sem = [p for p in prog if p["semaine"] == s]
    L = [f"# Semaine {s:02d} — {titre_semaine(sem)}", "",
         f"{len(sem)} publication{'s' if len(sem) > 1 else ''}, du {sem[0]['jour']} "
         f"au {sem[-1]['jour']}. Les légendes sont recopiées ici pour pouvoir les "
         "relire d'un coup ; celle qu'il faut coller est dans le dossier du jour.", ""]
    for p in sem:
        L += [f"## {p['jour'].capitalize()} — {GENRES[p['genre']]['titre']} · {p['titre']}", "",
              f"**Dossier** `{p['dossier']}` · {diapos[p['dossier'], s]} diapositives · "
              f"{en_clair(p['emotions'])}", "",
              f"> {legende_courte(os.path.join(CIBLE, f'semaine-{s:02d}', p['dossier'], 'legende.txt'))}",
              ""]
    open(os.path.join(CIBLE, f"semaine-{s:02d}", "SEMAINE.md"), "w",
         encoding="utf-8").write("\n".join(L))


def ecrire_csv(prog, diapos):
    with open(os.path.join(CIBLE, "calendrier.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["semaine", "jour", "rang", "genre", "dossier", "titre",
                    "emotions", "diapositives"])
        for p in prog:
            w.writerow([p["semaine"], p["jour"], p["rang"], GENRES[p["genre"]]["titre"],
                        f"semaine-{p['semaine']:02d}/{p['dossier']}", p["titre"],
                        en_clair(p["emotions"]), diapos[p["dossier"], p["semaine"]]])


def verifier(prog):
    """Refuse de monter le dossier si le compte ne tombe pas juste.

    Un carrousel oublié ou copié deux fois ne se voit pas dans un calendrier de
    dix-sept semaines, mais se voit tout de suite une fois les images publiées.
    """
    attendu = {"fiche": len(fiches()), "illustre": 30, "bd": 30}
    erreurs = []
    for g, n in attendu.items():
        vus = [p["slug"] for p in prog if p["genre"] == g]
        if len(vus) != n:
            erreurs.append(f"{g} : {len(vus)} publications au lieu de {n}")
        if len(set(vus)) != len(vus):
            erreurs.append(f"{g} : un slug apparaît deux fois")
        for p in (q for q in prog if q["genre"] == g):
            if not os.path.isdir(p["source"]):
                erreurs.append(f"source introuvable : {p['source']}")
    doubles = sum(1 for a, b in zip(prog, prog[1:]) if a["genre"] == b["genre"])
    if doubles:
        erreurs.append(f"{doubles} fois deux publications du même genre à la suite")
    if erreurs:
        raise SystemExit("\n".join("  ✗ " + e for e in erreurs))


def principal():
    prog = programme()
    verifier(prog)
    semaines = max(p["semaine"] for p in prog)
    shutil.rmtree(CIBLE, ignore_errors=True)
    os.makedirs(CIBLE, exist_ok=True)

    diapos = {}
    for p in prog:
        dest = os.path.join(CIBLE, f"semaine-{p['semaine']:02d}", p["dossier"])
        diapos[p["dossier"], p["semaine"]] = copier(p["source"], dest)

    ecrire_lisezmoi(prog, semaines, diapos)
    ecrire_plan(prog, semaines, diapos)
    ecrire_csv(prog, diapos)
    for s in range(1, semaines + 1):
        ecrire_semaine(prog, s, diapos)

    total = sum(diapos.values())
    print(f"{len(prog)} publications sur {semaines} semaines · {total} diapositives "
          f"× 2 formats = {total * 2} images dans publication/")
    return prog, diapos


if __name__ == "__main__":
    principal()
