from flask import request, jsonify, make_response
from migraine_calendar import app
import migraine_calendar.repository2 as repo

PREFIX = "/api/v1/migraines"


@app.route(PREFIX, methods=['GET'])
def home():
    return "Hello World"


@app.route(PREFIX + '/all', methods=['GET'])
def api_get_all():
    print("get all migraines")
    migraines = repo.get_all_migraines()
    print(migraines)
    return make_response(jsonify([m.as_dict() for m in migraines]), 200)


@app.route(PREFIX + '/<mid>', methods=['GET'])
def api_get_by_id(mid):
    print(f"get all migraine with id {mid}")
    migraine = repo.get_migraine_by_id(mid)
    return make_response(jsonify(migraine.as_dict()), 200)


@app.route(PREFIX, methods=['POST'])
def api_post_migraine():
    migraine = request.get_json(force=True)
    print(migraine)
    repo.insert_new_migraine(migraine)
    return make_response('', 201)


@app.route(PREFIX + '/<mid>', methods=['PUT'])
def api_put_migraine(mid):
    migraine = request.get_json(force=True)
    repo.update_migraine_by_id(mid, migraine)
    return make_response('', 201)


@app.route(PREFIX + '/<mid>', methods=['DELETE'])
def api_delete_migraine(mid):
    repo.delete_migraine_by_id(mid)
    return make_response('', 204)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404