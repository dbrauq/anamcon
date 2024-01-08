# ---------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# ---------------------------------

from config.config_main.config_merged import (USE_WEB_APP_DIALOG_AGENT_IDS,
                                             USE_AGENTS_BASE_DATA_PATH)
from config.config_anamnesis.elements_generator import create_agent_elements
from config.config_anamnesis.utils import *
from config.config_anamnesis.agent_models import *
from os.path import abspath, dirname, join, isfile
from os import mkdir, listdir
from json import load
from shutil import make_archive, copy
from config.config_anamnesis.agent_models import *

agents_path = join(dirname(abspath(__file__)), "anamnesis_agents")
anamnesis_data_path = join(dirname(abspath(__file__)), "anamnesis_data")

def create_agents_files():
    delete_folder_content(agents_path)
    mkdir(join(agents_path, "zip_agents"))
    for agent in USE_WEB_APP_DIALOG_AGENT_IDS:
        agent_path = join(agents_path, agent)
        copy_folder_content(join(USE_AGENTS_BASE_DATA_PATH, agent), 
                            agent_path)
        mkdir(join(agent_path, "intents"))
        mkdir(join(agent_path, "entities"))
        with open(join(anamnesis_data_path, agent + ".json"), "r") as anamnesis_file:
            agent_json = load(anamnesis_file)
            create_agent_elements(agent_json, agent, agent_path)

        # For formating the agent_json:
            from json import dumps
            with open(join(anamnesis_data_path, agent + "_standarized.json"), "w") as anamnesis_filenew:
                anamnesis_filenew.write(dumps(agent_json, indent=2, ensure_ascii=False))

def create_agents_zip_files():
    for agent in USE_WEB_APP_DIALOG_AGENT_IDS:
        agents_zip_path = join(agents_path, "zip_agents")
        agent_path = join(agents_path, agent)
        make_archive(join(agents_zip_path,agent),'zip',agent_path)

def update_web_app_agents():
    config_agents_zip_path = dirname(dirname(dirname(abspath(__file__))))+\
        "/config/config_anamnesis/anamnesis_agents/zip_agents"
    web_app_agents_zip_path = dirname(dirname(dirname(abspath(__file__))))+\
        "/src/web_app/dialog/agents_zip"
    delete_folder_content(web_app_agents_zip_path)
    for path in listdir(config_agents_zip_path):
        abs_path = join(config_agents_zip_path, path)
        if isfile(abs_path):
            copy(abs_path,web_app_agents_zip_path)

def load_agents_database():
    
    return



