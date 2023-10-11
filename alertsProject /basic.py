from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "JEY"

class Form(FlaskForm):
    name = StringField("Enter your name")
    submit = SubmitField("submit")

@app.route("/",methods = ["POST","GET"])
def home():
    form = Form()
    if form.validate_on_submit():
        flash("your name is "+form.name.data)
        return redirect(url_for("home"))
    return render_template("home.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)