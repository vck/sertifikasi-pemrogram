import os
from flask_sqlalchemy import SQLAlchemy
import random 
from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    flash, 
    g,
    send_from_directory,
    jsonify)

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///kredito.db"
app.config["UPLOAD_FOLDER"] = "static"
app.secret_key = "managaassQW"

db = SQLAlchemy(app)

from random import shuffle

class Dataset(db.Model):
    __tablename__ = 'datasets'

    id = db.Column(db.Integer, primary_key=True)
    param_a = db.Column(db.Integer)
    param_b = db.Column(db.Integer)
    param_c = db.Column(db.Integer)
    param_d = db.Column(db.Integer)
    param_e = db.Column(db.Integer)
    

    def __init__(self, param_a, param_b, param_c, param_d, param_e):
        self.param_a = param_a
        self.param_b = param_b
        self.param_c = param_c
        self.param_d = param_d
        self.param_e = param_e

    def __repr__(self):
        return '<id {}>'.format(self.id)

@app.route("/")
def index_view():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_view():
    if request.method == "POST":
        param_a = request.form["a1"]
        param_b = request.form["a2"]
        param_c = request.form["a3"]
        param_d = request.form["a4"]
        param_e = request.form["a5"]
        d = Dataset(param_a=param_a, 
                    param_b=param_b,
                    param_c=param_c,
                    param_d=param_d,
                    param_e=param_e)
        db.session.add(d)
        db.session.commit()
        return render_template("index.html", data=random.choice([0, 1]))