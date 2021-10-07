from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    return make_response({"asd": "123", "status": "ok"}, 200)
