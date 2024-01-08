# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from utils.colors import *

ANAMCON_TITLE_ASCII = "\
 █████  ███    ██  █████  ███    ███  ██████  ██████  ███    ██ \n\
██   ██ ████   ██ ██   ██ ████  ████ ██      ██    ██ ████   ██ \n\
███████ ██ ██  ██ ███████ ██ ████ ██ ██      ██    ██ ██ ██  ██ \n\
██   ██ ██  ██ ██ ██   ██ ██  ██  ██ ██      ██    ██ ██  ██ ██ \n\
██   ██ ██   ████ ██   ██ ██      ██  ██████  ██████  ██   ████ \n\
"
PROYECT_TITLE ="   An open, automated, and customizable web anamnesis system."
NEW_LINE = "\n"
SEPARATOR = "----------------------------------------------------------------"
DISCLAIMER = "                NOT INTENDED FOR MEDICAL USE"

def print_title() -> None:
    print(SEPARATOR)
    print(NEW_LINE)
    print(ANAMCON_TITLE_ASCII)
    print(BLUE_COLOR + PROYECT_TITLE + DEFAULT_COLOR)
    print(NEW_LINE)
    print(MAGENTA_COLOR + DISCLAIMER + DEFAULT_COLOR)
    print(NEW_LINE)
    print(SEPARATOR)
                                                                