"""
Dependencies:
    flask
    flask-login
    flask-sqlalchemy
    sqlite3
"""
from flask import Flask, render_template, Blueprint, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from db import KrakenDB, User


class Kraken():

    def __init__(self):

        import os,sqlite3
        self.os=os
        self.sqlite3=sqlite3

        self.db=SQLAlchemy()

        self.initFlask()

        self.db.init_app(self.app)

        self.loginManager=LoginManager()
        self.loginManager.login_view="auth_login"
        self.loginManager.init_app(self.app)

        @self.loginManager.user_loader
        def loadUser(user_id):
            return KrakenDB().getRow("users","username",f"'{user_id}'")

        self.app.run(host="127.0.0.1",port="1380")

    def initFlask(self):
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"]="secret-key-goes-here"
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
        self.initPages()

    def initPages(self):
        @self.app.route("/")
        def main_index(): return open("index.html","r").read()

        @self.app.route("/home/")
        @login_required
        def main_home():
            return render_template("home-nosite.html",name=current_user.name)

        @self.app.route("/login/")
        def auth_login(): return render_template("login.html")

        @self.app.route("/login/", methods=["post"])
        def auth_login_post():
            username=request.form.get("username");password=request.form.get("password")
            remember = True if request.form.get('remember') else False

            if not KrakenDB().rowExists("users","username",f"'{username}'"):
                flash("Username not recognised")
                return redirect(url_for("auth_login"))

            KrakenDB().passwordMatch(username)
            #if not KrakenDB().rowExists("users","password",f"'{check_password_hash}'")

            login_user(username,remember=remember)
            return redirect(url_for("main_home"))

        @self.app.route("/signup/")
        def auth_signup(): return render_template("signup.html")

        @self.app.route("/signup/", methods=["post"])
        def auth_signup_post():
            # signup validation code here

            name=request.form.get("name");email=request.form.get("email");username=request.form.get("username");password1=request.form.get("password");password2=request.form.get("password-repeat")

            if KrakenDB().rowExists("users","username",f"'{username}'"):
                flash("Username already exists")
                return redirect(url_for("auth_signup"))

            if KrakenDB().rowExists("users","email",f"'{email}'"):
                flash("Email already in use")
                return redirect(url_for("auth_signup"))

            verifyOutput=self.verifyField(name,"Name",canHaveSpace=True,canHaveSpecialChar=True)

            if len(verifyOutput) > 0:
                flash(verifyOutput,name,email,username)
                return redirect(url_for("auth_signup"))

            verifyOutput=self.verifyField(email,"Email",minLen=0,canHaveSpace=False,canHaveSpecialChar=True)

            if len(verifyOutput) > 0:
                flash(verifyOutput)
                return redirect(url_for("auth_signup"))

            verifyOutput=self.verifyField(username,"Username",canHaveSpecialChar=False)

            if len(verifyOutput) > 0:
                flash(verifyOutput)
                return redirect(url_for("auth_signup"))

            verifyOutput=self.verifyField(password1,"Password",minLen=8)

            if len(verifyOutput) > 0:
                flash(verifyOutput)
                return redirect(url_for("auth_signup"))

            if password1!=password2:
                flash("Passwords do not match")
                return redirect(url_for("auth_signup"))

            newUser=KrakenDB().createUser(username,email,name,generate_password_hash(password1,method="sha256"))
            # not using a hashing password yet as i cant be bothered to create the validation system with a hash

            return redirect(url_for("auth_login"))

        @self.app.route("/logout/")
        @login_required
        def auth_logout():
            logout_user()
            return redirect(url_for("auth_login"))

        self.blueprints={
            "main-index":main_index,
            "main-home":main_home,
            "auth-login":auth_login,
            "auth-signup":auth_signup,
            "auth-logout":auth_logout
        }

    def verifyField(self,field,fieldName,mustHaveChar=True,minLen=3,canHaveSpace=False,canHaveSpecialChar=True):
        specialChar="%&{}\\<>*?/$!'\":@+`|="

        if type(field) != str: Exception("HEY! that's not a string?")

        if len(field) == 0 and mustHaveChar: return f"{fieldName} is not filled out."
        if len(field) < minLen: return f"{fieldName} must be greater than {minLen-1} characters."
        if not canHaveSpace and " " in field: return f"{fieldName} cannot contain spaces."
        if not canHaveSpecialChar:
            for char in specialChar:
                if char in field:
                    return f"{fieldName} cannot contain '{char}'"

        return ""
Kraken()
