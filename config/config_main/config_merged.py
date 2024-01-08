# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from config.config_main.config_default import *
from config.config_main.config_override import *
from os.path import abspath, dirname
import json

# ---------------------------------
# [!] START MODE
# ---------------------------------
USE_START_MODE = locals().get("START_MODE", 
                                 DEFAULT_START_MODE)

# ---------------------------------
# [!] LOCALE CONFIGURATION
# ---------------------------------
USE_LANGUAGE = locals().get("LANGUAGE", 
                                 DEFAULT_LANGUAGE)

USE_AVAILABLE_LANGUAGES = locals().get("AVAILABLE_LANGUAGES", 
                                       DEFAULT_AVAILABLE_LANGUAGES)
USE_AVAILABLE_LANGUAGES_VERBOSE = locals().get("AVAILABLE_LANGUAGES_VERBOSE", 
                                       DEFAULT_AVAILABLE_LANGUAGES_VERBOSE)

# -------------------------------
# [!] LOGING CONFIGURATION
# -------------------------------
USE_LOGING_ENABLE = locals().get("LOGIN_ENABLE", 
                                 DEFAULT_LOGING_ENABLE)
USE_LOGING_LEVEL = locals().get("LOGING_LEVEL", 
                                DEFAULT_LOGING_LEVEL)
USE_LOGING_FILE_SRC = locals().get("LOGING_FILE_SRC", 
                                   DEFAULT_LOGING_FILE_SRC)
USE_LOGING_FILE_NAME = locals().get("LOGING_FILE_NAME", 
                                    DEFAULT_LOGING_FILE_NAME)

# -------------------------------
# [!] SERVER PORTS CONFIGURATION
# -------------------------------
USE_DB_PORT = locals().get("DB_PORT", 
                           DEFAULT_DB_PORT)
USE_WEB_APP_PORT = locals().get("WEB_APP_PORT", 
                                DEFAULT_WEB_APP_PORT)
USE_TERMINOLOGY_PORT = locals().get("TERMINOLOGY_PORT", 
                                    DEFAULT_TERMINOLOGY_PORT)
USE_WEB_SERVER_PORT = locals().get("WEB_SERVER_PORT", 
                                   DEAFAULT_WEB_SERVER_PORT)


# ---------------------------------
# [!] DATABASE_CONFIGURATION
# ---------------------------------
USE_DB_DUMP_DATA_PATH = locals().get("DB_DUMP_DATA_PATH", 
                                     DEFAULT_DB_DUMP_DATA_PATH)
USE_IMPORT_DATA_PATH = locals().get("IMPORT_DATA_PATH",
                                         DEFAULT_IMPORT_DATA_PATH)
USE_DB_AUTH_PATH = locals().get("DB_AUTH_PATH",
                                         DEFAULT_DB_AUTH_PATH)
USE_DB_DOCKER_NAME = locals().get("DB_DOCKER_NAME",
                                         DEFAULT_DB_DOCKER_NAME)
USE_DB_DOCKER_SAFE_DELETE = locals().get("DB_DOCKER_SAFE_DELETE",
                                         DEFAULT_DB_DOCKER_SAFE_DELETE)
USE_DB_PERSISTENT_MODE = locals().get("DB_PERSISTENT_MODE",
                                      DEFAULT_DB_PERSISTENT_MODE)
USE_DB_NAME = locals().get("DB_NAME",
                           DEFAULT_DB_NAME)
USE_DB_COLLECTIONS = locals().get("DB_COLLECTIONS",
                           DEFAULT_DB_COLLECTIONS)
DEFAULT_FORBIDDEN_USERNAMES = locals().get("FORBIDDEN_USERNAMES",
                                           DEFAULT_FORBIDDEN_USERNAMES)

# ---------------------------------
# [!] WEB_APP_CONFIGURATION
# ---------------------------------
USE_WEB_APP_COLOR_PALETTE = locals().get("WEB_APP_COLOR_PALETTE", 
                                         DEFAULT_WEB_APP_COLOR_PALETTE)
USE_WEB_APP_ANAMNESIS_MODES = locals().get("WEB_APP_ANAMNESIS_MODES", 
                                         DEFAULT_WEB_APP_ANAMNESIS_MODES)
USE_WEB_APP_ANAMNESIS_MODES_ICONS = locals().get("WEB_APP_ANAMNESIS_MODES_ICONS", 
                                         DEFAULT_WEB_APP_ANAMNESIS_MODES_ICONS)


# -------------------------------
# [!] WEB_APP_DIALOG CONFIGURATION
# -------------------------------
USE_SESSIONS_FILES_PATH = locals().get("SESSIONS_FILE_PATH", 
                                        DEFAULT_SESSIONS_FILES_PATH)

USE_WEB_APP_DIALOG_AUDIO_ENCODING = locals().get("WEB_APP_DIALOG_AUDIO_ENCODING", 
                                                 DEFAULT_WEB_APP_DIALOG_AUDIO_ENCODING)
USE_WEB_APP_DIALOG_INPUT_TEXT_NAME = locals().get("WEB_APP_DIALOG_INPUT_TEXT_NAME", 
                                                  DEFAULT_WEB_APP_DIALOG_INPUT_TEXT_NAME)
USE_WEB_APP_DIALOG_INPUT_AUDIO_NAME = locals().get("WEB_APP_DIALOG_INPUT_AUDIO_NAME", 
                                                   DEFAULT_WEB_APP_DIALOG_INPUT_AUDIO_NAME)
USE_WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH = locals().get("WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH", 
                                                         DEFAULT_WEB_APP_DIALOG_OUTPUT_AUDIO_TEMP_PATH)
USE_WEB_APP_DIALOG_NUM_AGENTS=locals().get("WEB_APP_DIALOG_NUM_AGENTS",
                                    DEFAULT_WEB_APP_DIALOG_NUM_AGENTS)
USE_AGENTS_BASE_DATA_PATH=locals().get("AGENTS_BASE_DATA_PATH",
                                       DEFAULT_AGENTS_BASE_DATA_PATH)
USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS = locals().get("GOOGLE_APPLICATION_CREDENTIALS_PATHS",
                                                        DEFAULT_GOOGLE_APPLICATION_CREDENTIALS_PATHS)
USE_GOOGLE_CLOUD_PROJECT_IDS=locals().get("GOOGLE_CLOUD_PROJECT_IDS", 
                                          DEFAULT_GOOGLE_CLOUD_PROJECT_IDS)
USE_WEB_APP_DIALOG_AGENT_IDS=locals().get("WEB_APP_DIALOG_AGENT_IDS",
                                          DEFAULT_WEB_APP_DIALOG_AGENT_IDS)
USE_WEB_APP_DIALOG_AGENT_LANGS = locals().get("WEB_APP_DIALOG_AGENT_LANGS",
                                              DEFAULT_WEB_APP_DIALOG_AGENT_LANGS)
USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS= locals().get("WEB_APP_DIALOG_AGENT_CONFIG_TEXTS",
                                              DEFAULT_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS)
USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS=locals().get("WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS",
                                              DEFAULT_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS)
USE_WEB_APP_DIALOG_ACTIVE_STEP_NAME = locals().get("WEB_APP_DIALOG_ACTIVE_STEP_NAME", 
                                                   DEFAULT_WEB_APP_DIALOG_ACTIVE_STEP_NAME)
USE_WEB_APP_DIALOG_PASIVE_STEP_NAME = locals().get("WEB_APP_DIALOG_PASIVE_STEP_NAME", 
                                                   DEFAULT_WEB_APP_DIALOG_PASIVE_STEP_NAME)
USE_WEB_APP_DIALOG_LANGUAGE_CODES = locals().get("WEB_APP_DIALOG_LANGUAGES_CODE", 
                                                 DEFAULT_WEB_APP_DIALOG_LANGUAGE_CODES)
USE_WEB_APP_DIALOG_TIMEZONE = locals().get("WEB_APP_DIALOG_TIMEZONE",
                                           DEFAULT_WEB_APP_DIALOG_TIMEZONE)
USE_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH = locals().get("WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH",
                                                               DEFAULT_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_BASE_PATH)
USE_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH = locals().get("WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH",
                                                              DEFAULT_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_BASE_PATH)
USE_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME = locals().get("WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME",
                                                                 DEFAULT_WEB_APP_DIALOG_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME)
USE_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES = locals().get("WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES",
                                                         DEFAULT_WEB_APP_DIALOG_AGENT_RESTORE_ZIP_NAMES)
USE_WEB_APP_AGENT_RESET_AFTER_REBOOT = locals().get("WEB_APP_AGENT_RESET_AFTER_REBOOT",
                                                         DEFAULT_WEB_APP_AGENT_RESET_AFTER_REBOOT)

# ---------------------------------
# [!] WEB_APP_EMAIL CONFIGURATION
# ---------------------------------
USE_WEB_APP_EMAIL_AUTH_PATH = locals().get("WEB_APP_EMAIL_AUTH_PATH", 
                                           DEFAULT_WEB_APP_EMAIL_AUTH_PATH)

# ---------------------------------
# [!] WEB_APP_AUTH CONFIGURATION
# ---------------------------------
USE_RESET_SESSIONS_AFTER_REBOOT_ENABLED = locals().get("RESET_SESSIONS_AFTER_REBOOT_ENABLED",
                                               DEFAULT_RESET_SESSIONS_AFTER_REBOOT_ENABLED)
USE_WEB_APP_AUTH_SECRET_KEY_LENGTH = locals().get("WEB_APP_AUTH_SECRET_KEY_LENGTH",
                                               DEFAULT_WEB_APP_AUTH_SECRET_KEY_LENGTH)
USE_WEB_APP_AUTH_SESSION_ENABLED = locals().get("WEB_APP_AUTH_SESSION_ENABLED",
                                               DEFAULT_WEB_APP_AUTH_SESSION_ENABLED )
USE_WEB_APP_AUTH_SESSION_LIFE_MINS = locals().get("WEB_APP_AUTH_SESSION_LIFE_MINS",
                                               DEFAULT_WEB_APP_AUTH_SESSION_LIFE_MINS)
USE_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION = locals().get("WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION",
                                               DEFAULT_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION)

# ---------------------------------
# [!] WEB_APP_REPORT_CONFIGURATION
# ---------------------------------
USE_WEB_APP_REPORTS_PATH = locals().get("WEB_APP_REPORTS_PATH",
                                        DEFAULT_WEB_APP_REPORTS_PATH)