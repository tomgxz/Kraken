class Encryption():
    def __init__(self):
        from cryptography.fernet import Fernet
        from dotenv import load_dotenv
        import os

        self.os=os
        self.cryptor=Fernet

        load_dotenv()

        self.usrFile="assets/bin/xugz.bin"
        self.pwdFile="assets/bin/vugx.bin"

    def getKey(self):
        return self.os.environ.get("KEY").encode()

    def decrypt(self,x):
        return self.cryptor(self.getKey()).decrypt(x).decode()

    def encrypt(self,x):
        return self.cryptor(self.getKey()).encrypt(x.encode())

    def usernameExists(self,usr):
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            for line in usrs:
                if usr == self.decrypt(line):
                    return True
        return False

    def credentialsExist(self,usr,pwd):
        userpos=0
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            itera=0
            for line in usrs:
                if usr == self.decrypt(line):
                    usrpos=itera
                    break
                userpos+=1
        with open(self.pwdFile,"rb") as pwdList:
            pwds=pwdList.readlines()
            if pwd == self.decrypt(pwds[userpos]):
                return True
        return False

    def verify(self,usr):
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            for line in usrs:
                if usr == self.decrypt(line):
                    return False
        return True

    def store(self,usr,pwd):
        with open(self.usrFile,"ab") as usrList:
            usrList.write(usr+"\n".encode())
            usrList.close()
        with open(self.pwdFile,"ab") as pwdList:
            pwdList.write(pwd+"\n".encode())
            pwdList.close()
