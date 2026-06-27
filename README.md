# IST 488/688 Final Project — Notebooks & Test Suite

Self-contained Colab notebooks for each pipeline stage, plus shared test fixtures and a master test runner.

## Files

| File | Owner | Purpose |
|---|---|---|
| `restaurant_scraper.ipynb` | Ryan | Web scraping + fetching layer |
| `discovery_agent_LAUREN.ipynb` | Lauren | Google Places API integration |
| `agents_LEYTISHA.ipynb` | Leytisha | OpenAI enrichment + structuring + query + **ethics** + **self-reflection** |
| `chromadb_store_TOBY.ipynb` | Toby | ChromaDB storage + reranked retrieval |
| `test_fixtures.json` | shared | Realistic test data at every pipeline stage |
| `test_suite.ipynb` | shared | Master test runner — exercises functions across all four notebooks |
| `README.md` | — | This file |

## Run order (production pipeline)

1. `discovery_agent_LAUREN.ipynb` → produces `restaurants_raw.json`
2. `agents_LEYTISHA.ipynb` (enrichment) → produces `restaurants_enriched.json`
3. `chromadb_store_TOBY.ipynb` → loads enriched records into Chroma
4. `agents_LEYTISHA.ipynb` (query + ethics + reflection) → calls `chroma_search` for final answers

## Instructor requirement coverage

| Req | Implementation | Where | Owner |
|---|---|---|---|
| 1a. Short-term memory | `conversation_history` list passed across turns | `agents_LEYTISHA.ipynb` §6 | Leytisha |
| 1b. Long-term memory | ChromaDB persistent store (`./chroma_store`) survives kernel restart | `chromadb_store_TOBY.ipynb` §2 | Toby |
| 2. RAG + reranking | Vector search + `_rerank()` (rating boost + city match) | `chromadb_store_TOBY.ipynb` §6 | Toby |
| 3. Tool/function to LLM | `RESTAURANT_SCRAPE_TOOL` defined by Ryan, called by Leytisha's enrichment agent | `restaurant_scraper.ipynb` §9; `agents_LEYTISHA.ipynb` §4 | Ryan + Leytisha |
| 4. Ethics rubric evaluation | `evaluate_ethics()` — LLM-as-judge across 5 dimensions (geographic fairness, price diversity, cuisine respect, transparency, faithfulness) | `agents_LEYTISHA.ipynb` §7 | Leytisha |
| 5. Method from student topic presentations | **Self-Refine** (generate → critique → revise) — `query_with_reflection()` | `agents_LEYTISHA.ipynb` §8 | Leytisha |

> **⚠️ Verify req 5 with the group.** Self-Refine is a common topic in human-centered AI courses but I don't know which methods were specifically presented in your section. If a different method was covered (HyDE, ReAct, multi-agent debate, chain-of-thought, etc.), swap §8 in Leytisha's notebook for that — the surrounding plumbing stays the same.

## Test fixtures (`test_fixtures.json`)

One JSON file with realistic test data at every stage of the pipeline. Anyone on the team can load it and verify their function works without needing API keys or upstream notebooks.

| Key | What it is | Who uses it |
|---|---|---|
| `raw_places_api_responses` | Real-shape responses from Places API (New) | Lauren — test `normalize_place` |
| `normalized_restaurants` | 8 normalized restaurant records | Ryan, Leytisha — input shape after Lauren |
| `enriched_restaurants` | 9 fully-enriched records (incl. one with `scrape_failed=True` edge case) | Toby, Leytisha — for ChromaDB ingest + query tests |
| `sample_html_pages` | 4 sample HTML pages (simple menu, menu links + PDF, Cloudflare block, empty) | Ryan — test extraction without network |
| `test_queries` | 6 queries with expected behavior assertions | Leytisha, Toby — test retrieval + query agent |
| `test_conversation` | 3-turn conversation for short-term memory testing | Leytisha — verify memory works |
| `mock_openai_responses` | Canned tool-call request + final response | Leytisha — test tool-call loop without API spend |
| `ethics_test_cases` | 3 scored cases (good response, biased response, hallucination) | Leytisha — verify ethics rubric scores correctly |

**Loading in any notebook:**
```python
import json
F = json.load(open("test_fixtures.json"))
# Then: F["normalized_restaurants"], F["test_queries"], etc.
```

## Test suite (`test_suite.ipynb`)

Master test runner. Inlines key functions from all four notebooks and tests them against `test_fixtures.json`. Run it to verify the whole pipeline works end-to-end.

**Sections:**
- §3 Lauren — `normalize_place` schema validation
- §4 Ryan — HTML extraction + menu link discovery + cache
- §5 Leytisha — structuring + retrieval + (optional) ethics + reflection
- §6 Toby — embedding + load + reranked search (uses local sentence-transformers, no OpenAI)
- §7 Full pipeline integration (requires OpenAI key)
- §8 Pass/fail summary

**Tests verified to pass offline (14/14):** schema validation, HTML extraction, menu-link discovery, retrieval ranking, structuring defaults. ChromaDB tests run when you install chromadb. OpenAI tests skip cleanly when no key is set.

## Setup checklist for any notebook

```python
# In Colab
from google.colab import userdata
import os
os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")           # for Leytisha + integration
os.environ["GOOGLE_PLACES_API_KEY"] = userdata.get("GOOGLE_PLACES_API_KEY")  # for Lauren
```

Then drag `test_fixtures.json` into the file panel (or `!wget` it from wherever you're sharing files).

## A note on the backup notebooks

These exist so the pipeline isn't blocked if anyone's piece slips. Don't share them preemptively — let people own their pieces and offer them only if someone's actually stuck. The test suite and fixtures, on the other hand, are useful to share with the whole group up front: anyone can run them to verify their own work without depending on the other notebooks being done.
