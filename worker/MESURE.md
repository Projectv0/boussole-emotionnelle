# La mesure d'audience — installation

*Compteur maison sur ton Worker Cloudflare. Gratuit, sans cookie, sans bannière de
consentement, et sans qu'aucune de tes données ni de celles des visiteurs ne parte chez
un tiers.*

Le code est écrit et branché. Il **ne fait rien** tant que trois choses manquent : la base,
la liaison, et l'adresse du Worker dans les pages. Aucun risque à laisser en l'état.

---

## Ce qui est mesuré, exactement

Six moments. Pour chacun, deux informations sont écrites : **le jour** et **le nom du
moment**. Pour une page du guide, son adresse en plus.

| Nom | Quand |
|---|---|
| `accueil` | quelqu'un ouvre la page du test |
| `article` | quelqu'un ouvre une page du guide (l'adresse est notée) |
| `test-debut` | clic sur « Commencer le test » |
| `test-fin` | les seize situations sont répondues |
| `paywall` | la fenêtre de choix de formule s'ouvre |
| `stripe` | départ vers le paiement |

**Rien d'autre n'est enregistré.** Pas d'adresse IP, pas de cookie, pas d'identifiant de
visite, pas d'empreinte de navigateur, pas de page d'origine.

### Ce que ça t'interdit de savoir, et qu'il faut accepter

Sans identifiant, **deux événements ne peuvent pas être rattachés à la même personne**. Tu
sauras « 300 ouvertures, 40 tests commencés, 12 finis, 2 départs vers Stripe ». Tu ne
sauras jamais combien de personnes distinctes, ni si quelqu'un est revenu, ni le chemin
d'un visiteur précis.

C'est le prix de l'absence de bannière de consentement — et pour la question que tu te
poses vraiment au lancement (*personne n'est venu, ou des gens sont venus et n'ont pas
payé ?*), des totaux suffisent.

---

## Installation — quinze minutes, une seule fois

### 1. Créer la base

Dans le tableau de bord Cloudflare : **Storage & Databases → D1 → Create database**.
Nomme-la `boussole`.

Ouvre l'onglet **Console** de la base et exécute :

```sql
CREATE TABLE IF NOT EXISTS compteur (
  jour      TEXT    NOT NULL,
  evenement TEXT    NOT NULL,
  page      TEXT    NOT NULL DEFAULT '',
  n         INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (jour, evenement, page)
);
```

La clé primaire porte sur les trois colonnes : une seule ligne par jour et par événement,
qu'on incrémente. La base reste minuscule même après des années.

### 2. Lier la base au Worker

**Worker → Settings → Bindings → Add → D1 database**

- Variable name : **`MESURE`** (exactement ce nom)
- D1 database : `boussole`

### 3. Poser le mot de passe de lecture

**Worker → Settings → Variables and Secrets → Add → Secret**

- Nom : **`MESURE_CLE`**
- Valeur : un mot de passe de ton choix, long et sans rapport avec tes autres mots de passe.

C'est lui qui protège l'accès au tableau. Sans lui, le Worker refuse toute lecture.

### 4. Déployer le Worker

Colle le contenu de `worker/verification.js` dans l'éditeur du Worker et déploie.

### 5. Me donner l'adresse du Worker

Quelque chose comme `https://boussole.<ton-compte>.workers.dev`.

Je la renseigne dans `index.html` et dans les 58 pages du guide — c'est la variable
`MESURE`, aujourd'hui vide. **Tant qu'elle est vide, aucune requête n'est émise nulle
part.** C'est le dernier geste, et c'est lui qui allume la mesure.

> La même adresse sert à la vérification d'achat, qui vit sur le même Worker. Si tu me la
> donnes maintenant, je branche les deux d'un coup — la mesure marchera tout de suite, la
> vérification attendra sa clé Stripe.

---

## Lire les chiffres

Ouvre dans ton navigateur :

```
https://<ton-worker>/mesure?cle=<MESURE_CLE>&jours=30
```

Tu obtiens du JSON : les totaux par événement, le détail par jour, et les quarante pages
du guide les plus ouvertes.

Pour en faire un tableau lisible, enregistre la réponse dans un fichier et lance :

```bash
python3 mesure.py chiffres.json
```

`mesure.py` accepte aussi l'adresse complète en argument, si tu préfères — mais elle
contient ton mot de passe, alors ne la colle pas n'importe où.

---

## Ce qu'il faut savoir sur la fiabilité

**Les nombres sont indicatifs, pas comptables.** Trois raisons, et aucune n'est grave :

- Les bloqueurs de publicité et la protection contre le pistage neutralisent la mesure.
  Le site fonctionne pareil, mais ces visites ne sont pas comptées.
- Le Worker vérifie l'origine de la requête, ce qui arrête un navigateur mais pas un outil
  en ligne de commande. Quelqu'un de déterminé pourrait gonfler les compteurs. Ajoute une
  **règle de limitation de débit** Cloudflare sur la route du Worker — elle est de toute
  façon nécessaire pour la vérification d'achat.
- `sendBeacon` est fiable mais pas garanti : un départ très brutal peut perdre un
  événement.

Ce qui compte n'est pas le nombre exact, ce sont les **proportions** et leur évolution.

## Ce que ça coûte

Rien, dans les limites du forfait gratuit Cloudflare : 100 000 écritures par jour sur D1
et 100 000 requêtes par jour sur le Worker. À six événements par visite, c'est de l'ordre
de 16 000 visites quotidiennes avant de s'en approcher.

## Si tu veux tout arrêter

Vide la variable `MESURE` dans les pages — ou dis-le-moi, c'est une ligne. Plus aucune
requête n'est émise. Pour effacer l'historique : `DELETE FROM compteur;` dans la console
D1.
