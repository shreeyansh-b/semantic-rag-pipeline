from app.api.services.chunks_store import ChunksStoreService
from app.api.services.vector_store import VectorStoreService


_vector_store: VectorStoreService = None


def set_vector_store(vs: VectorStoreService):
    global _vector_store  # pylint: disable=global-statement
    _vector_store = vs


def get_vs() -> VectorStoreService:
    return _vector_store


_chunks_store: ChunksStoreService = None


def set_chunks_store(cs: ChunksStoreService):
    global _chunks_store  # pylint: disable=global-statement
    _chunks_store = cs


def get_cs() -> ChunksStoreService:
    return _chunks_store
