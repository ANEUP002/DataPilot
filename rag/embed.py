from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-base-en-v1.5")

    def encode(self, texts, prefix=None):
        if isinstance(texts, str):
            texts = [texts]
        if prefix:
            texts = [f"{prefix}: {t}" for t in texts]
        emb = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False
        )

        return np.asarray(emb, dtype="float32")
