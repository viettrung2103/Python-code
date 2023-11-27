from flask import Flask, url_for,request

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def index():
    return "Hello Flask here"



if __name__ == "__main__":
    app.run(debug=True)