from .base import app
from .responses import *
from flask import jsonify

@app.route('/ping')
def summary():
    return ok("pong")
