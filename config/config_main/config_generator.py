# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from json import loads
from config.config_main.config_merged import *
from os.path import (abspath, 
                     dirname)

from re import *

def title():
    title = f"\
# -------------------------------\n\
# This file is part of AnamCon\n\
# by David Brau Queralt\n\
# -------------------------------\n\n\
"
    return title

def set_db_config():
    db_config_text = f"\
{title()}\
USE_DB_PORT=\"{USE_DB_PORT}\"\n\
USE_DUMP_DATA_PATH=\"{USE_DB_DUMP_DATA_PATH}\"\n\
USE_IMPORT_DATA_PATH=\"{USE_IMPORT_DATA_PATH}\"\n\
USE_DB_DOCKER_NAME=\"{USE_DB_DOCKER_NAME}\"\n\
USE_DB_AUTH_PATH=\"{USE_DB_AUTH_PATH}\"\n\
USE_DB_DOCKER_SAFE_DELETE={USE_DB_DOCKER_SAFE_DELETE}\n\
USE_DB_PERSISTENT_MODE={USE_DB_PERSISTENT_MODE}\n\
USE_DB_NAME=\"{USE_DB_NAME}\"\n\
USE_DB_COLLECTIONS={USE_DB_COLLECTIONS}\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/db_server/config_db.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(db_config_text)


def set_web_app_config():
    web_app_config_text = f"\
{title()}\
USE_LANGUAGE=\"{USE_LANGUAGE}\"\n\
USE_DB_PORT=\"{USE_DB_PORT}\"\n\
USE_WEB_APP_PORT=\"{USE_WEB_APP_PORT}\"\n\
USE_TERMINOLOGY_PORT=\"{USE_TERMINOLOGY_PORT}\"\n\
USE_WEB_SERVER_PORT=\"{USE_WEB_SERVER_PORT}\"\n\
USE_WEB_APP_AUTH_SESSION_LIFE_MINS={USE_WEB_APP_AUTH_SESSION_LIFE_MINS}\n\
USE_WEB_APP_COLOR_PALETTE=\"{USE_WEB_APP_COLOR_PALETTE}\"\n\
USE_SESSIONS_FILES_PATH=\"{USE_SESSIONS_FILES_PATH}\"\n\
USE_OUTPUT_AUDIO_TEMP_PATH=\"{USE_WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH}\"\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/config_web_app.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(web_app_config_text)


def set_web_app_db_models_config():
    web_app_db_models_text = f"\
{title()}\
USE_DB_PORT=\"{USE_DB_PORT}\"\n\
USE_DB_NAME=\"{USE_DB_NAME}\"\n\
USE_DB_COLLECTIONS={USE_DB_COLLECTIONS}\n\
USE_FORBIDDEN_USERNAMES={DEFAULT_FORBIDDEN_USERNAMES}\n\
USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS={USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS}\n\
USE_START_MODE=\"{USE_START_MODE}\"\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/db_models/config_models.py", "w") as web_app_db_models_config:
        web_app_db_models_config.write(web_app_db_models_text)


def set_web_app_dialog_config():
    web_app_dialog_config_text = f"\
{title()}\
# MANUALLY MODIFYING THIS FILE IS DISCOURAGED\n\
# TRY TO MODIFY THE MAIN CONFIG FILE INSTEAD (ON ANAMCON/CONFIG_OVERRIDE)\n\n\
from google.cloud import dialogflow\n\n\
USE_INPUT_AUDIO_ENCODING={USE_WEB_APP_DIALOG_AUDIO_ENCODING}\n\
USE_INPUT_TEXT_NAME=\"{USE_WEB_APP_DIALOG_INPUT_TEXT_NAME}\"\n\
USE_INPUT_AUDIO_NAME=\"{USE_WEB_APP_DIALOG_INPUT_AUDIO_NAME}\"\n\
USE_OUTPUT_AUDIO_TEMP_PATH=\"{USE_WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH}\"\n\
USE_NUM_AGENTS=\"{USE_WEB_APP_DIALOG_NUM_AGENTS}\"\n\
USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS={USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS}\n\
USE_GOOGLE_CLOUD_PROJECT_IDS={USE_GOOGLE_CLOUD_PROJECT_IDS}\n\
USE_AGENT_IDS={USE_WEB_APP_DIALOG_AGENT_IDS}\n\
USE_ACTIVE_STEP_NAME=\"{USE_WEB_APP_DIALOG_ACTIVE_STEP_NAME}\"\n\
USE_PASIVE_STEP_NAME=\"{USE_WEB_APP_DIALOG_PASIVE_STEP_NAME}\"\n\
USE_TIMEZONE=\"{USE_WEB_APP_DIALOG_TIMEZONE}\"\n\
USE_LANGUAGE_CODES={USE_WEB_APP_DIALOG_LANGUAGE_CODES}\n\
USE_AGENT_DOWNLOAD_ZIP_BASE_PATH=\"{USE_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH}\"\n\
USE_AGENT_RESTORE_ZIP_BASE_PATH=\"{USE_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH}\"\n\
USE_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME=\"{USE_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME}\"\n\
USE_AGENT_RESTORE_ZIP_NAMES={USE_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES}\n\
USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS={USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS}\n\
USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS={USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS}\n\
USE_WEB_APP_AGENT_RESET_AFTER_REBOOT={USE_WEB_APP_AGENT_RESET_AFTER_REBOOT}\n\
USE_START_MODE=\"{USE_START_MODE}\"\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/dialog/config_dialog.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(web_app_dialog_config_text)    

def set_web_app_email_config():
    web_app_email_text = f"\
{title()}\
USE_EMAIL_AUTH_PATH=\"{USE_WEB_APP_EMAIL_AUTH_PATH}\"\n\
USE_START_MODE=\"{USE_START_MODE}\"\n\
"   
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/net/config_email.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(web_app_email_text)

def set_web_app_auth_config():
    web_app_auth_text = f"\
{title()}\
USE_WEB_APP_AUTH_SECRET_KEY_LENGTH={USE_WEB_APP_AUTH_SECRET_KEY_LENGTH}\n\
USE_AVAILABLE_LANGUAGES={USE_AVAILABLE_LANGUAGES}\n\
USE_AVAILABLE_LANGUAGES_VERBOSE={USE_AVAILABLE_LANGUAGES_VERBOSE}\n\
USE_LANGUAGE =\"{USE_LANGUAGE}\"\n\
USE_AUTH_SESSION_ENABLED=\"{USE_WEB_APP_AUTH_SESSION_ENABLED}\"\n\
USE_SESSION_LIFE_MINS={USE_WEB_APP_AUTH_SESSION_LIFE_MINS}\n\
USE_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION={USE_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION}\n\
"   
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/auth/config_auth.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(web_app_auth_text)

def set_web_app_anamnesis_config():
    web_app_anamnesis_config = f"\
{title()}\
USE_AVAILABLE_ANAMNESIS_MODES={USE_WEB_APP_ANAMNESIS_MODES}\n\
USE_AGENT_IDS={USE_WEB_APP_DIALOG_AGENT_IDS}\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/anamnesis/config_anamnesis.py", "w") as web_app_anamnesis_config_file:
        web_app_anamnesis_config_file.write(web_app_anamnesis_config)

def set_web_app_report_config():
    web_app_report_config = f"\
{title()}\
USE_WEB_APP_REPORTS_PATH=\"{USE_WEB_APP_REPORTS_PATH}\"\n\
USE_START_MODE=\"{USE_START_MODE}\"\n\
"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/report/config_report.py", "w") as web_app_report_config_file:
        web_app_report_config_file.write(web_app_report_config)

def set_web_texts():
    set_web_anamnesis_texts()
    set_web_auth_texts()
    set_web_emails_texts()

def set_web_anamnesis_texts():
    web_app_views_main_data=f"\
{title()}\n\
USE_AVAILABLE_LANGUAGES={USE_AVAILABLE_LANGUAGES}\n\
USE_AVAILABLE_LANGUAGES_VERBOSE={USE_AVAILABLE_LANGUAGES_VERBOSE}\n\
USE_AVAILABLE_ANAMNESIS_MODES={USE_WEB_APP_ANAMNESIS_MODES}\n\
USE_AVAILABLE_ANAMNESIS_MODES_ICONS={USE_WEB_APP_ANAMNESIS_MODES_ICONS}\n\
"
    for lang in USE_AVAILABLE_LANGUAGES:
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                f"/config/config_main/web_texts/web_texts_{lang}.json","r") as web_texts_file:
            web_texts_json = web_texts_file.read()
        main_dic = loads(web_texts_json)["anamnesis"]
        lang_variable_main = f"USE_ANAMNESIS_TEXTS_{lang.upper()}"
        web_app_views_main_data += f"{lang_variable_main}={main_dic}\n"
    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/views/main/main_data.py", "w") as web_app_main_config:
        web_app_main_config.write(web_app_views_main_data)

def set_web_auth_texts():
    web_app_views_auth_data=f"\
{title()}\n\
USE_AVAILABLE_LANGUAGES={USE_AVAILABLE_LANGUAGES}\n\
USE_AVAILABLE_LANGUAGES_VERBOSE={USE_AVAILABLE_LANGUAGES_VERBOSE}\n\
"
    for lang in USE_AVAILABLE_LANGUAGES:
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                f"/config/config_main/web_texts/web_texts_{lang}.json","r") as web_texts_file:
            web_texts_json = web_texts_file.read()
        login_dic = loads(web_texts_json)["login"]
        lang_variable_login = f"USE_LOGIN_TEXTS_{lang.upper()}"
        web_app_views_auth_data += f"{lang_variable_login}={login_dic}\n"
        register_dic = loads(web_texts_json)["register"]
        lang_variable_register = f"USE_REGISTER_TEXTS_{lang.upper()}"
        web_app_views_auth_data += f"{lang_variable_register}={register_dic}\n"
        register_success_dic = loads(web_texts_json)["register_success"]
        lang_variable_register = f"USE_REGISTER_SUCCESS_TEXTS_{lang.upper()}"
        web_app_views_auth_data += f"{lang_variable_register}={register_success_dic}\n"
        terms_dic = loads(web_texts_json)["terms"]
        lang_variable_register = f"USE_TERMS_TEXTS_{lang.upper()}"
        web_app_views_auth_data += f"{lang_variable_register}={terms_dic}\n"

    with open(dirname(dirname(dirname(abspath(__file__))))+\
              "/src/web_app/views/auth/auth_data.py", "w") as web_app_dialog_config:
        web_app_dialog_config.write(web_app_views_auth_data)

def set_web_emails_texts():
    emails_data=f"\
{title()}\n\
USE_AVAILABLE_LANGUAGES={USE_AVAILABLE_LANGUAGES}\n\
"
    for lang in USE_AVAILABLE_LANGUAGES:
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                f"/config/config_main/web_emails/web_emails_texts_{lang}.json","r") as web_emails_texts_file:
                    web_emails_texts_json = web_emails_texts_file.read()
                    wellcome_email_dic = loads(web_emails_texts_json)["wellcome"]
                    lang_variable_wellcome = f"USE_WELLCOME_TEXTS_{lang.upper()}"
                    emails_data += f"{lang_variable_wellcome}={wellcome_email_dic}\n"
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                f"/config/config_main/web_emails/templates/wellcome_email.html","r") as wellcome_html_email_file:
                    wellcome_html_email = wellcome_html_email_file.read()
                    for (key, variable) in wellcome_email_dic.items():
                         wellcome_html_email = wellcome_html_email.replace(f"#{key}",variable)
        with open(dirname(dirname(dirname(abspath(__file__))))+\
              f"/src/web_app/net/email_templates/wellcome_email_{lang}.html", "w") as wellcome_html_email_file_lang:
                    wellcome_html_email_file_lang.write(wellcome_html_email)

def set_web_colors():
    style_routes = [
        "/src/web_app/views/auth/static/css/styles_base.css",
        "/src/web_app/views/auth/static/css/styles_login.css",
        "/src/web_app/views/auth/static/css/styles_register.css"
    ]
    for style_route in style_routes:
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                "/config/config_main/web_colors/web_color_palette_1.json","r") as web_colors_file:
            web_colors_json = web_colors_file.read()
        colors_dic = loads(web_colors_json)
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
            style_route,"r+") as style_file:
            style_text = style_file.read()
            for color_num in range(len(colors_dic)):
                color = colors_dic[f"color_{color_num}"]
                reg_ex = rf"/\*cs_{color_num}\*/.*?/\*ce_{color_num}\*/;"
                style_text = sub(reg_ex, f"/*cs_{color_num}*/{color}/*ce_{color_num}*/;",
                                  style_text, count=0)
        with open((dirname(dirname(dirname(abspath(__file__)))))+\
                style_route,"w") as style_file:       
            style_file.write(style_text)
