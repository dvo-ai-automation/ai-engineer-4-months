# bitcoin

Vraagt de actuele bitcoinkoers op bij de CoinCap-API en rekent hem om naar `n` bitcoin.

De API-key staat **niet** in de code — die komt uit een omgevingsvariabele (environment
variable: een instelling die in je terminal leeft, niet in je bestand). Zo kan hij nooit
per ongeluk mee naar GitHub.

De key zelf staat lokaal in `.env` in de root van deze repo. Dat bestand staat in
`.gitignore` en wordt dus nooit gepusht.

## Draaien

```bash
export COINCAP_API_KEY=je-key-hier
python bitcoin.py 2
```

`export` geldt per terminalvenster. Open je een nieuw venster, dan doe je hem opnieuw.
