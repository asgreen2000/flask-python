from flask import Flask, request
from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # set application root
    
    from .handlers.users import users as users_blueprint
    # register users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/users')
    return app