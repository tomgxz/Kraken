from flask_login import UserMixin
from __init__ import db

class User(UserMixin,db.Model):
    __tablename__="user"
    user_id = db.Column( db.String, primary_key=True)
        # PK user_id TEXT NOT NULL
    name = db.Column( db.String )
        # name TEXT
    email = db.Column( db.String, nullable=False, unique=True)
        # email TEXT NOT NULL UNIQUE
    password = db.Column( db.String, nullable=False)
        # password TEXT NOT NULL
    bio = db.Column( db.Text )
        # bio TEXT
    url = db.Column( db.Text )
        # url TEXT
    archived = db.Column( db.Boolean, nullable=False)
        # archived BOOLEAN NOT NULL (default False)
    tabpreference = db.Column( db.Float, nullable=False )
        # tabpreference INT NOT NULL (default four)
    sites = db.relationship("Site")
        # setup the foreign key

    def get_id(self): return self.user_id

class Site(db.Model):
    __tablename__="site"
    site_id = db.Column( db.Integer, primary_key=True)
        # PK site_id INT NOT NULL
    user_id = db.Column( db.String, db.ForeignKey("user.user_id"))
        # FK user_id TEXT NOT NULL (referecene User)
    name = db.Column( db.String, nullable=False)
        # name TEXT NOT NULL
    datecreated = db.Column( db.DateTime )
        # datecreated DATE
    private = db.Column( db.Boolean, nullable=False)
        # private BOOLEAN NOT NULL
    deleted = db.Column( db.Boolean, nullable=False)
        # deleted BOOLEAN NOT NULL
    staticpath = db.Column( db.Text )
        # staticpath TEXT

    def get_id(self): return self.site_id
