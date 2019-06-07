from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "aksjdhkjashdkjashdkjw"


@app.route("/")
def index():
    # session['name'] = "Abby"
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    print(request.form)
    session['name'] = request.form['name']
    return redirect("/")

@app.route("/success")
def success():
    # print(session['name'])
    return render_template("success.html")

@app.route("/buy/<product_id>")
def buy(product_id):
    print(product_id)
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)
