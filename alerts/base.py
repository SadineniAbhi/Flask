from flask import Flask, render_template, redirect ,url_for, session,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"


class Form(FlaskForm):
    submit = SubmitField("click me.")

@app.route("/",methods = ["GET","POST"])
def home():
    form = Form()

    if form.validate_on_submit():
        flash("you just clicked")
        return redirect(url_for("home"))
    return render_template("home.html",form = form)

if __name__ == "__main__":
    app.run(debug=True)