from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h2>Welcome to my web app</h2>'
