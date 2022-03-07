class Encryption():
    """ Encryption module for Kraken"""

    def __init__(self,master):
        """
        Constructs a :class: 'Encryption <Encryption>'
        """

        from cryptography.fernet import Fernet
        from dotenv import load_dotenv
        import os

        self.os=os
        self.cryptor=Fernet

        self.master=master

        load_dotenv()

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

        :returns: A boolean reffering to whether the username exists
        :rtype: bool
        """

        x=self.master.execute(f"SELECT EXISTS(SELECT * FROM users WHERE username='{usr}')").fetchone()
        if x[0]==1:
            return True
        return False

    def checkCredentials(self,usr,pwd):
        """
        See whether the username and password combination inputted match in the bin files

        :param usr str:
            A decrypted username to search for
        :param pwd str:
            A decrypted password to search for

        :returns: A boolean reffering to whether the credentials match
        :rtype: bool
        """

        if not self.usernameExists(usr):
            return False
        print(self.decrypt(self.master.execute(f"SELECT password FROM users WHERE username='{usr}'").fetchone()[0]))

    def createUser(self,usr,pwd):
        """
        Stores a username with an encrypted password. Params are passed in decrypted

        :param usr str:
            The username to store as the primary key
        :param pwd str:
            The password to be stored

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        print(f"INSERT INTO users (username password) VALUES ('{usr}','{str(self.encrypt(pwd))[2:]})")
        self.master.execute(f"INSERT INTO users (username password) VALUES ('{usr}','{str(self.encrypt(pwd))[2:]})")
        return True

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
