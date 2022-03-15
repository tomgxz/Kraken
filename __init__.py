"""
Dependencies:
    flask
    flask-login
    flask-sqlalchemy
    sqlite3
    pillow
    configparser
    datetime
"""
from flask import Flask, render_template, Blueprint, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from random import choice
from PIL import Image
from configparser import ConfigParser


db=SQLAlchemy()

class Kraken():

    global db

    def __init__(self):

        import os,sqlite3,datetime
        self.os=os
        self.sqlite3=sqlite3
        self.datetime=datetime

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
        self.initPages_main()
        self.initPages_auth()
        self.initPages_site_create()
        self.initPages_settings()

        @self.app.route("/@<name>/<site>")
        @self.app.route("/@<name>/<site>/home")
        @login_required
        def site_edit_home(name=None,site=None):
            if current_user.user_id!=name: return "External view of site"
            return render_template("site-edit-home.html")

    def initPages_main(self):
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

        @self.app.route("/help")
        def main_help():
            return "This page dont exist yet :("

    def initPages_auth(self):
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

    def initPages_site_create(self):
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
            sitedesc = request.form.get("new_site_desc")
            isPublic = request.form.get("new_site_privacy")=="public"

            sitename=replaceRepeatedDashesRecursion(replaceToDash(sitename.lower()))

            session["new_site_sitename"]=sitename
            session["new_site_sitedesc"]=sitedesc
            session["new_site_isPublic"]=isPublic

            return redirect(url_for("site_create_options_1"))

        @self.app.route("/home/new/1")
        @login_required
        def site_create_options_1():
            if not request.referrer == url_for("site_create",_external=True): return redirect(url_for("site_create"))
            return render_template("site-create-options-1.html")

        @self.app.route("/home/new/1", methods=["post"])
        @login_required
        def site_create_options_1_post():
            formOutput = request.form.get("new_site_color_options_dict").split(",")
            colorOptions = {}
            for pair in formOutput:
                x=pair.split(":")
                colorOptions[x[0]]=x[1]

            session["new_site_colorOptions"]=colorOptions

            return redirect(url_for("site_create_options_2"))

        @self.app.route("/home/new/2")
        @login_required
        def site_create_options_2():
            if not request.referrer == url_for("site_create_options_1",_external=True): return redirect(url_for("site_create"))
            return render_template("site-create-options-2.html")

        @self.app.route("/home/new/2", methods=["post"])
        @login_required
        def site_create_options_2_post():
            formOutput = request.form.get("new_site_font_face_list_active").split(",")
            session["new_site_fontOptions"]=formOutput
            return redirect(url_for("site_create_options_3"))

        @self.app.route("/home/new/3")
        @login_required
        def site_create_options_3():
            if not request.referrer == url_for("site_create_options_2",_external=True): return redirect(url_for("site_create"))
            return render_template("site-create-options-3.html")

        @self.app.route("/home/new/3", methods=["post"])
        @login_required
        def site_create_options_3_post():
            formOutput = request.form.get("new_site_style_options_list").split(",")
            styleOptions = {}
            for pair in formOutput:
                x=pair.split(":")
                if x[1] == "false": x[1]=False
                if x[1] == "true": x[1]=True
                if x[1] == "null": x[1]=None
                styleOptions[x[0]]=x[1]
            session["new_site_buttonOptions"]=styleOptions
            return redirect(url_for("site_create_generate"))

        @self.app.route("/home/new/generate")
        @login_required
        def site_create_generate():
            if not request.referrer == url_for("site_create_options_3",_external=True): return redirect(url_for("site_create"))
            siteSettings={
                "name":session["new_site_sitename"],
                "user":str(current_user.user_id),
                "desc":session["new_site_sitedesc"] if session["new_site_sitedesc"]!="" else "No Description Set",
                "created":str(self.datetime.datetime.utcnow()),
                "isPublic":session["new_site_isPublic"],
                "colorOptions":session["new_site_colorOptions"],
                "fontOptions":session["new_site_fontOptions"],
                "buttonOptions":session["new_site_buttonOptions"]
            }
            self.createSiteStructure(siteSettings)

            session["new_site_sitename"]="";session["new_site_sitedesc"]="";session["new_site_isPublic"]="";session["new_site_colorOptions"]={};session["new_site_fontOptions"]=[];session["new_site_buttonOptions"]={}

            return redirect(url_for("site_edit_home",name="@"+siteSettings["user"],site=siteSettings["name"]))

    def initPages_settings(self):
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

        @self.app.route("/account/settings/dev")
        @login_required
        def settings_dev():
            flash(7)
            return render_template("settings-dev.html")

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

        # FILE AND FOLDER GENERATION

        prefix="/static/data/userData/"

        folderStructure=[f"{prefix}{u}",f"{prefix}{u}/sites/"]

        self.generateFolderStructure(folderStructure)

        #pr="/   static/data/defaultIcons/default-"
        #defaultIcons=[f"{pr}1.png"]

        #img=Image.open(choice(defaultIcons))
        #img.save(f"/static/data/userIcons/{u}.png")

        self.db.session.add(newUser)
        self.db.session.commit()

    def createSiteStructure(self,siteSettings):
        sitePath=self.os.path.abspath(f"static/data/userData/{siteSettings['user']}/sites/{siteSettings['name']}")
        siteConfigFile=f"{sitePath}/site.ini"

        folderStructure=[f"{sitePath}",f"{sitePath}/output"]
        fileStructure=[siteConfigFile]

        self.generateFolderStructure(folderStructure)
        self.generateFileStructure(fileStructure)

        with open("txt.txt","w") as f:
            f.write(str(siteSettings))

        cfgContent=ConfigParser()
        cfgContent.read(siteConfigFile)

        section="settings"
        try: cfgContent.add_section(section)
        except: pass

        cfgContent.set(section,"name",siteSettings["name"])
        cfgContent.set(section,"user",siteSettings["user"])
        cfgContent.set(section,"desc",siteSettings["desc"])
        cfgContent.set(section,"isPublic",str(siteSettings["isPublic"]).lower())

        section="color"
        try: cfgContent.add_section(section)
        except: pass

        for key in siteSettings["colorOptions"]:
            cfgContent.set(section,key,siteSettings["colorOptions"][key])

        section="font"
        try: cfgContent.add_section(section)
        except: pass

        cfgContent.set(section,"header",siteSettings["fontOptions"][0])
        cfgContent.set(section,"body",siteSettings["fontOptions"][1])

        section="button"
        try: cfgContent.add_section(section)
        except: pass
        for key in siteSettings["buttonOptions"]:
            cfgContent.set(section,key,str(siteSettings["buttonOptions"][key]).lower())

        with open(siteConfigFile,"w") as f:
            cfgContent.write(f)
            f.close()

    def generateFolderStructure(self,folders):
        for folder in folders:
            if self.os.path.isdir(folder):
                continue
            try:
                self.os.makedirs(folder)
            except OSError as e:
                raise OSError(
                      e)

    def generateFileStructure(self,files):
        for file in files:
            if self.os.path.exists(file):
                continue
            try:
                with open(file,"w") as f:
                    f.close()
            except OSError as e:
                raise OSError(
                      e)

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
