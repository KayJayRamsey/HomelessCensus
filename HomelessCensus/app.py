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

 
