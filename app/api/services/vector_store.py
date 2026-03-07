import faiss
import numpy as np


class VectorStoreService:
    """Vector db store service"""

    def __init__(self, dimensions: int):
        self._index = faiss.IndexFlatL2(dimensions)

    def add(self, vectors: np.ndarray):
        """Add to vector store"""
        self._index.add(vectors)

    def search(self, query_vector: np.ndarray, k: int) -> tuple[np.ndarray, np.ndarray]:
        """Query upto nearest k neighbors in vector store"""
        return self._index.search(query_vector, k)

    @property
    def total(self):
        """Returns size of vector store"""
        return self._index.ntotal


def get_vector_store_service(dimensions: int = 384) -> VectorStoreService:
    """Factory method for vector store"""
    return VectorStoreService(dimensions)
