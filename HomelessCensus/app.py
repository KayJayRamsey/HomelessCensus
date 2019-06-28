from flask import Flask, render_template, redirect
from sqlalchemy import create_engine
from sqlconfig import password
import pymysql
pymysql.install_as_MySQLdb()

#Connect to SQL and Import
engine = create_engine(f'mysql://root:{password}@localhost:3306/'homelesscensus')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
session = Session(engine)

#Create an instance of Flask
app = Flask(__name__)

#Flask Route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/project<br/>"
        f"/api/v1.0/visualizations"
        f"/api/v1.0/dat"
    )