from flask import Blueprint, render_template, request, flash, redirect, url_for


resume = Blueprint("resume",__name__)

@resume.route('/resume')
def resume_page():
    return render_template("resume.html")