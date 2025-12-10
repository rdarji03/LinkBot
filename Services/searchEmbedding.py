import chromadb


chroma_client = chromadb.PersistentClient(path='chroma')
embedding_collebtion = chroma_client.get_collection('website_embedding')


class searchEmbedding:
    def __init__(self, embedding, website_id, n_result):
        self.embedding = embedding
        self.website_id = website_id
        self.n_result = n_result

    def search_chroma(self):
        search_result = embedding_collebtion.query(
            query_embeddings=[self.embedding],
            n_results=self.n_result,
            where={"website_id": str(self.website_id)}
        )
        return search_result
