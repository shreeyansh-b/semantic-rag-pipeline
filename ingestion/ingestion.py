from ingestion.loader import IngestionLoader
from ingestion.chunking import IngestionChunking


class Ingestion:

    def __init__(self, file_path: str = None):
        self._file_path = file_path

    def get_chunks_from_file_path(self) -> list[str]:
        """Returns chunks of md file which is loaded from self._file_path"""
        file_loader = IngestionLoader()
        chunker = IngestionChunking()
        md_file = file_loader.read_md_file(self._file_path)

        chunks = chunker.chunk_md_file(md_file)

        return chunks

    def get_chunks_from_content(self, content: str) -> list[str]:
        """Returns chunks from raw markdown string content"""
        chunker = IngestionChunking()
        lines = content.splitlines(keepends=True)
        return chunker.chunk_md_file(lines)


def get_ingestion_service(file_path: str = None) -> Ingestion:
    return Ingestion(file_path)
