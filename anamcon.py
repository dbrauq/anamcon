# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------


from utils.texts import *
from utils.anamcon_startup import *


if __name__ == "__main__":
    print_title()
    configure_system()
    if USE_START_MODE == "MANUAL":
        start_db_server()
        start_web_app()
        load_agents_into_database()
    elif USE_START_MODE == "DOCKER":
        start_docker_compose()
        load_agents_into_database()
    else:
        print("Unknown start mode. Please select \"DOCKER\" or \"MANUAL\" as START_MODE")




