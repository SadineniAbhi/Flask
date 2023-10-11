from flask import Flask, render_template, request,session,redirect,url_for
from wtforms import SubmitField,DateTimeField,StringField,RadioField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

class Form(FlaskForm):
    name = StringField("enter your name",validators=[DataRequired()])
    choise = RadioField("chooose your feild",choices=[('ML','ML'),("webdev","webdev")])
    submit = SubmitField("submit")


@app.route("/",methods=['GET','POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        session["name"] = form.name.data
        session["choise"] =form.choise.data
        return redirect(url_for("thankyou"))

    return render_template("home.html",form = form)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)