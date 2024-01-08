# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from src.db_server.mongodb_docker_manager import *

def configure_mongodb_docker_image():
    if (not exists_docker_mongodb_image()) or (not is_latest_docker_mongodb_image()):
        if exists_docker_mongodb_server() and USE_DB_DOCKER_SAFE_DELETE:
            stop_docker_mongodb_server()
            kill_docker_mongodb_server()
            rm_docker_mongodb_server()
            rm_docker_mongodb_image()
            download_latest_mongodb_docker_image()
        elif exists_docker_mongodb_server() and (not USE_DB_DOCKER_SAFE_DELETE):
            rm_docker_mongodb_server()
            rm_docker_mongodb_image()
            download_latest_mongodb_docker_image()
        else:
            download_latest_mongodb_docker_image()

def deploy_mongodb_docker_container():
    if exists_docker_mongodb_server() and USE_DB_DOCKER_SAFE_DELETE:
        stop_docker_mongodb_server()
        kill_docker_mongodb_server()
        rm_docker_mongodb_server()
        start_docker_mongodb_server()
    elif exists_docker_mongodb_server() and (not USE_DB_DOCKER_SAFE_DELETE):
        rm_docker_mongodb_server()
        start_docker_mongodb_server()
    else:
        start_docker_mongodb_server()

def configure_mongodb_collections():
    return

def load_mongodb_collections():
    return

def save_mongodb_collection():
    return