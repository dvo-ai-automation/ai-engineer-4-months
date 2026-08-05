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

---

## De doelstelling in één zin

> Als je een LLM betrouwbaar een specifieke taak kunt laten doen binnen een app, én je begrijpt genoeg om het te repareren als het stukgaat, dan ben je een AI engineer.

Je bouwt producten bovenop bestaande modellen. Geen calculus, geen backpropagation, geen transformer-internals. Dat is een ander vak (research scientist).

---

## De 4 fouten — lees dit elke maandag opnieuw

Deze fouten beëindigen een carrièreswitch in week 2, niet in maand 3.

**1. Beginnen met theorie en wiskunde.**
Fix: overslaan. Je pikt de concepten op als je ze in een echt project tegenkomt, en dán blijven ze hangen.

**2. Tutorials kijken in plaats van bouwen.**
Fix: de 30-minutenregel — per uur kijken/lezen minstens 30 minuten bouwen zónder tutorial open. Typ de voorbeelden zelf. Maak ze kapot. De errors zijn het leren.

**3. Tools leren in plaats van skills.**
Fix: leer de skill ónder de tool. Een betrouwbare prompt schrijven verloopt niet als een framework update. Deze roadmap is daarom per skill georganiseerd, niet per tool.

**4. Wachten tot je je klaar voelt om in het openbaar te bouwen.**
Fix: begin in maand 1. Elk project op GitHub op de dag dat je het af hebt, ook de lelijke. Niemand kijkt zo aandachtig mee dat je vroege werk je in verlegenheid brengt.

**De switcher's edge:** werkgevers vragen bij AI-functies steeds vaker om oordeelsvermogen, communicatie en het kunnen bezitten van een uitkomst — precies wat je uit je vorige carrière meebrengt en wat een 22-jarige met een CS-diploma nog niet heeft. Houd dit vier maanden lang in je achterzak.

---

## Maand 1 — Python en de plumbing (30 jul – 26 aug)

**Doel:** een functionele Python-developer worden die een API kan aanroepen, een klein project kan beheren en niet meer hoeft te googelen op basissyntax. Niet expert. Functioneel.

AI engineering is éérst software engineering. Als deze laag wankelt, wordt de AI-laag nooit betrouwbaar.

### Skills en picks

| Skill | Pick uit het artikel | Waar |
|---|---|---|
| Python | **CS50P** (Harvard, Introduction to Programming with Python) | cs50.harvard.edu/python |
| Git & GitHub | **GitHub Skills** (interactief, in GitHub zelf) | skills.github.com |
| Terminal | korte beginnerscursus, daarna er gewoon in leven | (MIT "Missing Semester" als je dieper wilt — missing.csail.mit.edu) |
| API's / HTTP | **MDN Web Docs HTTP overview** + **Python `requests` docs** | developer.mozilla.org/en-US/docs/Web/HTTP/Overview + requests.readthedocs.io |
| SQL | **SQLBolt** (~20 korte browserlessen) | sqlbolt.com |

Als CS50P te steil voelt als absolute beginner: de freeCodeCamp Python-cursus op YouTube is een zachtere oprit, maar behandel die als warming-up en kom terug naar CS50P zodra een leeg bestand je niet meer bang maakt.

### Waar je op focust

- **Python:** variabelen en datatypes → loops en condities → functies → collections (lists, dicts, sets, tuples) → file handling + JSON lezen/schrijven → net genoeg classes/OOP om andermans code te lezen → error handling met `try`/`except` → virtual environments en pip.
- **Git:** de kernloop `init, add, commit, push, pull` → branching en merging → `.gitignore` en waarom je nooit secrets of API-keys commit → een basis-README schrijven.
- **Terminal:** `cd, ls, pwd, mkdir, rm` → `cat, grep` → een Python-script draaien → een environment variable zetten (nodig zodra je API-keys hebt).
- **API's:** GET en POST in Python → JSON lezen/schrijven → statuscodes (200 ok, 401 verkeerde key, 429 rate limit, 500 serverfout) → wat een API-key is → lichte kennismaking met `async`/`await` (niet diep in duiken, alleen weten dat het bestaat).
- **SQL:** `SELECT, WHERE, GROUP BY, JOIN, ORDER BY`. Meer niet.

Niets uit je hoofd leren. Goed genoeg begrijpen om het snel op te zoeken, en ermee bouwen tot het blijft plakken.

### Weekindeling

- [ ] **Week 1 (30 jul – 5 aug):** setup afronden · CS50P start (variabelen, condities, loops, functies) · [prompt 1](prompts/01-python-learning-partner.md) vanaf dag 1 gebruiken
- [ ] **Week 2 (6 – 12 aug):** CS50P collections + file handling/JSON · GitHub Skills · een week lang alles via de terminal doen
- [ ] **Week 3 (13 – 19 aug):** CS50P exceptions, lichte OOP, venv/pip · **build: CLI-tool** (expense tracker die naar JSON leest/schrijft, 60–100 regels eigen code)
- [ ] **Week 4 (20 – 26 aug):** HTTP/API's/`requests` · **build: script dat Open-Meteo aanroept** en het resultaat netjes print · SQLBolt afronden

### Build targets

- [ ] CLI-tool die iets echts doet (~60–100 regels eigen code). Lelijk mag. Dat jij het schreef niet.
- [ ] Python-script dat een gratis publieke API zonder key aanroept (Open-Meteo — open-meteo.com/en/docs) en schoon geformatteerde output print.

### Milestone — af als je dit kunt

- [ ] Een Python-programma schrijven dat bestanden leest en schrijft, een API aanroept, en zijn eigen errors afhandelt zonder te crashen
- [ ] Die code versioneren met Git en in een GitHub-repo hebben staan
- [ ] Zonder aarzelen door de terminal bewegen
- [ ] Uitleggen wat een HTTP-request is en er één maken in Python
- [ ] Een basis-SQL-query draaien

> Dit is het minst spannende deel en tegelijk het moeilijkste, omdat de meeste mensen hier afhaken. Vanaf maand 2 bouw je mét AI.

---

## Maand 2 — Bouwen met LLM-API's (27 aug – 23 sep)

**Doel:** echte AI-features bouwen met model-API's. Dit is de kern van het hele vak; alles daarna bouwt hierop voort. Diepte in maand 2 betaalt zich meer terug dan diepte waar dan ook.

### Skills en picks

| Skill | Pick uit het artikel |
|---|---|
| Prompting | **Anthropic's interactive prompt engineering tutorial** (repo `anthropics/prompt-eng-interactive-tutorial`), daarna de officiële prompt-docs van Anthropic en OpenAI als naslag |
| Structured outputs | **Instructor** (Python) + Pydantic, met de officiële structured-output docs ernaast |
| Tool calling | **OpenAI function calling guide** en **Anthropic tool use docs** naast elkaar lezen, daarna een runnable notebook (OpenAI cookbook) |
| Conversation state | messages-documentatie van beide providers |
| Streaming | officiële streaming-docs + Simon Willison's uitleg van hoe streaming eronder werkt |
| Prompt injection | **OWASP-guide** |

### Waar je op focust

- **Prompting:** verschil system message vs. user message · specificiteit verslaat beleefdheid · chain-of-thought · few-shot voorbeelden · gevoel krijgen voor hoe kleine woordkeuzes grote outputverschillen geven.
- **Structured outputs:** een Pydantic-model definiëren · schema meegeven aan de API · omgaan met weigeringen en onverwachte output · verschil tussen échte structured outputs (schema afgedwongen) en losse JSON-mode (niet gegarandeerd).
- **Tool calling — het mentale model:** het model draait jouw functies niet. Het besluit dát er een tool nodig is en geeft een gestructureerd verzoek terug met functienaam en argumenten. Jouw code voert uit en geeft het resultaat terug. *Het model is de beslisser, jouw code zijn de handen.* De kwaliteit van je tool-beschrijvingen telt zwaarder dan beginners verwachten.
- **Conversation state:** modellen hebben geen geheugen tussen calls. Een gesprek is iets dat jíj beheert door de volledige history mee te sturen.
- **Streaming:** `stream` aanzetten, over de chunks itereren, het volledige antwoord uit de stukken samenstellen.
- **Kosten en tokens:** een token ≈ driekwart woord, input en output apart geprijsd. Vuistregel die echt geld scheelt: gebruik niet het grootste, duurste model voor simpele taken.
- **Failure handling:** rate limits opvangen en retryen met exponentiële backoff (de **Tenacity**-library doet dit met één decorator) · output valideren vóór je hem vertrouwt · nooit een onverwacht antwoord je hele app laten slopen.
- **Prompt injection:** het grootste beveiligingsrisico in LLM-apps. Kerndefensies: laat ongevalideerde modeloutput nooit automatisch consequente acties uitvoeren, en geef je tools de minste toegang die ze nodig hebben.

### Build targets

- [ ] **Prompt-oefening:** één echte taak (bv. een document samenvatten of feedback classificeren), vijf verschillende prompts ervoor schrijven, alle vijf draaien en de outputs naast elkaar leggen.
- [ ] **Bon-/factuurparser:** ruwe rommelige tekst zoals `"Invoice 123, $45.99 for 3 widgets, due March 30"` in, schoon gestructureerd object uit (factuurnummer, bedrag, aantal, vervaldatum). Gebruik [prompt 2](prompts/02-structured-data-extraction.md). Portfoliostuk.
- [ ] **Mini-assistent met drie tools:** `get_weather`, `calculate`, `search_notes` (die laatste zoekt gewoon in een hardcoded dictionary). Kijken hoe het model zelf de juiste kiest.
- [ ] **Multi-turn terminal-chatbot** die history bijhoudt en een reset-commando heeft.

### Milestone — af als je dit kunt

- [ ] Prompts schrijven die betrouwbare output geven voor een gegeven taak
- [ ] Gestructureerde JSON uit een model halen met Pydantic en Instructor
- [ ] Tool calling opzetten zodat een model jouw Python-functies kan draaien
- [ ] Een antwoord realtime streamen
- [ ] Multi-turn gespreksgeschiedenis beheren
- [ ] De tokenkosten van een request inschatten vóór je hem verstuurt
- [ ] API-fouten en slechte output afhandelen zonder crash
- [ ] Uitleggen wat prompt injection is

---

## Maand 3 — RAG en agents (24 sep – 21 okt)

**Doel:** systemen bouwen die modellen laten antwoorden uit jóuw documenten, en systemen die zelfstandig meerdere stappen zetten. Dit zijn de meest gevraagde praktische vaardigheden in AI engineering op dit moment.

De lat: één solide retrieval-systeem, één solide agent, begrijpen waarom elk onderdeel er zit, en het kunnen debuggen als het breekt.

### RAG in gewone taal

Je geeft het model een bibliotheek om dingen in op te zoeken. Documenten → in chunks knippen → elke chunk omzetten in een reeks getallen die de betekenis vangt → opslaan. Bij een vraag: vraag op dezelfde manier omzetten, de chunks vinden waarvan de getallen het dichtst bij liggen, die samen met de vraag aan het model geven. Al het andere is verfijning.

### Skills en picks

| Skill | Pick uit het artikel |
|---|---|
| Embeddings | Stack Overflow blog "intuitive introduction to text embeddings" (mentaal model) + OpenAI embeddings guide (in code) |
| Chunking | LangChain **RecursiveCharacterTextSplitter**, chunk size ~500, overlap ~50 |
| Vector database | **Chroma**, lokaal — docs.trychroma.com (pgvector later, als je app al Postgres gebruikt) |
| Reranking | Cohere reranking-docs |
| RAG-framework | **LlamaIndex** (search-first) |
| Agents | **Anthropic's "Building Effective Agents"** lezen vóór je één regel agent-code schrijft, daarna intro tot **LangGraph** |
| Evals | **DeepEval** algemeen, **Ragas** voor RAG |

### Waar je op focust

- **Embeddings:** wat een vector conceptueel is, waarom vergelijkbare tekst vergelijkbare vectoren geeft, hoe je ruwweg de afstand meet. De wiskunde eronder heb je niet nodig.
- **Chunking:** de afruil — te grote chunks verliezen precisie, te kleine verliezen context. Overlap voorkomt dat je betekenis verliest op de grens tussen twee chunks.
- **Vector-DB:** collection aanmaken, embeddings + metadata (bron, sectie) invoegen, queryen op similarity, filteren op metadata. Indexeringsalgoritmes hoef je niet te snappen.
- **Retrieval echt goed maken:** metadata-filtering (het verschil tussen speelgoed en een systeem waar iemand "alleen resultaten uit het Q4-rapport" kan vragen) · reranking (breed ophalen, dan terugscoren naar de beste paar).
- **Retrieval debuggen** — de belangrijkste gewoonte van deze maand: *de meeste RAG-fouten zijn retrieval-fouten, geen modelfouten.* Faalmodi: vraag en chunk matchen niet in getallenruimte (herschrijf de query) · relevante info verdeeld over twee chunks (meer overlap) · juiste chunk bestond maar haalde de top niet (haal er meer op, rerank terug). **Kijk altijd eerst wat er opgehaald werd voordat je het model de schuld geeft.**
- **Grounding en citaties:** geef de broninformatie per chunk mee in je prompt en instrueer het model die te citeren. → [prompt 3](prompts/03-grounded-rag-answering.md)

### Agents

Een agent is een loop waarin het model steeds de volgende stap kiest, die zet met een tool, naar het resultaat kijkt, en opnieuw kiest — tot de taak klaar is. **Mentaal model: een agent is een while-loop met een model dat de vertakkingen kiest.** Het denken zit in de prompt, de vertakking is het model dat een tool kiest, het doen is jouw code die de tool draait. De rest is plumbing.

Focus op: de loop perceive → decide → act → observe en hoe hij weet wanneer te stoppen · wat er gebeurt als een tool-call faalt binnen de loop · tool-beschrijvingen schrijven die het model echt kan gebruiken · state beheren.

**De waardevolste oefening van de maand:** bouw een kleine agent volledig from scratch, zonder framework, alleen de model-API. Drie tools, een doel, een loop. Dit laat je zien wat de frameworks verbergen. **Doe dit vóór je LangGraph aanraakt.**

### Wanneer je géén agent gebruikt

Dit onderscheidt iemand met oordeelsvermogen van iemand die het glimmende ding najaagt. Agents zijn trager, duurder, minder voorspelbaar en lastiger te debuggen.

> **Beslisregel:** één model-call als de taak in één prompt past · een vaste workflow als de stappen voorspelbaar zijn · een agent alléén als het aantal stappen echt onvoorspelbaar is en het model dynamisch moet beslissen.

Daartussen ligt veel productieve ruimte: chaining (output van de één is input van de ander), routing (input classificeren en naar een specialist sturen), parallelisatie (meerdere calls tegelijk, daarna combineren). De meeste echte problemen zijn workflows, geen agents.

### Evals

Bouw een set van 20–30 representatieve inputs met verwachte outputs of een scoringsrubriek. Draai je systeem daartegen bij elke promptwijziging, modelwissel of retrieval-aanpassing. *Elke promptwijziging zonder evals is een gok.*

### Build targets

- [ ] **Mini-RAG:** 20 zinnen over verwante onderwerpen embedden, functie die bij een nieuwe zin de drie meest vergelijkbare teruggeeft
- [ ] **"Chat met je documenten"-app** (hoofdportfoliostuk): 10–20 PDF's of tekstbestanden ingesten, vraag in → relevante chunks ophalen met reranking → geciteerd antwoord terug, met simpele interface
- [ ] **Agent from scratch**, zonder framework, drie tools
- [ ] **Eval-set** van 20–30 inputs op één van je systemen

### Milestone — af als je dit kunt

- [ ] Uitleggen wat een embedding is en waarom vergelijkbare tekst vergelijkbare vectoren geeft
- [ ] Een document zinnig chunken
- [ ] Embeddings opslaan en queryen in een vector-DB met metadata-filtering
- [ ] Reranking toevoegen
- [ ] Een retrieval-fout debuggen in plaats van het model de schuld geven
- [ ] Een complete RAG-pipeline bouwen die gegronde, geciteerde antwoorden geeft
- [ ] Een agent-loop from scratch implementeren
- [ ] Correct kiezen tussen één call, een workflow of een agent
- [ ] Een basis-eval draaien

---

## Maand 4 — Shippen, laten zien, betaald worden (22 okt – 18 nov)

**Doel:** alles wat je gebouwd hebt echt maken, en het omzetten in een baan of betaald werk. Hier stallen de meeste mensen: ze kunnen een demo bouwen maar niets shippen dat echt gebruik overleeft, en ze kunnen hun skills niet omzetten in inkomen.

### Genoeg deployment om gevaarlijk te zijn

Je hoeft geen infrastructuur-expert te worden. Je moet een werkende AI-app ergens neer kunnen zetten waar echte mensen hem gebruiken, zonder dat hij omvalt of je failliet maakt.

- Genoeg **Docker** om je app te packagen (einde van "works on my machine") — de officiële getting-started guide volstaat
- Die container ergens deployen
- **Kostenbeheersing:** harde spending limits op je API-accounts · caching zodat je niet twee keer voor dezelfde request betaalt · rate limiting zodat één gebruiker je rekening niet kan opblazen · goedkopere modellen waar die goed genoeg zijn
- **Observability:** LLM-apps hebben een eigen probleem — het model kan een perfect geslaagde response teruggeven die tegelijk nutteloos of fout is, en normale monitoring ziet dat niet. **Langfuse** tracet elke model-call: prompt, response, tokenkosten, latency. Zet dit op bij één project.

Niet overinvesteren. Eén app, netjes gedeployed, met kostenbeheersing en basis-tracing.

### Projecten omzetten in een baan

**Portfolio = drie gedeployde projecten**, elk met een README die echt werk doet.

> **De move die bijna niemand maakt:** zet in elke README een sectie over wat er misging en wat je anders zou doen. De meeste portfolio's doen alsof alles perfect werkte, wat oneerlijk of oppervlakkig overkomt. Een README die zegt "hier faalde mijn eerste aanpak, dit leerde ik, zo heb ik het opgelost" laat precies het oordeelsvermogen zien waar werkgevers nu op screenen. Dat is de switcher's edge, zichtbaar gemaakt.

**README-structuur (vijf secties):**
1. Welk probleem het project oplost
2. Wie het zou gebruiken
3. Welke aanpak je koos en waarom
4. Wat er misging en wat je leerde
5. Hoe je het draait

**Resume/profiel:** je hoeft niet te doen alsof je jaren ervaring hebt. Eén heldere regel volstaat — *"I build production LLM applications: RAG systems, agents, and API integrations. Here are three I've shipped."* — met links naar de projecten. Je vorige carrière is een troef, geen ding om te verbergen: "Voormalig [jouw vakgebied] die nu AI-systemen bouwt" is een sterker verhaal dan "junior developer".

**Building in public is je pipeline.** De beste kansen gaan naar wie zichtbaar was, niet naar wie stil op 500 vacatures solliciteerde.

### Kies een richting (één, niet alle drie)

- **AI product engineer** — snelst naar een startup-baan. Je hebt het meeste al uit maand 1–3. Ga dieper op complete, gepolijste apps en de productkant: hoe de app omgaat met een model dat fout zit, loading states, feedback van gebruikers. Ship twee of drie dingen die mensen echt kunnen proberen.
- **Applied ML** — voor diepere technische rollen. Voorbij API-calls: fine-tuning, wanneer wél/niet, open-source modellen lokaal draaien met **Ollama**, inference-optimalisatie. *Beslisregel: begin met prompting, voeg retrieval toe als het model jouw specifieke data nodig heeft, en fine-tune pas als prompting en retrieval de kwaliteit echt niet halen.*
- **AI automation** — snelst geld verdienen bij bedrijven. Echte workflows automatiseren, AI ketenen over e-mail, CRM's, documenten, spreadsheets. **n8n** voor visueel, **LangGraph** voor code. Verkoopbare build: een lead-qualification-systeem dat leads binnenhaalt, elke lead met een model onderzoekt en scoort, gepersonaliseerde outreach opstelt en alles logt.

### Milestone — af als je dit hebt

- [ ] Een gedeployde AI-app met echte kostenbeheersing
- [ ] Drie portfolioprojecten, elk met een eerlijke README
- [ ] Een heldere one-liner over wat je bouwt
- [ ] Een zichtbaar spoor van werk in het openbaar
- [ ] Een gekozen richting om dieper op te gaan

---

## Het eerlijke deel

Vier maanden gefocust werk maakt je inzetbaar op juniorniveau of klaar voor freelancewerk. Het maakt je geen senior — dat komt uit jaren dingen shippen onder echte beperkingen, en geen enkele gids comprimeert dat.

Wat vier maanden je wél koopt: het vermogen AI-systemen te bouwen, shippen en deployen die echte problemen oplossen. Dat is een oprecht waardevolle en oprecht aanneembare plek.

Wat mensen kapotmaakt is niet een traag tempo. Het is stoppen. Consistentie verslaat intensiteit, elke keer.

En alles rust op één gedrag: **bouwen, niet alleen kijken.** Elke maand heeft een project. Doe de projecten.

## De cijfers (bron: Glassdoor, juni 2026)

- Gemiddeld AI engineer-salaris VS: ~$143.500 · typische range $115.000 (25e percentiel) – $181.000 (75e) · toppers tot ~$223.000
- Senior AI engineers: gemiddeld ~$285.000 · range ~$221.000 – $375.000
- Recruiters die mensen in echte productie-AI plaatsen rapporteren mid-level basissalarissen tussen $155.000 en $200.000, op basis van getekende offers

**Marktcontext (PwC 2026 Global AI Jobs Barometer, >1 miljard vacatures):** banen die AI-skills vragen groeiden 69% tegenover 9% voor de totale markt (8x sneller) · 62% loonpremie voor AI-skills, op van 57% · het diploma-filter valt weg (66% → 59% van AI-augmented banen vraagt een diploma; bij AI-geautomatiseerd werk 53% → 44%) · entry-level rollen met hoge AI-blootstelling groeiden 35% sinds 2019, terwijl andere entry-level rollen 10% daalden.
