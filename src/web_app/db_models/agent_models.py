# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from pymongo import *
from db_models.config_models import *


def db_get_interaction_meaning(agent, intent_name):
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
                "intents.name": intent_name
            }
        },
        {
            "$limit":1
        },
        {
            "$project": {
                "_id": 0,
                "type": "$intents.type"
            }
        },
    ]
    response = list(anamnesis_collection.aggregate(pipeline))[0]["type"]
    if response:
        return response
    else:
        return False


def db_get_review_sentence_symptom(agent, sentence):
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
                "intents.name": "__anamnesis_aparatos"
            }
        },
        {
            "$limit":1
        },
        {
            "$unwind": "$intents.parameters"
        },
        {
            "$unwind": "$intents.parameters.prompts"
        },
        {
            "$match": {
                "intents.parameters.prompts": sentence
            }
        },
        {
            "$project": {
                "_id": 0,
                "symptom": "$intents.parameters.symptom"
            }
        }
    ]
    response = anamnesis_collection.aggregate(pipeline)
    response_list = list(response)
    if response_list:
        clean_response = response_list[0]["symptom"]
        return clean_response
    else:
        return False  
    
def db_get_symptom_and_region_from_intent(agent, intent):
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
                "region": "$intents.region"
            }
        }
    ]
    response = anamnesis_collection.aggregate(pipeline)
    if response:
        return list(response)[0]
    return False