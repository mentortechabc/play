from flask import Flask, render_template, request, g
import sqlite3
from FDataBase import FDataBase

DATABASE = 'main_db.sqlite'


app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["POST", "GET"])
def add_users_info():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        res = dbase.add_users_info(request.form['user_name'], request.form['user_email'],
                                   request.form['message'], request.form['start_interval'], request.form['end_interval'])
    return render_template('index.html', menu=dbase.get_slots())


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
