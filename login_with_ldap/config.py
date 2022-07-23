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
    MONGODB_SETTINGS = {
        'db': 'your_database',
        'host': 'localhost',
        'port': 27017
    }

    SECRET_KEY = 'adgjmptw'

    
class ProductionConfig(Config):
    """
    """
    LDAP_SERVER = 'ipa.demo1.freeipa.org'
    DEBUG = False
    MONGODB_SETTINGS = {
        'db': 'your_database',
        'host': 'localhost',
        'port': 27017
    }
    SECRET_KEY = 'adgjmptw'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}