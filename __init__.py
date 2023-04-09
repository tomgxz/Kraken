"""
Dependencies:
    flask
    flask-login
    flask-sqlalchemy
    pillow
    configparser
    datetime
    math

    npm install iframe-resizer --save
"""

# TODO: Fix color picker for site style generation page
# TODO: Add click listener to sections in dropdown
# TODO: make sure you dont render a random site that doesnt exist (line 83)

from flask import Flask, render_template, Blueprint, redirect, url_for, request, flash, session, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

# Flask is the application object
# render_template converts a Jinja file to html
# redirect redirects the website to another route function
# url_for fetches the url of a server resource
# request allows the code to handle form inputs
# flash sends messages to the client
# session allows for the usage of client-side variable storage
# Response is used when handling redirects

# SQLAlchemy manages the SQL database

# LoginManager is the object that manages signed in users
# login_user logs in a give user
# login_required makes sure that you have to be logged in to visit said site
# current_user gets the current logged in user
# logout_user logs out a user

from werkzeug.security import generate_password_hash, check_password_hash

# generate_password_hash and check_password_hash are used when generating and authenticating users

from configparser import ConfigParser
import math

# ConfigParser is used when read/writing the user and site .ini files
# math.floor is used for calculating file size

# Create the database object
databaseObject=SQLAlchemy()

# The main class of the application
class Kraken():
    """ Initializes the Kraken application and runs it on the given host and port

    :param host: The host of the application, given in the format ``"<i>.<i>.<i>.<i>"``
    :type host: str
    :param port: The port of the application
    :type port: int

    :returns: Void
    :rtype: None
    """

    # Global reference to database object
    global databaseObject

    def __init__(self,host:str,port:int) -> None:

        # Assign the database object to the local db reference
        self.db=databaseObject

        # import modules and add them to the object
        import os,datetime
        self.os = os
        self.datetime = datetime

        # Initialise the flask application
        self.initFlask()

        # Initialise the SQL database
        self.db.init_app(self.app)

        # Initialise the login manager
        self.loginManager = LoginManager()
        self.loginManager.login_view = "auth_login" # set which function routes to the login page
        self.loginManager.init_app(self.app)

        # Import the User and Site entities from models.py
        from models import User, Site
        self.User = User
        self.Site = Site

        # Fetches a row from the User table in the database
        @self.loginManager.user_loader
        def loadUser(user_id:str): 
            return self.User.query.get(user_id)

        # Run the Flask application
        self.app.run(host=host,port=port)

    def initFlask(self) -> None:
        """Initializes the Flask application by setting up the ``Flask`` object, configuring certain attributes, 
        and creating the website pages via the function ``self.initPages()``.

        :returns: Void
        :rtype: None
        """

        # Create the Flask application and set a secret key
        self.app = Flask(__name__)
        self.app.config["SECRET_KEY"]="secret-key-goes-here"
        # Set the database file URL to /db.sqlite in the root directory
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Initialise the website pages
        self.initPages()

    def initPages(self) -> None:
        """Assigns the ``Flask.app.route`` functions for all of the application pages.

        :returns: Void
        :rtype: None
        """

        # generate all of the website pages from the jinja2 html files in the /templates folder
        # jinja2 is a way of programatically generating html files using variables, iteration, and templates
        self.initPages_main()
        self.initPages_auth()
        self.initPages_site_create()
        self.initPages_settings()

        @self.app.route("/<name>/<site>/")
        @self.app.route("/<name>/<site>/home/")
        @login_required
        def site_edit_home(name:str="",site:str="") -> str:
            """Page for ``/<name>/<site>`` or ``/<name>/<site>/home``.

            The page contains the basic information about the site, and links to perform actions such as start editing.
            
            Flashes ``1``, the username, and the sitename to the page.

            :param name: The username of the owner of a site
            :type name: str, optional, defaults to ``""``
            :param site: The name of the site
            :type site: str, optional, defaults to ``""``

            :returns: The HTML content of the page, generated from the Jinja template syntax
            :rtype: str
            """

            flash(1)
            flash(name)
            flash(site)

            # If the current user is not the owner, render a different version
            if current_user.user_id != name: return "External view of site"

            return render_template("site-edit-home.html")

        @self.app.route("/<name>/<site>/edit/")
        @login_required
        def site_edit_app(name:str="",site:str="") -> str | Response:
            """Page for ``/<name>/<site>/edit``

            The page contains the editor for a given site. Can only be accessed if the user is the owner.
            
            Flashes ``2``, the username, and the sitename to the page.

            :param name: The username of the owner of a site
            :type name: str, optional, defaults to ``""``
            :param site: The name of the site
            :type site: str, optional, defaults to ``""``

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to the ``site_edit_home`` page if the user does not have the required permissions
            :rtype: str | Response
            """

            flash(2)
            flash(name)
            flash(site)

            # If the current user is not the owner, redirect to the site home
            if current_user.user_id != name: return redirect(url_for("site_edit_home"))

            return render_template("site-edit.html",name=name,site=site)

    def initPages_main(self):
        
        @self.app.route("/")
        def main_index() -> Response: 
            """Page for ``/``

            This page redirects to the login page.

            :returns: A redirect to ``auth_login``
            :rtype: Response
            """

            return redirect(url_for("auth_login"))


        @self.app.route("/home/")
        @login_required # User must be logged in to access this page, or it will redirect to the auth_login page (as setup in the constructor)
        def main_home() -> str:
            """Page for ``/home/``.

            This page is the homepage, containing links to all of the current user's sites.
            
            Requires a user to be logged in.
            
            Flashes a list of the users sites, in the format ``[<userid>,<sitename>,<isprivate>]``, if the user has any sites.

            :returns: The HTML content of the page, generated from the Jinja template syntax
            :rtype: str
            """

            # check to see if user has any sites
            if len(self.Site.query.filter_by(user_id=current_user.user_id).all()) > 0: # and False: 
                flash([[x.user_id,x.name,x.private] for x in self.Site.query.filter_by(user_id=current_user.user_id).all()])

                # For testing and design purposes, the flash command above was commented out 
                # and replaced with this command
                # flash([["user1","Site 1",True],["user1","Epic Webpage",False]])

                return render_template("home-sites.html")
            return render_template("home-nosite.html")

        @self.app.errorhandler(404)
        @self.app.route("/404")
        def main_404(e=None) -> str: return "Page not found - i.e. you made a mistake"

        @self.app.errorhandler(500)
        @self.app.route("/500")
        def main_500(e=None) -> str: return "Server go boom - i.e. I made a mistake"

        @self.app.route("/help")
        def main_help() -> str: return "This page dont exist yet :("

    def initPages_auth(self):

        @self.app.route("/login/")
        def auth_login() -> str | Response:
            """Page for ``/login/``.

            This page is the login page. It contains the login form.

            Will redirect to ``main_home`` if a user is logged in.

            Flashes an empty list of values (``[False,"","","",""]``) to stop errors when generating the Jinja template.

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to the ``main_home`` page if a user is logged in
            :rtype: str | Response
            """

            # Flash an empty list of values to stop errors in the Jinja code
            flash([False,"","","",""])

            # If a user is logged in, redirect to the homepage
            if current_user.is_authenticated: return redirect(url_for("main_home"))
            return render_template("login.html")

        @self.app.route("/login/", methods=["post"])
        def auth_login_post() -> Response:
            """POST method of ``/login/``.

            Fetches the given user information from the form via ``flask.request``, and validates it. The user is logged in if the data is valid,
            and shown an error message if it is not.

            Flashes an appropriate error message, if required.

            :returns: A redirect to the ``main_home`` or ``auth_login`` depending on the success of the login attempt
            :rtype: Response
            """

            # Get the filled-in items from the login form
            username:str = request.form.get("username")
            password:str = request.form.get("password")
            remember:bool = True if request.form.get('remember') else False

            # Fetch the user from the database. if there's no user it returns none
            user = self.User.query.filter_by(user_id=username).first()

            #  Check for correct password
            if not user or not check_password_hash(user.password, password):
                # Flashes true to signify an error, the error message, the username given, and the remember flag given
                # TODO: check whether it should flash True as well
                flash(['Please check your login details and try again.',username,remember])
                return redirect(url_for('auth_login'))

            login_user(user,remember=remember)
            return redirect(url_for("main_home"))

        @self.app.route("/signup/")
        def auth_signup() -> str | Response:
            """Page for ``/signup/``.

            This page is the signup page. It contains the signup form.

            Will redirect to ``main_home`` if a user is logged in.

            Flashes an empty list of values (``[False,"","","",""]``) to stop errors when generating the Jinja template.

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to the ``main_home`` page if a user is logged in
            :rtype: str | Response
            """

            # Flash an empty list of values to stop errors in the Jinja code
            flash([False,"","","",""])

            # If a user is logged in, redirect to the homepage
            if current_user.is_authenticated: return redirect(url_for("main_home"))

            return render_template("signup.html")

        @self.app.route("/signup/", methods=["post"])
        def auth_signup_post() -> Response:
            """POST method of ``/signup/``.

            Fetches the given user information from the form via ``flask.request``, and validates it via ``self.verifyField``. A new user is created if valid,
            or the user is shown an error message if it is not.

            :returns: A redirect to the ``main_home`` or ``auth_signup`` depending on the success of the signup attempt
            :rtype: Response
            """

            # Get the filled-in items from the signup form
            name:str = request.form.get("name")
            email:str = request.form.get("email")
            username:str = request.form.get("username")
            password1:str = request.form.get("password")
            password2:str = request.form.get("password-repeat")

            # the verifyField function returns either an empty string if the field meets the requirements
            # defined by the arguments, or an error message. So, if len(verifyOutput) > 0, that
            # means that the field is invalid

            # Verify the name input and return an error message if invalid
            verifyOutput:str = self.verifyField(name,"Name",canHaveSpace=True,canHaveSpecialChar=True)

            if len(verifyOutput) > 0:
                # Flashes true to signify an error, the error message, the name given (removed due to error), the email given, and the username given
                flash([True,verifyOutput,"",email,username])
                return redirect(url_for("auth_signup"))

            # Verify the email input and return an error message if invalid
            verifyOutput:str = self.verifyField(email,"Email",minLen=0,canHaveSpace=False,canHaveSpecialChar=True)

            if len(verifyOutput) > 0:
                # Flash an error message and the filled in values
                flash([True,verifyOutput,name,"",username])
                return redirect(url_for("auth_signup"))

            verifyOutput:str = self.verifyField(username,"Username",canHaveSpecialChar=False)

            # Verify the username input and return an error message if invalid
            if len(verifyOutput) > 0:
                # Flash an error message and the filled in values
                flash([True,verifyOutput,name,email,""])
                return redirect(url_for("auth_signup"))

            # Verify the password input and return an error message if invalid
            verifyOutput:str = self.verifyField(password1,"Password",minLen=8)

            if len(verifyOutput) > 0:
                # Flash an error message and the filled in values
                flash([True,verifyOutput,name,email,username])
                return redirect(url_for("auth_signup"))

            # Return an error message if the passwords do not match
            if password1!=password2:
                # Flash an error message and the filled in values
                flash([True,"Passwords do not match",name,email,username])
                return redirect(url_for("auth_signup"))

            # check whether this email already has an account
            if self.User.query.filter_by(email=email).first():
                flash([True,"That email is already in use",name,"",username])
                return redirect(url_for("auth_signup"))

            # check whether this username already exists
            user = self.User.query.filter_by(user_id=username).first()

            if user:
                flash([True,"That username is already in use",name,email,""])
                return redirect(url_for("auth_signup"))

            # create a new user in the database and server-side storage
            self.createUser(username,email,name,password1)

            # Log in the new user and redirect them to the homepage
            login_user(self.User.query.filter_by(user_id=username).first(),remember=False)
            return redirect(url_for("auth_login"))

        @self.app.route("/logout/")
        @self.app.route("/account/logout/")
        @login_required
        def auth_logout() -> Response:
            """Method for ``/logout/`` or ``/account/logout/``.
            
            Requires a user to be logged in.
            
            Logs out the current user.

            :returns: A redirect to ``auth_login``
            :rtype: Response
            """

            logout_user()
            return redirect(url_for("auth_login"))

    def initPages_site_create(self):

        @self.app.route("/home/new/")
        @login_required
        def site_create() -> str:
            """Page for ``/home/new/``.

            This page is the first site creation page. It contains inputs such as website name, description, and privacy setting.
            
            Requires a user to be logged in.

            Flashes a list of the user's current site names, to be used in client-side validation of the inputted website name.

            :returns: The HTML content of the page, generated from the Jinja template syntax
            :rtype: str
            """

            # get all current site names for the logged in user, then flash (send) it to the site, where it is processed by the JavaScript
            out:str = ""
            allusernames:list[str] = [x.name for x in self.Site.query.filter_by(user_id=current_user.user_id).all()]

            for name in allusernames: 
                out+=name+","

            flash(out[:-1])

            return render_template("site-create.html")

        @self.app.route("/home/new/", methods=["post"])
        @login_required
        def site_create_post():
            """POST method of ``/home/new/``.

            Fetches the given user information from the form via ``flask.request``, validates it, and stores it in ``flask.session``.

            :returns: A redirect to the ``site_create_options_1``
            :rtype: Response
            """

            def listToStr(var:list) -> str:
                """Turns a list into a string

                :param var: The list to merge
                :type var: list

                :returns: The merged list as a string
                :rtype: str
                """

                out:str = ""
                for char in var: out+=char
                return out
            
            def replaceToDash(var:str) -> str:
                """Replaces any invalid characters in a given string with a dash.
                Used to format the site name correctly so that there arent any errors

                :param var: The string to replace invalid characters
                :type var: string

                :returns: The formatted string
                :rtype: str
                """ 

                var:list[str] = list(var)
                for i in range(len(var)):
                    if var[i] not in "qwertyuiopasdfghjklzxcvbnm-._1234567890": var[i]="-"
                return listToStr(var)
            
            def replaceRepeatedDashesRecursion(var:str) -> str:
                """Removes any adjacent dashes in a string via recursion

                :param var: The string to format
                :type var: str

                :returns: The formatted string
                :rtype: str
                """

                var:list[str] = list(var)
                for i in range(len(var)):

                    # if this is the last character, return
                    if i+1 >= len(var): return listToStr(var)

                    # if this and the next character are dashes
                    if var[i] == "-" and var[i+1] == "-":
                        # remove this character
                        del var[i]
                        var = list(replaceRepeatedDashesRecursion(var))
                        return listToStr(var)

            # get the user inputs
            sitename:str = request.form.get("new_site_name")
            sitedesc:str = request.form.get("new_site_desc")
            isPublic:bool = request.form.get("new_site_privacy")=="public"

            # convert the sitename to lowercase, replace all illegal characters with dashes, and remove adjacent dashes
            sitename:str = replaceRepeatedDashesRecursion(replaceToDash(sitename.lower())) 

            # session can carry over variables between functions
            session["new_site_sitename"] = sitename
            session["new_site_sitedesc"] = sitedesc
            session["new_site_isPublic"] = isPublic

            return redirect(url_for("site_create_options_1"))

        @self.app.route("/home/new/1")
        @login_required
        def site_create_options_1() -> str | Response:
            """Page for ``/home/new/1``.

            This page is the second site creation page. It contains the color palette selection system
            
            Requires a user to be logged in.
            Requires the referrer to be ``site_create``

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to ``site_create`` if ``site_create`` was not the referrer.
            :rtype: str | Response
            """

            # stop people from starting halfway through the form i.e. if they didnt come from the previous site_create page, send them to the start
            if not request.referrer == url_for("site_create",_external=True): return redirect(url_for("site_create"))

            return render_template("site-create-options-1.html")

        @self.app.route("/home/new/1", methods=["post"])
        @login_required
        def site_create_options_1_post() -> Response:
            """POST method of ``/home/new/1``.

            Fetches the given user information from the form via ``flask.request``, validates it, and stores it in ``flask.session``.

            :returns: A redirect to the ``site_create_options_2``
            :rtype: Response
            """

            # new_site_color_options_dict is in the format
            # "key1:value,key2:value,key3:value"
            # so splitting by comma gives ["key1:value","key2:value","key3:value"]
            # then iterate through the list, split by colon, and add parts to dictionary
            
            # split into "k:v" list items
            formOutput:list[str] = request.form.get("new_site_color_options_dict").split(",")

            # create output dictionary
            colorOptions = dict()

            for pair in formOutput: # where pair is in the format "<key>:<value>"
                # split into ["<key>","<value>"]
                colonsplit:list[str] = pair.split(":")

                # append to dictionary - result = {... , "<key>":"<value>"}
                colorOptions[colonsplit[0]] = colonsplit[1]

            # add color options dictionary to session
            session["new_site_colorOptions"] = colorOptions

            # proceed to next page
            return redirect(url_for("site_create_options_2"))

        @self.app.route("/home/new/2")
        @login_required
        def site_create_options_2() -> str | Response:
            """Page for ``/home/new/2``.

            This page is the second third creation page. It contains the typeface selection system.
            
            Requires a user to be logged in.
            Requires the referrer to be ``site_create_options_1``

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to ``site_create`` if ``site_create_options_1`` was not the referrer.
            :rtype: str | Response
            """

            # stop people from starting halfway through the form i.e. if they didnt come from the previous site_create page, send them to the start
            if not request.referrer == url_for("site_create_options_1",_external=True): return redirect(url_for("site_create"))

            return render_template("site-create-options-2.html")

        @self.app.route("/home/new/2", methods=["post"])
        @login_required
        def site_create_options_2_post() -> Response:
            """POST method of ``/home/new/2``.

            Fetches the given user information from the form via ``flask.request``, validates it, and stores it in ``flask.session``.

            :returns: A redirect to the ``site_create_options_3``
            :rtype: Response
            """

            # new_site_font_face_list_active is in the format "<headerfontname>,<paragraphfontname>"
            # so split by comma to get ["<headerfontname>","<paragraphfontname>"]

            # get value from the active form element and split into list
            formOutput:list[str] = request.form.get("new_site_font_face_list_active").split(",")

            # store font selection in session
            session["new_site_fontOptions"]=formOutput

            # proceed to next page
            return redirect(url_for("site_create_options_3"))

        @self.app.route("/home/new/3")
        @login_required
        def site_create_options_3() -> str | Response:
            """Page for ``/home/new/2``.

            This page is the second third creation page. It contains the button styling selection system.
            
            Requires a user to be logged in.
            Requires the referrer to be ``site_create_options_2``

            :returns: The HTML content of the page, generated from the Jinja template syntax OR a redirect to ``site_create`` if ``site_create_options_2`` was not the referrer.
            :rtype: str | Response
            """

            # stop people from starting halfway through the form i.e. if they didnt come from the previous site_create page, send them to the start
            if not request.referrer == url_for("site_create_options_2",_external=True): return redirect(url_for("site_create"))

            return render_template("site-create-options-3.html")

        @self.app.route("/home/new/3", methods=["post"])
        @login_required
        def site_create_options_3_post() -> Response:
            """POST method of ``/home/new/2``.

            Fetches the given user information from the form via ``flask.request``, validates it, and stores it in ``flask.session``.

            :returns: A redirect to the ``site_create_generate``
            :rtype: Response
            """

            # similarly to the colour options, new_site_font_face_list_active is in the format
            # "key1:value,key2:value,key3:value"
            # so splitting by comma gives ["key1:value","key2:value","key3:value"]
            # then iterate through the list, split by colon, and add parts to dictionary

            # split into "k:v" list items
            formOutput:list[str] = request.form.get("new_site_style_options_list").split(",")

            # create output dictionary
            styleOptions = {}

            for pair in formOutput: # where pair is in the format "<key>:<value>"
                # split into ["<key>","<value>"]
                colonsplit:list[str] = pair.split(":")

                # Make sure that all variables are in the correct form
                match colonsplit[1]:
                    case "false": colonsplit[1] = False
                    case "true": colonsplit[1] = True
                    case "null": colonsplit[1] = None

                # append to dictionary - result = {... , "<key>":"<value>"}
                styleOptions[colonsplit[0]] = colonsplit[1]

            # store in session
            session["new_site_buttonOptions"] = styleOptions

            # proceed to site generation
            return redirect(url_for("site_create_generate"))

        @self.app.route("/home/new/generate")
        @login_required
        def site_create_generate() -> Response:
            """Method for ``/home/new/generate``.

            This page is the second third creation page. It contains the button styling selection system.
            
            Requires a user to be logged in.
            Requires the referrer to be ``site_create_options_3``

            :returns: A redirect to the new site homepage (``site_edit_home``) if successful OR a redirect to ``site_create`` if ``site_create_options_3`` was not the referrer.
            :rtype: Response
            """

            # stop people from starting halfway through the form i.e. if they didnt come from the previous site_create page, send them to the start
            if not request.referrer == url_for("site_create_options_3",_external=True): return redirect(url_for("site_create"))

            # Store session data into a dictionary, along with extra paramaters such as when the site was created and the user id
            siteSettings:dict[str,str | self.datetime] = {
                "name": session["new_site_sitename"],
                "user": str(current_user.user_id),
                "desc": session["new_site_sitedesc"] if session["new_site_sitedesc"]!="" else "No Description Set",
                "created": self.datetime.datetime.utcnow(),
                "isPublic": session["new_site_isPublic"],
                "colorOptions": session["new_site_colorOptions"],
                "fontOptions": session["new_site_fontOptions"],
                "buttonOptions": session["new_site_buttonOptions"]
            }

            # Create the site database object and local storage
            self.createSiteStructure(siteSettings)

            # Clear any used session variables
            session["new_site_sitename"] = ""
            session["new_site_sitedesc"] = ""
            session["new_site_isPublic"] = ""
            session["new_site_colorOptions"] = dict()
            session["new_site_fontOptions"] = list()
            session["new_site_buttonOptions"] = dict()

            # Redirect to the site homepage
            return redirect(url_for("site_edit_home",name=siteSettings["user"],site=siteSettings["name"]))

    def initPages_settings(self):
        @self.app.route("/account/settings/")
        @login_required
        def settings() -> Response:
            """Method for ``/account/settings/``.

            This page redirects to the settings homepage (``settings_profile``)

            :returns: A redirect to ``settings_profile``.
            :rtype: Response
            """

            return redirect(url_for("settings_profile"))

        @self.app.route("/account/settings/profile")
        @login_required
        def settings_profile() -> str:
            """Page for ``/account/settings/profile``.

            This page contains the settings Public Profile page.
            
            Requires a user to be logged in.
            
            Flashes ``1`` to inform the local navbar of the current page, and the URL for the user's profile picture.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            # Flash the URL for the user's profile picture
            flash(1,self.getUserImage(current_user.user_id))

            return render_template("settings-profile.html")

        @self.app.route("/account/settings/admin")
        @login_required
        def settings_admin() -> str:
            """Page for ``/account/settings/admin``.

            This page contains the settings Account page.
            
            Requires a user to be logged in.
            
            Flashes ``2`` to inform the local navbar of the current page.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            flash(2)
            return render_template("settings-admin.html")

        @self.app.route("/account/settings/looks")
        @login_required
        def settings_looks() -> str:
            """Page for ``/account/settings/looks``.

            This page contains the settings Appearance and Accessibility page.
            
            Requires a user to be logged in.
            
            Flashes ``3`` to inform the local navbar of the current page.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            flash(3)
            return render_template("settings-looks.html")

        @self.app.route("/account/settings/sites")
        @login_required
        def settings_sites() -> str:
            """Page for ``/account/settings/sites``.

            This page contains the settings My Sites page.
            
            Requires a user to be logged in.
            
            Flashes ``4`` to inform the local navbar of the current page, and a list of all of the user's sites in the format ``[userid,sitename,isprivate,sitesize]``.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            flash(4)

            # flash a list of the user's sites to be used in the site table.
            flash([[x.user_id,x.name,x.private,self.convertByteSize(self.getFolderSize(self.os.path.abspath(x.sitePath)))] for x in self.Site.query.filter_by(user_id=current_user.user_id).all()])
            
            return render_template("settings-sites.html")

        @self.app.route("/account/settings/code")
        @login_required
        def settings_code() -> str:
            """Page for ``/account/settings/``.

            This page contains the settings My Code page.
            
            Requires a user to be logged in.
            
            Flashes ``5`` to inform the local navbar of the current page.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            flash(5)
            return render_template("settings-code.html")

        @self.app.route("/account/settings/dev")
        @login_required
        def settings_dev() -> str:
            """Page for ``/account/settings/``.

            This page contains the settings Developer Settigns page.
            
            Requires a user to be logged in.
            
            Flashes ``7`` to inform the local navbar of the current page.            

            :returns: The HTML content of the page, generated from the Jinja template syntax.
            :rtype: str
            """

            flash(7)
            return render_template("settings-dev.html")

    def createUser(self,u:str,e:str,n:str,p:str) -> None:
        """Creates a new user in the database and in local storage.

        :param u: The username of the new user
        :type u: str
        :param e: The email of the new user
        :type e: str
        :param n: The name of the new user
        :type e: str
        :param p: The password of the new user
        :type p:

        :returns: Void
        :rtype: None
        """

        # Create a new User object using the varaibles given
        newUser = self.User(
            user_id=u,
            name=n,
            email=e,
            password=generate_password_hash(p,method='sha256'),
            bio="",
            url="",
            archived=False,
            tabpreference=4,
        )

        # Server-side folder generation

        prefix:str = "static/data/userData/"

        # create a list of required directories
        folderStructure:list[str] = [
            self.os.path.abspath(f"{prefix}{u}"),
            self.os.path.abspath(f"{prefix}{u}/sites/")
        ]
        
        # create the list of directories in the local storage
        self.generateFolderStructure(folderStructure)

        # add and commit the user to the database
        self.db.session.add(newUser)
        self.db.session.commit()

    def createSiteStructure(self,siteSettings:dict[str,str | any]) -> None:
        """Creates a new site in the database and in local storage.

        :param siteSettings: a dictionary containing the information about the site, with the keys: ``name`` ``user`` ``desc`` ``created`` ``isPublic`` ``colorOptions`` ``fontOptions`` ``buttonOptions``
        :type siteSettings: dict

        :returns: Void
        :rtype: None
        """

        # get the prefix for the site path
        sitePath:str = self.os.path.abspath(f"static/data/userData/{siteSettings['user']}/sites/{siteSettings['name']}")#

        # get the path for the site config file
        siteConfigFile:str = f"{sitePath}/site.ini"#

        # create a list of required directories
        folderStructure:list[str] = [
            f"{sitePath}",
            f"{sitePath}/output",
            f"{sitePath}/files"
        ]

        # create a list of required files
        fileStructure:list[str] = [
            siteConfigFile,
            f"{sitePath}/siteDat.json",
            f"{sitePath}/files/1.html"
        ]

        # create the required directories and files in the local storage
        self.generateFolderStructure(folderStructure)
        self.generateFileStructure(fileStructure)

        # create the JSON file for the site, which contains code locations
        with open(f"{sitePath}/siteDat.json","w") as f: 
            f.write("{\"pages\":{\"Home\":\"1.html\"},\"css\":{},\"js\":{}}")

        # create the default webpage for the site
        with open(f"{sitePath}/files/1.html","w") as f: 
            f.write(self.defaultHtmlPage(siteSettings["name"],siteSettings["desc"],siteSettings["user"]))

        # Create the config parser for the site.ini file
        with ConfigParser() as cfgContent:

            cfgContent.read(siteConfigFile)

            # create the required sections
            for section in ["settings","color","font","button"]:
                try: cfgContent.add_section(section)
                except: pass

            # Add basic information to the settings section
            cfgContent.set("settings","name",siteSettings["name"])
            cfgContent.set("settings","user",siteSettings["user"])
            cfgContent.set("settings","desc",siteSettings["desc"])

            # Add the color palette
            for key in siteSettings["colorOptions"]: 
                cfgContent.set("color",key,siteSettings["colorOptions"][key])

            # Add the typeface
            cfgContent.set("font","header",siteSettings["fontOptions"][0])
            cfgContent.set("font","body",siteSettings["fontOptions"][1])

            # Add any required button styling settings
            for key in siteSettings["buttonOptions"]: 
                cfgContent.set("button",key,str(siteSettings["buttonOptions"][key]).lower())

            # write to the site.ini file
            with open(siteConfigFile,"w") as f:
                cfgContent.write(f)
                f.close()

        # Create a new Site object using the varaibles given
        newSite = self.Site(
            name = siteSettings["name"],
            datecreated = siteSettings["created"],
            private = not siteSettings["isPublic"],
            deleted = False,
            user_id = siteSettings["user"],
            sitePath = sitePath,
        )

        # Add and commit the new site to the database
        self.db.session.add(newSite)
        self.db.session.commit()

    def generateFolderStructure(self,folders:list) -> None:
        """Creates directories in the local storage from the given list, if any of the directories do not already exist

        :param folders: A list of directory paths to create
        :type folders: list

        :returns: Void
        :rtype: None
        """

        for folder in folders: # Iterate through given list of directories
            # Ignore if directory already exists
            if self.os.path.isdir(folder): continue
            # Create the directory
            try: self.os.makedirs(folder)
            except OSError as e: raise e

    def generateFileStructure(self,files:list) -> None:
        """Creates empty files in the local storage from the given list, if any of the files do not already exist

        :param files: A list of file paths to create
        :type files: list

        :returns: Void
        :rtype: None
        """

        for file in files: # Iterate through given list of files
            # Ignore if file already exists
            if self.os.path.exists(file): continue

            try:
                # Create the empty file
                with open(file,"w") as f:
                    if self.os.path.splitext(file)[-1] == ".json": f.write("{\"content\":[]}")
                    f.close()
            except OSError as e: raise e

    def getUserImage(self,u:str) -> str: 
        """Returns the path of a given user's profile picture

        :param u: The username to fetch the profile picture of
        :type u: str

        :returns: A local path of the profile picture
        :rtype: str
        """
        
        return f"/data/userIcons/{u}.png"

    def verifyField(self,field:str,fieldName:str,mustHaveChar:bool=True,minLen:int=3,canHaveSpace:bool=False,canHaveSpecialChar:bool=True) -> str:
        """The validataion system for user inputs implemented in the signup page.

        :param field: The content of the field that is being validated.
        :type field: str
        :param fieldName: The name of the field that is being validated.
        :type fieldName: str
        :param mustHaveChar: Boolean flag determining whether the field must not be empty, defaults to ``True``
        :type mustHaveChar: bool, optional
        :param minLen: The minimum length of the field content, defaults to ``3``
        :type minLen: int, optional
        :param canHaveSpace: Boolean flag determining whether the field can have spaces, defaults to ``False``
        :type canHaveSpace: bool, optional
        :param canHaveSpecialChar: Boolean flag determining whether the field is allowed to contain any of ``%&{}\\<>*?/$!'\":@+|=``, defaults to ``True``
        :type canHaveSpecialChar: bool, optional

        :returns: An empty string if the field is valid OR an error message if the field is invalid
        :rtype: str
        """

        # List of special characters for the canHaveSpecialChar flag
        specialChar:str = "%&{}\\<>*?/$!'\":@+`|="

        # Make sure that the input given is a string, raise an exception if its not
        if type(field) != str: TypeError("HEY! that's not a string?")

        # Check through all the flags given and throw an appropriate error message if input is invalid

        # If it is empty and it must have content
        if len(field) == 0 and mustHaveChar: 
            return f"{fieldName} is not filled out."
        
        # If it is shorter than the minimum length
        if len(field) < minLen: 
            return f"{fieldName} must be greater than {minLen-1} characters."
        
        # If it has spaces when it shouldn't
        if not canHaveSpace and " " in field: 
            return f"{fieldName} cannot contain spaces."
        
        # If it can't have any special characters, and there are special characters in the field
        if not canHaveSpecialChar:
            for char in specialChar:
                if char in field:
                    return f"{fieldName} cannot contain '{char}'"

        return "" # Return an empty string if the input is valid

    def getFolderSize(self,path:str) -> int:
        """Gets the size of a given folder path.

        :param path: The path of the root folder
        :type path: str

        :returns: The size of the folder, in bytes
        :rtype: int
        """

        # Get the size of the base directory, should return 0
        size:int = self.os.path.getsize(path)

        # for all directories and files under the path
        for sub in self.os.listdir(path):
            subPath=self.os.path.join(path,sub) # get the path of the directory / file
            
            # get the size if it is a file
            if self.os.path.isfile(subPath): size+=self.os.path.getsize(subPath)
            
            # get the size if it is a directory
            elif self.os.path.isdir(subPath): size+=self.getFolderSize(subPath)

        # return the size, in bytes
        return size

    def convertByteSize(self,bytes:int) -> str:
        """Converts a given byte value into a human readable version

        :param bytes: The amount of bytes to convert
        :type bytes: int

        :returns: A human readable version of the value
        :rtype: str
        """

        # Zero check
        if bytes==0: return "0B"

        # All possible sizes
        sizes:tuple[str] = ("B","KB","MB","GB","TB","PB","EB","ZB","YB")

        i:int = int(math.floor(math.log(bytes,1024)))
        p:float = math.pow(1024,i)
        s:float = round(bytes/p,2)

        if i==0: s = int(s)

        return f"{s}{sizes[i]}"

    def getSiteCfg(self,siteName:str) -> list[str]:
        """Gets the content of the current user's given site's config file.

        :param siteName: the name of the site to check
        :type siteName: str

        :returns: The content of the config file
        :rtype: list[str]
        """
        
        # Get path of the config file
        cfgPath=self.os.path.abspath(f"static/data/userData/{current_user.user_id}/sites/{siteName}/site.ini")

        # Open a config parser for said path
        cfgContent=ConfigParser()
        cfgContent.read(cfgPath)

        # Return the config parser
        return cfgContent

    def defaultHtmlPage(self,n:str,d:str,u:str):
        """Returns the default HTML content for a new page

        :param n: The name of the site
        :type n: str
        :param d: The description of the site
        :type d: str
        :param u: The name of the owner
        :type u: str

        :returns: The default HTML content for a new page
        :rtype: str
        """
        
        return f"""<div class=\"page\" data-content-parentview></div>"""

if __name__ == "__main__": 
    # Initialise the application on port 1380
    Kraken("0.0.0.0",1380)
