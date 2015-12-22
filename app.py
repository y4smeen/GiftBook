from flask import Flask, render_template, session
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "Don't store this on github"
   app.run(host="0.0.0.0", port=8000)
