from flask import Blueprint, render_template, request, flash, url_for

stacks = Blueprint("stacks",__name__)

@stacks.route('tech-stacks')
def tech_stacks():
    return render_template("tech-stacks.html")