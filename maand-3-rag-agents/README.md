# Maand 3: RAG en agents

**24 september – 21 oktober 2026**

**Doel:** één solide retrieval-systeem en één solide agent bouwen, begrijpen waarom elk
onderdeel er zit, en ze kunnen debuggen als ze breken. Dat is de lat.

Volledige uitwerking: [tabblad Roadmap in het dashboard](https://dvo-ai-automation.github.io/ai-engineer-4-months/) · [ROADMAP.md](../ROADMAP.md)

## Resources

- Embeddings: Stack Overflow "intuitive introduction to text embeddings" + OpenAI embeddings guide
- Chunking: LangChain `RecursiveCharacterTextSplitter` (size ~500, overlap ~50)
- Vector-DB: **Chroma**, lokaal · https://docs.trychroma.com
- Reranking: Cohere reranking-docs
- RAG-framework: **LlamaIndex**
- Agents: Anthropic **"Building Effective Agents"**, lezen vóór je één regel agent-code schrijft, daarna LangGraph
- Evals: **DeepEval** algemeen, **Ragas** voor RAG

## Gereedschap

[Prompt 3: Grounded RAG Answering](../prompts/03-grounded-rag-answering.md)

## Twee dingen om te onthouden

- **De meeste RAG-fouten zijn retrieval-fouten, geen modelfouten.** Kijk altijd eerst wat er opgehaald werd voordat je het model de schuld geeft.
- **Een agent is een while-loop met een model dat de vertakkingen kiest.** Eén call als het in één prompt past · een vaste workflow als de stappen voorspelbaar zijn · een agent alleen als het aantal stappen echt onvoorspelbaar is.

## Builds

- [ ] `projecten/mini-rag/`: 20 zinnen embedden, top-3 meest vergelijkbare teruggeven
- [ ] `projecten/chat-met-documenten/`: 10–20 PDF's ingesten, retrieval + reranking, geciteerde antwoorden, simpele interface (hoofdportfoliostuk)
- [ ] `projecten/agent-from-scratch/`: geen framework, drie tools, eigen loop. **Doe dit vóór LangGraph.**
- [ ] `projecten/evals/`: 20–30 representatieve inputs met verwachte outputs

## Milestone

- [ ] Uitleggen wat een embedding is en waarom vergelijkbare tekst vergelijkbare vectoren geeft
- [ ] Een document zinnig chunken
- [ ] Embeddings opslaan en queryen met metadata-filtering
- [ ] Reranking toevoegen
- [ ] Een retrieval-fout debuggen
- [ ] Complete RAG-pipeline met gegronde, geciteerde antwoorden
- [ ] Agent-loop from scratch
- [ ] Correct kiezen tussen call, workflow en agent
- [ ] Een basis-eval draaien
