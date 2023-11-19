

#add this to terminal before run
#$env:FLASK_APP = "appName.py" >> set app for flask to know
#$env:FLASK_DEBUG = 1
# flask run

from flask import Flask, render_template, request, redirect


app = Flask(__name__)


#KEY- VALUE : NAME - SPORT
REGISTRANTS = {}

SPORTS = [
  "Basketball",
  "Soccer",
  "Ultimate Frisbee"
  ]

@app.route("/")
def index():
  return render_template("index.html", sports = SPORTS)

#when using checkbox >> form contain array of value, to check if all value is valid need to use form.getall()
#form.get("name"): only check the first value in this array
#form.getlist("name"): check all value in  in this array

@app.route("/register", methods=["POST","GET"])
def register():
  if request.method == "POST":
  # check version for form not contain checkbox (only one value per key)
  # if not request.form.get("name") or request.form.get("sport") not in SPORTS:

  # check version for form contain checkbox( array of value) (a key can contain array of value)

  #Validate name
    name = request.form.get("name")
    if not name:
      return render_template("error.html",message = "Missing name")
    
    #Validate sport
    sport = request.form.get("sport")
    if not sport:
      return render_template("error.html", message = "Missing sport")
    if sport not in SPORTS:
      return render_template("error.html", message = "Invalid sport")
    
    # Remember registrant
    REGISTRANTS[name] =sport  

    #if render the page directly, it conflict with SOLID principle, as dis functions do 2 feature: one is to register, another is to display 
    #registrants list
    # return render_template("registrants.html", registrants = REGISTRANTS) 
    return redirect("/registrants")
  else: # method is get
    return redirect("/")


@app.route("/registrants")
def registrants():
  # print(REGISTRANTS)
  return render_template("registrants.html", registrants = REGISTRANTS)