

#add this to terminal before run
#$env:FLASK_APP = "appName.py" >> set app for flask to know
#$env:FLASK_DEBUG = 1
# flask run

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  if request.method == "POST":
      name = request.form.get("name","World from Post")
      return render_template("greet.html",name = name)
  return render_template("index.html")

# @app.route("/greet", methods = ["POST"])
# def greet():
#   ##below line helps to get value from form, sent from index.html
#   name = request.form.get("name","World from Post")
  
  
#   # reqeust.args.get("key") >> retrieve value after the ?key= and process it
#   # name = request.args.get("name","World From Get")
#   return render_template("greet.html",name = name)


#add this to terminal before run
#$env:FLASK_APP = "appName.py" >> set app for flask to know
#$env:FLASK_DEBUG = 1
# flask run