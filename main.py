from flask import Flask, request
from Controller.websiteController import WebsiteController

app = Flask(__name__)


@app.route('/')
def welcome():
    return "flask api has been created"


@app.route('/website', methods=['POST'])
def get_url():
    url = request.form.get('url')
    return WebsiteController.handel_url(url)


if __name__ == "__main__":
    app.run(debug=True)
