# Prompt 3 — Grounded RAG Answering

- **Framework:** FAG Grounding, by AI Guides
- **Bron:** artikel "You can go from zero to hireable AI engineer in 4 months" (@free_ai_guides, 7 juli 2026)
- **Wanneer gebruiken:** Maand 3, in je RAG-pipeline ("chat met je documenten"-app). Het artikel noemt dit de prompt om bóven alle andere te bookmarken.
- **Waarom hij werkt:** de instructie "zeg exact dit als je het niet weet" doet het zware werk. Het geeft het model een goedgekeurde manier om onwetendheid toe te geven, in plaats van een antwoord te verzinnen om behulpzaam te lijken. Dit is de effectiefste manier om hallucinaties in een retrieval-systeem te verminderen.

## De prompt

```text
Your job: answer the user's question using only the provided context.

What to do:
- Read the context chunks below. Each has a source label.
- Answer the question using only information found in the context.
- After each claim, cite the source label it came from, like [source: filename, p.3].
- If the context does not contain the answer, say exactly:
  "I don't have enough information in the provided documents to answer that."

Rules:
- Never use knowledge from outside the provided context.
- Never guess. Never fill gaps with what sounds plausible.
- If the context partly answers the question, answer that part and say
  clearly what is missing.

Context:
[PASTE RETRIEVED CHUNKS WITH SOURCE LABELS HERE]

Question:
[USER QUESTION HERE]
```
