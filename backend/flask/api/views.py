from flask import jsonify, request, abort, make_response

from api import app
from .models import db_get_all_cat, db_get_cat, db_create_cat, db_edit_cat, db_delete_cat


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error':'Bad request'}), 400)

##### test #####
@app.route("/api/test/", methods=['GET'])
def get_stuff():
    test = {'hello':'world'}
    return jsonify(test)

##### categories #####
@app.route("/api/categories/", methods=['GET'])
def get_all_categories():
    categories = db_get_all_cat()
    json = []
    for id, name in categories:
        temp = {}
        temp['id'] = id
        temp['name'] = name
        json.append(temp)

    return jsonify({'categories':json})

@app.route("/api/categories/<int:category_id>", methods=['GET'])
def get_category(category_id):
    category = db_get_cat(category_id)
    if not category:
        abort(404)
    json = {}
    json['id'] = category[0][0]
    json['name'] = category[0][1]
    return jsonify({'categories':[json]})

@app.route("/api/categories/", methods=['POST'])
def add_category():
    if not request.json or 'name' not in request.json:
        abort(400)
    db_create_cat(request.json['name'])

    return jsonify({"Result":"True"}), 201

@app.route("/api/categories/<int:cat_id>", methods=['PUT'])
def edit_category(cat_id):
    if not request.json or 'name' not in request.json:
        abort(400)
    if not db_get_cat(cat_id):
        abort(404)
    db_edit_cat(cat_id,request.json['name'])
    json = {'id':cat_id, 'name':request.json['name']}

    return jsonify({"categories":[json]})

@app.route("/api/categories/<int:cat_id>", methods=['DELETE'])
def delete_category(cat_id):
    if not db_get_cat(cat_id):
        abort(404)
    db_delete_cat(cat_id)

    return jsonify({"Results":"True"})

##### posts #####
@app.route("/api/posts/", methods=['GET'])
def get_all_posts():
    posts = get_posts()
    json = []
    for id, date, bothering, c_id, goal, done in posts:
        temp = {}
        temp['id'] = id
        temp['bothering'] = bothering
        temp['category_id'] = c_id
        temp['goal'] = goal
        temp['done'] = done
        json.append(temp)

    return jsonify({'posts':json})

@app.route("/api/posts/<int:post_id>", methods=['GET'])
def get_post(post_id):
    pass

@app.route("/api/posts/", methods=['POST'])
def add_post():
    pass

@app.route("/api/posts/<int:post_id>", methods=['PUT'])
def edit_post(post_id):
    pass

# @app.route("/api/posts/", methods=['DELETE'])

