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
from random import choice
from PIL import Image

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

        from models import User, Site
        self.User = User
        self.Site = Site

        @self.loginManager.user_loader
        def loadUser(user_id):
            return self.User.query.get(user_id)

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
            if False:
                return render_template("home-sites.html")
            return render_template("home-nosite.html")

        @self.app.errorhandler(404)
        def main_404(e): return "Page not found - i.e. you made a mistake"

        @self.app.errorhandler(500)
        def main_500(e): return "Server go boom - i.e. I made a mistake"

        @self.app.route("/home/new/")
        @login_required
        def site_create():
            def getSiteNames(user_id): return self.Site.query.filter_by(user_id=user_id).all()

            return render_template("site-create.html",passedFunction_getSiteNames=getSiteNames)

        @self.app.route("/home/new/", methods=["post"])
        @login_required
        def site_create_post():

            def listToStr(var):
                out=""
                for char in var:
                    out+=char
                return out
            def replaceToDash(var):
                var=list(var)
                for i in range(len(var)):
                    if var[i] not in "qwertyuiopasdfghjklzxcvbnm-._1234567890":
                        var[i]="-"
                return listToStr(var)
            def replaceRepeatedDashesRecursion(var):
                var=list(var)
                for i in range(len(var)):
                    if i+1 >= len(var):
                        return listToStr(var)
                    if var[i] == "-" and var[i+1] == "-":
                        del var[i]
                        var = list(replaceRepeatedDashesRecursion(var))
                        return listToStr(var)

            sitename = request.form.get("new_site_name")
            isPublic = request.form.get("new_site_privacy")=="public"

            sitename=replaceRepeatedDashesRecursion(replaceToDash(sitename.lower()))

            return sitename

            return redirect(url_for("site_create_options"))

        @self.app.route("/home/new/1")
        @login_required
        def site_create_options_1():
            return render_template("site-create-options-1.html")

        @self.app.route("/account/settings/")
        @login_required
        def settings():
            return redirect(url_for("settings_profile"))

        @self.app.route("/account/settings/profile")
        @login_required
        def settings_profile():
            flash(1,self.getUserImage(current_user.user_id))
            return render_template("settings-profile.html")

        @self.app.route("/account/settings/admin")
        @login_required
        def settings_admin():
            flash(2)
            return render_template("settings-admin.html")

        @self.app.route("/account/settings/looks")
        @login_required
        def settings_looks():
            flash(3)
            return render_template("settings-looks.html")

        @self.app.route("/account/settings/sites")
        @login_required
        def settings_sites():
            flash(4)
            return render_template("settings-sites.html")

        @self.app.route("/account/settings/code")
        @login_required
        def settings_code():
            flash(5)
            return render_template("settings-code.html")

        @self.app.route("/help")
        def main_help():
            return "This page dont exist yet :("

        @self.app.route("/account/settings/dev")
        @login_required
        def settings_dev():
            flash(7)
            return render_template("settings-dev.html")

        @self.app.route("/login/")
        def auth_login():
            if current_user.is_authenticated:
                return redirect(url_for("main_home"))
            return render_template("login.html")

        @self.app.route("/login/", methods=["post"])
        def auth_login_post():
            username = request.form.get("username")
            password = request.form.get("password")
            remember = True if request.form.get('remember') else False

            user = self.User.query.filter_by(user_id=username).first()

            if not user or not check_password_hash(user.password, password):
                flash('Please check your login details and try again.')
                return redirect(url_for('auth_login'))

            login_user(user,remember=remember)
            return redirect(url_for("main_home"))

        @self.app.route("/signup/")
        def auth_signup():
            if current_user.is_authenticated:
                return redirect(url_for("main_home"))
            return render_template("signup.html")

        @self.app.route("/signup/", methods=["post"])
        def auth_signup_post():
            # signup validation code here

            name=request.form.get("name")
            email=request.form.get("email")
            username=request.form.get("username")
            password1=request.form.get("password")
            password2=request.form.get("password-repeat")

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

            user = self.User.query.filter_by(email=email).first()

            if user:
                flash("That email is already in use")
                return redirect(url_for("auth_login"))

            user = self.User.query.filter_by(user_id=username).first()

            if user:
                flash("That username is already in use")
                return redirect(url_for("auth_login"))

            self.createUser(username,email,name,password1)

            return redirect(url_for("auth_login"))

        @self.app.route("/account/logout/")
        @login_required
        def auth_logout():
            logout_user()
            return redirect(url_for("auth_login"))

    def createUser(self,u,e,n,p):
        newUser = self.User(
            user_id=u,
            name=n,
            email=e,
            password=generate_password_hash(p, method='sha256'),
            bio="",
            url="",
            archived=False,
            tabpreference=4,
        )

        #pr="/   static/data/defaultIcons/default-"
        #defaultIcons=[f"{pr}1.png"]

        #img=Image.open(choice(defaultIcons))
        #img.save(f"/static/data/userIcons/{u}.png")

        self.db.session.add(newUser)
        self.db.session.commit()

    def getUserImage(self,u):
        return f"/data/userIcons/{u}.png"

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
