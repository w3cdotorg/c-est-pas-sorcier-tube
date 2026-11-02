"""Construit le site à partir de template.html et episodes.json.

    python3 build.py                 -> index.html (GitHub Pages, document complet)
    python3 build.py --artifact DIR  -> DIR/index.html (fragment pour l'artefact claude.ai)

Les vignettes restent dans thumbs/<id>.jpg, référencées en chemin relatif.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='8' fill='%23ffc531'/%3E%3Ctext x='16' y='22.5' "
           "text-anchor='middle' font-family='Trebuchet MS,Arial,sans-serif' font-weight='700' "
           "font-size='16' fill='%233a2a00'%3E%3F!%3C/text%3E%3C/svg%3E")


# Site GitHub : rien de coché d'avance ; chaque navigateur garde ses « Déjà vu » en localStorage.
# Artefact : part de l'épisode déjà vu à la maison.
SITES = {
    "github": {"seedSeen": [], "seenNav": True},
    "artifact": {"seedSeen": ["dybWx0kAYJE"], "seenNav": True},
}


def page(site: str) -> str:
    data = json.loads((ROOT / "episodes.json").read_text(encoding="utf8"))
    payload = {k: data[k] for k in ("listed", "themes", "episodes")}
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (ROOT / "template.html").read_text(encoding="utf8")
    for mark in ("/*DATA*/", "/*SITE*/"):
        assert tpl.count(mark) == 1, f"marqueur {mark} absent ou en double"
    return tpl.replace("/*DATA*/", blob).replace("/*SITE*/", json.dumps(SITES[site]))


def standalone(body: str) -> str:
    head, sep, rest = body.partition("</style>")
    assert sep, "</style> introuvable"
    return ("<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
            "<meta name=\"description\" content=\"Épisodes de C'est pas sorcier pour les petits curieux, rangés par thème avec un âge indicatif.\">\n"
            f"<link rel=\"icon\" href=\"{FAVICON}\">\n"
            "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n"
            f"{head}</style>\n</head>\n<body>{rest}</body>\n</html>\n")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--artifact":
        body = page("artifact")
        out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
        (out / "index.html").write_text(body, encoding="utf8")
        print("fragment ->", out / "index.html")
    else:
        (ROOT / "index.html").write_text(standalone(page("github")), encoding="utf8")
        print("site ->", ROOT / "index.html")
