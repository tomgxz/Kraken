from flask_login import UserMixin

# Import the SQLAlchemy database object from the main class
from __init__ import databaseObject as db

# User class to store the user's information in the database
class User(UserMixin,db.Model):
  # Set the name of the table in the database to "user"
  __tablename__="user"

  # Define the columns in the table
  # Primary Key user_id as a string
  user_id = db.Column( db.String, primary_key=True )
  # Name as a string
  name = db.Column( db.String )
  # Email as a string, cannot be null and must be unique
  email = db.Column( db.String, nullable=False, unique=True )
  # Password as a string, cannot be null
  password = db.Column( db.String, nullable=False )
  # Bio as a text field
  bio = db.Column( db.Text )
  # URL as a text field
  url = db.Column( db.Text )
  # Archived flag as a boolean, cannot be null (default False)
  archived = db.Column( db.Boolean, nullable=False )
  # Tab preference as a number, cannot be null (default four)
  tabpreference = db.Column( db.Float, nullable=False )

  # Setup the foreign key relationship
  sites = db.relationship("Site")

  # Function to return the primary key
  def get_id(self): return self.user_id

# Site class to store the User's sites in the database
class Site(db.Model):
  # Set the name of the table in the database to "site"
  __tablename__="site"

  # Define the columns of the table
  # Primary Key site_id as an integer
  site_id = db.Column( db.Integer, primary_key=True )
  # Foreign Key user_id as a string, referring to user_id in the User table
  user_id = db.Column( db.String, db.ForeignKey("user.user_id") )
  # Name as a string, cannot be null
  name = db.Column( db.String, nullable=False )
  # Datecreated as a datetime format
  datecreated = db.Column( db.DateTime )
  # Private flag as a boolean, cannot be null
  private = db.Column( db.Boolean, nullable=False )
  # Deleted flag as a boolean, cannot be null (default False)
  deleted = db.Column( db.Boolean, nullable=False )
  # Sitepath as a text field
  sitePath = db.Column( db.Text )

  # Function to return the primary key
  def get_id(self): return self.site_id
