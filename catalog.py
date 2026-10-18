"""Produktkatalog „Pokémon 30 Jahre" (deutsche Edition) mit UVP.

Ein Shop-Titel wird über Schlüsselwörter einem Produkt zugeordnet.
Reihenfolge zählt: spezifische Produkte zuerst, der Einzelbooster ganz zum Schluss.
UVP-Quellen: Gameshop Marli / Monsterdealz / TCGcheck (Stand Oktober 2026).
"""

import re
import unicodedata

# (key, Anzeigename, UVP in €, Pflicht-Schlüsselwörter (eins davon muss vorkommen))
PRODUCTS = [
    ("upc", "Ultra-Premium-Kollektion (Tag/Nacht)", 199.99, ["ultra-premium", "ultra premium", "upc"]),
    ("ditto", "Premium-Kollektion Ditto", 46.99, ["ditto"]),
    ("figur", "Figuren-Kollektion Mew/Mewtu", 35.99, ["figuren-kollektion", "figuren kollektion", "figure collection"]),
    ("ttb", "Top-Trainer-Box", 55.00, ["top-trainer", "top trainer", "elite trainer", "ttb", "etb"]),
    ("minitin_display", "Mini-Tin Display (10 Tins)", 139.90, ["mini-tin display", "mini tin display", "mini-tin-display"]),
    ("bundle", "Boosterbundle (6 Booster)", 29.99, ["bundle"]),
    ("minitin", "Mini-Tin-Box", 13.99, ["mini-tin", "mini tin", "minitin"]),
    ("tin", "Tin-Box Feelinara-ex / Quajutsu-ex", 24.99, ["tin-box", "tin box", "tin #", "tin 1", "tin 2", "tin -", "tin tag", "tin nacht"]),
    ("deck", "Kampfdeck Psiana-ex / Nachtara-ex", 25.99, ["kampfdeck", "battle deck"]),
    ("ordner", "Ordner-Kollektion", 46.99, ["ordner", "binder"]),
    ("poster", "Poster-Kollektion", 23.99, ["poster"]),
    ("sticker", "Tech-Sticker-Kollektion", 19.99, ["sticker"]),
    ("knockout", "Knock-out-Kollektion", 12.99, ["knock-out", "knock out", "knockout"]),
    ("blister", "2er-Pack-Blister", 12.99, ["2er", "blister"]),
    ("ex", "Kollektion Feelinara-ex / Quajutsu-ex", 24.99, ["feelinara", "quajutsu", "ex-kollektion", "ex kollektion"]),
    ("booster", "Einzelbooster", 4.99, ["booster"]),
]

UVP = {k: uvp for k, _, uvp, _ in PRODUCTS}
NAMES = {k: name for k, name, _, _ in PRODUCTS}

# Fremdsprachen, Einzelkarten, Leerboxen, Pokémon-Center-Exklusivware usw.
EXCLUDE = [
    "englisch", "english", "(en)", " en ", " en,", " eng ", "japan", " jp", "(jp)", "chinesisch", "chinese",
    "t-chinese", "s-chinese", "koreanisch", "korean", "thai", "indonesisch", "franzosisch", "italienisch",
    "spanisch", "pokemon center", "einzelkarte", "graded", "psa ", "cgc ", "leer", "ohne booster",
    "kartenhullen", "sleeves", "kuscheltier", "plusch", "puzzle", "select-serie", "first partner",
    "multipack", "sortiert", "wizard", "acryl", " case", "schutzhulle", "schutzbox", "protector",
    "magnetic", "toploader", "aufbewahrung", "x booster", "x30", "lot ",
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return " " + re.sub(r"\s+", " ", text) + " "


def is_german_30_jahre(title: str) -> bool:
    t = normalize(title)
    if any(x in t for x in EXCLUDE):
        return False
    if "30 jahre" in t or "30-jahre" in t:
        return True
    # Manche Shops schreiben „30th … (Deutsch)"
    return ("30th" in t or "jubilaum" in t) and ("deutsch" in t or "(de)" in t or " de " in t)


def classify(title: str):
    """Gibt den Produkt-Key zurück oder None, wenn kein deutsches 30-Jahre-Produkt."""
    if not is_german_30_jahre(title):
        return None
    t = normalize(title)
    # Displays/Kisten mit mehreren Einheiten nur, wenn ausdrücklich im Katalog
    if "display" in t and "mini" not in t:
        return None
    for key, _, _, words in PRODUCTS:
        if any(w in t for w in words):
            return key
    return None
