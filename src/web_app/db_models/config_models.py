# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

USE_DB_PORT="27017"
USE_DB_NAME="anamcon"
USE_DB_COLLECTIONS={'users': 'users', 'anamnesis': 'anamnesis', 'agents': 'agents'}
USE_FORBIDDEN_USERNAMES=['none', 'admin', 'administrator', 'administrador', 'anamcon']
USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS=['$__intro', '$__continue', '$__end', '$__yes']
USE_START_MODE="DOCKER"
