from .base import app
from . import routes
from . import models as m
from waitress import serve

def main(argv):
   app.config['SQLALCHEMY_DATABASE_URI'] = None
   m.db.init_app(app)
   serve(app) 

