# backend/database.py
from flask_pymongo import PyMongo
mongo = PyMongo()
db = mongo.db
