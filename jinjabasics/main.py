from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")

@app.route("/<h>")
def hello(h):
    name = "bhi"
    letters = list(name)
    return render_template("basic.html",name = name,letters = letters )

if __name__ == "__main__":
    app.run(debug=True)