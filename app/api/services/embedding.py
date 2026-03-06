from typing import List
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """Service for generating text embeddings using sentence transformer."""

    DEFAULT_MODEL = "all-MiniLM-L6-v2"

    def __init__(self, model: str = DEFAULT_MODEL):
        self._model = SentenceTransformer(model)

    def get_embedding(self, sentences: List[str]):
        """Returns shape of embedded sentences"""
        if not sentences:
            raise ValueError("Sentences can not be empty.")

        embeddings = self._model.encode(sentences=sentences)
        # Embedding shape would return (no. of sentences, 384)
        # "384" is the number of neurons in final output of the model that is being used
        # And this will not changes if a longer sentence is passed
        # It's based on the model training. Using a different model might produce a higher/lower neuron count.

        # For a Vector Database to compare two things,
        # they must have the same number of dimensions.
        # You can't compare a 3D point (x,y,z) to a 2D point (x,y)—the math (Cosine Similarity) would break.

        print(embeddings.shape)

        # tolist() converts NumPy object to Python list
        # This can be returned as JSON if required
        print(embeddings.tolist())

        similarities = self._model.similarity(embeddings, embeddings)

        # returns
        # tensor([[1.0000, 0.5249],
        # [0.5249, 1.0000]])

        # Diagonal is always 1.0 because a sentence is always identical to itself.
        # Values range from -1.0 (opposite) to 1.0 (identical), this is Cosine Similarity.
        # 0.5249 means the two sentences share some meaning but are not the same.
        # Saying "52% similar" is fine for intuition
        # but technically it's a score of 0.5249 out of 1.0.
        print(similarities)

        return embeddings.shape, embeddings


def get_embedding_service() -> EmbeddingService:
    """Factory function to return Embedding service"""
    return EmbeddingService()
