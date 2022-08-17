from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tree.config import DevelopmentConfig

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # TODO test for os.environ for prod vs dev - only having dev is fine for now
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    # Migrations here?
    register_blueprints(app)

    return app


def register_blueprints(app):
    from tree.blueprints import cat

    app.register_blueprint(cat.blueprint)
