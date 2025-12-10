
from chromadb import PersistentClient

PERSIST_DIRECTORY = "./chroma"
COLLECTION_NAME = "website_embedding"
TARGET_ID = "607eb3f8-e3db-4cb4-9ac9-91eb0618e43f"   # replace this with the ID you want

client = PersistentClient(path=PERSIST_DIRECTORY)

collection = client.get_collection(
    name=COLLECTION_NAME,
)
# client.delete_collection(COLLECTION_NAME)

result = collection.get(
    ids=[TARGET_ID],
    include=["embeddings", "documents", "metadatas"]
)

print(result)
