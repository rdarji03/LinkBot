from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['LinkBot']
website_url_collection = db['crawled_website']
crawled_link = db['crawled_link']
crawled_link_data = db['crawled_link_data']


class storeCrawledData:
    def __init__(self, urls_list=None, website_url=None, website_id=None, website_page=None, chunk_data=None, url_id=None,chroma_id=None):
        self.urls = urls_list
        self.website_url = website_url
        self.website_id = website_id
        self.website_page = website_page
        self.chunk_data = chunk_data
        self.url_id = url_id
        self.chroma_id = chroma_id

    def is_url_exist(self):
        existing = website_url_collection.find_one({"url": self.website_url})
        return existing is not None

    def add_website_url(self):
        result = website_url_collection.insert_one({
            "url": self.website_url
        })

        return result.inserted_id

    def store_crawl_links(self):
        try:
            result = crawled_link.insert_one({
                "website_id": self.website_id,
                "crawled_url": self.website_url
            })
            return result.inserted_id
        except Exception as e:
            print(f"Error inserting crawled link data: {e}")
            return None

    def add_website_link_data(self):
        try:
            crawled_link_data.insert_one({
                "website_id": self.website_id,
                "url_id": self.url_id,
                "url_content": self.chunk_data,
                "embedding_index": self.chroma_id
            })

        except Exception as e:
            print(f"Error inserting crawled link data: {e}")
            return None
