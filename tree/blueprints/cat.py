import json
from flask import Blueprint, jsonify, request

from tree.db import get_db

blueprint = Blueprint('cat', __name__, url_prefix='/cat')


@blueprint.route('/', methods=['GET'])
def get_all_cats():
    db = get_db()
    result = db.execute('SELECT * FROM cat').fetchall()

    cats = []
    for cat in result:
        cats.append({
            'name': cat['name'],
            'size': cat['size'],
            'color': cat['color']
        })

    return jsonify(cats)


@blueprint.route('/', methods=['POST'])
def create_cat():
    data = request.get_json(force=True)
    name = data['name']
    size = data['size']
    color = data['color']

    db = get_db()
    db.execute(
        'INSERT INTO cat (name, size, color) VALUES (?, ?, ?)',
        (name, size, color)
    )
    db.commit()

    return f'{name} was created.', 201


@blueprint.route('/<int:id>', methods=['DELETE'])
def delete_cat(id):
    db = get_db()
    db.execute('DELETE FROM cat WHERE id = ?', (id,))
    db.commit()

    return 'Deleted', 200
