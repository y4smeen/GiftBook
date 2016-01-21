from flask import Flask, render_template, request, redirect, session, url_for
import urllib2, json, urllib, math, time, string

app = Flask(__name__)

@app.route('/' ) #methods=["POST","GET"]
def index():
    return render_template("home.html")
#    if request.method == 'POST':
#        start = request.form['start']
#        end = request.form['end']
#        startCor = geo_loc()
#        endCor = geo_loc()
#        return render_template("results.html")
#    else:
#        return render_template("base.html")

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Don't store this on github"
   app.run(host="0.0.0.0", port=7000)
