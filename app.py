from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Real shit. I have another rapper to chill with"