import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)

engine = create_engine("sqlite:///db/insurance.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Medical = Base.classes.medical

# Create our session (link) from Python to the DB
session = Session(engine)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/plots")
def sample(plots):

   sel = [
        Medical.age,
        Medical.sex,
        Medical.bmi,
        Medical.children,
        Medical.smoker,
        Medical.region,
        Medical.charges,
    ]

    results = db.session.query(*sel).filter(Medical).all()
 
    # Create a dictionary entry for each row of metadata information
    data = {}
    for result in results:
        Medical["age"] = result[0]
        Medical["sex"] = result[1]
        Medical["bmi"] = result[2]
        Medical["children"] = result[3]
        Medical["smoker"] = result[4]
        Medical["region"] = result[5]
        Medical["charges"] = result[6]

    print(data)
    return jsonify(data)

@app.route("/")
def index():
    """Return the homepage."""

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
