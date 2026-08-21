# Expense tracker

Een CLI-tool die uitgaven aanneemt, ze valideert, wegschrijft naar JSON en bij het afsluiten
je totaal van vandaag en van deze maand teruggeeft. 87 regels eigen Python, 5 unit tests,
geen dependencies buiten de standaardbibliotheek.

Dit is de eindbuild van maand 1. Hij brengt samen wat CS50P 3, 5 en 6 los aanleerden:
exceptions voor kapotte input, File I/O voor de opslag, unit tests voor mijn eigen functies.

---

## Wat het doet

```console
$ python expenseV4.py
Welkom bij de expense tracker. Typ Ctrl+D om te stoppen.

Input (bedrag, yyyy-mm-dd, opmerking): 4.20, 2026-08-21, koffie
Jouw uitgave is opgeslagen
Input (bedrag, yyyy-mm-dd, opmerking): kat, 2026-08-21, typfout
Bedraginvoer was onjuist
Input (bedrag, yyyy-mm-dd, opmerking): 38.90, 2026-08-21, boodschappen
Jouw uitgave is opgeslagen
Input (bedrag, yyyy-mm-dd, opmerking): ^D

Programma is succesvol afgesloten

Totale uitgaven vandaag: €43.10
Totale uitgaven deze maand is: €43.10
```

De regel met `kat` erin is het punt: foute invoer laat het programma niet crashen. Hij zegt
wat er mis is en vraagt opnieuw. Vijf soorten kapotte input worden opgevangen — geen getal,
verkeerd datumformaat, te weinig velden, te veel velden, en `Ctrl+D` als afsluiter.

## Zelf draaien

```bash
cd maand-1-fundament/projecten/expense-tracker
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python expenseV4.py
```

De tests:

```bash
pytest -q
# 5 passed
```

## De vier versies

De map bevat `expenseV1.py` t/m `expenseV4.py`. Die staan er bewust nog, want de tweede
regel van dit traject is dat alles publiek gaat, ook de lelijke tussenstappen.

| Bestand | Wat erbij kwam |
|---|---|
| `expenseV1.py` | Eén input uitlezen en terugprinten. 10 regels. |
| `expenseV2.py` | Input opsplitsen in bedrag/datum/opmerking, functies aanroepen, optellen. |
| `expenseV3.py` | Validatie met `try`/`except`, opslag in JSON, totalen per dag en per maand. |
| `expenseV4.py` | **De werkende versie.** Maandtotaal telt nu op `%Y-%m` in plaats van een hardcoded `2026-`. |

De sprong van V2 naar V3 is waar het echte werk zit: daar ging het van "leest input" naar
"vertrouwt geen enkele input en houdt zijn data buiten het programma".

## Wat ik hier geleerd heb

- **Validatie is een aparte functie.** `valideer_input()` geeft een dict terug als de invoer
  deugt en `False` als hij dat niet doet. Dat de rest van het programma daarop kan
  vertrouwen, maakt de hoofdloop leesbaar.
- **`try`/`except` rond precies één ding.** `float()` en `datetime.strptime()` hebben elk hun
  eigen blok, zodat de foutmelding kan zeggen wát er mis was.
- **Testen dwingt je functies uit elkaar te trekken.** Ik kon `valideer_input()` alleen
  testen omdat hij niets print en niets opslaat — hij rekent en geeft terug. Dat had ik niet
  bedacht vóór ik de tests schreef.
- **`with open(...)` doet het sluiten voor je**, en `json.dump(..., indent=2)` houdt het
  bestand leesbaar voor een mens.

## Wat er nog niet goed aan is

Eerlijk, want dit is een leerlogboek en niet een etalage:

- `test_expense.py` importeert nog uit `expenseV3`, terwijl `expenseV4` de werkende versie is.
  De tests slagen, maar ze dekken de verkeerde file.
- Het pad naar `expenses.json` is relatief, dus het programma werkt alleen als je hem start
  vanuit deze map.
- `aanvullen()` crasht als `expenses.json` niet bestaat of leeg is. Er hoort een `try`/`except`
  omheen die met een lege lijst begint.
- Geen manier om een uitgave te verwijderen of te corrigeren, en geen categorieën.

Deze lijst is het startpunt voor de volgende ronde, niet een excuus.
