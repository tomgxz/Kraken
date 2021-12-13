class Encryption():
    def __init__(self,logger):
        from cryptography.fernet import Fernet
        from dotenv import load_dotenv
        import os

        self.os=os
        self.cryptor=Fernet

        load_dotenv()

        self.usrFile="data/bin/xugz.bin"
        self.pwdFile="data/bin/vugx.bin"

        self.logger=logger

        self.logger.info("Encryption object initialised")

    def getKey(self):
        return self.os.environ.get("KEY").encode()

    def decrypt(self,x):
        return self.cryptor(self.getKey()).decrypt(x).decode()

    def encrypt(self,x):
        return self.cryptor(self.getKey()).encrypt(x.encode())

    def usernameExists(self,usr):
        self.logger.info("Searching for username...")
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            for line in usrs:
                if usr == self.decrypt(line):
                    self.logger.info("Username exists")
                    return True
        self.logger.info("Username does not exist")
        return False

    def credentialsExist(self,usr,pwd):
        self.logger.info("Searching for credentials...")
        usrpos=None
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            itera=0
            for line in usrs:
                if usr == self.decrypt(line):
                    usrpos=itera
                    self.logger.info("Username exists")
                    break
        if usrpos is None:
            self.logger.info("Username does not exist")
            return False
        with open(self.pwdFile,"rb") as pwdList:
            pwds=pwdList.readlines()
            if pwd == self.decrypt(pwds[usrpos]):
                self.logger.info("Password exists")
                return True
        self.logger.info("Password does not exist")
        return False

    def store(self,usr,pwd):
        self.logger.info("Storing Credentials...")
        with open(self.usrFile,"ab") as usrList:
            usrList.write(usr+"\n".encode())
            usrList.close()
        with open(self.pwdFile,"ab") as pwdList:
            pwdList.write(pwd+"\n".encode())
            pwdList.close()
        self.logger.info("Credentials stored")
