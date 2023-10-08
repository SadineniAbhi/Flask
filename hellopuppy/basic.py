from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello Puppy!!</h1>"

@app.route("/information")
def info():
    return "<h1>puppies are cute</h1>"

@app.route("/hello/<name>")
def droute(name):
    return "<h1>Hello {}!!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)