from os.path import abspath, dirname, join
from config.config_main.config_merged import (USE_WEB_APP_DIALOG_AGENT_IDS,
                                              USE_WEB_APP_DIALOG_AGENT_LANGS)
from config.config_anamnesis.utils import *
from json import loads, dumps

def create_agent_elements(agent_json, agent, agent_path):
    create_agent_entities(agent_json["entities"], agent, agent_path)
    create_agent_intents(agent_json["intents"], agent, agent_path)

def create_agent_entities(entities_json, agent, agent_path):
    agent_num = USE_WEB_APP_DIALOG_AGENT_IDS.index(agent)
    agent_main_lang = USE_WEB_APP_DIALOG_AGENT_LANGS[agent_num][0]
    entity_path = join(agent_path, "entities")
    for entity in entities_json:
        entity_name = entity["name"]     
        entity_main=f'\
            {{\
            "id": "{create_uuidv4()}",\
            "name": "{entity_name}",\
            "isOverridable": true,\
            "isEnum": false,\
            "isRegexp": false,\
            "automatedExpansion": true,\
            "allowFuzzyExtraction": false\
            }}'
        entity_main_json = loads(entity_main)
        entity_entries="["
        for option in entity["options"]:
            option_value = option["concept_terms"][0]
            synonyms = option["concept_terms"][:]
            option_synonyms = '['
            for synonym in synonyms:
                option_synonyms += f'\"{synonym}\",'
            option_synonyms = option_synonyms[:-1] + ']' 
            entity_entries=entity_entries + f'\
                {{\
                "value": "{option_value}",\
                "synonyms": {option_synonyms}\
                }},'
        entity_entries = entity_entries[:-1] + "]"
        entity_entries_json = loads(entity_entries)
        
        with open(join(entity_path, entity_name+".json"),"w") as entity_main_file:
            entity_main_file.write(dumps(entity_main_json, indent=2, ensure_ascii=False))
        with open(join(entity_path, entity_name+"_entries_"+agent_main_lang+".json"),"w") as entity_entries_file:
            entity_entries_file.write(dumps(entity_entries_json, indent=2, ensure_ascii=False))
    return

def create_agent_intents(intents_json, agent, agent_path):
    agent_num = USE_WEB_APP_DIALOG_AGENT_IDS.index(agent)
    agent_main_lang = USE_WEB_APP_DIALOG_AGENT_LANGS[agent_num][0]
    intent_path = join(agent_path, "intents")
    for intent in intents_json:
        intent_name = intent["name"]
        intent_action = intent["action"]
        intent_training_texts = intent["training_texts"]
        fallback = "false" if intent_training_texts else "true"
        intent_responses = "["
        for response in intent["responses"]:
            intent_responses += "\"" + response + "\"" + ","
        intent_responses = intent_responses[:-1] + "]"
        if(len(intent["parameters"])>0):
            intent_parameters = "["
            for param in intent["parameters"]:
                param_name = param["name"]
                param_required = param["required"]
                if param_required:
                    param_required = "true"
                else:
                    param_required = "false"
                param_data_type = param["entity"]
                param_prompts = param["prompts"]
                intent_prompts = "["
                for prompt in param_prompts:
                    intent_prompts += f'\
                    {{\
                    "lang": "{agent_main_lang}",\
                    "value": "{prompt}"\
                    }},'
                intent_prompts = intent_prompts[:-1] + "]"
                intent_parameters += f'\
                {{\
                    "id": "{create_uuidv4()}",\
                    "name": "{param_name}",\
                    "required": {param_required},\
                    "dataType": "@{param_data_type}",\
                    "value": "${param_name}",\
                    "defaultValue": "",\
                    "isList": false,\
                    "prompts": {intent_prompts},\
                    "promptMessages": [],\
                    "noMatchPromptMessages": [],\
                    "noInputPromptMessages": [],\
                    "outputDialogContexts": []\
                }}'
                intent_parameters += ","
            intent_parameters = intent_parameters[:-1] + "]"
        else:
            intent_parameters = "[]"
        intent_main=f'\
            {{\
            "id": "{create_uuidv4()}",\
            "name": "{intent_name}",\
            "auto": true,\
            "contexts": [],\
            "responses": [\
                {{\
                    "resetContexts": false,\
                    "action": "{intent_action}",\
                    "affectedContexts": [],\
                    "parameters": {intent_parameters},\
                    "messages": [\
                        {{\
                            "type": "0",\
                            "title": "",\
                            "textToSpeech": "",\
                            "lang": "{agent_main_lang}",\
                            "speech": {intent_responses},\
                            "condition": ""\
                        }}\
                    ],\
                    "speech": []\
                }}\
            ],\
            "priority": 500000,\
            "webhookUsed": false,\
            "webhookForSlotFilling": false,\
            "fallbackIntent": {fallback},\
            "events": [],\
            "conditionalResponses": [],\
            "condition": "",\
            "conditionalFollowupEvents": []\
            }}'
        intent_main_json = loads(intent_main)
        if intent_training_texts:
            intent_usersays = "["
            for text in intent_training_texts:
                training_text = f'{{\
                "id": "{create_uuidv4()}",\
                "data": [\
                    {{\
                        "text": "{text}",\
                        "userDefined": false\
                    }}\
                ],\
                "isTemplate": false,\
                "count": 0,\
                "lang": "es",\
                "updated": 0\
                }},'
                intent_usersays += training_text
            intent_usersays = intent_usersays[:-1]
            intent_usersays += "]"
            intent_usersays_json = loads(intent_usersays)
        with open(join(intent_path, intent_name+".json"),"w") as intent_main_file:
            intent_main_file.write(dumps(intent_main_json, indent=2, ensure_ascii=False))
        if intent_training_texts:
            with open(join(intent_path, intent_name+"_usersays_"+\
                       USE_WEB_APP_DIALOG_AGENT_LANGS[agent_num][0] + ".json"),"w") as intent_usersays_file:
                intent_usersays_file.write(dumps(intent_usersays_json, indent=2, ensure_ascii=False))