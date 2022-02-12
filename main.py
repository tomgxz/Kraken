import cherrypy

class Kraken():

    def __init__(self):

        try: import os,sqlite3
        except ModuleNotFoundError:
            print("Module missing, exiting")
            raise SystemExit()

        self.cherrypy=cherrypy
        self.os=os
        self.sqlite3=sqlite3

        try: from encryption import Encryption
        except ModuleNotFoundError:
            print("Module missing, exiting")
            raise SystemExit()

        self.cryptor=Encryption(self)

        self.DB_PATH="./static/db/.db"
        self.db_connection=self.sqlite3.connect(self.DB_PATH)
        self.db_cursor=self.db_connection.cursor()
        self.db_tables=[]

        self.setupDatabase()
        self.initClasses()

        self.config={
            "global":{
                "server.socket_host":"127.0.0.1",
                "server.socket_port":1380,
            },
            "/":{
                "tools.sessions.on":True,
                "tools.staticdir.root":os.path.abspath(os.getcwd())
            },
            "/static":{
                "tools.staticdir.on":True,
                "tools.staticdir.dir":"./static"
            },
            "/generator":{
                "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
                "tools.response_headers.on": True,
                "tools.response_headers.headers": [("Content-Type", "text/plain")],
            }
        }

        cherrypy.engine.subscribe("start",self.setupDatabase)
        self.webapp=self.Home()
        self.webapp.generator=self.AppWebService()
        self.webapp.admin=self.Admin()
        cherrypy.quickstart(self.webapp,"/",self.config)

    def initClasses(self):
        class Home():
            @cherrypy.expose
            def index(self):
                return open("index.html")

        class Admin:
            @cherrypy.expose
            def index(self):
                return "Private area"

        class AppWebService():
            @cherrypy.tools.accept(media="text/plain")
            def GET(self):
                cherrypy.session["ts"] = time.time()
                r = execute("SELECT value FROM user_string WHERE session_id=?",[cherrypy.session.id])
                return r.fetchone()

            def POST(self, length=8):
                some_string = "".join(random.sample(string.hexdigits, int(length)))
                cherrypy.session["ts"] = time.time()
                execute("INSERT INTO user_string VALUES (?, ?)",[cherrypy.session.id, some_string])
                return some_string

            def PUT(self, another_string):
                cherrypy.session["ts"] = time.time()
                execute("UPDATE user_string SET value=? WHERE session_id=?",[another_string, cherrypy.session.id])

            def DELETE(self):
                cherrypy.session.pop("ts", None)
                execute("DELETE FROM user_string WHERE session_id=?",[cherrypy.session.id])

        self.Home=Home
        self.Admin=Admin
        self.AppWebService=AppWebService

    def execute(self,command):
        r=self.db_cursor.execute(command)
        self.db_connection.commit()
        return r

    def createTable(self,name,*a):
        argString=""
        for x in a:
            argString+=f"{x}, "
        r=self.execute(F"CREATE TABLE IF NOT EXISTS {name} ({argString[:-2]})")
        self.db_tables.append(name)
        return r

    def setupDatabase(self):
        self.execute("PRAGMA foreign_keys = ON")
        self.createTable(
            "users",
            "username TEXT PRIMARY KEY",
            "password TEXT"
        )
        self.createTable(
            "sites",
            "site_id INTEGER PRIMARY KEY",
            "user_id INTEGER",
            "sitename TEXT",
            "sitedesc TEXT",
            "siteloc TEXT",
            "FOREIGN KEY (user_id) REFERENCES users(user_id)"
        )


Kraken()
