# Reprendre la série « scène vécue »

*État au 18 septembre 2026. Tout ce qu'il faut pour finir, sans rien avoir à redécouvrir.*

---

## Où on en est

**27 carrousels sur 30 sont complets.** 141 illustrations sur 150 ont été régénérées avec les
fiches de personnages ; les 30 carrousels sont montés dans `sortie/`, en 1080 × 1350 et
1080 × 1920, avec leurs légendes.

**Ce qui bloque : les crédits nanobanana sont épuisés.** L'API répond
`You need to recharge to create task`. Neuf illustrations n'ont donc pas pu être refaites et
datent de la première passe, avec leurs défauts de continuité.

| Post | Titre | Diapositives à refaire |
|---|---|---|
| **30** | JEUDI, 18 H 50. ON SONNE. ELLE SAIT POURQUOI. | les 5 — carrousel entier |
| **29** | 21 H 40. LE CANAPÉ. LA TÉLÉ ÉTEINTE. | 3 sur 5 |
| **17** | 19 H 02. SON AMI ANNULE. IL EST DÉSOLÉ. | 1 sur 5 |

La liste exacte des neuf identifiants est dans `file/a-refaire.json`.

**Coût pour finir : 180 crédits** (9 images × 20 crédits en 1K). Le plus petit forfait suffit.
Recharger sur <https://nanobanana.io/pricing>, avec le compte `cavalier1231@hotmail.fr` — c'est
sur ce compte que la série a été générée.

---

## Étape 1 — Régénérer les neuf

Ouvrir <https://nanobanana.io/create> dans Chrome, connecté au bon compte, puis coller le
moteur ci-dessous dans la console. Il génère en parallèle et garde les URL en mémoire.

```js
window.__file = []; window.__fait = {}; window.__echecs = []; window.__actif = false;
window.__RATIO = '3:4';
window.__PREF = 'https://cdn.nanobanana.io/production/predictions/8d00112f-81da-469a-af7e-bf59dae9a372/';

window.__une = async function(it){
  const c = await fetch('/api/task/create', {method:'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify({model:'nano-banana-2', prompt: it.s,
      params:{aspect_ratio: window.__RATIO, resolution:'1K', num_outputs:1}})});
  const cj = await c.json();
  const pid = cj && cj.data && cj.data.predictionId;
  if(!pid) throw new Error('création refusée : ' + JSON.stringify(cj).slice(0,120));
  for(let i = 0; i < 70; i++){
    await new Promise(r => setTimeout(r, 3000));
    const v = await fetch('/api/task/check', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({predictionId: pid})});
    const vj = await v.json();
    const res = vj && vj.data && vj.data.result;
    if(res && res.length && res[0].url) return res[0].url;
    if(vj && vj.data && vj.data.status === 'failed') throw new Error('génération échouée');
  }
  throw new Error('délai dépassé');
};

window.__lancer = function(n){
  window.__actif = true;
  const ouvrier = async () => {
    while(window.__file.length){
      const it = window.__file.shift();
      try{ window.__fait[it.n] = await window.__une(it); }
      catch(e){ window.__echecs.push({n: it.n, e: String(e.message || e)}); }
    }
  };
  Promise.all(Array.from({length: n || 3}, ouvrier)).then(() => { window.__actif = false; });
};

window.__etat = () => ({file: window.__file.length, faits: Object.keys(window.__fait).length,
                        echecs: window.__echecs.length, actif: window.__actif});
window.__lot = (d, n) => Object.entries(window.__fait).slice(d, d + (n || 9))
  .map(([k, u]) => k + '|' + u.replace(window.__PREF, '')).join('\n');
```

Puis charger la file et ne garder que les neuf à refaire :

```js
const r = await fetch('https://raw.githubusercontent.com/Projectv0/boussole-emotionnelle/main/reseaux-sociaux-bd/file/a-generer.json');
const j = await r.json();
const refaire = new Set((await (await fetch('https://raw.githubusercontent.com/Projectv0/boussole-emotionnelle/main/reseaux-sociaux-bd/file/a-refaire.json')).json()).a_refaire);
window.__file = j.filter(x => refaire.has(x.n));
window.__lancer(3);
```

Suivre avec `window.__etat()`. Quand `file` tombe à 0, récolter avec `window.__lot(0, 9)`.

**Le préfixe CDN peut changer** si le compte change. Il se lit dans n'importe quelle URL
renvoyée : c'est tout ce qui précède le nom de fichier.

## Étape 2 — Télécharger, redétecter les têtes, recomposer

Coller la sortie de `__lot` dans le script de téléchargement, qui remplace les fichiers en
place :

```bash
cd "/Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd"
# effacer d'abord les anciennes, sinon le script les considère comme déjà présentes
python3 -c "import json;[print(n) for n in json.load(open('file/a-refaire.json'))['a_refaire']]" \
  | while read n; do rm -f "illustrations/$n.jpg"; done
./aspirer.sh <<'EOF'
nom-de-l-illustration|1789...-uuid.jpeg
…
EOF
swift detecter-visages.swift illustrations/*.jpg > file/visages.json
python3 assembleur.py 17 29 30
```

**La détection des têtes est à refaire dès qu'une illustration change.** `file/visages.json`
dit où sont les visages ; l'assembleur y pointe les queues de bulles. Une image remplacée
sans redétection garde les coordonnées de l'ancienne, et les queues désignent le vide.

Si une image ressort **sans aucune tête** — Vision est entraîné sur des photos et rate les
personnages de trois quarts, de dos ou très stylisés —, relever la position à l'œil dans
`file/tetes-manuelles.json`. Le fichier explique son propre format ; attention, il est en
fractions du **panneau**, donc après rognage du cadre, alors que `file/visages.json` est en
fractions du fichier d'origine. Pour vérifier qu'aucune bulle ne se retrouve sans tête :

```bash
cd "/Users/cavalier/Dev/Site Emotion/reseaux-sociaux-bd"
python3 -c "
import json, sys; sys.path.insert(0,'.')
import assembleur as A; A.format_actif('instagram')
d=json.load(open('contenus.json',encoding='utf-8'))
manque=[(p['numero'],i) for p in d['posts'] for i,s in enumerate(p['slides'],1)
        if s.get('bulles') and not A.visages(s.get('illustration'))]
print(manque or 'toutes les bulles ont une tête à viser')
"
```

Puis **rouvrir les trois posts et vérifier de quel côté chaque personnage est dessiné** : le
côté des bulles a été relu à l'œil pour les vingt-sept autres, et les neuf images refaites
peuvent très bien inverser les personnages par rapport à l'ancienne version. Une bulle qui
change de côté change aussi l'ordre de lecture — l'assembleur décale alors la réponse vers le
bas tout seul, mais il faut regarder le résultat. Les deux règles sont dans `GUIDE-STYLE.md`.

## Étape 3 — Relire

Les trois relectures précédentes sont à refaire sur l'ensemble, pas seulement sur les trois
posts corrigés : la règle du tiers supérieur vide n'a été vérifiée que sur deux scènes.
Découper en trois lots de dix posts, sur les `instagram/` uniquement, en cherchant dans cet
ordre : une bulle qui couvre un visage, deux bulles qui se chevauchent, du texte coupé, des
lettres dessinées dans l'illustration, des mains ou visages déformés, une incohérence de
personnage entre diapositives d'une même scène.

**À quoi s'attendre.** Les mains déformées resteront : c'est le défaut le plus tenace du
générateur, et la série illustrée précédente a demandé deux passes ciblées. Prévoir une
vingtaine de régénérations supplémentaires, soit 400 crédits de plus.

---

## Ce qu'il faut savoir avant de toucher à quoi que ce soit

**La fiche de personnages est ce qui fait tenir la série.** Chaque post porte un champ
`fiche` dans `contenus.json`, répété mot pour mot au début des prompts de toutes ses
diapositives. Sans elle, les personnages changent de visage, de coiffure et de vêtements
d'une diapositive à l'autre — c'est le défaut qui a coûté une régénération complète.
`file/a-generer.json` est reconstruit en collant `fiche` + `SCENE:` + prompt + le suffixe de
`suffixe-style.txt`. Si tu modifies un prompt, refais ce fichier.

**Le suffixe de style ne se modifie jamais en cours de série.** C'est lui qui tient l'unité
des 150 illustrations. Deux règles y sont essentielles et ont été ajoutées après coup : le
tiers supérieur du cadre reste vide, sinon les bulles tombent sur des visages ; et aucun mot,
aucune marque, aucune étiquette n'est dessiné, après qu'un « MILK » se soit écrit sur une
brique de lait.

**Le générateur ne garde aucune mémoire d'une image à l'autre.** J'ai testé les trois
paramètres d'image de référence de l'API — `image_urls`, `images`, `image` : tous acceptés
sans erreur, tous ignorés, la sortie n'ayant aucun rapport avec la référence. Ne pas
réessayer cette piste.

**Ne jamais demander de texte à l'image.** Les bulles et le narrateur sont dessinés par
`assembleur.py`, en vrai français. Un prompt contenant `speech bubble`, `text`, `sign` ou
`writing` est à refaire.

**Un « / » dans le texte du narrateur** est une coupure de ligne voulue ; l'assembleur la
traduit en retour à la ligne.

---

## Le dossier

| | |
|---|---|
| `GUIDE-STYLE.md` | l'analyse de @darkybloom, ce qu'on lui emprunte et ce qu'on ne lui emprunte pas. À lire en premier. |
| `contenus.json` | les 30 scènes : titres, bulles, narrateurs, prompts, fiches de personnages. La source de tout. |
| `suffixe-style.txt` | le suffixe collé à la fin de chaque prompt. |
| `assembleur.py` | compose illustrations + bulles + narrateur, dans les deux formats. |
| `detecter-visages.swift` | repère les têtes sur les illustrations, pour que les queues de bulles pointent vers elles. À relancer après toute régénération. |
| `file/visages.json` | sa sortie : une tête = x, y, largeur, hauteur, en fractions du fichier d'origine. |
| `file/tetes-manuelles.json` | les têtes que Vision ne voit pas, relevées à l'œil, en fractions du panneau. |
| `aspirer.sh` | télécharge un lot depuis le CDN, au format `nom\|fichier` sur l'entrée standard. |
| `file/a-generer.json` | les 150 prompts complets, prêts à envoyer. |
| `file/a-refaire.json` | les neuf qui restent. |
| `illustrations/` | les 150 images. Hors dépôt. |
| `sortie/` | les 30 carrousels montés. Hors dépôt. |
