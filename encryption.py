class Encryption():
    def __init__(self):
        from cryptography.fernet import Fernet
        from dotenv import load_dotenv
        import os

        self.os=os
        self.cryptor=Fernet

        load_dotenv()

    def getKey(self):
        return self.os.environ.get("KEY").encode()

    def decrypt(self,x):
        return self.cryptor(self.getKey()).decrypt(x).decode()

    def encrypt(self,x):
        return self.cryptor(self.getKey()).encrypt(x.encode())
