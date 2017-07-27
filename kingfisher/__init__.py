import os
from .base import app
from . import routes
from . import models as m
from waitress import serve

def main(argv):
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://postgres:postgres@localhost/kingfisher')
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   m.db.init_app(app)
   serve(app) 

