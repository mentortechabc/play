from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Main Page</h1>"


@app.route("/login")
def login():
    print("request:", request)
    print("request.cookies:", request.cookies)
    log = "no"
    if request.cookies.get('logged'):
        log = request.cookies.get('logged')

    res = make_response(f"<h1>Authorized </h1> logged: {log}")
    res.set_cookie("logged", "yes")
    return res


if __name__ == "__main__":
    app.run(debug=False)
