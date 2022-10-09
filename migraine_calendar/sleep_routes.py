from flask import request, jsonify, make_response
from migraine_calendar import app
import migraine_calendar.repository as repo

PREFIX = "/api/v1/sleep"


@app.route(PREFIX + '/all', methods=['GET'])
def api_get_all_sleeps():
    print("get all sleeps")
    sleeps = repo.get_all_sleeps()
    print(sleeps)
    return make_response(jsonify([m.as_dict() for m in sleeps]), 200)


@app.route(PREFIX + '/<mid>', methods=['GET'])
def api_get_sleep_by_id(sid):
    print(f"get sleep with id {sid}")
    sleep = repo.get_sleep_by_id(sid)
    return make_response(jsonify(sleep.as_dict()), 200)


@app.route(PREFIX, methods=['POST'])
def api_post_sleep():
    sleep = request.get_json(force=True)
    print(sleep)
    repo.insert_new_sleep(sleep)
    return make_response('', 201)


@app.route(PREFIX + '/<mid>', methods=['PUT'])
def api_put_sleep(mid):
    sleep = request.get_json(force=True)
    repo.update_sleep_by_id(mid, sleep)
    return make_response('', 201)


@app.route(PREFIX + '/<mid>', methods=['DELETE'])
def api_delete_sleep(mid):
    repo.delete_sleep_by_id(mid)
    return make_response('', 204)
