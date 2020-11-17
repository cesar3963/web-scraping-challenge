from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():

    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars=mars_dict)


@app.route("/mars_scrape.py")
def scrape():
  
    mars_dict = mongo.db.mars_dict
    mars_data = mars_scrape.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)