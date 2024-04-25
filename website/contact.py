from flask import Blueprint, render_template, request, flash, redirect, url_for

contact = Blueprint("contact",__name__)

@contact.route('/contact')
def contact_route():
    return render_template("contact.html")