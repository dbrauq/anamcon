# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from flask import Flask
from flask_session import Session
from config_web_app import *
from views.main.main_routes import main_blueprint
from views.auth.auth_routes import auth_blueprint
from auth.identifier import create_web_app_secret_key
from os.path import dirname, abspath
from datetime import timedelta

from dialog.config_dialog import USE_WEB_APP_AGENT_RESET_AFTER_REBOOT,USE_AGENT_IDS
from dialog.agent_manager import *


class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__, 
                        template_folder="", 
                        static_folder="")
        self.app.register_blueprint(main_blueprint)
        self.app.register_blueprint(auth_blueprint)
        self.app.config["SESSION_PERMANENT"] = True
        self.app.config['ERROR_404_HELP'] = False
        self.app.config["SESSION_TYPE"] = "filesystem"
        self.app.config["SESSION_FILE_DIR"] = USE_SESSIONS_FILES_PATH
        self.app.config["PERMANENT_SESSION_LIFETIME"] =\
              timedelta(seconds=USE_WEB_APP_AUTH_SESSION_LIFE_MINS)
        secret_key = create_web_app_secret_key()
        self.app.secret_key = secret_key
        Session(self.app)

    def run(self, port):
        self.app.run(port=port, host="0.0.0.0")

if __name__ == "__main__":
    if USE_WEB_APP_AGENT_RESET_AFTER_REBOOT:
        for agent in USE_AGENT_IDS:
            dialog_agent = Dialog_Agent(agent).restore()
            print("[!] Agent " + agent + " has been restored")
    web_app = FlaskApp()
    web_app.run(USE_WEB_APP_PORT)