###

#
import re

# pattern (criteria)
email_pattern = r'^[\w.-]+@[\w.-]+\.com$'

def read_email():
    with open ('email.txt','r', encoding="utf-8") as file:
        return file.read()

def email_sender():
    content=read_email()
    match=re.search(r"From:.*<(.+?)>",content)
    return match.group(1)

def email_recipient():
    content=read_email()
    match=re.search(r"To:.*<(.+?)>",content)
    return match.group(1)

def email_subject():
    content=read_email()
    match=re.search(r"Subject:(.*)",content)
    return match.group(1)

def email_body():
    content=read_email()
    body=re.split(r"\n\n",content,1)
    return body[1]