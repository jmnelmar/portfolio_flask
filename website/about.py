from flask import Blueprint, render_template, request, flash, redirect, url_for


about = Blueprint("about",__name__)

@about.route('/about')
def about_and_skills():
    return render_template("about.html")