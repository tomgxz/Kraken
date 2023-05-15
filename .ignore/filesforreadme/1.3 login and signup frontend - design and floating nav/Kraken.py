from flask import Flask, render_template, redirect, flash

# Flask is the application object
# render_template converts a Jinja file to html
# redirect redirects the website to another root function
# flash sends messages to the client

# The main class of the application
class Kraken():
  def __init__(self,host,port):
    # Create the Flask application and set a secret key
    self.app = Flask(__name__)
    self.app.config["SECRET_KEY"]="secret-key-goes-here"

    # Initialise the website pages
    self.initPages()

    # Run the Flask application
    self.app.run(host=host,port=port)

  def initPages(self):

    # Home page route
    @self.app.route("/")
    def main_home():
      return "Hi o/"

    # Login page route
    @self.app.route("/login/")
    def auth_login():
      return render_template("login.html")

    # Signup page route
    @self.app.route("/signup/")
    def auth_signup():
      return render_template("signup.html")

if __name__ == "__main__":
  # Initialise the application on port 1380
  Kraken("0.0.0.0",1380)
