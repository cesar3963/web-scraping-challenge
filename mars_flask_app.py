from flask import Flask, render_template, redirect
import Pyclient
import mars_scrape

app = Flask(__name__)

conn = "clientdb://localhost:27017/mars_app"
client = Pyclient.clientClient(conn)

# app.config["client_URI"] = "clientdb://localhost:27017/mars_app"
# client = Pyclient(app)

@app.route("/")
def index():

    mars_dict = client.db.mars_dict.find_one()
    return render_template("index.html", mars=mars_dict)


@app.route("/mars_scrape.py")
def scrape():
  
    mars_dict = client.db.mars_dict
    mars_data = mars_scrape.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)