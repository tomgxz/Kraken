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

db=SQLAlchemy()

class Kraken():

    global db

    def __init__(self):

        import os,sqlite3
        self.os=os
        self.sqlite3=sqlite3

        self.db=db

        self.initFlask()

        self.db.init_app(self.app)

        self.loginManager=LoginManager()
        self.loginManager.login_view="auth_login"
        self.loginManager.init_app(self.app)

        from models import User
        self.User = User

        @self.loginManager.user_loader
        def loadUser(username):
            return self.User.query.get(username)

        self.app.run(host="127.0.0.1",port="1380")

    def initFlask(self):
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"]="secret-key-goes-here"
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.initPages()

    def initPages(self):
        @self.app.route("/")
        def main_index(): return redirect(url_for("auth_login"))

        @self.app.route("/home/")
        @login_required
        def main_home():
            return render_template("home-nosite.html",name=current_user.name)

        @self.app.route("/login/")
        def auth_login(): return render_template("login.html")

        @self.app.route("/login/", methods=["post"])
        def auth_login_post():
            username = request.form.get("username")
            password = request.form.get("password")
            remember = True if request.form.get('remember') else False

            user = self.User.query.filter_by(username=username).first()

            if not user or not check_password_hash(user.password, password):
                flash('Please check your login details and try again.')
                return redirect(url_for('auth_login'))

            login_user(username,remember=remember)
            return redirect(url_for("main_home"))

        @self.app.route("/signup/")
        def auth_signup(): return render_template("signup.html")

        @self.app.route("/signup/", methods=["post"])
        def auth_signup_post():
            # signup validation code here

            name=request.form.get("name")
            email=request.form.get("email")
            username=request.form.get("username")
            password1=request.form.get("password")
            password2=request.form.get("password-repeat")

            #if KrakenDB().rowExists("users","username",f"'{username}'"):
            #    flash("Username already exists")
            #    return redirect(url_for("auth_signup"))

            #if KrakenDB().rowExists("users","email",f"'{email}'"):
            #    flash("Email already in use")
            #    return redirect(url_for("auth_signup"))

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

            user = User.query.filter_by(email=email).first()

            if user:
                flash("That username is already in use")
                return redirect(url_for("auth_login"))

            newUser = User(username=username, email=email, name=name, password=generate_password_hash(password1, method='sha256'))

            self.db.session.add(newUser)
            self.db.session.commit()

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

if __name__ == "__main__":
    Kraken()
