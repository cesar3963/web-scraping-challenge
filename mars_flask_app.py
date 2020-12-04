from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mango = PyMongo(app)


# app.config["mango_URI"] = "mangodb://localhost:27017/mars_app"
# mango = Pymango(app)

@app.route("/")
def index():

    mars = mango.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/mars_scrape")
def scrape():
  
    mars = mango.db.mars
    mars_data = mars_scrape.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Compleated successfully"

if __name__ == "__main__":
    app.run(debug=True)