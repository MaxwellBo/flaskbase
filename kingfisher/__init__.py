import os
import waitress

from .base import app
from . import routes
from . import models

def main(argv):
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql://postgres:postgres@localhost/kingfisher')
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

   models.db.init_app(app)

   waitress.serve(app)

