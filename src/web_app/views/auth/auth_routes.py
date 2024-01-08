# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------


from os.path import abspath, dirname
from flask import (Blueprint, 
                   render_template, 
                   send_file,
                   redirect,
                   jsonify,
                   session,
                   request)
from views.auth.auth_data import *
from auth.auth import *
from auth.lang import get_best_web_language



auth_blueprint = Blueprint("auth", __name__)
base_path = dirname(dirname(dirname(abspath(__file__))))


@auth_blueprint.route("/login", defaults={"lang": None}, methods=["GET"])
@auth_blueprint.route("/login/<lang>", methods=["GET"])
def login(lang):
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/login/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("", 404)
        USE_LOGIN_TEXTS = globals().get(f"USE_LOGIN_TEXTS_{lang.upper()}")
        return render_template("/views/auth/templates/login.html",
                            LANGUAGE=lang,
                            USE_LOGIN_TEXTS=USE_LOGIN_TEXTS,
                            USE_AVAILABLE_LANGUAGES=USE_AVAILABLE_LANGUAGES,
                            USE_AVAILABLE_LANGUAGES_VERBOSE=USE_AVAILABLE_LANGUAGES_VERBOSE)
    

@auth_blueprint.route("/register", defaults={"lang": None}, methods=["GET"])
@auth_blueprint.route("/register/<lang>", methods=["GET"])
def register(lang):
    session.get("register_success")
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/register/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("", 404)
        USE_REGISTER_TEXTS = globals().get(f"USE_REGISTER_TEXTS_{lang.upper()}")
        return render_template("/views/auth/templates/register.html",
                            LANGUAGE=lang,
                            USE_REGISTER_TEXTS=USE_REGISTER_TEXTS,
                            USE_AVAILABLE_LANGUAGES=USE_AVAILABLE_LANGUAGES,
                            USE_AVAILABLE_LANGUAGES_VERBOSE=USE_AVAILABLE_LANGUAGES_VERBOSE)

@auth_blueprint.route("/register_successful", defaults={"lang": None}, methods=["GET"])
@auth_blueprint.route("/register_successful/<lang>", methods=["GET"])
def register_success(lang):
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/register_successful/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("", 404)
        USE_REGISTER_SUCCESS_TEXTS = globals().get(f"USE_REGISTER_SUCCESS_TEXTS_{lang.upper()}")
        USERNAME = session.get("language")
        return render_template("/views/auth/templates/register_successful.html",
                            LANGUAGE=lang,
                            USE_REGISTER_SUCCESS_TEXTS=USE_REGISTER_SUCCESS_TEXTS,
                            USE_AVAILABLE_LANGUAGES=USE_AVAILABLE_LANGUAGES,
                            USE_AVAILABLE_LANGUAGES_VERBOSE=USE_AVAILABLE_LANGUAGES_VERBOSE,
                            USERNAME = USERNAME)
    

@auth_blueprint.route("/terms", defaults={"lang": None}, methods=["GET"])
@auth_blueprint.route("/terms/<lang>", methods=["GET"])
def terms(lang):
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/terms/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("", 404)
        USE_TERMS_TEXTS = globals().get(f"USE_TERMS_TEXTS_{lang.upper()}")
        return render_template("/views/auth/templates/terms.html",
                            LANGUAGE=lang,
                            USE_TERMS_TEXTS=USE_TERMS_TEXTS,
                            USE_AVAILABLE_LANGUAGES=USE_AVAILABLE_LANGUAGES,
                            USE_AVAILABLE_LANGUAGES_VERBOSE=USE_AVAILABLE_LANGUAGES_VERBOSE)


# Not implemented
@auth_blueprint.route("/recover", defaults={"lang": None}, methods=["GET"])
@auth_blueprint.route("/recover/<lang>", methods=["GET"])
def recover(lang):
    if lang == None:
        language = session.get("language")
        if language is None:
            language = get_best_web_language(request.headers.get("Accept-Language").split(","))
            session["language"] = language
        return redirect("/login/" + language)
    else:
        if lang in USE_AVAILABLE_LANGUAGES:
            session["language"] = lang
        else:
            return ("", 404)
        USE_TERMS_TEXTS = globals().get(f"USE_TERMS_TEXTS_{lang.upper()}")
        return redirect("/login")


@auth_blueprint.route("/register_successful/styles_base", methods=["GET"])
@auth_blueprint.route("/register/styles_base", methods=["GET"])
@auth_blueprint.route("/terms/styles_base", methods=["GET"])
@auth_blueprint.route("/login/styles_base", methods=["GET"])
def style_base():
    return send_file(base_path + "/views/auth/static/css/styles_base.css")

@auth_blueprint.route("/login/styles_login", methods=["GET"])
def style_login():
    return send_file(base_path + "/views/auth/static/css/styles_login.css")

@auth_blueprint.route("/register/styles_register", methods=["GET"])
def style_register():
    return send_file(base_path + "/views/auth/static/css/styles_register.css")

@auth_blueprint.route("/register_successful/styles_register_successful", methods=["GET"])
def style_register_successful():
    return send_file(base_path + "/views/auth/static/css/styles_register_successful.css")


@auth_blueprint.route("/terms/styles_terms", methods=["GET"])
def style_terms():
    return send_file(base_path + "/views/auth/static/css/styles_terms.css")

@auth_blueprint.route("/register_successful/logo_icon", methods=["GET"])
@auth_blueprint.route("/register/logo_icon", methods=["GET"])
@auth_blueprint.route("/terms/logo_icon", methods=["GET"])
@auth_blueprint.route("/login/logo_icon", methods=["GET"])
def logo_icon():
    return send_file(base_path + "/views/auth/static/img/logo_icon.png")

@auth_blueprint.route("/register_successful/logo_text", methods=["GET"])
@auth_blueprint.route("/register/logo_text", methods=["GET"])
@auth_blueprint.route("/terms/logo_text", methods=["GET"])
@auth_blueprint.route("/login/logo_text", methods=["GET"])
def logo_text():
    return send_file(base_path + "/views/auth/static/img/logo_text.png")

@auth_blueprint.route("/register_successful/language_icon_use/<lang>", methods=["GET"])
@auth_blueprint.route("/register/language_icon_use/<lang>", methods=["GET"])
@auth_blueprint.route("/terms/language_icon_use/<lang>", methods=["GET"])
@auth_blueprint.route("/login/language_icon_use/<lang>", methods=["GET"])
def language_icon_use(lang):
    language = session.get("language")
    return send_file(base_path + f"/views/auth/static/img/language_icon_{lang.lower()}.png")

@auth_blueprint.route("/register_successful/language_icon/<lang>", methods=["GET"])
@auth_blueprint.route("/register/language_icon/<lang>", methods=["GET"])
@auth_blueprint.route("/terms/language_icon/<lang>", methods=["GET"])
@auth_blueprint.route("/login/language_icon/<lang>", methods=["GET"])
def language_icon_es(lang):
    return send_file(base_path + f"/views/auth/static/img/language_icon_{lang}.png")

@auth_blueprint.route("/register/username_js", methods=["GET"])
def username_register_js():
    return send_file(base_path + f"/views/auth/static/js/username_register.js")

@auth_blueprint.route("/register/available_username", methods=["POST"])
def available_username():
    language = session.get("language")
    if language in USE_AVAILABLE_LANGUAGES:
        username = request.get_json()["username"]
        available = auth_available_username(username)
        if available:
            js_consts = globals().get(f"USE_REGISTER_TEXTS_{language.upper()}")
            available_button_text = js_consts["js_consts"]["available_username_text"]
            error_text = js_consts["js_consts"]["username_error_text"]
        else:
            js_consts = globals().get(f"USE_REGISTER_TEXTS_{language.upper()}")
            available_button_text = js_consts["js_consts"]["not_available_username_text"]
            error_text = js_consts["js_consts"]["username_error_text"]
        return jsonify(available = available,
            available_button_text=available_button_text,
            error_text = error_text)
            
@auth_blueprint.route("/register/get_username_error_text", methods=["GET"])
def username_error_text():
    language = session.get("language")
    if language in USE_AVAILABLE_LANGUAGES:
        js_consts = globals().get(f"USE_REGISTER_TEXTS_{language.upper()}")
        error_text = js_consts["js_consts"]["username_error_text"]
        return jsonify(error_text = error_text)
    

@auth_blueprint.route("/register/password_js", methods=["GET"])
def password_register_js():
    return send_file(base_path +\
                      f"/views/auth/static/js/password_register.js")
    

@auth_blueprint.route("/register/get_password_error_text", methods=["GET"])
def password_error_text():
    language = session.get("language")
    if language in USE_AVAILABLE_LANGUAGES:
        js_consts = globals().get(f"USE_REGISTER_TEXTS_{language.upper()}")
        error_text = js_consts["js_consts"]["password_error_text"]
        return jsonify(error_text = error_text)

@auth_blueprint.route("/register/email_js", methods=["GET"])
def email_register_js():
    return send_file(base_path +\
                      f"/views/auth/static/js/email_register.js")

@auth_blueprint.route("/register/get_email_error_text", methods=["GET"])
def email_error_text():
    language = session.get("language")
    if language in USE_AVAILABLE_LANGUAGES:
        js_consts = globals().get(f"USE_REGISTER_TEXTS_{language.upper()}")
        error_text = js_consts["js_consts"]["email_error_text"]
        return jsonify(error_text = error_text)
    
@auth_blueprint.route("/register/valid_register_js", methods=["GET"])
def valid_form_register_js():
    return send_file(base_path +\
                      f"/views/auth/static/js/valid_form_register.js")

@auth_blueprint.route("/register/valid_login_js", methods=["GET"])
def valid_form_login_js():
    return send_file(base_path +\
                      f"/views/auth/static/js/valid_form_login.js")

@auth_blueprint.route("/register/process", methods=["GET", "POST"])
def register_process():
    language = session.get("language")
    if language in USE_AVAILABLE_LANGUAGES:
        form_data = request.form
        try:
            username = auth_register_user(form_data, language)
            if(username != None):
                return redirect("/register_successful")
            else:
                return redirect("/register")
        except Exception as e:
            return ("", 400)

@auth_blueprint.route("/login/process", methods=["GET", "POST"])
def login_process():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user_data={"username": username, "password": password}
    valid_credentials = auth_login_user(user_data)
    if valid_credentials:
        session["session_logged_id"] =  True
        session["username"] = username.lower()
    return jsonify(valid_credentials = valid_credentials)

@auth_blueprint.route("/logout", methods=["GET", "POST"])
def logout():
    session["session_logged_id"] =  False
    session["username"] = None
    return redirect("/login")