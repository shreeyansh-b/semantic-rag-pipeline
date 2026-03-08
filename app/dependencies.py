from app.api.services.chunks_store import ChunksStoreService
from app.api.services.generation import GenerationService
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


_generation_service: GenerationService = None


def set_generation_service(gs: GenerationService):
    global _generation_service  # pylint: disable=global-statement
    _generation_service = gs


def get_gs() -> GenerationService:
    return _generation_service
