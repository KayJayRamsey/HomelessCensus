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

 Plotly.d3.csv('3dbardata.csv', function (rows) {
            function unpack(rows, key) {
                return rows.map(function (row) { return row[key]; });
            }

            var trace1 = {
                x: unpack(rows, 'age'), y: unpack(rows, 'bmi'), z: unpack(rows, 'charges'),
                mode: 'markers',
                marker: {
                    size: 8,
                    line: {
                        color: 'rgba(217, 217, 217, 0.14)',
                        width: 0.5
                    },
                    opacity: 0.8
                },
                type: 'scatter3d'
            };


            var data = [trace1];
            var layout = {
                xaxis:{title:'X AXIS TITLE'},
                   yaxis:{title:'Y AXIS TITLE'},
                   zaxis:{title:'Z AXIS TITLE'},
                margin: {
                    l: 0,
                    r: 0,
                    b: 0,
                    t: 0
                }
            };
            Plotly.newPlot('myDiv', data, layout);
        });
