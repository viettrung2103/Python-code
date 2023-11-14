from flask import Flask, render_template, request

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
def calculator():
    args = request.args
    num1 = float(args.get("number1"))
    num2 = float(args.get("number2"))
    total_sum = num1 + num2
    return str(total_sum)




# @app.route ("/") is the same as @app.route
# @app.route
# def main_hello():
#     return "<p>Hello world</p>"

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(user_reload=True, debug = True)