import mongoengine
from config import Config


client = mongoengine.connect(host=Config.MONGODB_URL)