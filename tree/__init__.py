from flask import Flask


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def allo_world():
        return "<h1>Allo, World!</h1>"

    return app
