# Maand 2 — Bouwen met LLM-API's

**27 augustus – 23 september 2026**

**Doel:** echte AI-features bouwen met model-API's. Dit is de kern van het vak — diepte hier
betaalt zich meer terug dan diepte waar dan ook in het traject.

Volledige uitwerking: [../ROADMAP.md](../ROADMAP.md#maand-2--bouwen-met-llm-apis-27-aug--23-sep)

## Resources

- Prompting: `anthropics/prompt-eng-interactive-tutorial` (GitHub), daarna de officiële prompt-docs van Anthropic en OpenAI
- Structured outputs: **Instructor** + Pydantic, met de officiële structured-output docs
- Tool calling: OpenAI function calling guide + Anthropic tool use docs, náást elkaar
- Streaming: officiële streaming-docs + Simon Willison's uitleg
- Retries: **Tenacity**
- Security: OWASP-guide over prompt injection

## Gereedschap

[Prompt 2 — Structured Data Extraction](../prompts/02-structured-data-extraction.md)

## Builds

- [ ] `projecten/prompt-vergelijking/` — één taak, vijf prompts, outputs naast elkaar
- [ ] `projecten/invoice-parser/` — rommelige tekst in, schoon gestructureerd object uit (portfoliostuk)
- [ ] `projecten/mini-assistent/` — drie tools: `get_weather`, `calculate`, `search_notes`
- [ ] `projecten/terminal-chatbot/` — multi-turn met history en reset-commando

## Milestone

- [ ] Prompts die betrouwbare output geven voor een gegeven taak
- [ ] Gestructureerde JSON uit een model met Pydantic en Instructor
- [ ] Tool calling waarmee een model jouw Python-functies draait
- [ ] Een antwoord realtime streamen
- [ ] Multi-turn gespreksgeschiedenis beheren
- [ ] Tokenkosten inschatten vóór verzending
- [ ] API-fouten en slechte output afhandelen zonder crash
- [ ] Uitleggen wat prompt injection is
