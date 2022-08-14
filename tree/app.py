# from flask import Flask

# from tree.extensions import db


# def create_app():
#     # Create and configure app
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

#     # Init database
#     db.init_app(app)

#     # Migrations here?

#     # Import Blueprints
#     from tree.blueprints import (cat)

#     # Register Blueprints / endpoints
#     app.register_blueprint(cat.blueprint)

#     return app
