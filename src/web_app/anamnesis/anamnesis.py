# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from db_models.anamnesis_models import *
from anamnesis.config_anamnesis import *
from auth.identifier import create_uuidv4
from dialog.dialog import *

def anamnesis_add_new_anamnesis(username, anamnesis_mode):
    if anamnesis_mode in USE_AVAILABLE_ANAMNESIS_MODES:
        dialogflow_session_id = str(create_uuidv4())
        agent_id = USE_AGENT_IDS[USE_AVAILABLE_ANAMNESIS_MODES.index(anamnesis_mode)]
        return db_add_new_anamnesis(username, agent_id, anamnesis_mode, dialogflow_session_id)
    else:
        return False

def anamnesis_get_all_navigation_anamnesis(username):
    return db_get_all_navigation_anamnesis(username)

def anamnesis_delete_anamnesis(username, anamnesis_timestamp):
    return db_delete_anamnesis(username, anamnesis_timestamp)

def anamnesis_get_anamnesis_data(username, anamnesis_timestamp):
    return db_get_anamnesis_data(username, anamnesis_timestamp)

def anamnesis_get_all_anamnesis_dialog_texts(username, anamnesis_timestamp):
    return db_get_all_anamnesis_dialog_texts(username, anamnesis_timestamp)

def anamnesis_update_anamnesis_title(username, anamnesis_timestamp, title):
    db_update_anamnesis_title(username, anamnesis_timestamp, title)

def anamnesis_update_anamnesis_status(username, anamnesis_timestamp, status):
    db_update_anamnesis_status(username, anamnesis_timestamp, status)

def anamnenesis_send_dialog_text(username, anamnesis_timestamp, text):
    aditional_data = db_get_anamnesis_mode_and_dialogflow_session_id(username, anamnesis_timestamp)
    if not aditional_data:
        return {"interaction_id":"-1", "response": "-1"}
    anamnesis_mode = aditional_data.get("anamnesis_mode")
    dialogflow_session_id = aditional_data.get("dialogflow_session_id")
    agent = USE_AGENT_IDS[USE_AVAILABLE_ANAMNESIS_MODES.index(anamnesis_mode)]
    interaction_id = str(create_uuidv4())
    response = dialog_send_text(username, anamnesis_timestamp, agent, dialogflow_session_id, interaction_id, text)
    return {"interaction_id":interaction_id, "response": response}

def anamnesis_send_dialog_audio(username, anamnesis_timestamp, audio):
    aditional_data = db_get_anamnesis_mode_and_dialogflow_session_id(username, anamnesis_timestamp)
    if not aditional_data:
        return {"interaction_id":"-1", "response": "-1"}
    anamnesis_mode = aditional_data.get("anamnesis_mode")
    dialogflow_session_id = aditional_data.get("dialogflow_session_id")
    agent = USE_AGENT_IDS[USE_AVAILABLE_ANAMNESIS_MODES.index(anamnesis_mode)]
    interaction_id = str(create_uuidv4())
    response = dialog_send_audio(username, anamnesis_timestamp, agent, dialogflow_session_id, interaction_id, audio)
    return {"interaction_id":interaction_id, "response": response}