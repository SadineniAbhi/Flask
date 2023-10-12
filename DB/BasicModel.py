import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def __repr__(self):
        print("the student name is {} and age is {}".format(self.name,self.age))