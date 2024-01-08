# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------


from auth.config_auth import (USE_LANGUAGE,
                              USE_AVAILABLE_LANGUAGES)


def get_best_web_language(accepted_web_languages):
    for language in accepted_web_languages:
        lang = language[0:2]
        if lang in USE_AVAILABLE_LANGUAGES:
            return lang
    return USE_LANGUAGE

