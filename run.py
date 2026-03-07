from app.api.services.embedding import get_embedding_service
from ingestion.ingestion import get_ingestion_service
import faiss


ingestion_service = get_ingestion_service("./data/access_control.md")
chunks = ingestion_service.get_chunks_from_file_path()

embedding_service = get_embedding_service()


embeddings = embedding_service.get_embedding(chunks)

dimensions = embeddings[0][1]
vectors = embeddings[1]

index = faiss.IndexFlatL2(dimensions)

index.add(vectors)


print("Total vectors in index:", index.ntotal)

query = embedding_service.get_embedding(
    ["Production access is restricted to authorized engineering personnel to maintain system security."])

k = 4
distances, indices = index.search(query[1], k)
print("Nearest indices:", indices)
print("Distances:", distances)
