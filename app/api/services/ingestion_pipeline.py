from app.api.services.embedding import get_embedding_service
from app.dependencies import get_cs, get_vs
from ingestion.ingestion import get_ingestion_service


class IngestionPipeline:

    def __init__(self):
        self._ingestion_service = get_ingestion_service()
        self._embedding_service = get_embedding_service()

    def run(self, text: str):
        """Runs the ingestion pipeline"""
        chunks = self._ingestion_service.get_chunks_from_content(text)
        _, vectors = self._embedding_service.get_embedding(chunks)
        # dimensions = shape[1]

        vector_store = get_vs()

        vector_store.add(vectors)

        chunks_store = get_cs()

        chunks_store.add(chunks)

        return chunks


def get_ingestion_pipeline() -> IngestionPipeline:
    """Factory function for ingestion pipeline"""
    return IngestionPipeline()
