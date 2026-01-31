import faiss
import numpy as np


class VectorIndex:
    """
    Simple FAISS wrapper for similarity search.

    Responsibilities:
    - store embeddings
    - search nearest neighbors
    - return matching texts
    """

    def __init__(self, dim: int):
        # We use Inner Product (dot product)
        # because embeddings are normalized (cosine similarity)
        self.index = faiss.IndexFlatIP(dim)

        # store original texts alongside vectors
        self.texts = []

    def add(self, embeddings: np.ndarray, texts: list[str]):
        """
        Add embeddings + corresponding texts to index

        embeddings: (N, dim)
        texts: list[str]
        """

        self.index.add(embeddings.astype("float32"))
        self.texts.extend(texts)

    def search(self, query_embedding: np.ndarray, k: int = 3):
        """
        Search top-k similar texts

        query_embedding: (1, dim)
        returns: list[str]
        """

        scores, indices = self.index.search(query_embedding.astype("float32"), k)

        results = [self.texts[i] for i in indices[0]]
        return results
