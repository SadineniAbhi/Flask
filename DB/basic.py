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


class Parents(db.Model):
    p_id = db.Column(db.Integer, primary_key = True)
    p_name = db.Column(db.Text)

    #one parent to many children
    children = db.relationship("Children",lazy="dynamic", backref = "parents")

    def __init__(self,p_name):
        self.p_name = p_name

    def __repr__(self):
        if self.children.count()>0:
            children_names = [child.c_name for child in self.children]
            return "parent name is {} and children are {}".format(self.p_name,children_names)
        else:
            return "parent name is {} ".format(self.p_name)


class Children(db.Model):

    c_name = db.Column(db.Text)
    c_id = db.Column(db.Integer,primary_key = True)
    p_id = db.Column(db.Integer,db.ForeignKey("parents.p_id"))

    def __init__(self,c_name,p_id):
        self.c_name = c_name
        self.p_id = p_id

    def __repr__(self):
        return "HI i am an child and my name is {} and my parent is {}".format(self.c_name,self.p_id)


class Sibling(db.Model):
    s_id = db.Column(db.Integer,primary_key = True)
    s_name = db.Column(db.Text)

    c_id = db.Column(db.Integer,db.ForeignKey("children.c_id"))

    def __init__(self,s_name,c_id):
        self.s_name = s_name
        self.c_id = c_id
