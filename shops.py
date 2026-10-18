"""Shop-Liste. Drei Abfragearten:

- shopify:  Shopify-Suche (/search/suggest.json), liefert Preis + Verfügbarkeit direkt
- jsonld:   Suchseite mit schema.org-Produktdaten; fehlt die Verfügbarkeit, wird die Produktseite geprüft
- links:    Kategorie-/Suchseite → Produktlinks einsammeln → jede Produktseite prüfen

Neuen Shop hinzufügen = einen Eintrag ergänzen. Shops, die automatische Abfragen
blocken (Stand 18.10.2026: Thalia, Galeria, Kaufland, Weltbild, Fantasywelt), fehlen bewusst.
"""

SHOPS = [
    # Kleine TCG-Shops (Shopify)
    {"name": "Geeks Heaven", "type": "shopify", "base": "https://geeksheaven.de", "queries": ["30 jahre"]},
    {"name": "Starz Collectibles", "type": "shopify", "base": "https://starzcollectibles.de", "queries": ["30 jahre"]},
    {"name": "Card-Binder", "type": "shopify", "base": "https://card-binder.com", "queries": ["30 jahre", "30th deutsch"]},

    # TCG-Fachhändler mit eigener Shop-Software
    {"name": "Card-Corner", "type": "links", "base": "https://www.card-corner.de",
     "url": "https://www.card-corner.de/pokemon-30-jahre",
     "link_pattern": r'href="(https://www\.card-corner\.de/Pokemon-30-Jahre-[A-Za-z0-9-]+)"'},
    {"name": "Steinehelden", "type": "links", "base": "https://steinehelden.de",
     "url": "https://www.steinehelden.de/search?sSearch=pokemon+30+jahre",
     "link_pattern": r'href="(https://steinehelden\.de/[^"]*30-Jahre[^"]*/\d+)"'},
    {"name": "Alternate", "type": "links", "base": "https://www.alternate.de",
     "url": "https://www.alternate.de/listing.xhtml?q=pokemon+30+jahre",
     "link_pattern": r'href="(https://www\.alternate\.de/[^"]*30-Jahre[^"]*/html/product/\d+)"'},

    # Große Händler
    # MediaMarkt/Saturn funktionieren lokal, blocken aber GitHub-Server (403) – daher aus.
    # {"name": "MediaMarkt", "type": "jsonld", "base": "https://www.mediamarkt.de",
    #  "url": "https://www.mediamarkt.de/de/search.html?query=pokemon%2030%20jahre"},
    # {"name": "Saturn", "type": "jsonld", "base": "https://www.saturn.de",
    #  "url": "https://www.saturn.de/de/search.html?query=pokemon%2030%20jahre"},
    {"name": "Müller", "type": "jsonld", "base": "https://www.mueller.de",
     "url": "https://www.mueller.de/search/?q=pokemon+30+jahre+sammelkarten"},
    {"name": "Otto", "type": "jsonld", "base": "https://www.otto.de",
     "url": "https://www.otto.de/suche/pokemon%2030%20jahre/"},
]
