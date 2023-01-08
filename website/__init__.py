#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from joblib import load
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import dash_table
from dash_app import create_dash_application
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    create_dash_application(app)
    from .views import views
    from .auth import auth
      
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
     
    
    from .models import User, Note
    with app.app_context():
        db.create_all()  

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

