from .base import app
from flask import jsonify

@app.route('/ping')
def summary():
    return jsonify("pong")
