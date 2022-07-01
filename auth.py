from crypt import methods
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.router('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html" text="testing", user="tim")

@auth.router('/logout')
def logout():
    return render_template("logout.html")

@auth.router('/sing-up', methods=['GET', 'POST'] )
def sing_up():
    return render_template("sing_up.html")