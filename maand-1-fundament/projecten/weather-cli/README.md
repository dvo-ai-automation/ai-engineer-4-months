# Weather CLI

> **Status: nog niet gebouwd.** De omgeving staat klaar, de code niet. Dit bestand is er eerder
> dan het script — je ziet hier eerst het plan en straks pas of het gelukt is.

Het tweede en laatste project van maand 1. Een script dat de [Open-Meteo API](https://open-meteo.com/en/docs)
aanroept en het weer schoon leesbaar in de terminal print.

## Waarom deze build

De [expense tracker](../expense-tracker/) leest en schrijft bestanden en handelt zijn eigen
errors af. [`bitcoin.py`](../../cs50/Libraries/bitcoin/) roept een externe API aan. Wat ik nog
niet heb gedaan is die twee in één programma combineren — en dat is precies de mijlpaal van
maand 1:

> Een Python-programma dat bestanden leest/schrijft, een API aanroept en zijn eigen errors
> afhandelt zonder te crashen.

Open-Meteo vraagt geen API-key. Dat is bewust: het haalt één obstakel weg, zodat de aandacht
naar het request en het uitpakken van het JSON-antwoord gaat in plaats van naar authenticatie.

## Wat het moet gaan doen

- Een plaatsnaam aannemen en die omzetten naar coördinaten
- Met `requests` een GET-request doen naar Open-Meteo
- Het JSON-antwoord uitpakken en alleen tonen wat je wilt weten — geen ruwe dump
- Niet crashen als er geen internet is, de plaats niet bestaat, of de API traag is
- Netjes reageren op de statuscodes die ertoe doen: 200, 404, 429, 500

## Wat er al staat

```
.venv/              virtual environment, aangemaakt 20 aug
requirements.txt    requests 2.34.2 en zijn dependencies
```

Zelf opzetten:

```bash
cd maand-1-fundament/projecten/weather-cli
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Wat ik hier wil leren

Niet het script zelf — dat is een middel. Het gaat om de vraag die de roadmap overslaat:
**wat is een HTTP-request fysiek?** De lijst statuscodes (200 ok, 401 verkeerde key, 429 rate
limit, 500 serverfout) is pas te onthouden als het model eronder klopt. Elke LLM-aanroep die
ik vanaf maand 2 doe is in de kern ditzelfde request, dus deze laag moet zitten.

---

*Deze README wordt bijgewerkt zodra het script draait — inclusief een demo van de output en
een eerlijk kopje over wat er nog niet aan deugt, net als bij de [expense tracker](../expense-tracker/README.md).*
