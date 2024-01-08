# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------


from json import load
from src.db_server.console import run_blocking_command
from src.db_server.config_db import *
from pymongo import *
from json import loads

with open(USE_DB_AUTH_PATH, 'r') as auth_file:
        auth_data = load(auth_file)
        USE_DB_AUTH_USER = auth_data.get("user")
        USE_DB_AUTH_PASSWORD = auth_data.get("pass")

def start_docker_mongodb_server():
    docker_command = f"\
docker run -d \
--name {USE_DB_DOCKER_NAME} \
-p {USE_DB_PORT}:27017 \
-v {USE_DUMP_DATA_PATH}:/data/dump \
-e MONGODB_INITDB_ROOT_USERNAME={USE_DB_AUTH_USER} \
-e MONGODB_INITDB_ROOT_PASSWORD={USE_DB_AUTH_PASSWORD} \
mongo:latest --dbpath /data/db\
"
    run_blocking_command(docker_command)

def get_docker_mongodb_server_id():
    docker_command=f"docker ps -f \"name={USE_DB_DOCKER_NAME}\" -aq"
    (stdout, stderr) = run_blocking_command(docker_command)
    return stdout.strip()

def exists_docker_mongodb_server():
    if get_docker_mongodb_server_id() != "":
        return True
    else:
        return False

def stop_docker_mongodb_server():
    docker_command =f"docker stop {get_docker_mongodb_server_id()}"
    run_blocking_command(docker_command)

def kill_docker_mongodb_server():
    docker_command =f"docker kill {get_docker_mongodb_server_id()}"
    run_blocking_command(docker_command)
     
def rm_docker_mongodb_server():
    docker_command =f"docker rm -f {get_docker_mongodb_server_id()}"
    run_blocking_command(docker_command)

def download_latest_mongodb_docker_image():
    docker_command = "docker pull mongo:latest"
    run_blocking_command(docker_command)

def get_mongodb_docker_image_id():
    docker_command=f"docker images -f \"reference=mongo\" -q"
    (stdout, stderr) = run_blocking_command(docker_command)
    return stdout.strip()

def rm_docker_mongodb_image():
    docker_command =f"docker rmi -f {get_mongodb_docker_image_id()}"
    run_blocking_command(docker_command)

def exists_docker_mongodb_image():
    if get_mongodb_docker_image_id() != "":
        return True
    else:
        return False

def is_latest_docker_mongodb_image():
    docker_command = "docker inspect mongo"
    (stdout, stderr) = run_blocking_command(docker_command)
    json_data = loads(stdout)
    if json_data[0]["RepoTags"][0].split(":")[-1] == "latest":
        return True
    else:
        return False
    