# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from pymongo import *
from datetime import datetime
from bson import ObjectId
from db_models.config_models import *
from db_models.auth_models import db_get_user_id_by_username

def db_add_new_anamnesis(username, agent_id, anamnesis_mode, dialogflow_session_id):
    creation_datetime = datetime.now() 
    user_id = db_get_user_id_by_username(username)
    anamnesis = {
        "user_id":user_id,
        "username":username,
        "title":"Sin título",
        "agent_id":agent_id,
        "anamnesis_mode":anamnesis_mode,
        "dialogflow_session_id":dialogflow_session_id,
        "creation_datetime":creation_datetime,
        "last_interaction_datetime":None,
        "status":"created",
        "dialog":[],
        "symptoms":[],
        "symptoms_details":[],
        "duration_seconds":None,
        "number_interactions":0
    }
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    response = anamnesis_collection.insert_one(anamnesis)
    if(response.inserted_id):
        return True
    else:
        return False
    
def db_get_all_navigation_anamnesis(username):
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    anamnesis_elements = anamnesis_collection.find({"username":username})\
                                             .sort("creation_datetime",-1)
    navigation_anamnesis = []
    for anamnesis in anamnesis_elements:
        creation_datetime = anamnesis["creation_datetime"]
        anamnesis_data = {
            "anamnesis_mode":anamnesis["anamnesis_mode"],
            "creation_date":creation_datetime.strftime("%Y-%m-%d | %H:%M:%S"),
            "creation_timestamp":str(creation_datetime.timestamp()),
            "title":anamnesis["title"],
            "status":anamnesis["status"]
        }
        navigation_anamnesis.append(anamnesis_data)
    if navigation_anamnesis:
        return navigation_anamnesis
    else:
        return None
    
def db_delete_anamnesis(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    response = anamnesis_collection.delete_one(query)
    if(response.deleted_count > 0):
        return True
    else:
        return False

def db_get_anamnesis_mode(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    projection = {
        "_id":0,
        "anamnesis_mode":1
    }
    response = anamnesis_collection.find_one(query, projection)
    if response:
        return response.get("anamnesis_mode")
    else:
        return False
    
def db_get_anamnesis_mode_and_dialogflow_session_id(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    projection = {
        "_id":0,
        "anamnesis_mode":1,
        "dialogflow_session_id":1
    }
    response = anamnesis_collection.find_one(query, projection)
    if response:
        return response
    else:
        return False
    
def db_update_anamnesis_title(username, anamnesis_timestamp, title):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    update ={
        "$set": {
            "title":title
        }
    }
    response = anamnesis_collection.update_one(query, update)
    if response.modified_count > 0:
        return response
    else:
        return False
    
def db_update_anamnesis_status(username, anamnesis_timestamp, status):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    update ={
        "$set": {
            "status":status
        }
    }
    response = anamnesis_collection.update_one(query, update)
    if response.modified_count > 0:
        return response
    else:
        return False

def db_get_all_anamnesis_dialog_texts(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    projection = {
        "_id":0,
        "dialog":1
    }
    response = anamnesis_collection.find_one(query, projection)
    if response:
        dialog = response.get("dialog")
        dialog_texts = []
        if(len(dialog)>0):
            for interaction in dialog:
                interaction_texts ={
                    "query_text": interaction.get("query_text"),
                    "query_interpreted_text": interaction.get("query_interpreted_text"),
                    "response_text": interaction.get("response_text")
                }
                dialog_texts.append(interaction_texts)
        return dialog_texts
    else:
        return False

def db_get_anamnesis_data(username, anamnesis_timestamp):
    if (anamnesis_timestamp): 
        anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    else:
        anamnesis_datetime = None
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    pipeline = [
        {
            "$match": {
                "username": username,
                "creation_datetime": anamnesis_datetime
            }
        },
        {
            "$unwind": "$dialog"
        },
        {
            "$sort":{"dialog.interaction_datetime":-1}
        },
        {
            "$limit":1
        },
        {
            "$project": {
                "_id":0,
                "anamnesis_mode":1,
                "status":1,
                "title":1,
                "agent_id":1,
                "dialog.intent":1,
                "dialog.interaction_meaning": 1,
                "dialog.complete_intent": 1,
                "dialog.new_intent":1,
                "symptoms":1,
                "creation_datetime":1,
                "last_interaction_datetime":1,
                "duration_seconds":1,
                "number_interactions":1
            }
        },
    ]
    a='.strftime("%Y-%m-%d | %H:%M:%S")'
    response = list(anamnesis_collection.aggregate(pipeline))
    if response:
        final_response = response[0]
        duration_seconds = final_response["duration_seconds"]
        hours = duration_seconds // 3600
        minutes = (duration_seconds % 3600) // 60
        seconds = duration_seconds % 60
        final_response["duration_seconds"] = "{:02}:{:02}:{:02}".format(int(hours),int(minutes),int(seconds))
        final_response["creation_datetime"] = final_response["creation_datetime"].strftime("%Y-%m-%d | %H:%M:%S")
        final_response["last_interaction_datetime"] = final_response["last_interaction_datetime"].strftime("%Y-%m-%d | %H:%M:%S")
        return final_response
    else:
        return False
    
def db_get_anamnesis_symptoms(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    query = {
        "username": username,
        "creation_datetime": anamnesis_datetime
    }
    projection = {
        "_id":0,
        "symptoms":1
    }
    response = anamnesis_collection.find_one(query, projection)
    if response:
        return response["symptoms"]
    else:
        return False

def db_get_all_anamnesis_data(username, anamnesis_timestamp):
    anamnesis_datetime = datetime.fromtimestamp(float(anamnesis_timestamp))
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["anamnesis"]]
    pipeline = [
        {
            "$match": {
                "username": username,
                "creation_datetime": anamnesis_datetime
            }
        },
        {
            "$unwind": "$dialog"
        },
        {
            "$sort":{"dialog.interaction_datetime":-1}
        }
    ]
    response = list(anamnesis_collection.aggregate(pipeline))
    if response:
        return response[0]
    else:
        return False