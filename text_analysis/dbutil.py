import pymongo
from pymongo import MongoClient

# initiate mongo client
def get_mongo_connection():
    client = MongoClient('localhost',27017)

    db = client.local

    return db

# get mongodb collection
def get_mongo_collection(db):
    collection = db.wordcount

    return collection

# insert items
def insert_bulk_data(db, json):
    result = db.insert_many(json)

# insert items by loop
def insert_text_analysis_data(tbl, counter):
    for word,cnt in counter.most_common(50):
        tbl.insert_one({word:cnt})

# select all items
def findAll(db):

    collection = get_mongo_collection(db)

    #item = collection.find_one()
    items = collection.find()

    for item in collection.find():
        print(item)
