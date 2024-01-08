# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from google.cloud.dialogflow_v2 import (Agent, 
                                        AgentsClient, 
                                        SetAgentRequest, 
                                        RestoreAgentRequest, 
                                        DeleteAgentRequest, 
                                        ExportAgentRequest)
from os import environ
from dialog.config_dialog import (USE_GOOGLE_CLOUD_PROJECT_IDS, 
                           USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS,
                           USE_AGENT_IDS,
                           USE_AGENT_RESTORE_ZIP_BASE_PATH,
                           USE_AGENT_RESTORE_ZIP_NAMES,
                           USE_AGENT_DOWNLOAD_ZIP_BASE_PATH,
                           USE_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME,
                           USE_LANGUAGE_CODES,
                           USE_TIMEZONE,
                           USE_START_MODE)
from time import time
from os.path import dirname, abspath


class Dialog_Agent:
    def __init__(self, agent_id=USE_AGENT_IDS[0]):
        self._agent_num = USE_AGENT_IDS.index(agent_id)
        if USE_START_MODE == "DOCKER":
            environ["GOOGLE_APPLICATION_CREDENTIALS"] = dirname(dirname(abspath(__file__))) + "/secure/"+\
                  USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS[self._agent_num].split("/")[-1]
        if USE_START_MODE == "MANUAL":
            environ["GOOGLE_APPLICATION_CREDENTIALS"] = USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS[self._agent_num]
        self._agent_client = AgentsClient()
        self._project_id = USE_GOOGLE_CLOUD_PROJECT_IDS[self._agent_num]
        self._parent_path = self._agent_client.common_project_path(self._project_id)
   
    def _get_agent_num(self):
        return self._agent_num

    def _get_agent_client(self):
        return self._agent_client
    
    def _get_parent_path(self):
        return self._parent_path
    
    def _get_agent(self):
        agent = self._agent_client.get_agent(parent=self._parent_path)
        return agent
        
    def exists(self):
        try:
            self._get_agent()
            return True
        except Exception as error:
            error_message = str(error)
            if f"No DesignTimeAgent found for project \'{USE_GOOGLE_CLOUD_PROJECT_IDS[self._get_agent_num()]}\'" in error_message:
                return False
            else:
                raise ConnectionError(f"Unable to perform has_agent validation of project: \
                                      {USE_GOOGLE_CLOUD_PROJECT_IDS[self._get_agent_num()]}.\
                                      Verify internet connection")

    def get_name(self):
        return self._get_agent().display_name
    
    def create(self):
        agent = Agent(
            parent=self._parent_path,
            display_name=USE_AGENT_IDS[self._get_agent_num()],
            default_language_code=USE_LANGUAGE_CODES[0],
            time_zone=USE_TIMEZONE,
        )
        request = SetAgentRequest(
            agent=agent,
        )
        self._agent_client.set_agent(request=request)
     
    def restore(self, zip_path=None):
        if zip_path == None:
            if USE_START_MODE == "DOCKER":
                zip_path= dirname(dirname(abspath(__file__)))+"/dialog/agents_zip/"+f"{USE_AGENT_RESTORE_ZIP_NAMES[self._get_agent_num()]}"
            if USE_START_MODE == "MANUAL":
                zip_path=f"{USE_AGENT_RESTORE_ZIP_BASE_PATH}/{USE_AGENT_RESTORE_ZIP_NAMES[self._get_agent_num()]}"
        with open(zip_path, 'rb') as agent_zip:
            agent_content = agent_zip.read()
        request_content = RestoreAgentRequest(
            parent=self._parent_path,
            agent_content=agent_content
        )
        self._agent_client.restore_agent(request=request_content)
        
    def download(self, zip_path=None):
        if zip_path == None:
            zip_path=USE_AGENT_DOWNLOAD_ZIP_BASE_PATH
        request_content = ExportAgentRequest(parent=self._parent_path)
        agent = self._agent_client.export_agent(request=request_content).result().agent_content
        zip_file_path = f"{zip_path}/{self.get_name()}_{USE_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME}_{round(time())}.zip"
        with open(zip_file_path,"wb") as zip_file:
            zip_file.write(agent)

    def delete(self):
        request_content = DeleteAgentRequest(
            parent=self._parent_path,
        )
        self._agent_client.delete_agent(request=request_content)
