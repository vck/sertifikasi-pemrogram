import os
from flask_sqlalchemy import SQLAlchemy
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

#from dbmodel import Dataset

@app.route("/")
def index_view():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_view():
    if request.method == "POST":
        pass
