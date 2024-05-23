from flask import Flask 
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jkjhbfytwaascefas asf'
    

    from .views import views
    from .about import about
    from .resume import resume
    from .tech_stacks import stacks
    from .contact import contact
    from .projects import projects

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(about, url_prefix = '/')
    app.register_blueprint(resume, url_prefix = '/')
    app.register_blueprint(stacks, url_prefix = '/')    
    app.register_blueprint(contact, url_prefix = '/')
    app.register_blueprint(projects, url_prefix = '/')

    return app