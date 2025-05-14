from bson.objectid import ObjectId
from django import template
from pymongo import MongoClient
from utils.utils import get_mongo_db

register = template.Library()

def get_author(id_):
    db = get_mongo_db()
    author = db.author.find_one({"_id": ObjectId(id_)})
    if author:
        return author.get('fullname', 'Unknown Author')
    return "Unknown Author"

register.filter('author', get_author)
