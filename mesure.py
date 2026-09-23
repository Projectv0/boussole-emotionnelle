#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met en tableau les chiffres du compteur d'audience.

    python3 mesure.py chiffres.json        un fichier enregistré depuis le navigateur
    python3 mesure.py https://…/mesure?cle=…&jours=30
    cat chiffres.json | python3 mesure.py

Le Worker renvoie du JSON ; ce script en fait quelque chose qui se lit. Il calcule
surtout l'entonnoir — la suite arrivée → test commencé → test fini → formule
affichée → départ vers Stripe —, parce que c'est le seul endroit où les nombres
disent quoi faire : l'étape où la chute est la plus brutale est celle à reprendre.

Ces nombres comptent des ÉVÉNEMENTS, pas des personnes. Aucun identifiant n'est
enregistré, donc deux événements ne peuvent pas être rattachés au même visiteur.
Les pourcentages ci-dessous sont des rapports entre totaux, pas des taux de
conversion par personne — ils se comparent d'une semaine à l'autre, ils ne se
lisent pas comme « 30 % des visiteurs ont fait X ».

Installation et déploiement : voir worker/MESURE.md.
"""
import json, sys, urllib.request

# L'ordre du parcours, du premier au dernier pas.
ETAPES = [("accueil",    "Ouverture de l'accueil"),
          ("test-debut", "Test commencé"),
          ("test-fin",   "Test terminé"),
          ("paywall",    "Choix de formule affiché"),
          ("stripe",     "Départ vers le paiement")]


def charger(source):
    if source is None:
        return json.load(sys.stdin)
    if source.startswith("http"):
        with urllib.request.urlopen(source, timeout=30) as r:
            return json.load(r)
    return json.load(open(source, encoding="utf-8"))


def barre(part, largeur=28):
    plein = int(round(part * largeur))
    return "█" * plein + "·" * (largeur - plein)


def principal(source):
    d = charger(source)
    if "erreur" in d:
        print("le Worker a répondu :", d["erreur"])
        return 1

    totaux = {t["evenement"]: t["n"] for t in d.get("total", [])}
    print(f"Du {d.get('depuis','?')} à aujourd'hui · {d.get('jours','?')} jours\n")

    depart = totaux.get("accueil", 0)
    print("L'ENTONNOIR")

    # Les pertes d'abord, l'affichage ensuite : la marche à reprendre est la PLUS
    # haute, et on ne peut pas le savoir avant de les avoir toutes vues. Signaler
    # chaque chute forte séparément désignait trois étapes sur quatre, donc aucune.
    pertes, precedent = {}, None
    for cle, _ in ETAPES:
        n = totaux.get(cle, 0)
        if precedent:
            pertes[cle] = 100 * (1 - n / precedent)
        precedent = n
    pire = max(pertes, key=pertes.get) if pertes else None

    precedent = None
    for cle, nom in ETAPES:
        n = totaux.get(cle, 0)
        part = n / depart if depart else 0
        chute = ""
        if cle in pertes:
            chute = f"   −{pertes[cle]:.0f} %"
            if cle == pire:
                chute += "  ← c'est ici qu'on perd le plus"
        print(f"  {nom:<26} {n:>6}  {barre(part)}{chute}")
        precedent = n

    lus = totaux.get("article", 0)
    if lus:
        print(f"\n  {'Pages du guide ouvertes':<26} {lus:>6}"
              "   (elles ne passent pas par l'accueil)")

    articles = d.get("articles") or []
    if articles:
        print("\nLES PAGES DU GUIDE LES PLUS OUVERTES")
        for a in articles[:15]:
            nom = a["page"].replace("/guide/", "").replace(".html", "")
            print(f"  {nom:<46} {a['n']:>6}")

    parJour = d.get("parJour") or []
    if parJour:
        jours = sorted({l["jour"] for l in parJour}, reverse=True)[:14]
        index = {(l["jour"], l["evenement"]): l["n"] for l in parJour}
        cles = [c for c, _ in ETAPES] + ["article"]
        print("\nLES QUATORZE DERNIERS JOURS")
        print("  " + " " * 12 + "".join(f"{c[:8]:>10}" for c in cles))
        for j in jours:
            print(f"  {j:<12}" + "".join(f"{index.get((j, c), 0):>10}" for c in cles))

    if not totaux:
        print("Aucun événement enregistré pour l'instant.\n"
              "C'est normal tant que la variable MESURE des pages est vide : "
              "rien n'est envoyé. Voir worker/MESURE.md.")
    return 0


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1] if len(sys.argv) > 1 else None))
