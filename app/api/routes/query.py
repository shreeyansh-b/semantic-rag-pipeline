from fastapi import APIRouter, File, HTTPException, UploadFile, Body

from app.api.services.embedding import get_embedding_service
from app.api.services.retrieval import get_retrieval_service
from app.dependencies import get_cs, get_vs
from app.models.request import QueryRequest

query_router = APIRouter()


@query_router.post("/query")
def query(payload: QueryRequest):
    """Query for a string from vector store"""
    vector_store = get_vs()
    retrieval_service = get_retrieval_service(vector_store)
    embedding_service = get_embedding_service()
    _, query_vector = embedding_service.get_embedding([payload.query_txt])

    distances, indices = retrieval_service.retrieve(query_vector)

    chunks_store = get_cs()

    chunks = chunks_store.get(indices[0])

    return {"status": "ok", "distances": distances, "indices": indices, "chunks": chunks}
