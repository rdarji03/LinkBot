import chromadb
import uuid
from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


class StoreEmbeddings:
    def __init__(self, data_text: str, website_id: None):
        self.data_text = data_text
        self.website_id = website_id
        self.chroma_client = chromadb.PersistentClient(path="chroma")
        self.chroma_collection = self.chroma_client.get_or_create_collection(
            name="website_embedding", metadata={"hnsw:space": "cosine"}, embedding_function=None
        )

    def createEmbedding(self):
        sentence_embedding = model.encode(self.data_text)
        chroma_id = self.store_embedding_chroma(sentence_embedding)
        return chroma_id

    def store_embedding_chroma(self, chroma_db):
        generate_id = str(uuid.uuid4())
        self.chroma_collection.add(
            ids=[generate_id],
            embeddings=[chroma_db.tolist()],
            documents=[self.data_text],
            metadatas=[{"source": "crawler","website_id": str(self.website_id)}],
        )

        return generate_id
