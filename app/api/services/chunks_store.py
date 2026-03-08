class ChunksStoreService:

    def __init__(self):
        self._chunks: list[str] = []

    def add(self, chunks: list[str]):
        self._chunks.extend(chunks)

    def get(self, indices: list[int]) -> list[str]:

        # [self._chunks[idx]  for idx  in indices]
        #  ↑ what I want      ↑ each    ↑ from where

        # [self._chunks[idx] for idx in indices if idx < len(self._chunks)]
        #                                       ↑ optional filter

        # [what  for each  in where]
        # Added if check if FAISS returns index -1
        return [self._chunks[idx] for idx in indices if idx >= 0 and idx < len(self._chunks)]


def get_chunks_store_service() -> ChunksStoreService:
    return ChunksStoreService()
