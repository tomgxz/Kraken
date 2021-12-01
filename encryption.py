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

    def verify(self,usr):
        with open(self.usrFile,"rb") as usrList:
            usrs=usrList.readlines()
            for line in usrs:
                dec=self.decrypt(line)
                print(dec,usr)
                if usr == dec:
                    return False
        return True

    def store(self,usr,pwd):
        with open(self.usrFile,"ab") as usrList:
            usrList.write(usr+"\n".encode())
            usrList.close()
        with open(self.pwdFile,"ab") as pwdList:
            pwdList.write(pwd+"\n".encode())
            pwdList.close()
