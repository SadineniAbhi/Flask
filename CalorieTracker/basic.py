import os
from flask import Flask,url_for,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))


# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#reads and updates the changes in the database design
Migrate(app,db)

class FoodItems(db.Model):
    item = db.Column(db.Text,primary_key = True)
    calories = db.Column(db.Integer)
    protein = db.Column(db.Integer)
    def __init__(self,item,calories,protein):
        self.item = item
        self.calories = calories
        self.protein = protein

    def __repr__(self):
        return "item {} has {} calories per gram".format(self.calories,self.item)

class EatenFood(db.Model):
    item = db.Column(db.Text)
    weight = db.column(db.Text)

    def __init__(self,item,weight):
        self.item = item
        self.weight = weight

    def __repr__(self):
        return "today i ate {} grams of {}".format(self.weight,self.item)


