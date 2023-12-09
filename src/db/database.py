from pymongo import MongoClient
from config import get_settings

DB_USER = get_settings().DB_USER
DB_PASS = get_settings().DB_PASS
DB_SERVER = get_settings().DB_SERVER

def get_client():
    print("conectando...")
    uri = f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_SERVER}"
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Connected to Database!")
    except Exception as e:
        print(e)
    return client

def get_database(db_name: str):
    client = get_client()
    return client[db_name]

def get_collection(db_name: str, collection_name: str):
    db = get_database(db_name)
    return db[collection_name]

##############################################################
#                          Create                            #
##############################################################

def insert_one(db_name: str, collection_name: str, data: dict):
    collection = get_collection(db_name, collection_name)
    insert = collection.insert_one(data)
    collection.database.client.close()
    return insert

def insert_many(db_name: str, collection_name: str, data: list):
    collection = get_collection(db_name, collection_name)
    insert = collection.insert_many(data)
    collection.database.client.close()
    return insert

##############################################################
#                          Read                              #
##############################################################

def find_one(db_name: str, collection_name: str, filter: dict):
    collection = get_collection(db_name, collection_name)
    find = collection.find_one(filter)
    collection.database.client.close()
    return find

def find_many(db_name: str, collection_name: str, filter: dict):
    collection = get_collection(db_name, collection_name)
    find = collection.find(filter)
    collection.database.client.close()
    return find

def find_all(db_name: str, collection_name: str):
    collection = get_collection(db_name, collection_name)
    find = collection.find({})
    collection.database.client.close()
    return find

##############################################################
#                          Update                            #
##############################################################

def update_one(db_name: str, collection_name: str, filter: dict, data: dict):
    collection = get_collection(db_name, collection_name)
    update = collection.update_one(filter, data)
    collection.database.client.close()
    return update

def update_many(db_name: str, collection_name: str, filter: dict, data: dict):
    collection = get_collection(db_name, collection_name)
    update = collection.update_many(filter, data)
    collection.database.client.close()
    return update

##############################################################
#                          Delete                            #
##############################################################

def delete_one(db_name: str, collection_name: str, filter: dict):
    collection = get_collection(db_name, collection_name)
    delete = collection.delete_one(filter)
    collection.database.client.close()
    return delete

def delete_many(db_name: str, collection_name: str, filter: dict):
    collection = get_collection(db_name, collection_name)
    delete = collection.delete_many(filter)
    collection.database.client.close()
    return delete






