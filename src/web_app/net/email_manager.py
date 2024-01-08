# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from email.message import EmailMessage
from smtplib import SMTP_SSL
from json import load
from os.path import dirname, abspath
from net.config_email import USE_EMAIL_AUTH_PATH, USE_START_MODE

if USE_START_MODE == "DOCKER":
    with open(dirname(dirname(abspath(__file__))) + "/secure/anamcon-dialogflow-email.json", 'r') as auth_file:
            auth_data = load(auth_file)
            USE_EMAIL_AUTH_EMAIL = auth_data.get("email")
            USE_EMAIL_AUTH_PASSWORD = auth_data.get("pass")
else:
    with open(USE_EMAIL_AUTH_PATH, 'r') as auth_file:
            auth_data = load(auth_file)
            USE_EMAIL_AUTH_EMAIL = auth_data.get("email")
            USE_EMAIL_AUTH_PASSWORD = auth_data.get("pass")

def send_email_to_one(recipient, subject, email_message, content="html", attachments_paths=None):
    email = EmailMessage()
    email["From"] = USE_EMAIL_AUTH_EMAIL
    email["To"] = recipient
    email["Subject"] = subject
    if content=="html":
        email.set_content(email_message, subtype="html", charset="utf-8")
    else:
        email.set_content(email_message, charset="utf8")
    smtp = SMTP_SSL("smtp.gmail.com")
    if attachments_paths:
        for attachment_path in attachments_paths:
            attachment_name = attachment_path.split("/")[-1]
            attachment_subtype = attachment_path.split(".")[-1]
            if attachment_subtype in ["jpg","jpeg","gif","bmp"]:
                attachment_type = "image"
            elif attachment_subtype == "txt":
                attachment_type = "text"
            else:
                attachment_type = "application"    
            with open(attachment_path, "rb") as attachment_file:
                attachment_data = attachment_file.read()
            email.add_attachment(
                attachment_data,
                maintype=attachment_type,
                subtype=attachment_subtype,
                filename=attachment_name
            )
    smtp.login(USE_EMAIL_AUTH_EMAIL, USE_EMAIL_AUTH_PASSWORD)
    smtp.sendmail(USE_EMAIL_AUTH_PASSWORD, recipient, email.as_string())
    smtp.quit()

def send_email_to_many(recipients, subject, email_message, attachments_paths=None):
    for recipient in recipients:
        send_email_to_one(recipient, subject, email_message, attachments_paths)