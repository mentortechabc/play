from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/json')
def json():
    return {"value": 123}


@app.route('/page')
def html():
    with open("./page.html", "r") as f:
        return f.read()
