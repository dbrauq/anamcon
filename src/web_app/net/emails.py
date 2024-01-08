# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from os.path import abspath, dirname
from net.email_manager import *


def send_new_user_wellcome_email(username, email, language):
    email_template_path = f"{dirname(abspath(__file__))}/email_templates/wellcome_email_{language}.html"
    with open(email_template_path, "r") as email_template_file:
        email_template = email_template_file.read()
        email_content = email_template.replace("@user",username).replace("@email", email)
        subject = email_content.split("<title>")[1].split("</title>")[0].replace("\n","").strip()
        print(subject)
        send_email_to_one(email, subject, email_content)
