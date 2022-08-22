from flask import Flask

app = Flask(__name__)


@app.route("/")
def allo_world():
    return "<h1>Allo, World!</h1>"
