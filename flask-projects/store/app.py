from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# My Controller
@app.route("/")
def index():
  books = db.execute("SELECT * FROM books")
  return render_template("index.html", books = books)

@app.route("/add-book",methods = ["GET","POST"])
def add_book():
  if request.method == "POST":
    book_title = request.form.get("title")
    db.execute("INSERT INTO books (title) VALUES (?)",book_title)
    return redirect("/")
  return render_template("add-book.html")

@app.route("/cart", methods = ["GET", "POST"])
def cart():
  
  #Ensure cart exists
  if "cart" not in session:
    session["cart"] = []

  #POST
  if request.method == "POST":
    book_id = request.form.get("id")
    if book_id and book_id not in session["cart"]:
      session["cart"].append(book_id)
      return redirect("/cart")
    
  #GET
  #in cs50 library, when insert a list of ID to (?), the result will be (1,2,3,..)
  books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
  print(session["cart"])
  return render_template("cart.html", books = books)

# ['1', '2', '7']
@app.route("/cart/remove", methods = ["POST"])
def cart_remove():
  if request.method == "POST":
    id = request.form.get("id")
    session["cart"].remove(id)
  return redirect("/cart")