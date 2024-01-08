# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from pymongo import *
from datetime import datetime
from db_models.config_models import *

def db_available_username(username):
    if username.lower() in USE_FORBIDDEN_USERNAMES: 
        return False
    else:
        if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
        else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
        database = mongo_client["anamcon"]
        users_collection = database["users"]
        response = users_collection.count_documents({"username": username})
    if response > 0: 
        return False
    else:
        return True

def db_register_user(user_data, language, user_role="patient"):
    birth_date = user_data.get("birth_date")
    if birth_date != None: birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    print(birth_date)
    user={
        "username":user_data.get("username"),
        "password":user_data.get("password"),
        "id_type":user_data.get("id_type"),
        "id":user_data.get("id"),
        "name":user_data.get("name"),
        "surname":user_data.get("surname"),
        "birth_date":birth_date,
        "sex":user_data.get("sex"),
        "gender":user_data.get("gender"),
        "email":user_data.get("email"),
        "telephone_number":user_data.get("telephone_number"),
        "adress":user_data.get("adress"),
        "zip":user_data.get("zip"),
        "country":user_data.get("country"),
        "health_provider":user_data.get("health_provider"),
        "health_number":user_data.get("health_number"),
        "creation_datetime": datetime.utcnow(),
        "language": language,
        "user_role":"patient"
    }
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    users_collection = database[USE_DB_COLLECTIONS["users"]]
    response = users_collection.insert_one(user)
    if(response.inserted_id):
        return True
    else:
        return False

def db_login_user(user_data):
    query={
        "username":user_data.get("username"),
        "password":user_data.get("password"),
    }
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    users_collection = database[USE_DB_COLLECTIONS["users"]]
    response = users_collection.find_one(query)
    if response is not None:
        return True
    else:
        return False

def db_get_user_id_by_username(username):
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    users_collection = database[USE_DB_COLLECTIONS["users"]]
    user=users_collection.find_one({"username": username})
    if user:
        return user["_id"]
    else:
        return None