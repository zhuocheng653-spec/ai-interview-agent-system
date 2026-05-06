import numpy as np
from rag.embedder import get_embedding

class VectorStore:
    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text):
        embedding = get_embedding(text)
        self.texts.append(text)
        self.vectors.append(embedding)

    def search(self, query, top_k=2):
        query_vec = get_embedding(query)

        scores = []
        for vec in self.vectors:
            score = np.dot(query_vec, vec)
            scores.append(score)

        top_indices = np.argsort(scores)[-top_k:]
        return [self.texts[i] for i in top_indices]
