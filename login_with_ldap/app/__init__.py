from flask import Flask
from config import app_config
from app.connection.db_connector import db as db_connector 

app = Flask(__name__, instance_relative_config=True)


def create_app(config_name):
    app.config.from_object(app_config[config_name])
    
    from .handlers.users import users as users_blueprint
    # register users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')
    return app