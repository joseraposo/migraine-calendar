import repository as repo
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/api/v1/migraines/all', methods=['GET'])
def api_get_all():
    migraines = repo.get_all_migraines()
    print(migraines)
    return make_response(jsonify(migraines), 200)


@app.route('/api/v1/migraines/<mid>', methods=['GET'])
def api_get_by_id(mid):
    migraine = repo.get_migraine_by_id(mid)
    return make_response(jsonify(migraine), 200)


@app.route('/api/v1/migraines', methods=['POST'])
def api_post_migraine():
    migraine = request.get_json(force=True)
    print(migraine)
    repo.insert_new_migraine(migraine)
    return make_response('', 201)


@app.route('/api/v1/migraines/<mid>', methods=['PUT'])
def api_put_migraine(mid):
    migraine = request.get_json(force=True)
    repo.update_migraine_by_id(mid, migraine)
    return make_response('', 201)


@app.route('/api/v1/migraines/<mid>', methods=['DELETE'])
def api_delete_migraine(mid):
    repo.delete_migraine_by_id(mid)
    return make_response('', 204)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == '__main__':
    repo.init_db()
    app.run()
