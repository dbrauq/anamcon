# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from db_models.auth_models import *
from auth.config_auth import *
from net.emails import *
from datetime import datetime
from os.path import dirname, abspath, isfile, join
from os import listdir, remove

def auth_clean_session_files(path = dirname(dirname(abspath(__file__)))+"/sessions"):
     for file in listdir(path):
          file_path = join(path, file)
          if isfile(file_path):
            try:
                 remove(file_path)
            except Exception:
                 print(f"Unable to delete {file_path}: {Exception}")

def auth_login_user(data_dict):
    data_dict_sanitized = auth_sanitize_log_in_user(data_dict)
    result = db_login_user(data_dict)
    return result

def auth_sanitize_log_in_user(data_dict):
    #Pending sanitization impelentation
    data_dict["username"] = data_dict.get("username").lower()
    return data_dict

def auth_register_user(data_inmutable_multi_dict, language):
    data_dict = get_dict_from_inmutable_multi_dict(data_inmutable_multi_dict)
    for key, value in data_dict.items():
        if value == '': data_dict[key] = None
    data_dict_sanitized = auth_sanitize_register_user(data_dict)
    result = db_register_user(data_dict, language)
    if result:
        username = data_dict_sanitized["username"]
        email = data_dict_sanitized["email"]
        if USE_WEB_APP_AUTH_REGISTER_EMAIL_CONFIRMATION:
            send_new_user_wellcome_email(username, email, language)
        return username
    else:
        return None

def get_dict_from_inmutable_multi_dict(data_inmutable_multi_dict):
    data_dict = {}
    for key, value in data_inmutable_multi_dict.items():
        data_dict[key] = value
    return data_dict

def auth_sanitize_register_user(data_dict):
    #Pending sanitization impelentation
    data_dict["username"] = data_dict.get("username").lower()
    return data_dict

def auth_available_username(username):
    username_sanitized = auth_sanitize_available_user(username)
    return db_available_username(username_sanitized)

def auth_sanitize_available_user(username):
    #Pending sanitization impelentation
    return username.lower()
