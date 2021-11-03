from flask import Flask, make_response
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    return make_response({"asd": "123", "status": "ok", "time": time.time()}, 200)
