from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_apispec import use_kwargs, marshal_with, doc
from webargs import fields
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec

db = SQLAlchemy()
migrate = Migrate()


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    migrate.init_app(app, db)
    ma = Marshmallow(app)
    CORS(app)

    ## SWAGGER ##
    spec = APISpec(
        title="Tree API",
        version="v1",
        openapi_version="2.0.0",
        plugins=[MarshmallowPlugin()]
    )

    app.config.update(
        {"APISPEC_SPEC": spec, "APISPEC_SWAGGER_URL": "/swagger/"})
    FlaskApiSpec(app)

    swaggerui_blueprint = get_swaggerui_blueprint(
        "/api-docs",
        "/static/swagger.json",
        config={"app_name": "Tree API"}
    )
    app.register_blueprint(swaggerui_blueprint)
    #############

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
    @use_kwargs({
        "username": fields.String(required=True, description="The Users username")
    })
    @marshal_with(users_schema)
    @doc(
        description="",
        tags=[]
    )
    def create_user(username):
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return result, 201

    @app.route("/user/<int:id>", methods=['GET'])
    def get_user_by_id(id):
        user = User.query.get(id)
        user_dumped = user_schema.dump(user)
        return user_dumped, 200

    @app.route("/user", methods=["DELETE"])
    def delete_user():
        request_content = request.get_json()
        User.query.filter_by(id=request_content["id"]).delete()
        db.session.commit()
        return f"user id: {request_content['id']} was deleted", 200

    return app
