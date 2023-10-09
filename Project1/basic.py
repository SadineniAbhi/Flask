from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/thankyou.html")
def thankyou():
    username = request.args.get("username")

    status = 'passed'

    if username[-1].isdigit() == False:
        status = 'failed' 
    def CapCheck(name):
        for char in name:
            if char.isupper():
                return True
        return False
    
    def LowerCheck(name):
        for char in name:
            if char.islower():
                return True
        return False

    if CapCheck(username) == False:
        status = False
    if LowerCheck(username) == False:
        status = False

    return render_template("thankyou.html",status=status)

if __name__ == "__main__":
    app.run(debug = True)

