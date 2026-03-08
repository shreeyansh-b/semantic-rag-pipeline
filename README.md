# semantic-rag-pipeline

A RAG (Retrieval-Augmented Generation) pipeline built from scratch no LangChain, no abstractions. Just raw pieces wired together manually.

## What it does

You upload a markdown file. It gets chunked by heading, embedded into vectors, and stored in FAISS. When you query, your question gets embedded the same way, FAISS finds the nearest chunks (cosine similarity under the hood), and Gemini answers the question using those chunks as context.

```
Upload .md file
    ↓
Chunk by heading
    ↓
Embed with all-MiniLM-L6-v2  →  384-dimensional vectors
    ↓
Store in FAISS (in-memory)  +  ChunksStore (flat list, indices stay in sync)
    ↓
Query comes in  →  embed query  →  FAISS nearest neighbour search
    ↓
Map indices back to chunk text
    ↓
Gemini 2.5 Flash answers using retrieved chunks as context
```

## Stack

- **FastAPI** — two routes: `/ingest` and `/query`
- **sentence-transformers** — `all-MiniLM-L6-v2` for embeddings (384 dimensions, fixed regardless of sentence length)
- **FAISS (faiss-cpu)** — vector similarity search, in-memory `IndexFlatL2`
- **Google Gemini** — `gemini-2.0-flash` for answer generation
- **Pydantic** — request validation

## Project structure

```
app/
  main.py                        # FastAPI app, shared singletons, load_dotenv
  dependencies.py                # shared state (vector store, chunks store, generation service)
  api/
    routes/
      ingest.py                  # POST /ingest — file upload, chunking, embedding
      query.py                   # POST /query — semantic search + LLM answer
    services/
      embedding.py               # SentenceTransformer wrapper
      ingestion_pipeline.py      # orchestrates chunking + embedding on ingest
      vector_store.py            # FAISS index wrapper (add, search)
      chunks_store.py            # flat list — keeps chunk text in sync with FAISS indices
      retrieval.py               # maps FAISS indices back to chunk text
      generation.py              # Gemini client wrapper
  models/
    request.py                   # IngestRequest, QueryRequest

ingestion/
  loader.py                      # reads .md file → list of lines
  chunking.py                    # splits by heading, skips code blocks
  ingestion.py                   # Ingestion class, wraps loader + chunker

data/
  access_control.md
  refund_policy.md
  incident_response.md
```

## Setup

```bash
# create and activate virtual env
python -m venv rag-env
rag-env\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_key_here
```

Get a key at https://ai.google.dev/gemini-api/docs/api-key (free tier is fine — 1500 requests/day).

## Running

```bash
uvicorn app.main:app --reload
```

## Usage

**Ingest a file:**

```bash
curl -X POST http://localhost:8000/ingest -F "file=@./data/access_control.md"
```

**Query:**

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query_txt": "Who has write access to production"}'
```

## A few things worth knowing

**Why FAISS indices and chunk text are stored separately** — FAISS only stores vectors, it has no idea what text those vectors came from. So `ChunksStore` keeps a flat list that stays in sync: the first chunk ingested is at index 0, second at index 1, and so on. Multiple files just extend the same list. When FAISS returns `[2, 5, 0]`, those are direct indices into `ChunksStore`.

**Why embeddings are 384 dimensions** — that's the output size of `all-MiniLM-L6-v2`. It doesn't matter how long your sentence is, the output is always 384 numbers. Two vectors must have the same dimensions to compute cosine similarity (you can't compare a 3D point to a 2D point — the math breaks).

**Why the vector store is a singleton** — FAISS is in-memory. If you created a new index on every request, the data from the previous ingest would be gone. The index lives in `main.py` and is shared across routes via `dependencies.py`.

**Chunking strategy** — splits on markdown headings (`#`, `##`, etc.) and accumulates lines under each heading into one chunk. Code blocks are tracked so headings inside \`\`\` fences don't trigger a new chunk.
