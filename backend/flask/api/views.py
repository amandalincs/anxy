from flask import jsonify, request, abort, make_response

from api import app
from .models import db_get_all_cat, db_get_cat, db_create_cat, db_edit_cat, db_delete_cat, db_get_all_posts, db_get_post, db_create_post, db_edit_post, db_delete_post,  db_get_posts_by_date


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
def edit_category(category_id):
    if not request.json or 'name' not in request.json:
        abort(400)
    if not db_get_cat(category_id):
        abort(404)
    db_edit_cat(category_id,request.json['name'])

    return jsonify({"Results":"True"})

@app.route("/api/categories/<int:cat_id>", methods=['DELETE'])
def delete_category(category_id):
    if not db_get_cat(category_id):
        abort(404)
    db_delete_cat(category_id)

    return jsonify({"Results":"True"})

##### posts #####
@app.route("/api/posts/", methods=['GET'])
def get_all_posts():
    posts = db_get_all_posts()
    json = []
    print(posts)
    for id, date, bothering, c_id, goal, done in posts:
        temp = {}
        temp['id'] = id
        temp['date'] = date
        temp['bothering'] = bothering
        temp['category_id'] = c_id
        temp['goal'] = goal
        temp['done'] = done
        json.append(temp)

    return jsonify({'posts':json})

@app.route("/api/posts/<int:post_id>", methods=['GET'])
def get_post(post_id):
    post = db_get_post(post_id)
    if not post:
        abort(404)
    json = {}
    json['id'] = post[0][0]
    json['date'] = post[0][1]
    json['bothering'] = post[0][2]
    json['category_id'] = post[0][3]
    json['goal'] = post[0][4]
    json['done'] = post[0][5]

    return jsonify({'posts':[json]})
    
@app.route("/api/posts/", methods=['POST'])
def add_post():
    print("adding..")

    if not request.json:
        print("not a json")
        abort(400)
    if 'bothering' not in request.json:
        print("bothering")
        abort(400)
    if 'c_id' not in request.json:
        print("c_id")
        abort(400)
    if 'goal' not in request.json:
        print("goal")
        abort(400)
    
    db_create_post(request.json['bothering'], int(request.json['c_id']), request.json['goal'])

    return jsonify({"Results":"True"}), 201
    
@app.route("/api/posts/<int:post_id>", methods=['PUT'])
def edit_post(post_id):
    if not request.json:
        abort(400)
    if 'bothering' not in request.json:
        abort(400)
    if 'c_id' not in request.json:
        abort(400)
    if 'goal' not in request.json:
        abort(400)
    if 'done' not in request.json:
        abort(400)
    
    if not db_get_post(post_id):
        abort(404)

    db_edit_post(post_id,request.json['bothering'],request.json['c_id'],request.json['goal'],request.json['done'])

    return jsonify({"Results":"True"})
    
# @app.route("/api/posts/", methods=['DELETE'])

@app.route("/api/posts/<int:month>/<int:day>/<int:year>", methods=['GET'])
def get_posts_by_date(month, day, year):
    posts = db_get_posts_by_date(month, day, year)
    json = []
    for _,_,bothering,c_id,goal,_ in posts:
        temp = {}
        temp['bothering'] = bothering
        temp['category_id'] = c_id
        temp['goal'] = goal
        json.append(temp)
    
    return jsonify({'posts':json})
