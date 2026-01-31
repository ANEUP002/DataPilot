from rag.embed import Embedder

e = Embedder()

v1 = e.encode("hello world")
print(v1.shape)

v2 = e.encode(["hello", "world"])
print(v2.shape)
