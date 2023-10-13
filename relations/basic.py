import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#reads and updates the changes in the database design
Migrate(app,db)

class Puppy(db.Model):
    __tablename__ = "puppy"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    #one to many
    #puppy to many toys
    toys = db.relationship("Toy",backref="puppy",lazy ="dynamic")

    #one to one
    #one puppy --one owner
    owner = db.relationship("Owner",backref = "puppy", uselist = False)
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return "my name is {} and owner is {}".format(self.name,self.owner.name)
        else:
            return f"Puppy name is {self.name} and has no owner"

    def report_toys(self):
        print("here are my toys")
        for toy in self.toys:
            print(toy.item_name)
class Toy(db.Model):

    __tablename__ = "toyd"
    id = db.Column(db.text)
    item_name = db.Column(db.text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id

class Owner(db.Model):
    __tablename__ = "Owner"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer,db.ForeignKey("puppies.id"))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id






































