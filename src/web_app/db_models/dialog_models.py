# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from pymongo import *
from datetime import datetime
from bson import ObjectId
from db_models.config_models import *
from db_models.agent_models import *


def db_add_new_dialog_interaction_to_anamnesis(username, anamnesis_timestamp, interaction_data):
    last_interaction_datetime = datetime.now() 
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
    interaction_data["interaction_datetime"] = last_interaction_datetime
    if response:
        push_update = {
            "$push": {
                "dialog": interaction_data
            }   
        }
        response_2 = anamnesis_collection.update_one(query, push_update)
        duration = (last_interaction_datetime - anamnesis_datetime).total_seconds()
        if(interaction_data["interaction_mode"] == "active"):
            update = {
                "$set": {
                    "last_interaction_datetime": last_interaction_datetime,
                    "duration_seconds": duration
                },
                "$inc": {
                    "number_interactions": 1,
                }   
            }
        else:
            update = {
                "$set": {
                    "last_interaction_datetime": last_interaction_datetime,
                    "duration_seconds": duration
                }
            }
        response_3 = anamnesis_collection.update_one(query, update)
        intent = interaction_data["intent"]
        agent = interaction_data["agent_id"]
        if interaction_data["complete_intent"] and interaction_data["interaction_meaning"] == "symptom":
            symptom_details = db_get_symptom_and_region_from_intent(agent, intent)
            symptom_title = symptom_details["symptom_title"]
            symptom_region = symptom_details["region"]

            push_update_2 = {
                "$push": {
                    "symptoms": {interaction_data["intent"]:{
                        "interaction_id": interaction_data["interaction_id"],
                        "title": symptom_details["symptom_title"],
                        "region": symptom_details["region"]
                        }
                    },
                }
            }
            response_4 = anamnesis_collection.update_one(query, push_update_2)

               
        return True
    else:
        return False