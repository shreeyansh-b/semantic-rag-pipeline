from app.api.services.vector_store import VectorStoreService


_vector_store: VectorStoreService = None


def set_vector_store(vs: VectorStoreService):
    global _vector_store  # pylint: disable=global-statement
    _vector_store = vs


def get_vs() -> VectorStoreService:
    return _vector_store
