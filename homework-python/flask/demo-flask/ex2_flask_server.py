from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return "index"


@app.route("/about")
def about():
    return "<h1>О сайте</h1>"


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/about2")
def about2():
    return render_template('about2.html')


@app.route("/index2")
def index2():
    return render_template('index2.html', title="О сайте", menu=menu, link=url_for('about2'))


if __name__ == "__main__":
    app.run(debug=True)
