# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from utils.colors import *
from utils.console import *
from config.config_startup import *
from config.config_main.config_merged import *
from src.db_server.db_server import *
from src.web_app.sessions.sessions_manager import *
from os.path import (abspath, 
                     dirname)


def correct_message():
    message = GREEN_COLOR + " [✓]" + DEFAULT_COLOR + " "
    return message

def error_message():
    message = RED_COLOR + " [✗]" + DEFAULT_COLOR + " "
    return message

def warning_message():
    message = YELLOW_COLOR + " [!]" + DEFAULT_COLOR + " "
    return message

def start_function_message():
    message = BLUE_COLOR + " [➜]" + DEFAULT_COLOR + " "
    return message

def image_message():
    message = YELLOW_COLOR + YELLOW_COLOR + "[*]" + DEFAULT_COLOR + " "
    return message

def service_message():
    message = YELLOW_COLOR + "[@]" + DEFAULT_COLOR + " "
    return message

def configure_system():
    print(start_function_message() + "Setting main system configuration.")
    set_main_config()
    print(correct_message() + "Main configuration settings set correctly.")
    if USE_WEB_APP_AGENT_RESET_AFTER_REBOOT:
        print(warning_message() + "Anamnesis Agents Reset has been enabled.")
        print(start_function_message() + "Configuring Anamnesis Agents.")
        set_anamnesis_config()
        print(correct_message() + "Anamnesis Agents configuration set correctly.")
    else:
        print(warning_message() + "Anamnesis Agents Reset has been disabled. Agents remain configured as they were previously.")
    
def start_db_server():
    print(start_function_message() + "Configuring MongoDB (database) Docker image.")
    configure_mongodb_docker_image()
    print(correct_message() + image_message() + "MongoDB (database) Docker image correctly configured.")
    print(start_function_message() + "Deploying MongoDB (database) container.")
    deploy_mongodb_docker_container()
    print(correct_message() + service_message() + "MongoDB (database) container running as a service.")

def load_agents_into_database ():
    print(start_function_message() + "Loading anamnesis agents into database.")
    load_agents()
    print(correct_message() + "All anamnesis agents have been correctly loaded into the database.")

def start_terminology_server():
    return

def start_web_app():
    if USE_RESET_SESSIONS_AFTER_REBOOT_ENABLED:
        print(warning_message() + "Sessions reset after reboot enabled.")
        print(start_function_message() + "Resetting session files.")
        delete_sessions()
        print(correct_message() + image_message() + "Session files have been reset.")
    else:
        print(warning_message() + "Sessions reset after reboot disabled. Previous sessions will be preserved.")
    print(start_function_message() + "Configuring Web-App Docker image.")
    print(correct_message() + image_message() + "Main Web-App Docker image correctly configured.")
    print(start_function_message() + "Deploying Web-App Docker container.")
    print(correct_message() + service_message() + "Web-App Docker container running as a service.")
    return

def start_docker_compose():
    print(warning_message() + "Docker mode selected. Note that certain configuration features are enabled by default in Docker mode.")
    print(start_function_message() + "Starting Docker microservices. Please wait.")
    run_blocking_command("docker-compose up -d")
    print(correct_message() + image_message() + "All systems are working correctly. You can connect to the system at http://127.0.0.1:5000/")
    return

def start_system():
    print()
    return
