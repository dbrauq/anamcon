# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from dialog.dialog_manager import *
from db_models.dialog_models import *
from db_models.anamnesis_models import *
from db_models.agent_models import *
from dialog.config_dialog import *
from os.path import dirname, abspath


def dialog_send_text(username, anamnesis_timestamp, agent, session_id, interaction_id, text,interaction_mode="active"):
    interaction_type = "text"
    query_text = text
    if text in USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS or text in USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS: interaction_mode = "pasive"
    text_interaction = Dialog_Session(session_id, agent_id=agent).text_interaction(text)
    agent_id = text_interaction._get_agent_id()
    query_interpreted_text = text_interaction.get_query_text()
    query_sentiment_type = text_interaction.get_input_sentiment_type()
    query_sentiment_intensity = text_interaction.get_input_sentiment_intensity()
    intent = text_interaction.get_intent_name()
    complete_intent = text_interaction.all_requierd_params_present()
    intent_confidence = text_interaction.get_intent_confidence()
    intent_parameters_and_values = text_interaction.get_intent_parameters_and_values()
    response_text = text_interaction.get_response_text()
    response_audio = text_interaction.get_response_audio()
    if USE_START_MODE == "DOCKER":
        text_interaction.save_audio_response(dirname(dirname(abspath(__file__))) + "/sessions/audio/" + interaction_id +".wav")
    else:
        text_interaction.save_audio_response(USE_OUTPUT_AUDIO_TEMP_PATH + interaction_id +".wav")
    interaction_meaning = db_get_interaction_meaning(agent_id, intent)
    new_intent = all(value == "" for value in intent_parameters_and_values.values())
    interaction_data ={
        "interaction_id":interaction_id,
        "interaction_mode":interaction_mode,
        "interaction_type":interaction_type,
        "query_text":query_text,
        "agent_id":agent_id,
        "query_interpreted_text":query_interpreted_text,
        "query_sentiment_type":query_sentiment_type,
        "query_sentiment_intensity":query_sentiment_intensity,
        "intent":intent,
        "complete_intent":complete_intent,
        "new_intent":new_intent,
        "intent_confidence":intent_confidence,
        "intent_parameters_and_values":intent_parameters_and_values,
        "response_text":response_text,
        "interaction_meaning":interaction_meaning
    }
    if(interaction_meaning == "review"):
        symptoms = db_get_anamnesis_symptoms(username,anamnesis_timestamp)
        review_symptom = db_get_review_sentence_symptom(agent, response_text)
        if symptoms is not None and review_symptom is not None:
            for symptom in symptoms:
                for name, UID in symptom.items(): 
                    if name == review_symptom:
                        db_add_new_dialog_interaction_to_anamnesis(username, anamnesis_timestamp, interaction_data)
                        return dialog_send_text(username, anamnesis_timestamp, agent, session_id, interaction_id, "$__assisted")
    result = db_add_new_dialog_interaction_to_anamnesis(username, anamnesis_timestamp, interaction_data)
    return response_text

def dialog_send_audio(username, anamnesis_timestamp, agent, session_id, interaction_id, audio):
    interaction_type = "speech"
    query_text = None
    interaction_mode = "active"
    audio_interaction = Dialog_Session(session_id, agent_id=agent).speech_interaction(audio)
    agent_id = audio_interaction._get_agent_id()
    query_interpreted_text = audio_interaction.get_query_text()
    query_sentiment_type = audio_interaction.get_input_sentiment_type()
    query_sentiment_intensity = audio_interaction.get_input_sentiment_intensity()
    intent = audio_interaction.get_intent_name()
    complete_intent = audio_interaction.all_requierd_params_present()
    intent_confidence = audio_interaction.get_intent_confidence()
    intent_parameters_and_values = audio_interaction.get_intent_parameters_and_values()
    response_text = audio_interaction.get_response_text()
    response_audio = audio_interaction.get_response_audio()
    if USE_START_MODE == "DOCKER":
        audio_interaction.save_audio_response(dirname(dirname(abspath(__file__))) + "/sessions/audio/" + interaction_id +".wav")
    else:
        audio_interaction.save_audio_response(USE_OUTPUT_AUDIO_TEMP_PATH + interaction_id +".wav")
    interaction_meaning = db_get_interaction_meaning(agent_id, intent)
    new_intent = all(value == "" for value in intent_parameters_and_values.values())
    interaction_data ={
        "interaction_id":interaction_id,
        "interaction_mode":interaction_mode,
        "interaction_type":interaction_type,
        "query_text":"",
        "agent_id":agent_id,
        "query_interpreted_text":query_interpreted_text,
        "query_sentiment_type":query_sentiment_type,
        "query_sentiment_intensity":query_sentiment_intensity,
        "intent":intent,
        "complete_intent":complete_intent,
        "new_intent":new_intent,
        "complete_intent":complete_intent,
        "intent_confidence":intent_confidence,
        "intent_parameters_and_values":intent_parameters_and_values,
        "response_text":response_text,
        "interaction_meaning":interaction_meaning

    }
    if(interaction_meaning == "review"):
        symptoms = db_get_anamnesis_symptoms(username,anamnesis_timestamp)
        review_symptom = db_get_review_sentence_symptom(agent, response_text)
        if symptoms is not None and review_symptom is not None:
            for symptom in symptoms:
                for name, UID in symptom.items(): 
                    if name == review_symptom:
                        db_add_new_dialog_interaction_to_anamnesis(username, anamnesis_timestamp, interaction_data)
                        return dialog_send_text(username, anamnesis_timestamp, agent, session_id, interaction_id, "$__assisted")
    result = db_add_new_dialog_interaction_to_anamnesis(username, anamnesis_timestamp, interaction_data)
    return response_text