from Services.UserEmbedding import userEmbedding
from Services.searchEmbedding import searchEmbedding
from Services.modelQuerry import modelQuerry


class SearchQuerry:
    @staticmethod
    def SearchEmbedding(search_querry, w_id):
        user_embedding = SearchQuerry.UserQuerryEmbedding(search_querry)
        search_embedding = searchEmbedding(
            embedding=user_embedding,
            website_id=w_id,
            n_result=3
        )
        search_embedding_result = search_embedding.search_chroma()
        result_doc = search_embedding_result['documents']
        model_querry = modelQuerry(result_doc, search_querry)
        return model_querry.generate_answer()
    def UserQuerryEmbedding(u_querry):
        user_querry_embedding = userEmbedding(u_querry)
        u_querry_data = user_querry_embedding.createEmbedding()
        return u_querry_data
