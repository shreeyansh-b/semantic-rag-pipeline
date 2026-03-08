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
        return [self._chunks[idx] for idx in indices]


def get_chunks_store_service() -> ChunksStoreService:
    return ChunksStoreService()
