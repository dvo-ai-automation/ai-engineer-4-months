# bitcoin

Vraagt de actuele bitcoinkoers op bij de CoinCap-API en rekent hem om naar `n` bitcoin.

De API-key staat **niet** in de code. Hij komt uit een omgevingsvariabele (environment
variable: een instelling die buiten je programma leeft en die je code opvraagt in plaats van
bevat). Zo kan hij nooit per ongeluk mee naar GitHub.

De key zelf staat lokaal in `.env` in de root van deze repo. Dat bestand staat in
`.gitignore` en wordt dus nooit gepusht. `python-dotenv` leest het in bij het starten, dus
je hoeft niets te exporteren.

De key gaat mee als `Authorization: Bearer`-header, niet als `?apiKey=` in de URL. Een URL
belandt in server-logs, proxy-logs en je eigen shell-history; een header niet.

## Draaien

```bash
cd "maand-1-fundament/cs50/libraries/bitcoin"
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python bitcoin.py 2
```

Werkt ook zonder `.env`, als je de key liever per venster zet:

```bash
export COINCAP_API_KEY=je-key-hier
python bitcoin.py 2
```

`export` geldt per terminalvenster. Open je een nieuw venster, dan doe je hem opnieuw. Dat
is precies het ongemak waar `.env` een eind aan maakt.
