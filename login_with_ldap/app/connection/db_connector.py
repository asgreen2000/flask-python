from pymongo import MongoClient
from config import Config


client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGODB_DB]