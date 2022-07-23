class Config(object):
    """
    """
    MONGODB_URL = "mongodb+srv://asgreen:14042023@cluster0.aywbz.mongodb.net/lvtn?retryWrites=true&w=majority"
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