from flask import Flask, render_template, redirect, flash, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Flask is the application object
# render_template converts a Jinja file to html
# redirect redirects the website to another route function
# flash sends messages to the client
# request allows the code to handle form inputs
# url_for fetches the url of a server resource
# SQLAlchemy manages the SQL database

# Create the database object
databaseObject = SQLAlchemy()

# The main class of the application
class Kraken():

  # Global reference to database object
  global databaseObject

  def __init__(self,host,port):
    # Assign the database object to the local db reference
    self.db=databaseObject

    # Initialise the flask application
    self.initFlask()

    # Initialise the SQL database
    self.db.init_app(self.app)

    # Import the User and Site entities from models.py
    from models import User, Site
    self.User=User
    self.Site=Site

    # Run the Flask application
    self.app.run(host=host,port=port)

  def initFlask(self):
    # Create the Flask application and set a secret key
    self.app = Flask(__name__)
    self.app.config["SECRET_KEY"]="secret-key-goes-here"
    self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
    # Set the database file URL to /db.sqlite in the root directory
    self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialise the website pages
    self.initPages()

  def initPages(self):

    # Home page route
    @self.app.route("/")
    def main_home():
      return "Hi o/"

    # Login page route
    @self.app.route("/login/")
    def auth_login():
      # Flash an empty list of values to stop errors in the Jinja code
      flash([False,"","","",""])
      return render_template("login.html")

    # Login post route
    @self.app.route("/login/", methods=["post"])
    def auth_login_post():
      # Get the filled-in items from the login form
      username = request.form.get("username")
      password = request.form.get("password")
      remember = True if request.form.get('remember') else False

      # TODO: get the user from the database. if there's no user it returns none
      if False:
        # Flashes true to signify an error, the error message, the username given, and the remember flag given
        flash([True,'Please check your login details and try again.',username,remember])
        return redirect(url_for('auth_login'))

      # TODO: check for correct password
      if False:
        flash([True,'Please check your login details and try again.',username,remember])
        return redirect(url_for('auth_login'))

      # TODO: login user
      return redirect(url_for("main_home"))

    # Signup page route
    @self.app.route("/signup/")
    def auth_signup():
      # Flash an empty list of values to stop errors in the Jinja code
      flash([False,"","","",""])
      return render_template("signup.html")

    # Signup post route
    @self.app.route("/signup/", methods=["post"])
    def auth_signup_post():
      # Get the filled-in items from the signup form
      name=request.form.get("name")
      email=request.form.get("email")
      username=request.form.get("username")
      password1=request.form.get("password")
      password2=request.form.get("password-repeat")

      # the verifyField function returns either an empty string if the field meets the requirements
      # defined by the arguments, or an error message. So, if len(verifyOutput) > 0, that
      # means that the field is invalid

      # Verify the name input and return an error message if invalid
      verifyOutput=self.verifyField(name,"Name",canHaveSpace=True,canHaveSpecialChar=True)

      if len(verifyOutput) > 0:
        # Flashes true to signify an error, the error message, the name given (removed due to error), the email given, and the username given
        flash([True,verifyOutput,"",email,username])
        return redirect(url_for("auth_signup"))

      # Verify the email input and return an error message if invalid
      verifyOutput=self.verifyField(email,"Email",minLen=0,canHaveSpace=False,canHaveSpecialChar=True)

      if len(verifyOutput) > 0:
        # Flash an error message and the filled in values
        flash([True,verifyOutput,name,"",username])
        return redirect(url_for("auth_signup"))

      # Verify the username input and return an error message if invalid
      verifyOutput=self.verifyField(username,"Username",canHaveSpecialChar=False)

      if len(verifyOutput) > 0:
        # Flash an error message and the filled in values
        flash([True,verifyOutput,name,email,""])
        return redirect(url_for("auth_signup"))

      # Verify the password input and return an error message if invalid
      verifyOutput=self.verifyField(password1,"Password",minLen=8)

      if len(verifyOutput) > 0:
        # Flash an error message and the filled in values
        flash([True,verifyOutput,name,email,username])
        return redirect(url_for("auth_signup"))

      # Return an error message if the passwords do not match
      if password1!=password2:
        # Flash an error message and the filled in values
        flash([True,"Passwords do not match",name,email,username])
        return redirect(url_for("auth_signup"))

      # TODO: check whether this email already has an account

      if False:
        flash([True,"That email is already in use",name,"",username])
        return redirect(url_for("auth_signup"))

      # TODO: check whether this username already exists

      if False:
        flash([True,"That username is already in use",name,email,""])
        return redirect(url_for("auth_signup"))

      # TODO: create a new user in the database

      return redirect(url_for("auth_login"))

  def verifyField(self,field,fieldName,mustHaveChar=True,minLen=3,canHaveSpace=False,canHaveSpecialChar=True):
    # List of special characters for the canHaveSpecialChar flag
    specialChar="%&{}\\<>*?/$!'\":@+`|="

    # Make sure that the input given is a string, raise an exception if its not
    if type(field) != str: Exception("HEY! that's not a string?")

    # Check through all the flags given and throw an appropriate error message if input is invalid
    if len(field) == 0 and mustHaveChar: return f"{fieldName} is not filled out."
    if len(field) < minLen: return f"{fieldName} must be greater than {minLen-1} characters."
    if not canHaveSpace and " " in field: return f"{fieldName} cannot contain spaces."
    if not canHaveSpecialChar:
      for char in specialChar:
        if char in field:
          return f"{fieldName} cannot contain '{char}'"

    return "" # Return an empty string if the input is valid

if __name__ == "__main__":
  # Initialise the application on port 1380
  Kraken("0.0.0.0",1380)
