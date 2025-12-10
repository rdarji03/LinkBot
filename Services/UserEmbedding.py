from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


class userEmbedding:
    def __init__(self, user_querry:str):
        self.user_querry = user_querry

    def createEmbedding(self):
        user_embedding = model.encode(self.user_querry)
        return user_embedding
