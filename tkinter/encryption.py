class Encryption():
    """ Encryption module for Kraken"""
    
    def __init__(self,logger):
        """
        Constructs a :class: 'Encryption <Encryption>'

        :param logger object:
            A refference to the logging object used throughout the Kraken code
        """
        
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
        """
        Generates and returns the encryption key

        :returns: An byte-encoded string
        :rtype: str
        """
        
        return self.os.environ.get("KEY").encode()

    def decrypt(self,x):
        """
        Decrypts a string. The string must have been encoded by this module.
        
        :param x str:
            The encrypted string to decrypt.

        :returns: The decrypted string
        :rtype: str
        """
        
        return self.cryptor(self.getKey()).decrypt(x).decode()

    def encrypt(self,x):
        """
        Encrypts a string.

        :param x str:
            The string to encrypt.

        :returns: The encrypted byte-encoded string
        :rtype: str
        """
        
        return self.cryptor(self.getKey()).encrypt(x.encode())

    def usernameExists(self,usr):
        """
        See whether a username exists in the username bin file

        :param usr str:
            A decrypted username to search for

        :returns: A boolean reffering to whether the username exists in the file
        :rtype: bool
        """
        
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
        """
        See whether the username and password combination inputted match in the bin files

        :param usr str:
            A decrypted username to search for
        :param pwd str:
            A decrypted password to search for

        :returns: A boolean reffering to whether the credentials match
        :rtype: bool
        """
        
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
                itera+=1
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
        """
        Stores an encrypted username and password. Both paramaters must have been previously encrypted by this module.

        :param usr str:
            An encrypted byte-encoded string containing the username to store
        :param pwd str:
            An encrypted byte-encoded string containing the password to store

        :returns: A boolea determining whether the process was successful
        :rtype: bool
        """
        
        self.logger.info("Storing Credentials...")
        with open(self.usrFile,"ab") as usrList:
            usrList.write(usr+"\n".encode())
            usrList.close()
        with open(self.pwdFile,"ab") as pwdList:
            pwdList.write(pwd+"\n".encode())
            pwdList.close()
        self.logger.info("Credentials stored")
        return True

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
