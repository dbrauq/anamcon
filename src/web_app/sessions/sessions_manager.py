# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from src.web_app.config_web_app import *
from os.path import dirname, abspath, isfile, isdir, join
from os import listdir, remove, rmdir

def delete_sessions():
    delete_folder_content(USE_SESSIONS_FILES_PATH)
    delete_folder_content(USE_OUTPUT_AUDIO_TEMP_PATH)
    return

def delete_folder_content(folder):
    for path in listdir(folder):
        abs_path = join(folder, path)
        if isfile(abs_path): remove(abs_path)
        elif isdir(abs_path):
            delete_folder_content(abs_path)
            rmdir(abs_path)