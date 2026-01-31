from .embed import Embedder
from .index import VectorIndex
from .reranker import Reranker


class Retriever:
    """
    Full retrieval pipeline:

    embed → FAISS → rerank
    """

    def __init__(self, schema_docs: list[str]):
        print("[Retriever] Initializing...")

        self.embedder = Embedder()

        # ---- STEP 1: embed all schema once ----
        embeddings = self.embedder.encode(schema_docs, prefix = "passage")

        # ---- STEP 2: build FAISS index once ----
        self.index = VectorIndex(embeddings.shape[1])
        self.index.add(embeddings, schema_docs)

        # ---- STEP 3: cross encoder reranker ----
        self.reranker = Reranker()

        print("[Retriever] Ready.")

    def retrieve(self, question: str, k: int = 10, final_k: int = 3):
        """
        question → top relevant schema docs

        k = candidates from FAISS (fast)
        final_k = results after reranking (accurate)
        """

        # ---- embed query ----
        query_vec = self.embedder.encode(question, prefix = 'query')

        # ---- fast similarity search ----
        candidates = self.index.search(query_vec, k)

        # ---- smart reranking ----
      # returns [(doc, score)]
        ranked = self.reranker.rerank(question, candidates, final_k)

        MIN_SCORE = 0.2

        filtered = [doc for doc, score in ranked if score >= MIN_SCORE]

        # fallback if everything filtered
        if filtered:
            return filtered
        else:
            return [ranked[0][0]]