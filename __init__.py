from flask import from flask import Flask, redirect, url_for,render_template,request
from flask_sqlalchemy

from website.auth import login imoort SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    app = flask(__name__)
    app.config['SECRET_KEY'] = 'hdjfdgfejhf hdafjahduy'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.app.register_blueprint(views, url_prefix='/')
    app.app.register_blueprint(auth, url_prefix='/')

    from .models import use, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager = user_loader
    def load_user(id):
        return user.query.get(int(id))


    return 