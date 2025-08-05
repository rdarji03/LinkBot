from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


load_dotenv()

db_url = os.getenv('db_url')
db_client = AsyncIOMotorClient(db_url)
db = db_client['ScrappyBot']
