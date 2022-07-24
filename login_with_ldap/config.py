import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    """
    """
    MONGODB_URL = os.environ.get('MONGODB_URL')
    MONGODB_DB = "lvtn"
class DevelopmentConfig(Config):
    """
    """
    LDAP_SERVER = 'ipa.demo1.freeipa.org'
    DEBUG = True
    SQLALCHEMY_ECHO = True

    SECRET_KEY = 'adgjmptw'
    FLASK_ENV = 'development'

    
class ProductionConfig(Config):
    """
    """
    LDAP_SERVER = 'ipa.demo1.freeipa.org'
    DEBUG = False
    SECRET_KEY = 'adgjmptw'
    FLASK_ENV = 'production'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}