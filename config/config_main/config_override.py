# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from os.path import abspath, dirname

# ---------------------------------
# [!] START MODE
# ---------------------------------
START_MODE = "DOCKER"

# ---------------------------------
# [!] LOCALE CONFIGURATION
# ---------------------------------
#LANGUAGE = "es"
#AVAILABLE_LANGUAGES_VERBOSE=[["Español", "(España)"], ["English", "(USA)"]]


# -------------------------------
# [!] LOGGING CONFIGURATION
# -------------------------------
#LOGING_ENABLE = False
# Set loging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
#LOGING_LEVEL = "CRITICAL"
#LOGING_FILE_SRC = "/logging"
#LOGING_FILE_NAME = "logging.log"

# -------------------------------
# [!] SERVER PORTS CONFIGURATION
# -------------------------------
#DB_PORT = 27017
#WEB_APP_PORT = 5000
#TERMINOLOGY_PORT = 5001
#WEB_SERVER_PORT = 8080


# ---------------------------------
# [!] DATABASE_CONFIGURATION
# ---------------------------------
DB_DUMP_DATA_PATH = "/home/brautu/Desktop/DB"
IMPORT_DATA_PATH = "/home/brautu/Desktop/DB"
DB_AUTH_PATH = "/home/brautu/Desktop/Secure/anamcon-docker.json"
#DB_DOCKER_NAME="anamcon_db"
#DB_DOCKER_SAFE_DELETE=False
#DEFAULT_DB_PERSISTENT_MODE = False
#DB_NAME = "anamcon"
#DEFAULT_DB_COLLECTIONS = {"users":"users", "anamnesis":"anamnesis", "agents":"agents"}
#FORBIDDEN_USERNAMES = ["none", "admin", "administrator", "administrador", "anamcon"]


# ---------------------------------
# [!] WEB_APP_CONFIGURATION
# ---------------------------------
#WEB_APP_COLOR_PALETTE = "web_color_palette_1"
#WEB_APP_ANAMNESIS_MODES = ["general", "psico"]
#WEB_APP_ANAMNESIS_MODES_ICONS = ["🗣️ ","🧠"]


# -------------------------------
# [!] WEB_APP_DIALOG CONFIGURATION
# -------------------------------
#SESSIONS_FILES_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/sessions/sessions_files"
#WEB_APP_DIALOG_AUDIO_ENCODING = "dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16"
#WEB_APP_DIALOG_INPUT_TEXT_NAME = "text"
#WEB_APP_DIALOG_INPUT_AUDIO_NAME = "audio"
#WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/dialog/temp/temp_audio.wav"
WEB_APP_DIALOG_NUM_AGENTS = 2
AGENTS_BASE_DATA_PATH="/home/brautu/Desktop/Secure/agents"
GOOGLE_APPLICATION_CREDENTIALS_PATHS = ["/home/brautu/Desktop/Secure/anamcon-dialogflow-5d7dc4a25ca9.json", 
                                       "/home/brautu/Desktop/Secure/anamcon-dialogflow-v2-0216d384d28c.json"]
GOOGLE_CLOUD_PROJECT_IDS = ["anamcon-dialogflow", 
                            "anamcon-dialogflow-v2"]
WEB_APP_DIALOG_AGENT_IDS = ["Anam",
                            "Anam2"]
#WEB_APP_DIALOG_AGENT_LANGS=[["es"],
#                            ["es"]]
#WEB_APP_DIALOG_AGENT_CONFIG_TEXTS=["$__intro","$__continue","$__end"]
#WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS=["$__assisted"]

#WEB_APP_DIALOG_ACTIVE_STEP_NAME = "Active"
#WEB_APP_DIALOG_PASIVE_STEP_NAME = "Pasive"
#WEB_APP_DIALOG_LANGUAGE_CODES = ["es-ES"]
#WEB_APP_DIALOG_TIMEZONE = "Europe/Madrid"
#WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/dialog/agent_zip"
#WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/dialog/agent_zip"
#WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME="download"
WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES = [WEB_APP_DIALOG_AGENT_IDS[0] + ".zip",
                                          WEB_APP_DIALOG_AGENT_IDS[1] + ".zip"]
WEB_APP_AGENT_RESET_AFTER_REBOOT = True

# ---------------------------------
# [!] WEB_APP_EMAIL CONFIGURATION
# ---------------------------------
WEB_APP_EMAIL_AUTH_PATH = "/home/brautu/Desktop/Secure/anamcon-dialogflow-email.json"

# ---------------------------------
# [!] WEB_APP_AUTH CONFIGURATION
# ---------------------------------
RESET_SESSIONS_AFTER_REBOOT_ENABLED = False
#WEB_APP_AUTH_SECRET_KEY_LENGTH = 256
#WEB_APP_AUTH_SESSION_ENABLED = True
#WEB_APP_AUTH_SESSION_LIFE_MINS = 43200
#WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION = True

# ---------------------------------
# [!] WEB_APP_REPORT_CONFIGURATION
# ---------------------------------
#WEB_APP_REPORTS_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/report/generated_reports"


