from rag.embed import Embedder
from rag.index import VectorIndex

# fake schema docs
docs = [
    "Table calls has columns agent_name and talk_time",
    "Table agents has columns team and supervisor",
    "Table sales has revenue and date"
]

print("Loading embedder...")
embedder = Embedder()

print("Encoding docs...")
embeddings = embedder.encode(docs)

print("Building FAISS index...")
index = VectorIndex(embeddings.shape[1])
index.add(embeddings, docs)

print("Encoding query...")
query_vec = embedder.encode("average talk time per agent")

print("Searching...")
results = index.search(query_vec, k=2)

print("\nTop matches:")
for r in results:
    print("-", r)
