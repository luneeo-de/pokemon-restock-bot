# Pokémon 30 Jahre – Restock-Bot

Prüft alle ~3 Minuten 44 deutsche (und österreichische) Shops auf Produkte der deutschen Edition „Pokémon 30 Jahre“ und schickt
einen Telegram-Ping, sobald etwas **lieferbar** ist und **höchstens UVP + 10 %** kostet.
Scalper-Preise und Fremdsprachen (EN/JP/CN/KR) werden ignoriert.

| Datei | Inhalt |
|---|---|
| `catalog.py` | Produkte, UVP, Erkennungsregeln |
| `shops.py` | Shop-Liste (neuen Shop = ein Eintrag) |
| `bot.py` | Abfrage, Preisfilter, Telegram, Zustand |
| `.github/workflows/check.yml` | Zeitplan auf GitHub Actions |

## Lokal testen

```bash
DRY_RUN=1 python3 bot.py
```

## Einstellungen

- Aufschlag ändern: GitHub → Settings → Secrets and variables → Actions → *Variables* → `MAX_AUFSCHLAG_PROZENT`
- Secrets: `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID` (Chat-ID per `python3 setup_telegram.py <TOKEN>`)
- Jeden Tag um 9 Uhr kommt ein kurzes Lebenszeichen. Ist ein Shop ~1 Stunde lang nicht erreichbar, kommt eine Warnung.

Hinweis: GitHub pausiert geplante Workflows, wenn das Repo 60 Tage keinen Commit hatte – dann im Tab *Actions* wieder aktivieren.
