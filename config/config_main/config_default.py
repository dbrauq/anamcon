# ---------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# ---------------------------------

from os.path import abspath, dirname

# ---------------------------------
# default_config.py
# ---------------------------------
# ---------------------------------
# [!] START MODE
# ---------------------------------
DEFAULT_START_MODE = "DOCKER"

# ---------------------------------
# [!] LOCALE CONFIGURATION
# ---------------------------------
DEFAULT_LANGUAGE = "es"
DEFAULT_AVAILABLE_LANGUAGES=["es", "en"]
DEFAULT_AVAILABLE_LANGUAGES_VERBOSE=[["Español", "(España)"], ["English", "(USA)"]]


# ---------------------------------
# [!] LOGING CONFIGURATION
# ---------------------------------
DEFAULT_LOGING_ENABLE = True
DEFAULT_LOGING_LEVEL = "CRITICAL"
DEFAULT_LOGING_FILE_SRC = "/loging"
DEFAULT_LOGING_FILE_NAME = "loging.log"

# ---------------------------------
# [!] SERVER PORTS CONFIGURATION
# ---------------------------------
DEFAULT_DB_PORT = 27017
DEFAULT_WEB_APP_PORT = 5000
DEFAULT_TERMINOLOGY_PORT = 5050
DEAFAULT_WEB_SERVER_PORT = 8081

# ---------------------------------
# [!] DATABASE_CONFIGURATION
# ---------------------------------
DEFAULT_DB_DUMP_DATA_PATH = "path/to/data/dump"
DEFAULT_IMPORT_DATA_PATH = "path/to/import/data/dump"
DEFAULT_DB_AUTH_PATH = "path/to/credentials"
DEFAULT_DB_DOCKER_NAME="anamcon_db"
DEFAULT_DB_DOCKER_SAFE_DELETE = False
DEFAULT_DB_PERSISTENT_MODE = False
DEFAULT_DB_NAME = "anamcon"
DEFAULT_DB_COLLECTIONS = {"users":"users", "anamnesis":"anamnesis", "agents":"agents"}
DEFAULT_FORBIDDEN_USERNAMES = ["none", "admin", "administrator", "administrador", "anamcon"]

# ---------------------------------
# [!] WEB_APP_CONFIGURATION
# ---------------------------------
DEFAULT_SESSIONS_FILES_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/sessions/sessions_files"
DEFAULT_WEB_APP_COLOR_PALETTE = "web_color_palette_1"
DEFAULT_WEB_APP_ANAMNESIS_MODES = ["general", "psico"]
DEFAULT_WEB_APP_ANAMNESIS_MODES_ICONS = ["🗣️ ","🧠"]


# ---------------------------------
# [!] WEB_APP_DIALOG_CONFIGURATION
# ---------------------------------
DEFAULT_WEB_APP_DIALOG_AUDIO_ENCODING = "dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16"
DEFAULT_WEB_APP_DIALOG_INPUT_TEXT_NAME = "text"
DEFAULT_WEB_APP_DIALOG_INPUT_AUDIO_NAME = "audio"
DEFAULT_WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/sessions/audio/"
DEFAULT_AGENTS_BASE_DATA_PATH = "path/to/agents_base_data_path"
DEFAULT_GOOGLE_APPLICATION_CREDENTIALS_PATHS = ["path/to/credentials_agent_1_file.json", 
                                               "path/to/credentials_agent_2_file.json"]
DEFAULT_GOOGLE_CLOUD_PROJECT_IDS = ["google_cloud_project_id_1", 
                                    "google_cloud_project_id_2"]
DEFAULT_WEB_APP_DIALOG_NUM_AGENTS = 2
DEFAULT_WEB_APP_DIALOG_AGENT_IDS = ["agent_1_id",
                                    "agent_2_id"]
DEFAULT_WEB_APP_DIALOG_AGENT_LANGS=[["es"],
                                    ["es"]]
DEFAULT_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS=["$__intro","$__continue","$__end","$__yes"]
DEFAULT_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS=["$__assisted"]
DEFAULT_WEB_APP_DIALOG_ACTIVE_STEP_NAME = "Active"
DEFAULT_WEB_APP_DIALOG_PASIVE_STEP_NAME = "Pasive"
DEFAULT_WEB_APP_DIALOG_LANGUAGE_CODES = ["es-ES"]
DEFAULT_WEB_APP_DIALOG_TIMEZONE = "Europe/Madrid"
DEFAULT_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/dialog/agents_zip"
DEFAULT_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/dialog/agents_zip"
DEFAULT_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME="download"
DEFAULT_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES = [DEFAULT_WEB_APP_DIALOG_AGENT_IDS[0] + ".zip",
                                                 DEFAULT_WEB_APP_DIALOG_AGENT_IDS[1] + ".zip"]
DEFAULT_WEB_APP_AGENT_RESET_AFTER_REBOOT = True


# ---------------------------------
# [!] WEB_APP_EMAIL_CONFIGURATION
# ---------------------------------
DEFAULT_WEB_APP_EMAIL_AUTH_PATH = "path/to/credentials"


# ---------------------------------
# [!] WEB_APP_AUTH_CONFIGURATION
# ---------------------------------
DEFAULT_RESET_SESSIONS_AFTER_REBOOT_ENABLED = True
DEFAULT_WEB_APP_AUTH_SECRET_KEY_LENGTH = 256
DEFAULT_WEB_APP_AUTH_SESSION_ENABLED = True
DEFAULT_WEB_APP_AUTH_SESSION_LIFE_MINS = 43200
DEFAULT_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION = True

# ---------------------------------
# [!] WEB_APP_REPORT_CONFIGURATION
# ---------------------------------
DEFAULT_WEB_APP_REPORTS_PATH = dirname(dirname(dirname(abspath(__file__))))+"/src/web_app/report/generated_reports"

