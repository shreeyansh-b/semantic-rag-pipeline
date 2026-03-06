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

from app.api.services.embedding import get_embedding_service
from app.models.request import IngestRequest

app = FastAPI()

embedding_service = get_embedding_service()


@app.post("/ingest")
def ingestion(payload: IngestRequest):
    return embedding_service.get_embedding(payload.sentences)
