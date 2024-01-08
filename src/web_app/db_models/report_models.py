# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from pymongo import *
from datetime import datetime
from db_models.config_models import*


def db_get_full_user_data(username):
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    users_collection = database[USE_DB_COLLECTIONS["users"]]
    query = {
        "username": username,
    }
    response = users_collection.find_one(query)
    if response:
        return response
    else:
        return False


def db_get_full_anamnesis_data(username, anamnesis_timestamp):
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
    response = anamnesis_collection.find_one(query)
    if response:
        return response
    else:
        return False
    

def db_get_symptom_identifier_and_region_from_intent(agent, intent):
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["agents"]]
    pipeline = [
        {
            "$unwind": "$intents"
        },
        {
            "$match": {
                "agent_name": agent,
                "intents.name": intent
            }
        },
        {
            "$project": {
                "_id": 0,
                "symptom_name":"$intents.name",
                "symptom_title": "$intents.title",
                "region": "$intents.region",
                "identifier": "$intents.concept_identifiers"
            }
        }
    ]
    response = anamnesis_collection.aggregate(pipeline)
    if response:
        return list(response)[0]
    return False

def db_get_parameter_title_from_intent_param(agent, intent, param):
    if USE_START_MODE=="DOCKER":
            mongo_client = MongoClient("mongodb", int(USE_DB_PORT))
    else:
            mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    anamnesis_collection = database[USE_DB_COLLECTIONS["agents"]]
    pipeline = [
        {
            "$unwind": "$intents"
        },
        {
            "$unwind": "$intents.parameters"
        },
        {
            "$match": {
                "agent_name": agent,
                "intents.name": intent,
                "intents.parameters.name": param
            }
        },
        {
            "$project": {
                "_id": 0,
                "parameter_title":"$intents.parameters.title"
            }
        }
    ]
    response = anamnesis_collection.aggregate(pipeline)
    if response:
        return list(response)[0]
    return False