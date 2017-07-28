from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from .base import app
from . import models

migrate = Migrate(app, models.db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
