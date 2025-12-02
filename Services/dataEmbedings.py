from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


class StoreEmbeddings:
    def __init__(self, data_text: str):
        self.data_text = data_text

    def createEmbedding(self):
        sentence_embedding = model.encode(self.data_text)
        return np.array(sentence_embedding, dtype="float32")
