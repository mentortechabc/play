import sqlite3
from pathlib import Path

from flask import g, Flask, request, make_response

app = Flask(__name__)

DATABASE = Path(__file__).parent.joinpath("local.sqlite")


def get_db():
    print("getting db connection")
    db = getattr(g, '_database', None)
    if db is None:
        print("creating a new connection")

        db = g._database = sqlite3.connect(DATABASE)
    print("returning db connection")
    return db


@app.teardown_appcontext
def close_connection(exception):
    print("close_connection")
    db = getattr(g, '_database', None)
    if db is not None:
        print("closing existing connection")
        db.close()
    print("close_connection end")


@app.route("/")
def index():
    print("route /")
    cur = get_db().cursor()
    print("cur", cur)
    return "<h1>Main Page</h1>"


@app.route("/login")
def login():
    print("route /login")
    cur = get_db().cursor()
    print("cur", cur)
    print("request:", request)
    print("request.cookies:", request.cookies)
    log = "no"
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Authorized </h1> logged: {log}")
    res.set_cookie("logged", "yes")
    return res


if __name__ == "__main__":
    app.run(debug=True, port=8000)
