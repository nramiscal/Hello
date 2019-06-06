from flask import Flask, render_template

app = Flask(__name__)

num = 1
colour = "yellow"
name = "Nina"

@app.route("/")
def index():
    return render_template("index.html", num=num, color=colour, name=name)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/<int:num>")
def number(num):
    return render_template("index.html", num=num, name=name, color=color)

@app.route("/<int:num>/<color>")
def color(num, color):
    return render_template("index.html", num=num, name=name, color=color)


if __name__ == "__main__":
    app.run(debug=True)
