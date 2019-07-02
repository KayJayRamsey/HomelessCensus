import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///insurance.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Samples_Metadata = Base.classes.medical
Medical = Base.classes.medical

session = Session(engine)

@app.route("/")
def welcome():
    try:
        return render_template('index.html')
    except:
        return redirect("/plots", code=302)
        

@app.route("/plots")
def samples():

    stmt = session.query(Medical).statement
    df = pd.read_sql_query(stmt, session.bind)

    
    # Format the data to send as json
    age = df["age"].map(int)
    bmi = df["bmi"].map(int)
    charges = df["charges"].map(int)
    data = {"age": age.values.tolist(),"bmi": bmi.values.tolist(),"charges": charges.values.tolist()}
    
    return jsonify(data), redirect("/", code=302)


if __name__ == "__main__":
