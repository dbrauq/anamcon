# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from os.path import (abspath, 
                     dirname,
                     exists)
from flask import (Blueprint, 
                   render_template,
                   send_file,
                   redirect,
                   jsonify,
                   session,
                   request)
from auth.lang import get_best_web_language
from views.main.main_data import *
from anamnesis.anamnesis import *
from dialog.config_dialog import (USE_OUTPUT_AUDIO_TEMP_PATH,
                                  USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS)
from dialog.audio import *
from report.report import *


main_blueprint = Blueprint("main", __name__)
base_path = dirname(dirname(dirname(abspath(__file__))))

@main_blueprint.route("/anamnesis", defaults={"lang": None}, methods=["GET"])
@main_blueprint.route("/anamnesis/<lang>", methods=["GET"])
@main_blueprint.route("/", defaults={"lang": None}, methods=["GET"])
@main_blueprint.route("/<lang>", methods=["GET"])
def anamnesis(lang):
    logged_in = session.get("session_logged_id")
    if logged_in != True:
        return redirect("/login")
    else:
        language = session.get("language") if lang is None else lang
    if language is None:
        language = get_best_web_language(request.headers.get("Accept-Language").split(","))
        session["language"] = language
        return redirect("/" + language)
    else:
        if language in USE_AVAILABLE_LANGUAGES:
            USERNAME = session.get("username")
            USE_ANAMNESIS_TEXTS = globals().get(f"USE_ANAMNESIS_TEXTS_{language.upper()}")
            return render_template("/views/main/templates/anamnesis.html",
                                USERNAME=USERNAME,
                                USE_ANAMNESIS_TEXTS=USE_ANAMNESIS_TEXTS,
                                LANGUAGE=language,
                                USE_AVAILABLE_LANGUAGES=USE_AVAILABLE_LANGUAGES,
                                USE_AVAILABLE_LANGUAGES_VERBOSE=USE_AVAILABLE_LANGUAGES_VERBOSE)
        else:
            return ("", 404)   

@main_blueprint.route("/anamnesis/styles_base", methods=["GET"])
def style_base():
    return send_file(base_path + "/views/main/static/css/styles_base.css")

@main_blueprint.route("/anamnesis/styles_main", methods=["GET"])
def style_main():
    return send_file(base_path + "/views/main/static/css/styles_main.css")

@main_blueprint.route("/anamnesis/logo_icon", methods=["GET"])
def logo_icon():
    return send_file(base_path + "/views/main/static/img/logo_icon.png")

@main_blueprint.route("/anamnesis/main_icon", methods=["GET"])
def main_icon():
    return send_file(base_path + "/views/main/static/img/main_icon.png")

@main_blueprint.route("/anamnesis/reports_icon", methods=["GET"])
def reports_icon():
    return send_file(base_path + "/views/main/static/img/reports_icon.png")

@main_blueprint.route("/anamnesis/user_icon", methods=["GET"])
def user_icon():
    return send_file(base_path + "/views/main/static/img/user_icon.png")

@main_blueprint.route("/anamnesis/log_out_icon", methods=["GET"])
def log_out_icon():
    return send_file(base_path + "/views/main/static/img/log_out_icon.png")

@main_blueprint.route("/anamnesis/language_icon_use/<lang>", methods=["GET"])
def language_icon_use(lang):
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/language_icon_use/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("Not Found", 404)
    return send_file(base_path + f"/views/main/static/img/language_icon_{lang.lower()}.png")

@main_blueprint.route("/anamnesis/language_icon/<lang>", methods=["GET"])
def language_icon_es(lang):
    return send_file(base_path + f"/views/main/static/img/language_icon_{lang}.png")

@main_blueprint.route("/anamnesis/sound_off", methods=["GET"])
def sound_off():
    return send_file(base_path + "/views/main/static/img/sound_off.png")

@main_blueprint.route("/anamnesis/sound_off_active", methods=["GET"])
def sound_off_active():
    return send_file(base_path + "/views/main/static/img/sound_off_active.png")

@main_blueprint.route("/anamnesis/sound_on", methods=["GET"])
def sound_on():
    return send_file(base_path + "/views/main/static/img/sound_on.png")

@main_blueprint.route("/anamnesis/sound_on_active", methods=["GET"])
def sound_on_active():
    return send_file(base_path + "/views/main/static/img/sound_on_active.png")

@main_blueprint.route("/anamnesis/message", methods=["GET"])
def message():
    return send_file(base_path + "/views/main/static/img/message.png")

@main_blueprint.route("/anamnesis/micro", methods=["GET"])
def micro():
    return send_file(base_path + "/views/main/static/img/micro.png")

@main_blueprint.route("/anamnesis/mini_user", methods=["GET"])
def mini_user():
    return send_file(base_path + "/views/main/static/img/mini_user.png")

@main_blueprint.route("/anamnesis/mini_system", methods=["GET"])
def mini_system():
    return send_file(base_path + "/views/main/static/img/mini_system.png")

@main_blueprint.route("/anamnesis/loading_icon", methods=["GET"])
def loading_icon():
    return send_file(base_path + "/views/main/static/img/loading_icon.gif")

@main_blueprint.route("/anamnesis/body_icon", methods=["GET"])
def body_icon():
    return send_file(base_path + "/views/main/static/img/body.png")

@main_blueprint.route("/anamnesis/anamnesis_js", methods=["GET"])
def anamnesis_js():
    return send_file(base_path + f"/views/main/static/js/anamnesis.js")

@main_blueprint.route("/anamnesis/resize_js", methods=["GET"])
def resize_js():
    return send_file(base_path + f"/views/main/static/js/resize.js")

@main_blueprint.route("/logout", methods=["GET"])
def log_out():
    session["session_logged_id"]=None
    session["username"]=None
    session["active_anamnesis"]=None
    session["active_anamnesis_mode"]=None
    return redirect("/login")

@main_blueprint.route("/anamnesis/get_available_anamnesis", methods=["GET"])
def get_available_anamnesis_modes():
    return jsonify(available_anamnesis_modes = USE_AVAILABLE_ANAMNESIS_MODES,
                   available_anamnesis_modes_icons = USE_AVAILABLE_ANAMNESIS_MODES_ICONS)


@main_blueprint.route("/anamnesis/active_session", methods=["GET"])
def active_sesion():
    active_session = session.get("session_logged_id")
    return jsonify(active_session = active_session)

@main_blueprint.route("/anamnesis/navigation_texts", methods=["GET"])
def anamnesis_navigation_texts():
    language = session.get("language")
    USE_ANAMNESIS_TEXTS = globals().get(f"USE_ANAMNESIS_TEXTS_{language.upper()}")

    return jsonify(delete_confirm_text = USE_ANAMNESIS_TEXTS["delete_confirm_text"],
                   no_navigation_icon_text = USE_ANAMNESIS_TEXTS["no_navigation_icon_text"],
                   no_navigation_main_text = USE_ANAMNESIS_TEXTS["no_navigation_main_text"],
                   no_anamnesis_icon_text = USE_ANAMNESIS_TEXTS["no_anamnesis_icon_text"],
                   no_anamnesis_main_text = USE_ANAMNESIS_TEXTS["no_anamnesis_main_text"],
                   start_anamnesis_text_1 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_1"], 
                   start_anamnesis_text_2 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_2"],
                   start_anamnesis_text_3_1 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_3_1"],
                   start_anamnesis_text_3_2 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_3_2"],
                   start_anamnesis_text_4 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_4"],
                   start_anamnesis_text_5_1 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_5_1"],
                   start_anamnesis_text_5_2 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_5_2"],
                   start_anamnesis_text_6 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_6"],
                   start_anamnesis_text_7 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_7"],
                   start_anamnesis_text_8 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_8"],
                   start_anamnesis_text_9 = USE_ANAMNESIS_TEXTS["start_anamnesis_text_9"],
                   summary_title_text_1 = USE_ANAMNESIS_TEXTS["summary_title_text_1"],
                   summary_title_text_2 = USE_ANAMNESIS_TEXTS["summary_title_text_2"],
                   summary_title_text_3 = USE_ANAMNESIS_TEXTS["summary_title_text_3"],
                   summary_data_type_text = USE_ANAMNESIS_TEXTS["summary_data_type_text"],
                   summary_data_state_text = USE_ANAMNESIS_TEXTS["summary_data_state_text"],
                   summary_data__duration_text = USE_ANAMNESIS_TEXTS["summary_data__duration_text"],
                   summary_data_creation_datetime_text = USE_ANAMNESIS_TEXTS["summary_data_creation_datetime_text"],
                   summary_data_last_interaction_datetime_text = USE_ANAMNESIS_TEXTS["summary_data_last_interaction_datetime_text"],
                   summary_data_num_interactions_text = USE_ANAMNESIS_TEXTS["summary_data_num_interactions_text"])


@main_blueprint.route("/anamnesis/get_all_navigation_anamnesis", methods=["GET"])
def get_all_navigation_anamnesis():
    username = session.get("username")
    if username != None:
        navigation_anamnesis = anamnesis_get_all_navigation_anamnesis(username)
        return jsonify(navigation_anamnesis = navigation_anamnesis)
    else: 
        redirect("/login")

@main_blueprint.route("/anamnesis/new_anamnesis", methods=["POST"])
def new_anamnesis():
    data = request.get_json()
    anamnesis_mode = data["anamnesis_mode"]
    username = session.get("username")
    if username != None:
        new_anamnesis_created = anamnesis_add_new_anamnesis(username, anamnesis_mode)
        return jsonify(new_anamnesis_created = new_anamnesis_created)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/delete_anamnesis", methods=["POST"])
def delete_anamnesis():
    data = request.get_json()
    anamnesis_timestamp = data["anamnesis_timestamp"]
    username = session.get("username")
    if username != None:
        deleted_anamnesis = anamnesis_delete_anamnesis(username, anamnesis_timestamp)
        return jsonify(deleted_anamnesis = deleted_anamnesis)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/set_active_anamnesis", methods=["POST"])
def set_active_anamnesis():
    data = request.get_json()
    anamnesis_timestamp = data["anamnesis_timestamp"]
    anamnesis_mode = data["anamnesis_mode"]
    username = session.get("username")
    if username != None:
        session["active_anamnesis"] = anamnesis_timestamp
        session["active_anamnesis_mode"] = anamnesis_mode
        return jsonify(anamnesis_timestamp = anamnesis_timestamp)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/get_active_anamnesis", methods=["GET"])
def get_active_anamnesis():
    username = session.get("username")
    if username != None:
        active_anamnesis = session.get("active_anamnesis")
        return jsonify(active_anamnesis = active_anamnesis)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/get_anamnesis_data", methods=["GET"])
def get_all_anamnesis_conversation():
    username = session.get("username")
    active_anamnesis = session.get("active_anamnesis")
    if username != None:
        anamnesis_dialog_data = anamnesis_get_anamnesis_data(username,active_anamnesis)
        return jsonify(anamnesis_dialog_data = anamnesis_dialog_data)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/update_anamnesis_title", methods=["POST"])
def update_anamnesis_title():
    data = request.get_json()
    anamnesis_timestamp = data["anamnesis_timestamp"]
    anamnesis_title = data["anamnesis_title"]
    username = session.get("username")
    if username != None:
        update = anamnesis_update_anamnesis_title(username, anamnesis_timestamp, anamnesis_title)
        return jsonify(update = update)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/start_anamnesis", methods=["POST"])
def start_anamnesis():
    data = request.get_json()
    anamnesis_timestamp = data["anamnesis_timestamp"]
    username = session.get("username")
    if username != None:
        update = anamnesis_update_anamnesis_status(username, anamnesis_timestamp, "recording")
        return jsonify(update = update)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/complete_anamnesis", methods=["POST"])
def complete_anamnesis():
    data = request.get_json()
    anamnesis_timestamp = data["anamnesis_timestamp"]
    username = session.get("username")
    if username != None:
        update = anamnesis_update_anamnesis_status(username, anamnesis_timestamp, "completed")
        return jsonify(update = update)
    else:
        redirect("/login")



@main_blueprint.route("/anamnesis/send_dialog_text", methods=["POST"])
def send_dialog_text():
    data = request.get_json()
    username = session.get("username")
    anamnesis_timestamp = data["anamnesis_timestamp"]
    text = data["text"]
    if (username != None) and(len(text)>0):
        response = anamnenesis_send_dialog_text(username, anamnesis_timestamp, text)
        return jsonify(response = response["response"], interaction_id = response["interaction_id"])
    else:
        return redirect("/login")

@main_blueprint.route("/anamnesis/send_dialog_audio", methods=["POST"])
def send_dialog_audio():
    data = request.get_json()
    username = session.get("username")
    anamnesis_timestamp = data["anamnesis_timestamp"]
    audio_bytes = bytes(list(data["audio"].values()))
    audio_wav_bytes = audio_convert_to_wav(audio_bytes)
    if ((username != None)):
        response = anamnesis_send_dialog_audio(username, anamnesis_timestamp, audio_wav_bytes)
        return jsonify(response = response["response"], interaction_id = response["interaction_id"])
    else:
        return redirect("/login")
    
@main_blueprint.route("/anamnesis/get_dialog_texts", methods=["POST"])
def get_dialogs():
    data = request.get_json()
    username = session.get("username")
    anamnesis_timestamp = data["anamnesis_timestamp"]
    if (username != None) and (anamnesis_timestamp!= None):
        anamnesis_texts = anamnesis_get_all_anamnesis_dialog_texts(username, anamnesis_timestamp)
        frontend_anamnesis_texts = []
        for interaction in anamnesis_texts:
            if interaction["query_text"] in USE_WEB_APP_DIALOG_AGENT_CONFIG_TEXTS:
                interaction["query_text"] = ""
                interaction["query_interpreted_text"] = ""
            if interaction["query_text"] in USE_WEB_APP_DIALOG_AGENT_ASSISTED_TEXTS:
                interaction["query_text"] = ""
                interaction["query_interpreted_text"] = ""
                frontend_anamnesis_texts[len(frontend_anamnesis_texts)-1]["response_text"]=""
            frontend_anamnesis_texts += [interaction]
        return jsonify(anamnesis_texts=frontend_anamnesis_texts)
    else:
        return jsonify(anamnesis_texts="")

@main_blueprint.route("/anamnesis/last_audio_response/<interaction>", methods=["GET"])
def last_audio_response(interaction):
    username = session.get("username")
    if USE_START_MODE == "DOCKER":
        audio_path = dirname(dirname(dirname(abspath(__file__)))) + "/sessions/audio/" + interaction +".wav"
    else:
        audio_path = USE_OUTPUT_AUDIO_TEMP_PATH+ interaction +".wav"
    print(audio_path)
    if (username != None) and(exists(audio_path)):
         if(exists(audio_path)):
            if USE_START_MODE == "DOCKER":
                return send_file(dirname(dirname(dirname(abspath(__file__)))) + "/sessions/audio/" + interaction +".wav")
            else:
                return send_file(USE_OUTPUT_AUDIO_TEMP_PATH+ interaction +".wav")
         else:
             return ("", 404)
    else:
        redirect("/login")

@main_blueprint.route("/anamnesis/download_report", methods=["POST"])
def download_reports():
    data = request.get_json()
    username = session.get("username")
    anamnesis_timestamp = data["anamnesis_timestamp"]
    if (username != None) and (anamnesis_timestamp!= None):
        file_src = create_and_get_report_path(username, anamnesis_timestamp)
        return send_file(file_src)
    else:
        redirect("/login")