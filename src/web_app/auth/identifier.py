# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from secrets import choice
from string import (ascii_letters, 
                    digits, 
                    punctuation)
from uuid import uuid4
from cryptography.fernet import Fernet
from json import load
from auth.config_auth import USE_WEB_APP_AUTH_SECRET_KEY_LENGTH


def create_uuidv4():
    return uuid4()

def create_secret_key(length):
    characters = ascii_letters + digits + punctuation
    secret_key_chars = [choice(characters) for i in range(length)]
    secret_key = "".join(secret_key_chars)
    return secret_key

def create_web_app_secret_key(length=USE_WEB_APP_AUTH_SECRET_KEY_LENGTH):
    return create_secret_key(length)

def create_fernet_key():
    return Fernet.generate_key()

def encrypt_data(data, key, signature=""):
    fernet = Fernet(key)
    token = fernet.encrypt((signature + data).encode())
    return token

def decrypt_data(token, key):
    fernet = Fernet(key)
    data = fernet.decrypt(token).decode()
    return data
