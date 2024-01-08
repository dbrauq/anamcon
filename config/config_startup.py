# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from config.config_anamnesis.anamnesis_generator import *
from config.config_main.config_generator import *


def set_main_config():
    set_db_config()
    set_web_app_config()
    set_web_app_db_models_config()
    set_web_app_anamnesis_config()
    set_web_app_dialog_config()
    set_web_app_email_config()
    set_web_app_auth_config()
    set_web_app_report_config()
    set_web_texts()
    set_web_colors()

def set_anamnesis_config():
    create_agents_files()
    create_agents_zip_files()
    update_web_app_agents()

def load_agents():
    db_load_agents()