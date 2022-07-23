import flask
from flask import request, jsonify, make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Hello World"


@app.route('/api/v1/migraines/all', methods=['GET'])
def api_all():
    return jsonify("hello")


@app.route('/api/v1/migraines', methods=['POST'])
def api_put_migraine():
    migraine = request.get_json(force=True)
    print(migraine)
    return make_response(jsonify(migraine), 201)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
