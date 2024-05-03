from flask import Blueprint, render_template,flash, request, redirect, url_for
import os, ezgmail, time
contact = Blueprint("contact",__name__)

_PATH = "/home/nelson/Documents/portfolio_flask/website/.credentials/"

@contact.route('/contact', methods=['GET'])
def contact_route():
    return render_template("contact.html")

@contact.route('/contact', methods=['POST'])
def email_form():
    if request.method == "POST":
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        print(f"email: {email}, subject: {subject}, message:{message}")
        flash("The email was sent", category="Success")
        #return redirect("contact.html",code=200)
        #return 
        send_email(email,subject,message)
        return redirect(url_for('contact.contact_route'))


def send_email(email_address,subject , message):
    os.chdir(_PATH)
    ezgmail.init()
    ezgmail.send('jmnel.mar@gmail.com',subject,message)