from flask import Blueprint

blueprint = Blueprint('cat', __name__, url_prefix='/cat')


@blueprint.route('/', methods=['GET'])
def get_all_cats():
    return 'hi'
