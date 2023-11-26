from flask import Flask, render_template, request, Response

import json

app = Flask (__name__)

@app.route("/")
# @app.route("/home/")
def index():
    return render_template("index.html")

@app.route('/<name>')
def print_me(name):
    # return "Test string"
    return "hi {}".format(name)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/sum")
def calc():
    args = request.args
    num1 = float(args.get("number1"))
    num2 = float(args.get("number2"))
    total_sum = num1 + num2
    return str(total_sum)

@app.route("/sum_v1")
def calc_sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total = number1 + number2
    
    response = {
        "number1": number1,
        "number2": number2,
        "total": total,
    }
    
    return response

@app.route("/echo/")
@app.route("/echo/<text>")
def echo(text = None):
    if text == None :
        return "no text detected. Please write something after /echo/ in the url"
    
    else:
        response = {
            "echo": text +" " + text
        }
        
        return response
    
@app.route('/sum_v2/<number1>/<number2>')
def calc_sum2(number1,number2):
    try:
        number1 = float(number1)
        number2 = float(number2)
        total = number1 + number1
        response = {
            "num1" : number1,
            "num2" : number2,
            "total_sum" : total,
            "status": 200
        }
        json_response =json.dumps(response)
        http_response = Response(response=json_response,status = 200, mimetype="application/json")
        return http_response
    except ValueError:
        response = {
            "message":"Invalid number is added",
            "status":500
            #should be status 400: for wrong input added
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status = 500,mimetype="application/json")
        
        return http_response

@app.route("/calculator", methods = ["GET"])   
def calculator():
    return render_template("calculator.html")     


@app.route("/result", methods = ["POST"])
def result():
    number1 = int(request.form.get("number1"))
    number2 = int(request.form.get("number2"))
    maths = request.form.get("maths")
    if maths == "sum":
        result = number1 + number2  
    elif maths == "minus":
        result = number1 - number2
    elif maths == "multi":
        result = number1 * number2
    elif maths == "divide":
        if number2 == 0:
            result = "Cannot divide by 0"
        else: 
            result = number1 / number2
    
    return render_template("result.html", 
                           number1 = number1, 
                           number2 = number2, 
                           maths = maths,
                           result = result
                           )    
# @app.route(/sum_v2/<number1>/)
# @app.route("/calculator/<name>")
# @app.route("/calculator/", methods  = ['POST','GET'])
# def calculator(name=None):
#     if request.method == 'GET':
#         user = request.args.get('userName')
#         return redirect(url_for('calculator',name = user))
#     else:
#         user = request.form['userName']
#         return redirect(url_for('calculator',name = user))

# @app.route("/success")
# def succuss(name=None):
#     return render_template('success.html', name = name)

# @app.route ("/") is the same as @app.route
# @app.route
# def main_hello():
#     return "<p>Hello world</p>"

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": error_code
    }
    json_reponse = json.dumps(response)
    http_response = Response(response=json_reponse, status=404, mimetype="application/json")
    return http_response

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(use_reloader = True, host= '127.0.0.1', port=5000)