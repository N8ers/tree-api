import sqlite3
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    migrate.init_app(app, db)
    ma = Marshmallow(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username

    class UserSchema(ma.SQLAlchemyAutoSchema):
        class Meta:
            id = ma.auto_field()
            username = ma.auto_field()

            # fields to expose
            fields = ("id", "username")

    user_schema = UserSchema()
    users_schema = UserSchema(many=True)

    @app.route("/")
    def allo_world():
        return "<h1>Allo, World!</h1>"

    @app.route("/user", methods=['GET'])
    def get_all_users():
        all_users = User.query.all()
        all_users_dumped = users_schema.dump(all_users)
        return all_users_dumped, 200

    @app.route("/user", methods=['POST'])
    def create_user():
        request_content = request.get_json()
        print(request_content)
        user = User(username=request_content['username'])
        print(user)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return result, 201

    """ TODO
    @app.route("/user/<int:id>", methods=['GET'])
    def get_user_by_id():
        return ""

    @app.route("/user", methods=["DELETE"])
    def delete_user():
        return ""
    """

    return app
