

#add this to terminal before run
#$env:FLASK_APP = "appName.py" >> set app for flask to know
#$env:FLASK_DEBUG = 1
# flask run

from flask import Flask, render_template, request


app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
  return render_template("index.html", sports = SPORTS)

#when using checkbox >> form contain array of value, to check if all value is valid need to use form.getall()
#form.get("name"): only check the first value in this array
#form.getlist("name"): check all value in  in this array

@app.route("/register", methods=["POST"])
def register():
  # check version for form not contain checkbox (only one value per key)
  # if not request.form.get("name") or request.form.get("sport") not in SPORTS:

  # check version for form contain checkbox( array of value) (a key can contain array of value)
  if not request.form.get("name"):
    return render_template("failure.html")
  for sport in request.form.getlist("sport"):
    if sport not in SPORTS:
      return render_template("failure.html")
    

  return render_template("success.html")
  
