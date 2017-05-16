from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_admin import Admin
from flask_login import LoginManager
from config import config



moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
admin = Admin()
login_mg = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    pagedown.init_app(app)
    login_mg.init_app(app)

    return app
