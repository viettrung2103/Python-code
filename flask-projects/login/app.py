from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

#set the config of the session to be delete when tab is close, or user quit the browser
app.config["SESSION_PERMANENT"] = False
#let the content of the session to be saved in server(backend), not in cookie(client), for privacy
app.config["SESSION_TYPE"] = "filesystem"
#activate session in this app
Session(app)

@app.route("/")
def index():
  name = session.get("name")
  if not name:
    return redirect("/login")
  return render_template("index.html", name = name)

@app.route("/login", methods=["POST","GET"])
def login():
  if request.method == "POST":
    session["name"] = request.form.get("name")
    return redirect("/")
  return render_template("login.html")

@app.route("/logout")
def logout():
  #clear user session
  session.clear()
  return redirect("/")