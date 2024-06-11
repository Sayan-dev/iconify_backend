import pymongo
import os

mongo_client = pymongo.MongoClient(os.getenv("DB_URL"))

database = mongo_client['iconify']