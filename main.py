from flask import Flask, request
from Controller.websiteController import WebsiteController
from Controller.UserQuerryController import SearchQuerry
app = Flask(__name__)


@app.route('/')
def welcome():
    return "flask api has been created"


@app.route('/website', methods=['POST'])
def get_url():
    url = request.form.get('url')
    return WebsiteController.handel_url(url)


@app.route('/search', methods=['POST'])
def user_querry():
    website_id = request.form.get('website_id')
    search_querry = request.form.get('search_querry')
    return SearchQuerry.SearchEmbedding(search_querry, website_id)


if __name__ == "__main__":
    app.run(debug=True)
