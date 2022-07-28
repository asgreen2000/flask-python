import mongoengine
from config import Config


db_connector = mongoengine.connect(host=Config.MONGODB_URL)