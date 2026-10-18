"""Shop-Liste. Drei Abfragearten:

- shopify:  Shopify-Suche (/search/suggest.json), liefert Preis + Verfügbarkeit direkt
- jsonld:   Suchseite mit schema.org-Produktdaten; fehlt die Verfügbarkeit, wird die Produktseite geprüft
- links:    Kategorie-/Suchseite → Produktlinks einsammeln → jede Produktseite prüfen

Neuen Shop hinzufügen = einen Eintrag ergänzen. Shops, die automatische Abfragen
blocken (Stand 18.10.2026: Thalia, Galeria, Kaufland, Smyths, Rossmann, Pokémon Center, Conrad,
Cyberport, Bücher.de, Netto, Aldi, Rewe, Bol, Euronics, Fantasywelt u. a.), fehlen bewusst.
"""

SHOPS = [
    # Kleine TCG-Shops (Shopify)
    {"name": "Geeks Heaven", "type": "shopify", "base": "https://geeksheaven.de", "queries": ["30 jahre"]},
    {"name": "Starz Collectibles", "type": "shopify", "base": "https://starzcollectibles.de", "queries": ["30 jahre"]},
    {"name": "Card-Binder", "type": "shopify", "base": "https://card-binder.com", "queries": ["30 jahre", "30th deutsch"]},

    # TCG-Fachhändler mit eigener Shop-Software
    # Card-Corner: Hinweistexte („Benachrichtigung … sobald") stehen auf jeder Seite → stattdessen Warenkorb-Button prüfen
    {"name": "Card-Corner", "type": "links", "text_check": False, "require_text": "In den Warenkorb",
     "base": "https://www.card-corner.de",
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
    {"name": "Lidl", "type": "lidl", "base": "https://www.lidl.de",
     "queries": ["pokemon 30 jahre", "pokemon sammelkarten"]},
    {"name": "EDEKA24", "type": "links", "base": "https://www.edeka24.de",
     "url": "https://www.edeka24.de/index.php?lang=0&cl=search&searchparam=pokemon+30+jahre",
     "link_pattern": r'href="(https://www\.edeka24\.de/Pokemon-[^"?]*30-Jahre[^"?]*\.html)',
     "price_regex": r'<div class="price">\s*([\d.,]+)\s*€',
     "avail_regex": r'<li class="delivery-text product-note ([a-z-]*)"', "avail_ok": ["available"]},

    # Spielwaren
    {"name": "Toys-for-Fun", "type": "links", "base": "https://www.toys-for-fun.com",
     "url": "https://www.toys-for-fun.com/de/catalogsearch/result/?q=pokemon+30+jahre",
     "link_pattern": r'href="(https://www\.toys-for-fun\.com/de/pokemon-[a-z0-9-]*30-jahre[a-z0-9-]*\.html)"'},
    {"name": "Rofu", "type": "links", "base": "https://www.rofu.de",
     "url": "https://www.rofu.de/suche?searchPhrase=pokemon+30+jahre",
     "link_pattern": r'"url":"(https://www\.rofu\.de/[a-z0-9-]*\.html)"'},

    # Weitere TCG-Shops (Shopify)
    {"name": "Cardcosmos", "type": "shopify", "base": "https://cardcosmos.de", "queries": ["30 jahre", "30 jahre top trainer", "30 jahre mini tin"]},
    {"name": "Packhunter", "type": "shopify", "base": "https://packhunter.de", "queries": ["30 jahre"]},
    {"name": "Toy Treasure", "type": "shopify", "base": "https://toy-treasure.com", "queries": ["30 jahre", "30 jahre mini tin"]},
    {"name": "Racoon Rises", "type": "shopify", "base": "https://racoon-rises.com", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "CardBuddys", "type": "shopify", "base": "https://cardbuddys.de", "queries": ["30 jahre"]},
    {"name": "CrispyCards", "type": "shopify", "base": "https://crispycards.de", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "Card-Knights", "type": "shopify", "base": "https://www.card-knights.de", "queries": ["30 jahre deutsch", "30 jahre kollektion", "30 jahre mini tin"]},
    {"name": "JustNerds TCG", "type": "shopify", "base": "https://justnerdstcg.de", "queries": ["30 jahre deutsch", "30 jahre"]},
    {"name": "Trinket Mage", "type": "shopify", "base": "https://trinket-mage.eu", "queries": ["30 jahre", "30 jahre mini tin", "30 jahre top trainer box"]},
    {"name": "Prime Protector", "type": "shopify", "base": "https://primeprotector.at", "queries": ["30 jahre"]},
    {"name": "KARDS Greifswald", "type": "shopify", "base": "https://kardsgreifswald.de", "queries": ["pokemon 30 jahre", "30 jahre top trainer"]},
    {"name": "Pushdich-TCG", "type": "shopify", "base": "https://www.pushdich-tcg.de", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "Feenturm", "type": "shopify", "base": "https://feenturm.de", "queries": ["30th celebration deutsch"]},
    {"name": "Steelduck", "type": "shopify", "base": "https://www.steelduck.de", "queries": ["30 jahre deutsch", "30 jahre top trainer box", "30 jahre mini tin"]},
    {"name": "Peer-Online", "type": "shopify", "base": "https://www.peer-online.de", "queries": ["30 jahre", "30 jahre mini tin"]},
    {"name": "TradingToys", "type": "shopify", "base": "https://www.tradingtoys.de", "queries": ["30 jahre top trainer box", "30 jahre booster bundle"]},
    {"name": "Prückis Cards", "type": "shopify", "base": "https://pruckis.de", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "Underpaid Collectibles", "type": "shopify", "base": "https://underpaidcollectibles.com", "queries": ["30 jahre", "30 jahre deutsch"]},
    {"name": "Major Cards TCG", "type": "shopify", "base": "https://majorcardstcg.com", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "RocketCardStore", "type": "shopify", "base": "https://rocketcardstore.de", "queries": ["30 jahre"]},
    {"name": "Dirricards", "type": "shopify", "base": "https://dirricards.de", "queries": ["30 jahre top trainer box", "30 jahre kollektion"]},
    {"name": "Brofessor Eich", "type": "shopify", "base": "https://brofessoreich.de", "queries": ["30 jahre", "30 jahre kollektion"]},
    # Österreich (liefern nach DE)
    {"name": "Kamikura TCG", "type": "shopify", "base": "https://kamikuratcg.com", "queries": ["30th celebration de", "30th celebration"]},
    {"name": "MerchFox", "type": "shopify", "base": "https://www.merchfox.at", "queries": ["30 jahre", "30 jahre kollektion"]},
    {"name": "Comic Galerie Wien", "type": "shopify", "base": "https://shop.comic-galerie.at", "queries": ["30 jahre", "30 jahre tin"]},
    {"name": "Cardcorner Krems", "type": "shopify", "base": "https://cardcorner.at", "queries": ["30 jahre deutsch", "30 jahre"]},

    # TCG-/Spieleläden mit eigener Shop-Software
    {"name": "Gate to the Games", "type": "links", "every": 540, "base": "https://www.gate-to-the-games.de",
     "url": "https://www.gate-to-the-games.de/?qs=Pokemon-30-Jahre+deutsch&af=100",
     "link_pattern": r'href="(https://www\.gate-to-the-games\.de/Pokemon-30-Jahre-[^"#]+)"'},
    {"name": "Comic Planet", "type": "links", "every": 540, "base": "https://www.comicplanet.de",
     "url": "https://www.comicplanet.de/search?search=pokemon+30+jahre",
     "link_pattern": r'href="(https://www\.comicplanet\.de/sammelkarten/pokemon/deutsch/[^"]*pokemon-30-jahre-[^"]+)"'},
    {"name": "Spielgetuschel", "type": "links", "every": 540, "base": "https://spielgetuschel.de",
     "url": "https://spielgetuschel.de/?qs=pokemon+30+jahre",
     "link_pattern": r'href="(https://spielgetuschel\.de/Pokemon-30-Jahre-[^"#]+)"'},
    {"name": "TcG Love", "type": "links", "every": 540, "base": "https://tcg-love.de",
     "url": "https://tcg-love.de/?s=%2230+Jahre%22&post_type=product",
     "link_pattern": r'href="(https://tcg-love\.de/pokemon-30-jahre-[^"]+)"'},
    {"name": "Zambomba", "type": "links", "every": 540, "base": "https://www.zambomba.de",
     "url": "https://www.zambomba.de/?s=pokemon+30+jahre&post_type=product",
     "link_pattern": r'href="(https://www\.zambomba\.de/shop/pokemon-30-jahre-[^"]+)"'},
    {"name": "Sonnenstil", "type": "links", "every": 540, "base": "https://sonnenstil.shop",
     "url": "https://sonnenstil.shop/?s=pokemon+30+jahre&post_type=product",
     "link_pattern": r'href="(https://sonnenstil\.shop/products/[^"]*30-jahre[^"]*)"'},
]
