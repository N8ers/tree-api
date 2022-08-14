from flask import Blueprint, jsonify, request

from tree.extensions import db

from tree.models.cat import Cat

blueprint = Blueprint('cat', __name__, url_prefix='/cat')


@blueprint.route('/', methods=['GET'])
def get_all_cats():

    result = Cat.query.all()

    cats = []
    for cat in result:
        cats.append({
            'name': cat.name,
            'size': cat.size,
            'color': cat.color
        })

    return jsonify(cats)


@blueprint.route('/', methods=['POST'])
def create_cat():
    data = request.get_json(force=True)
    name = data['name']

    new_cat = Cat(name=data['name'], size=data['size'], color=data['color'])
    db.session.add(new_cat)
    db.session.commit()

    return f'{name} was created.', 201


@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_cat(id):
    Cat.query.filter(Cat.id == id).delete()
    db.session.commit()

    return 'Deleted', 200
