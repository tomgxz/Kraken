from flask import Flask

# Flask is the application object

# The main class of the application
class Kraken():
  def __init__(self,host,port):
    # Create the Flask application and set a secret key
    self.app = Flask("Kraken")
    self.app.config["SECRET_KEY"]="secret-key-goes-here"

    # Initialise the website pages
    self.initPages()

    # Run the Flask application
    self.app.run(host=host,port=port)

  def initPages(self):

    # Home page route
    @self.app.route("/")
    def main_index():
      # Display the returned text
      return "This is the homepage!"

if __name__ == "__main__":
  # Initialise the application on port 1380
  Kraken("0.0.0.0",1380)
