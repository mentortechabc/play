"""
how to run
1) install flask (maybe using virtualenvs)
2) change directory accordingly
3) export FLASK_APP=flask_server.py
4) python -m flask run

You must see something like

     * Serving Flask app 'flask_server.py' (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

"""

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
