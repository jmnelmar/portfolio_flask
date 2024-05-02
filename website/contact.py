from flask import Blueprint, render_template,flash, request, redirect, url_for
import os, ezgmail
contact = Blueprint("contact",__name__)

_PATH = ".credentials/"

@contact.route('/contact', methods=['POST'])
def contact_route():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        
        flash("OK")
    return render_template("contact.html")


def send_email(email_address,subject , message):
    os.chdir(_PATH)
    ezgmail.init()
    ezgmail.send('jmnel.mar@gmail.com','Test Subject','Testing messages sent by gmail 1')