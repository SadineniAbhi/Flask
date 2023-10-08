from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template("thankyou.html",first= first, last = last)

if __name__ == "__main__":
    app.run(debug=True)