import numpy as np

from app.api.services.vector_store import VectorStoreService


class RetrievalService:
    """Used to retrieve from vector store"""

    def __init__(self, vector_store: VectorStoreService):
        self._vector_store = vector_store

    def retrieve(self, query_vector: np.ndarray, k: int = 4) -> list[str]:
        """Retrieve from vector store"""
        distance, indices = self._vector_store.search(query_vector, k)

        return distance.tolist(), indices.tolist()


def get_retrieval_service(vector_store: VectorStoreService) -> RetrievalService:
    """Factory function for retrieval service"""
    return RetrievalService(vector_store)
