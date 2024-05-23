from flask import Blueprint, render_template, request, flash, redirect, url_for


projects = Blueprint("projects",__name__)

@projects.route('/projects')
def project_page():
    return render_template("card.html")