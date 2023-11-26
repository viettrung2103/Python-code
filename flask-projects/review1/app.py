from flask import Flask, url_for,request,render_template,redirect

app = Flask(__name__)

@app.route("/", methods =["GET"])
def index():
  args = request.args
  # if result == None:
  #   return render_template("index.html",result = result)
  # else:
  number1 = args.get("number1",None)
  number2 = args.get("number2",None)
  number3 = args.get("number3",None)
  # number1 = request.form.get("number1")
  # number2 = request.form.get("number2")
  # number3 = request.form.get("number3")
  if number1 != None and number2 != None and number3 != None:
    result = round((float(number1) + float(number2) + float(number2)) / 3,2)
    # if result == None:
    #   return render_template("index.html",result = result)
    # else:
    # return render_template("index.html", result = result)
  else:
    result = None
  return render_template("index.html", result= result)  

if __name__ == "__main__":
  app.run(debug=True)