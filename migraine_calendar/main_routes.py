from flask import render_template, url_for, request, jsonify, make_response
from migraine_calendar import app
import migraine_calendar.repository as repo


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    migraines = repo.get_all_migraines()
    return render_template('home.html', migraines=migraines)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html', title="About")
