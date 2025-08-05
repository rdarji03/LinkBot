import requests
from app.services.website_store import store_website


def validate_url(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {
                "status": True,
                "message": "Valid URL",
            }
        else:
            return {"status": False, "message": "Invalid URL"}
    except requests.RequestException as e:
        return {"status": False, "message": str(e)}


async def main(url):
    try:
        is_valid_url = validate_url(url)
        if is_valid_url['status']:
            add_website = await store_website(url)
            if add_website:
                return {"status": True, "message": add_website['message'], "data": add_website['data']}
        else:
            return {
                "status": False,
                "message": is_valid_url.get("message", "URL not valid"),
                "data": []
            }

    except Exception as e:
        return {'stauts': False, "message": str(e)}
