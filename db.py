class KrakenDB():
    def __init__(self):
        import sqlite3
        self.sqlite3=sqlite3

        self.DB_PATH=".db"
        self.db_connection=self.sqlite3.connect(self.DB_PATH)
        self.db_cursor=self.db_connection.cursor()
        self.db_tables=["users"]

    def __del__(self):
        self.db_cursor.close()
        self.db_connection.close()

    def rowExists(self,table,key,value):
        return self.execute(f"SELECT EXISTS(SELECT * FROM {table} WHERE {key}={value})").fetchone()[0]==1

    def createUser(self,username,email,name,password):
        return self.execute(f"INSERT INTO users (username,password,email,name) VALUES ('{username}','{password}','{email}','{name}')")

    def getRow(self,table,key,value):
        return self.execute(f"SELECT * FROM {table} WHERE {key}={value}")

    def passwordMatch(self,pk):
        print("PasswordMatch output",self.execute(f"SELECT password FROM users WHERE username='{pk}'"))

    def execute(self,command):
        r=self.db_cursor.execute(command)
        self.db_connection.commit()
        return r

class User():
    id=None
    email=None
    password=None
    name=None
