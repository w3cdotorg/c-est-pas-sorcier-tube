# C'est pas sorcier Tube

Une sélection de 154 épisodes de *C'est pas sorcier* pour les petits curieux, rangés en 16 thèmes avec un âge indicatif (4 ans +, 5-6 ans, 7 ans +). L'interface s'inspire de [HackerTube](https://hackertube.org/) : menu des thèmes, mur de vignettes, page de lecture avec la suite du thème.

Site : https://w3cdotorg.github.io/c-est-pas-sorcier-tube/

Les épisodes sont lus depuis la [chaîne YouTube officielle](https://www.youtube.com/channel/UCENv8pH4LkzvuSV_qHIcslg). Ce site est un index non officiel, sans lien avec France Télévisions. Les âges sont une estimation d'après le sujet.

## Fonctions

- filtres par âge et par thème, recherche sans accents, « Au hasard ! » (jamais les 7 ans + sauf filtre choisi)
- listes « Déjà vu », « J'aime », « Plus tard » et historique, gardées dans le navigateur (`localStorage`)
- lecteur intégré (youtube-nocookie) sur GitHub Pages, lien vers YouTube ailleurs
- adresses partageables : `#theme-mer`, `#v-<id YouTube>`, `#pour-commencer`…

## Fichiers

| Fichier | Rôle |
|---|---|
| `episodes.json` | les données : thèmes (clé, nom, description, teinte) et épisodes (id YouTube, thème, âge, « pour commencer », titre, durée en minutes) |
| `thumbs/<id>.jpg` | vignettes 320 × 180 |
| `template.html` | la page (CSS + JS, sans dépendance) avec le marqueur `/*DATA*/` |
| `build.py` | injecte les données et produit `index.html` |

Après une modification de `episodes.json` ou de `template.html` :

```sh
python3 build.py
```

Liste relevée sur la chaîne officielle le 23 octobre 2026.
