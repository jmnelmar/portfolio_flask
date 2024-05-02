from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/')
def contacts_sent_email():
    return render_template("contacts.html")
    

