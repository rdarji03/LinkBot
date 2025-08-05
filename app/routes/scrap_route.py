from fastapi import APIRouter
from app.schemas.website_schemas import Website
from app.services.scrapper_service import main

router = APIRouter(prefix="/api")


@router.post('/website')
async def get_website(website: Website):
    data = await main(website.url)
    return data
