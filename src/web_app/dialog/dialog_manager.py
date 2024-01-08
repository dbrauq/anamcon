# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------


from google.cloud import dialogflow
from dialog.config_dialog import (USE_INPUT_AUDIO_ENCODING,
                                  USE_OUTPUT_AUDIO_TEMP_PATH,
                                  USE_AGENT_IDS,
                                  USE_LANGUAGE_CODES,
                                  USE_GOOGLE_CLOUD_PROJECT_IDS,
                                  USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS,
                                  USE_START_MODE)
from re import search
from os import environ
from os.path import dirname, abspath
from abc import ABC, abstractmethod


class _Interaction(ABC):
    def __init__(self, input, session_id, agent_id, agent_num, project_id, language_code):
        super().__init__()
        self._input = input
        self._session_id = session_id
        self._agent_id = agent_id
        self._agent_num = agent_num
        self._project_id = project_id
        self._language_code = language_code
        self._audio_encoding = USE_INPUT_AUDIO_ENCODING
        self.response = None

    def _get_input(self):
        return self._input

    def _get_session_id(self):
        return self._session_id

    def _get_agent_id(self):
        return self._agent_id

    def _get_agent_num(self):
        return self._agent_num

    def _get_project_id(self):
        return self._project_id

    def _get_language_code(self):
        return self._language_code

    def _get_audio_encoding(self):
        return self._audio_encoding
    
    def _get_response(self):
        return self._response
    
    def get_response_text(self):
        return self._get_response().query_result.fulfillment_text
    
    def get_response_audio(self):
        return self._get_response().output_audio
    
    def save_audio_response(self,path=(dirname(dirname(abspath(__file__)))) + "/sessions/audio/" + "temp_audio.wav"):
        audio = self.get_response_audio()
        with open(path, "wb") as audio_file:
            audio_file.write(audio)
    
    def _get_response_audio_config(self):
        return self._get_response().output_audio_config
    
    def get_response_audio_encoding(self):
        return str(self._get_response_audio_config().audio_encoding).split(".")[1]
    
    def get_response_audio_speaking_rate(self):
        return self._get_response_audio_config().synthesize_speech_config.speaking_rate

    def get_query_text(self):
        return self._get_response().query_result.query_text
    
    def get_intent_name(self):
        return self._get_response().query_result.intent.display_name
    
    def get_intent_confidence(self):
        return self._get_response().query_result.intent_detection_confidence

    def get_intent_parameters_and_values(self):
        parameters={}
        parameter_names = [param for param in self._get_response().query_result.parameters]
        parameter_values = [value for value in self._get_response().query_result.parameters.values()]
        for i in range(len(parameter_names)):
            if str(type(parameter_values[i])) == "<class 'proto.marshal.collections.maps.MapComposite'>":
                parameter_values[i] = list(parameter_values[i].items())[0][1]
            parameters[parameter_names[i]]=parameter_values[i]   
        return parameters
    
    def get_intern_parameter_names(self):
        return list(self.get_intent_parameters_and_values().keys())
    
    def get_intent_parameter_values(self):
        return list(self.get_intent_parameters_and_values().values())
    
    def all_requierd_params_present(self):
        return self._get_response().query_result.all_required_params_present
    
    def get_input_sentiment_analysis(self):
        sentiment = str(self._get_response().query_result.sentiment_analysis_result)
        if ("score" in sentiment) and ("magnitude" in sentiment):
            sentiment_type = float(search(r"score.*\n",sentiment).group().split(": ")[1])
            sentiment_intensity = float(search(r"magnitude.*\n",sentiment).group().split(": ")[1])
            return [sentiment_type,sentiment_intensity]
        else:
            return [0,0]
    
    def get_input_sentiment_type(self):
        return self.get_input_sentiment_analysis()[0]
    
    def get_input_sentiment_intensity(self):
        return self.get_input_sentiment_analysis()[1]
    
    @abstractmethod
    def save(self):
        return

class Text_Interaction(_Interaction):
    def __init__(self, text_input, session_id, agent_id, agent_num, project_id, language_code):
        super().__init__(text_input, session_id, agent_id, agent_num, project_id, language_code)
        session_client= dialogflow.SessionsClient()
        session = session_client.session_path(self._get_project_id(), self._get_session_id())
        input_text = dialogflow.TextInput(text=self._input, language_code=self._get_language_code())
        query_input = dialogflow.QueryInput(text=input_text)
        request = dialogflow.DetectIntentRequest(session=session, query_input=query_input)
        self._response = session_client.detect_intent(request=request)
    
    def save(self):
        return


class Audio__Interaction(_Interaction):
    def __init__(self, audio_input, session_id, agent_id, agent_num, project_id, language_code, direct_input = True):
        super().__init__(audio_input, session_id, agent_id, agent_num, project_id, language_code)
        self._audio_encoding = USE_INPUT_AUDIO_ENCODING
        session_client= dialogflow.SessionsClient()
        session = session_client.session_path(self._get_project_id(), self._get_session_id())
        if direct_input:
            input_audio = audio_input
        else:
            with open(self._input, "rb") as audio_file:
                input_audio = audio_file.read()
        audio_config = dialogflow.InputAudioConfig(audio_encoding=self._get_audio_encoding(),language_code=self._get_language_code())
        query_input = dialogflow.QueryInput(audio_config=audio_config)
        request = dialogflow.DetectIntentRequest(session=session,query_input=query_input,input_audio=input_audio)
        self._response = session_client.detect_intent(request=request)                   
    
    def get_speech_recognition_confidence(self):
        return self._get_response().query_result.speech_recognition_confidence
    
    def save(self):
        return
    

class Dialog_Session:
    def __init__(self, session_id, agent_id=USE_AGENT_IDS[0], language_code=USE_LANGUAGE_CODES[0]):
        self.session_id = session_id
        self._agent_id = agent_id
        self._agent_num = USE_AGENT_IDS.index(agent_id)
        self._project_id = USE_GOOGLE_CLOUD_PROJECT_IDS[self._agent_num]
        self._language_code = language_code
        if USE_START_MODE == "DOCKER":
            environ["GOOGLE_APPLICATION_CREDENTIALS"] = dirname(dirname(abspath(__file__))) + "/secure/"+\
                  USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS[self._agent_num].split("/")[-1]
        if USE_START_MODE == "MANUAL":
            environ["GOOGLE_APPLICATION_CREDENTIALS"] = USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS[self._agent_num]
        return
    
    def _get_project_id(self):
        return self._project_id
    
    def _get_session_id(self):
        return self.session_id
    
    def _get_language_code(self):
        return self._language_code
    
    def speech_interaction(self, audio_input_path, direct_input = True):
        _interaction = Audio__Interaction(audio_input_path, self.session_id, self._agent_id, 
                                          self._agent_num, self._project_id, self._language_code, direct_input=direct_input)
        _interaction.save()
        return _interaction

    def text_interaction(self, text_input):
        _interaction = Text_Interaction(text_input, self.session_id, self._agent_id, self._agent_num, 
                                        self._project_id, self._language_code)
        _interaction.save()
        return _interaction
        
    def save(self):
        return None

#test_audio_example
#Dialog_Session("3262178461871").text_interaction("Cuentame un chiste").save_audio_response()