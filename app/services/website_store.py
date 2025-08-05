from app.database import db
from uuid import uuid4
from app.models.website_model import WebsiteCreate

website_collection = db['crawl_website']


async def store_website(url):
    crawl_id = uuid4()
    url = str(url)  

    existed_website = await website_collection.find_one({'website_name': url})

    if existed_website:
        return {
            "status": True,
            "message": "Website already present",
            "data": {
                "website": existed_website["website_name"],
                "id": str(existed_website["crawl_id"])
            }
        }

    data = WebsiteCreate(
        website_name=url,
        crawl_id=str(crawl_id)
    )

    response = await website_collection.insert_one(data.dict())

    return {
        "status": True,
        "message": "Website Added Successfully",
        "data": {
            "website": url,
            "id": str(crawl_id)
        }
    }
