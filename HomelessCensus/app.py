from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_data = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_data = mongo.db.mars_data
    mars_info = scrape_mars.mars_news()
    mars_info = scrape_mars.nasa_image()
    mars_info = scrape_mars.mars_weather_data()
    mars_info = scrape_mars.mars_table_data()
    mars_info = scrape_mars.space_facts()
    mars_data.update({}, mars_info, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
  
