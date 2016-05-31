import pymongo
from pymongo import MongoClient

# initiate mongo client
def get_mongo_connection():
    client = MongoClient('localhost',27017)

    db = client.movies

    return db

# get mongodb collection
def get_mongo_collection(db):
    collection = db.movies

    return collection

# insert items
def insert_bulk_data(db, json):
    result = db.insert_many(json)

# select all items
def findAll(db):

    collection = get_mongo_collection(db)

    #item = collection.find_one()
    items = collection.find()

    for item in collection.find():
        print(item)
