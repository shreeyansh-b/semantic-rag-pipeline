#
# Document Ingestion Service
#     ↓
# Chunking + Embedding
#     ↓
# Vector DB (FAISS or pgvector)
#     ↓
# FastAPI Query Service
#     ↓
# LLM Answer Generation
#     ↓
# Logging + Evaluation Pipeline
#


from typing import List

from fastapi import Body, FastAPI

from app.api.services.chunks_store import get_chunks_store_service
from app.api.services.embedding import get_embedding_service
from app.api.services.vector_store import get_vector_store_service
from app.dependencies import set_chunks_store, set_vector_store
from app.api.routes.ingest import ingest_router
from app.api.routes.query import query_router


app = FastAPI()

vector_store = get_vector_store_service(384)

set_vector_store(vector_store)

chunks_store = get_chunks_store_service()

set_chunks_store(chunks_store)


embedding_service = get_embedding_service()

app.include_router(ingest_router)
app.include_router(query_router)
