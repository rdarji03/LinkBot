from flask import request, jsonify
from Services.websiteCrawler import websiteCrawller
from Services.storeCrawledData import storeCrawledData


import validators
import requests


class WebsiteController:
    @staticmethod
    def handel_url(url):
        if not url:
            return jsonify({
                "status": False,
                "message": "Enter url"
            })

        if not validators.url(url):
            return jsonify({
                "status": False,
                "message": "Enter valid url"
            })

        try:
            response = requests.get(url)
            if response.status_code == 200:

                store_website_data = storeCrawledData(website_url=url)
                is_website_exist = store_website_data.is_url_exist()

                if is_website_exist:
                    return jsonify({
                        "status": True,
                        "message": 'Website Already PResent'
                    })

                website_id = store_website_data.add_website_url()
                crawler = websiteCrawller(url, website_id)
                data = crawler.crawlLink()
                return jsonify({
                    "status": True,
                    "message": 'Website is crawled'
                })
            else:
                return jsonify({
                    "status": True,
                    "message": "URL is not reachable"
                })

        except requests.exceptions.RequestException as e:
            return jsonify({
                'status': False,
                "message": f"Error occurred while accessing the URL: {str(e)}"
            })
