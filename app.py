from flask import Flask, render_template, request, redirect, session, url_for
import urllib2, json, urllib, math, time, string
import utils

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if (request.method == "GET"):
        return render_template("home.html")
    else:
        origin = request.form['origin']
        destination = request.form['destination']
        results = utils.findTrain(origin, destination)
        return render_template("results.html", routes=results)
#    if request.method == 'POST':
#        start = request.form['start']
#        end = request.form['end']
#        startCor = geo_loc()
#        endCor = geo_loc()
#        return render_template("results.html")
#    else:
#        return render_template("base.html")

# @app.route('/results')
# def results():
#     origin = request.form['origin']
#     destination = request.form['destination']
#     submit = request.form['submit']
#     results = findTrain(origin, destination)
#     return render_template("results.html", routes=results)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

    
if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Don't store this on github"
   app.run(host="0.0.0.0", port=7000)
