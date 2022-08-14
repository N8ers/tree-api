from flask import Flask

from tree.extensions import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)

    # Migrations here?

    register_blueprints(app)

    return app


def register_blueprints(app):
    from tree.blueprints import cat

    app.register_blueprint(cat.blueprint)
