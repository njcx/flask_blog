from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import *

app = create_app('production')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("shell", Shell)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()
