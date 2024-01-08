# ---------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# ---------------------------------

from pymongo import *
from config.config_main.config_merged import (USE_WEB_APP_DIALOG_AGENT_IDS,
                                             USE_AGENTS_BASE_DATA_PATH,
                                             USE_DB_PORT,
                                             USE_DB_NAME,
                                             USE_DB_COLLECTIONS)
from os.path import abspath, dirname, join
from json import load

def db_load_agents():
    for agent in USE_WEB_APP_DIALOG_AGENT_IDS:
        db_load_agent(agent)

def db_load_agent(agent):
    mongo_client = MongoClient("localhost", int(USE_DB_PORT))
    database = mongo_client[USE_DB_NAME]
    agents_collection = database[USE_DB_COLLECTIONS["agents"]]
    agent_json_file_path = (join(join(dirname(abspath(__file__)), "anamnesis_data"),agent + ".json"))
    with open (agent_json_file_path, "r") as agent_file:
        agent_data = load(agent_file)
        response = agents_collection.insert_one(agent_data)
    if response:
        return response
    else:
        return False



    