import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/insurance.csv"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Medical_cost = Base.classes.insurance2


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Medical_cost).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        Medical_cost.age,
        Medical_cost.sex,
        Medical_cost.bmi,
        Medical_cost.children,
        Medical_cost.smoker,
        Medical_cost.region,
        Medical_cost.charges,
    ]

    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()
 
    # Create a dictionary entry for each row of metadata information
    sample_metadata = {}
    for result in results:
        Medical_cost["age"] = result[0]
        Medical_cost["sex"] = result[1]
        Medical_cost["bmi"] = result[2]
        Medical_cost["children"] = result[3]
        Medical_cost["smoker"] = result[4]
        Medical_cost["region"] = result[5]
        Medical_cost["charges"] = result[6]

    print(sample_metadata)
    return jsonify(sample_metadata)


@app.route("/samples/<sample>")
def samples(sample):
    """Return `variable`, `group`,and `value`."""
    stmt = db.session.query(Medical_cost).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["group", "variable", sample]]
    # Format the data to send as json
    data = {
        "variable": sample_data.otu_id.values.tolist(),
        "value": sample_data[sample].values.tolist(),
        "group": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
