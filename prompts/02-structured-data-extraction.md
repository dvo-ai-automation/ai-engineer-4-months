# Prompt 2: Structured Data Extraction

- **Framework:** FAG Extractor, by AI Guides
- **Bron:** artikel "You can go from zero to hireable AI engineer in 4 months" (@free_ai_guides, 7 juli 2026)
- **Wanneer gebruiken:** Maand 2, bij het onderdeel *structured outputs*. Dit patroon werkt al vóórdat je Pydantic/Instructor erbovenop zet; gebruik het bij de bon/invoice-parser.
- **Bekende faalmodus (uit het artikel):** het model wikkelt de JSON soms in markdown code fences of zet er een vriendelijke zin voor, waardoor je parser stukloopt. Fix: strip de code fences vóór het parsen, én wees expliciet dat je alleen het JSON-object wilt (dit patroon doet dat al).

## De prompt

```text
Your job: extract structured data from the text I provide and return it
as clean JSON.

What to do:
- Read the input text carefully.
- Pull out only the fields listed under Output below.
- If a field is missing from the text, use null. Do not guess or invent.
- Return only the JSON object. No explanation, no markdown, no preamble.

Rules:
- Every value must be traceable to something in the input text.
- Dates in YYYY-MM-DD format. Numbers as numbers, not strings.
- If the text is ambiguous, prefer null over a confident wrong answer.

Output: a JSON object with these fields:
{
  "field_one": string or null,
  "field_two": number or null,
  "field_three": list of strings or empty list
}

Input text:
[PASTE THE TEXT HERE]
```
