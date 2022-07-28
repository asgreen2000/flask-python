from flask import Flask
from config import app_config
import logging
from flask_cors import CORS
import flask_profiler

app = Flask(__name__, instance_relative_config=True)
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
from app.connection import db_connector 

# profiler


def create_app(config_name):
    
    app.config.from_object(app_config[config_name])
    
    from .handlers.users import users as users_blueprint
    # register users_blueprint
    app.register_blueprint(users_blueprint, url_prefix='/api/users')
    return app