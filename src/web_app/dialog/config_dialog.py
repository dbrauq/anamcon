# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

# MANUALLY MODIFYING THIS FILE IS DISCOURAGED
# TRY TO MODIFY THE MAIN CONFIG FILE INSTEAD (ON ANAMCON/CONFIG_OVERRIDE)

from google.cloud import dialogflow

USE_INPUT_AUDIO_ENCODING=dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16
USE_INPUT_TEXT_NAME="text"
USE_INPUT_AUDIO_NAME="audio"
USE_OUTPUT_AUDIO_TEMP_PATH="/home/brautu/Desktop/anamcon/src/web_app/sessions/audio/"
USE_NUM_AGENTS="2"
USE_GOOGLE_APPLICATION_CREDENTIALS_PATHS=['/home/brautu/Desktop/Secure/anamcon-dialogflow-5d7dc4a25ca9.json', '/home/brautu/Desktop/Secure/anamcon-dialogflow-v2-0216d384d28c.json']
USE_GOOGLE_CLOUD_PROJECT_IDS=['anamcon-dialogflow', 'anamcon-dialogflow-v2']
USE_AGENT_IDS=['Anam', 'Anam2']
USE_ACTIVE_STEP_NAME="Active"
USE_PASIVE_STEP_NAME="Pasive"
USE_TIMEZONE="Europe/Madrid"
USE_LANGUAGE_CODES=['es-ES']
USE_AGENT_DOWNLOAD_ZIP_BASE_PATH="/home/brautu/Desktop/anamcon/src/web_app/dialog/agents_zip"
USE_AGENT_RESTORE_ZIP_BASE_PATH="/home/brautu/Desktop/anamcon/src/web_app/dialog/agents_zip"
USE_AGENT_DOWNLOAD_ZIP_MIDDLE_NAME="download"
USE_AGENT_RESTORE_ZIP_NAMES=['Anam.zip', 'Anam2.zip']
USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS=['$__intro', '$__continue', '$__end', '$__yes']
USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS=['$__assisted']
USE_WEB_APP_AGENT_RESET_AFTER_REBOOT=True
USE_START_MODE="DOCKER"
