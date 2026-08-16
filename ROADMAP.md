# Roadmap: van nul naar hireable AI engineer in 4 maanden

Gebaseerd op het artikel *"You can go from zero to hireable AI engineer in 4 months. Here's the exact path."*
(@free_ai_guides, 7 juli 2026 — https://x.com/i/article/2074513567701680128)

- **Start:** donderdag 30 juli 2026
- **Einde:** woensdag 18 november 2026 (16 weken)
- **Tempo:** 15–25 uur per week. Het artikel rekent met 15–20 u/w voor het 4-maandenpad, dus dit tempo haalt het comfortabel.

| Maand | Periode | Thema |
|---|---|---|
| 1 | 30 jul – 26 aug | Python en de plumbing |
| 2 | 27 aug – 23 sep | Bouwen met LLM-API's |
| 3 | 24 sep – 21 okt | RAG en agents |
| 4 | 22 okt – 18 nov | Shippen, laten zien, betaald worden |

> ### 📊 [De volledige uitwerking staat in het dashboard →](https://dvo-ai-automation.github.io/ai-engineer-4-months/)
>
> Per maand: alle skills met hun gekozen resource, de bouwopdrachten, de valkuilen, de
> mijlpalen en de actuele voortgang. Dit bestand houdt alleen nog vast wat vaststaat —
> het dashboard houdt bij waar je staat.

---

## De doelstelling in één zin

> Als je een LLM betrouwbaar een specifieke taak kunt laten doen binnen een app, én je begrijpt genoeg om het te repareren als het stukgaat, dan ben je een AI engineer.

Je bouwt producten bovenop bestaande modellen. Geen calculus, geen backpropagation, geen
transformer-internals. Dat is een ander vak (research scientist).

---

## De twee regels waar alles op rust

1. **De 30-minutenregel** — per uur kijken of lezen minstens 30 minuten bouwen zónder tutorial
   open. Typ de voorbeelden zelf. Maak ze kapot. De errors zijn het leren.
2. **Alles gaat publiek** — elk project op GitHub op de dag dat je het af hebt, ook de lelijke.

---

## De 4 fouten — lees dit elke maandag opnieuw

Deze fouten beëindigen een carrièreswitch in week 2, niet in maand 3.

**1. Beginnen met theorie en wiskunde.**
Fix: overslaan. Je pikt de concepten op als je ze in een echt project tegenkomt, en dán blijven ze hangen.

**2. Tutorials kijken in plaats van bouwen.**
Fix: de 30-minutenregel hierboven.

**3. Tools leren in plaats van skills.**
Fix: leer de skill ónder de tool. Een betrouwbare prompt schrijven verloopt niet als een framework update. Deze roadmap is daarom per skill georganiseerd, niet per tool.

**4. Wachten tot je je klaar voelt om in het openbaar te bouwen.**
Fix: begin in maand 1. Niemand kijkt zo aandachtig mee dat je vroege werk je in verlegenheid brengt.

**De switcher's edge:** werkgevers vragen bij AI-functies steeds vaker om oordeelsvermogen,
communicatie en het kunnen bezitten van een uitkomst — precies wat je uit je vorige carrière
meebrengt en wat een 22-jarige met een CS-diploma nog niet heeft. Houd dit vier maanden lang
in je achterzak.

---

## Verdiepen — begrippen die deze roadmap niet uitlegt

*Bijgehouden sinds 14 aug 2026, op basis van de vragen die tijdens het bouwen opkwamen. De
roadmap noemt deze termen als bullet point alsof je ze al kent; voor een beginner zijn het
gaten. Deze lijst staat bewust hier en niet in het dashboard — het zijn jouw open vragen,
geen onderdeel van het oorspronkelijke plan.*

- [x] **Environment variable** — uitgelegd 14 aug, in de praktijk gebruikt 16 aug. Een waarde
      die búiten je programma leeft en die je code opvraagt in plaats van bevat. Bestaat zodat
      je API-keys niet in je repo belanden. `export` geldt alleen in het venster waarin je het
      typt — daarom `.env` + `python-dotenv`, en `.env` altijd in `.gitignore`. Toepassing:
      [`bitcoin.py`](maand-1-fundament/cs50/Libraries/bitcoin/bitcoin.py) haalt zijn
      CoinCap-key uit `COINCAP_API_KEY` in plaats van uit de code.
- [x] **Branching en merging** — geleerd 16 aug op deze repo: het dashboard en deze herschrijving
      zijn op een aparte branch gebouwd en pas daarna samengevoegd. Een merge-conflict veroorzaken
      en oplossen staat nog open; dat komt vanzelf.
- [ ] **Virtual environment (venv)** — zelfde familie als de env var: iets buiten je code dat
      bepaalt hoe hij draait. Zonder dit installeer je in maand 2 geen enkele SDK.
      **Eerstvolgende om op te pakken.**
- [ ] **`async`/`await`** — de roadmap zegt "weet dat het bestaat" en legt niet uit wát er dan
      bestaat. Eén alinea is genoeg; hoeft niet vóór maand 2 af.
- [ ] **Wat een HTTP-request/response fysiek ís** — de roadmap springt meteen naar statuscodes
      (200/401/429/500). Die lijst is pas betekenisvol als het onderliggende model klopt.
      Hoort bij week 4.

---

## Waar de rest gebleven is

De volledige uitgeschreven roadmap — alle skills per maand, de picks, de "hoeveel is genoeg"-
grenzen per resource, de CS50P-volgorde en de mijlpalen — staat nu in het
[dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/), en de tekstversie
blijft opvraagbaar in de git-history:

```bash
git show aee8ab0:ROADMAP.md
```
