#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complète les données structurées des pages du guide.

    python3 balisage.py            écrit
    python3 balisage.py --lire     dit ce qui manque, sans rien toucher

Deux manques que l'audit de mise en marché a relevés, et que rien ne répare tout seul.

**Le balisage Article était inerte sur les 23 premiers articles.** Sans `datePublished`
ni `author`, le type Article est déclaré mais ne peut produire aucun résultat enrichi :
la balise est là, elle ne sert à rien. Les 35 articles écrits ensuite portaient déjà
leurs dates ; ce sont les plus anciens — donc les mieux installés — qui en manquaient.

**Aucune page ne portait de fil d'Ariane.** Sous un résultat de recherche, Google
affiche alors l'URL brute plutôt que « Accueil › Le guide › … ». C'est un gain
d'affichage, pas de classement, mais il est gratuit.

Les dates viennent de git, jamais d'une saisie : `datePublished` est le premier commit
qui a créé le fichier, `dateModified` le dernier qui l'a touché. Comme pour sitemap.py,
relancer après le commit — sinon les dates sont celles d'avant.

Le script est idempotent : il remplace ce qu'il a écrit au lieu de l'empiler.
"""
import glob, html, json, os, re, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://boussole-emotionnelle.fr"

# La même entité que le `publisher` déjà présent dans chaque article et que le bloc
# Organization de l'accueil. Nommer l'éditeur comme auteur est exact et rend le
# balisage Article opérant ; signer d'un nom de personne est une décision éditoriale
# qui ne se prend pas dans un script.
EDITEUR = {"@type": "Organization", "name": "Boussole émotionnelle", "url": SITE + "/"}

MARQUE = "<!-- fil d'Ariane : écrit par balisage.py -->"


def dates(chemin):
    """(création, dernière modification) en ISO, d'après l'historique git."""
    r = subprocess.run(["git", "log", "--format=%cI", "--", chemin],
                       capture_output=True, text=True, cwd=BASE)
    jours = [l.strip()[:10] for l in r.stdout.splitlines() if l.strip()]
    if not jours:
        import datetime
        d = datetime.date.fromtimestamp(os.path.getmtime(chemin)).isoformat()
        return d, d
    return jours[-1], jours[0]


def titre_court(texte, nom):
    """Le nom de la page dans le fil d'Ariane.

    Le h1 est pris comme base — il est plus lisible que le <title>, qui porte en plus
    la promesse de clic. Mais presque tous les h1 du guide sont bâtis « sujet : ce
    qu'on en dit », et un fil d'Ariane n'affiche que quelques mots avant de couper :
    on garde donc la partie avant le deux-points, qui est précisément le sujet.
    """
    m = re.search(r"<h1[^>]*>(.*?)</h1>", texte, re.S)
    if not m:
        return nom.replace(".html", "").replace("-", " ").capitalize()
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    gauche = re.split(r"\s*[:—]\s*", t)[0]
    # Un sujet réduit à un ou deux mots ne nomme plus rien ; on garde alors le h1 entier.
    return gauche if len(gauche) >= 12 else t


def fil(nom, texte):
    """Le bloc BreadcrumbList de la page, en JSON compact."""
    etapes = [("Accueil", SITE + "/"), ("Le guide", SITE + "/guide/")]
    if nom != "index.html":
        etapes.append((titre_court(texte, nom), f"{SITE}/guide/{nom}"))
    o = {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [{"@type": "ListItem", "position": i, "name": n, "item": u}
                             for i, (n, u) in enumerate(etapes, 1)]}
    return (MARQUE + '\n<script type="application/ld+json">'
            + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>")


def article_complete(bloc, cree, modifie):
    """Ajoute au bloc Article ce qui lui manque. Rend None si rien ne change."""
    o = json.loads(bloc)
    if o.get("@type") != "Article":
        return None
    avant = json.dumps(o, ensure_ascii=False, sort_keys=True)
    o.setdefault("datePublished", cree)
    o["dateModified"] = max(modifie, o.get("datePublished", modifie))
    o.setdefault("author", EDITEUR)
    if json.dumps(o, ensure_ascii=False, sort_keys=True) == avant:
        return None
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))


def passe(chemin, ecrire):
    nom = os.path.basename(chemin)
    t = texte = open(chemin, encoding="utf-8").read()
    faits = []

    if nom != "index.html":
        cree, modifie = dates(os.path.relpath(chemin, BASE))
        for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            neuf = article_complete(bloc, cree, modifie)
            if neuf:
                t = t.replace(bloc, neuf, 1)
                faits.append("Article")

    # Le fil d'Ariane se pose juste avant </head>, et remplace celui d'un passage
    # précédent plutôt que de s'y ajouter.
    t = re.sub(re.escape(MARQUE) + r'\n<script type="application/ld\+json">.*?</script>\n',
               "", t, flags=re.S)
    t = t.replace("</head>", fil(nom, t) + "\n</head>", 1)
    if t == texte:
        return []
    # Distinguer la pose d'un fil absent de la réécriture d'un fil devenu faux : les
    # deux modifient le fichier, et n'annoncer que la première ferait dire « 0 page
    # modifiée » à un passage qui en a réécrit cinquante-huit.
    faits.append("fil d'Ariane" if MARQUE not in texte else "fil d'Ariane (revu)")
    if ecrire:
        open(chemin, "w", encoding="utf-8").write(t)
    return faits


def sommaire(ecrire):
    """Recale les noms de l'ItemList du sommaire sur les <title> réels des pages.

    Cette liste est une copie : renommer un article ne la met pas à jour, et onze
    entrées annonçaient encore d'anciens titres. Un sommaire qui décrit ses pages
    autrement qu'elles ne se nomment apprend au moteur à s'en méfier.
    """
    chemin = os.path.join(BASE, "guide", "index.html")
    t = texte = open(chemin, encoding="utf-8").read()
    ecarts = []
    for bloc in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        if '"ItemList"' not in bloc:
            continue
        o = json.loads(bloc)
        for e in o["mainEntity"]["itemListElement"]:
            page = os.path.join(BASE, "guide", e["url"].rstrip("/").rsplit("/", 1)[-1])
            if not os.path.exists(page):
                continue
            reel = re.search(r"<title>(.*?)</title>", open(page, encoding="utf-8").read(),
                             re.S).group(1)
            if e.get("name") != reel:
                ecarts.append(e["name"])
                e["name"] = reel
        if ecarts:
            t = t.replace(bloc, json.dumps(o, ensure_ascii=False, indent=1), 1)
    if ecarts and ecrire:
        open(chemin, "w", encoding="utf-8").write(t)
    return ecarts


def principal(ecrire=True):
    fichiers = sorted(glob.glob(os.path.join(BASE, "guide", "*.html")))
    n = 0
    for f in fichiers:
        faits = passe(f, ecrire)
        if faits:
            n += 1
            if not ecrire:
                print("  %-46s %s" % (os.path.basename(f), " · ".join(faits)))
    verbe = "complétées" if ecrire else "à compléter"
    print(f"{n} pages {verbe} sur {len(fichiers)}")
    ecarts = sommaire(ecrire)
    print(f"sommaire : {len(ecarts)} entrées recalées sur le titre réel de la page"
          if ecarts else "sommaire : les 57 entrées nomment les pages comme elles se nomment")
    return 0


if __name__ == "__main__":
    sys.exit(principal(ecrire="--lire" not in sys.argv))
