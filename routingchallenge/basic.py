from flask import Flask 

app = Flask("__main__")

@app.route("/<name>")
def droutchallenge(name):
    if name[-1] != 'y':
        name = name + 'y'
    else:
        name = name[0:-1] + "iful"
    return "<h1>{}</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)
