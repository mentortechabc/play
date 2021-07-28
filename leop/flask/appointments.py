from flask import Flask
from flask import render_template
from db import query_db

app = Flask(__name__)


@app.route("/")
def bookings_handler():
    bookings = query_db()
    return render_template('appointments.html', name="Maria", bookings=bookings)


if __name__ == "__main__":
    app.run(debug=True)
