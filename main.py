class Kraken():
    """ Core application interface for Kraken """

    def __init__(self):
        """ Constructs a :class: 'Kraken <Kraken>' """

        import fontawesome
        
        # import os library here, required to generate logger
        import os
        self.os=os

        # information files
        self.sessionFile="data/session.txt"
        self.logFile="data/log/latest.log"

        # generate the logger
        self.initLogger()
    
        # import required built-in libraries - error catching not required as all python installations will have these
        import time,threading,random,datetime
        self.time=time
        self.threading=threading
        self.threads=[]
        self.random=random
        self.datetime=datetime

        from configparser import ConfigParser
        self.configparser=ConfigParser

        # import tkinter elements
        import tkinter
        from tkinter.font import Font
        from tkinter import ttk
        self.tkinter=tkinter
        self.tkinterFont=Font
        self.ttk=ttk

        # image handling
        try:
            from PIL import ImageTk, Image
            
        except ModuleNotFoundError as e: # import error
            self.logger.error("PIL (pillow) module not found - exiting program")
            self.logger.exception(e)
            raise SystemExit
        
        else:
            self.pilImageTk=ImageTk
            self.pilImage=Image

        self.logger.info("Required modules imported")

        # internal modules
        try:
            from encryption import Encryption

            from assets.screen.loadingscreen import LoadingScreen
            from assets.screen.loginloadingscreen import LoginLoadingScreen
            from assets.screen.loginscreen import LoginScreen
            from assets.screen.menuscreen import MenuScreen
            from assets.screen.screen import Screen
            from assets.screen.signupscreen import SignupScreen

            from assets.tk.popup import Popup
            from assets.tk.dangerpopup import DangerPopup
            from assets.tk.successpopup import SuccessPopup
            from assets.tk.newsitepopup import NewSitePopup
            
        except ModuleNotFoundError as e: # import error
            self.logger.error("Internal module not found - exiting program")
            self.logger.exception(e)
            raise SystemExit
        
        else:
            self.Encryptor=Encryption(self.logger)
            self.popup=Popup
            self.dangerPopup=DangerPopup
            self.successPopup=SuccessPopup
            self.newSitePopup=NewSitePopup

        self.logger.info("Classes imported")

        self.init() # generate tkinter

        LoginScreen(self,self.root) # load up the loading screen

        self.logger.info("Tkinter mainloop started")
        self.root.mainloop()

    def appendSessionFile(self,key,value):
        """
        Adds an entry to the session.txt file found in the data/ directory. Entry is in the format <param key>:<param value>

        :param key str:
            The key of the entry. Will be succeeded by :param value:
        :param value str:
            The value of the entry. Will be prefixed by :param key:

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        
        self.logger.info("Appending data to session file")
        
        with open(self.sessionFile,"r") as f:
            old=f.read()
            f.close()

        with open(self.sessionFile,"w") as f:
            if old != "":
                f.write(f"{old}\n{key}:{value}")
            else:
                f.write(f"{key}:{value}")

        self.logger.info("Data appended to session file")
        
        return True

    def init(self):
        """
        Initialises the application and writes the creation of the application to the session.txt file

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        
        self.root=self.tkinter.Tk()

        self.logger.info("Tkinter main root initalised")

        self.appendSessionFile("datecreated",self.datetime.datetime.now())

        #with open(self.sessionFile,"w") as f:
        #    f.write(f"datecreated:{self.datetime.datetime.now()}")

        self.root.title("Kraken") # window title
        self.root.tk.call("wm","iconphoto",self.root._w,self.tkinter.PhotoImage(file="assets/images/icon/512-512/kraken-icon-png-primary-512-512.png")) # icon
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry(f"{int(self.w/1.5)}x{int(self.h/1.5)}")
        self.root.minsize(int(1920/2),int(1080/2))
        #self.root.state("zoomed") # fullscreen

        self.logger.info("Tkinter main root formatted")

        return True

    def initLogger(self):
        """
        Initialises the logger and resets the log and session file

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        
        commands=[] # used to store log commands before the log has been generated, so that they can be appended

        #if not (self.os.path.exists(self.sessionFile) or self.os.path.exists(self.logFile)):
        if self.os.path.exists(self.sessionFile) and self.os.path.exists(self.logFile): # if both files exist, session.txt and latest.log
            with open(self.sessionFile,"r") as f:
                lines=f.read()
                if lines == "": # if there are no lines in the file
                    commands.append(lambda:self.logger.warning("Session file is empty"))
                    self.previousSessionData={}
                else:
                    self.previousSessionData={line.split(":")[0]:line.split(":")[1] for line in [x.strip("\n") for x in lines.split("\n")]}
                
            open(self.sessionFile,"w").close() # clear file

            logFileInt=1
            logFileName=None
            try:
                logFileName=f"data/log/{self.previousSessionData['datecreated']}-%.log"
            except KeyError as e: # no attribute found in the session data
                commands.append(lambda:self.logger.error("No date created attribute in session file - previous log file will be deleted"))
            else:
                while True:
                    if self.os.path.exists(logFileName.replace("%",str(logFileInt))):
                        logFileInt+=1
                    else:
                        break

                with open(self.logFile,"r") as f1:
                    with open(logFileName.replace("%",str(logFileInt)),"w") as f2:
                        f2.write(f1.read())

            open(self.logFile,"w").close() # clear file

        elif self.os.path.exists(self.sessionFile) and not(self.os.path.exists(self.logFile)): # if latest.log doesnt exist
            commands.append(self.logger.warning("Previous log file does not exist"))
            open(self.logFile,"w").close()

        elif (not self.os.path.exists(self.sessionFile)) and (not self.os.path.exists(self.logFile)): # if neither exists
            commands.append(lambda:self.logger.warning("Previous log file does not exist"))
            commands.append(lambda:self.logger.warning("Session file does not exist"))

            # clear both files
            open(self.logFile,"w").close()
            open(self.sessionFile,"w").close()

        else: # anything else
            commands.append(lambda:self.logger.warning("Session file does not exist"))

            # clear both files
            open(self.logFile,"w").close()
            open(self.sessionFile,"w").close()

        try:
            from assets.log.logger import Logger
            
        except ModuleNotFoundError as e: # import error
            self.logger.error("Internal module not found - exiting program")
            self.logger.exception(e)
            raise SystemExit
        
        else:
            
            self.logger=Logger(sessionFile=self.sessionFile,logFile=self.logFile) # generate the logger

            for command in commands:
                command()

            self.logger.info("Logging initialised")

        return True
        

    def clearAll(self):
        """
        Destroys all tkinter elements except for the main root window

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        
        for child in self.root.winfo_children():
            child.destroy()
        self.logger.info("Cleared all tkinter widgets")
        return True

    def loginVerify(self,origin):
        """
        Verifies the credentials given on the login screen and acts appropriatley. Uses the Encryption class to determine whether the credentials exist

        :param origin object:
            A reference to the object which called this function. In this case, it will be the :LoginScreen:

        :returns: Will return False if the credentials are invalid
        :rtype: bool
        """
        
        u=origin.usernameTextVar.get()
        p=origin.passwordTextVar.get()

        if not self.Encryptor.usernameExists(u):
            self.dangerPopup(origin,"Verification Error","Username not recognised.")
            return False
        
        if not self.Encryptor.credentialsExist(u,p):
            self.dangerPopup(origin,"Verification Error","Incorrect credentials.")
            return False

        self.successPopup(origin,"Login Successful","You are being logged in",command=self.clearAll)
        self.appendSessionFile("username",u)

        self.username=u
        self.userdir=f"data/user/{u}"
        self.usersitesdir=f"{self.userdir}/sites"
        self.usercfg=f"{self.userdir}/user.ini"
        self.userhassites=not self.os.listdir(self.usersitesdir)==[]

        origin.next()


    def verifyField(self,field,fieldName,mustHaveChar=True,minLen=3,canHaveSpace=False,canHaveSpecialChar=True):
        """
        Validates an input from a tkinter entry field.

        :param field str:
            The string to be checked.
        :param fieldName str:
            The name of the tkinter entry containing :field:. Only used for user ease.
        :param mustHaveChar bool:
            (Optional, True) Does the code check to see whether :field: has any characters in.
        :parm minLen int:
            (Optional, 3) What is the minimum length of :field:.
        :param canHaveSpace bool:
            (Optional, False) Can :field: contain spaces.
        :param canHaveSpecialChar bool:
            (Optional, True) Can :field: contain certain special characters (listed below)

        Special characters used in the :canHaveSpecialChar: checking:
            %&{}\\<>*?/$!'\":@+`|=

        :returns: A boolean identifying whether the field is valid, and a string containing the error message if it is not. If the field is valid it will return an empty string.
        :rtype: bool, str
        """
        
        specialChar="%&{}\\<>*?/$!'\":@+`|="
            
        if type(field) != str:
            raise Exception("HEY! thats not a string?")
            
        if len(field) == 0 and mustHaveChar:
            return False,f"{fieldName} is not filled out."
        if len(field) < minLen:
            return False,f"{fieldName} must be greater than {minLen-1} characters."
        if not canHaveSpace and " " in field:
            return False,f"{fieldName} cannot contain spaces."
        if not canHaveSpecialChar:
            for char in specialChar:
                if char in field:
                    return False,f"{fieldName} cannot contain '{char}'"

        return True,""
            

    def signupVerify(self,origin):
        """
        Verifies the credentials given on the signup screen and acts appropriatley. Uses the Encryption class to check the user can exist, and create the user.

        :param origin object:
            A reference to the object which called this function. In this case, it will be the :SignupScreen:
        
        :returns: A boolean determining whether the user was created.
        :rtype: bool
        """
        
        n=origin.nameTextVar.get()
        u=origin.usernameTextVar.get()
        p1=origin.password1TextVar.get()
        p2=origin.password2TextVar.get()


        res,out=self.verifyField(n,"Name",canHaveSpace=True,canHaveSpecialChar=False)
        
        if res==False:
            self.dangerPopup(origin,"Validation Error",out)
            return False
        
        res,out=self.verifyField(u,"Username",canHaveSpecialChar=False)

        if res==False:
            self.dangerPopup(origin,"Validation Error",out)
            return False
        
        res,out=self.verifyField(p1,"Password",minLen=8)

        if res==False:
            self.dangerPopup(origin,"Validation Error",out)
            return False

        if p1 != p2:    
            self.dangerPopup(origin,"Validation Error","Passwords do not match.")
            return False

        if self.Encryptor.usernameExists(u):
            self.dangerPopup(origin,"Validation Error","An account with this username already exists.")
            return False
        
        self.Encryptor.store(self.Encryptor.encrypt(u),self.Encryptor.encrypt(p1))

        self.generateUser(u,n)

        self.successPopup(origin,"Sign up successful","You can now log in",command=origin.onLoginOptionClickEvent)
        
    def generateUser(self,usr,name):
        """
        Generates the nesseccary files for a user to exist.

        :param usr str:
            The username of the user
        :param name str:
            The name of the user

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """

        userConfigFile=f"data/user/{usr}/user.ini"
        
        folderStructure=[
            f"data/user/{usr}/",
            f"data/user/{usr}/sites/"
        ]

        fileStructure=[
            userConfigFile,
        ]

        self.generateFolderStructure(folderStructure)
        self.generateFileStructure(fileStructure)

        self.generateUserData(userConfigFile,usr,name)

        return True

    def generateUserData(self,file,usr,name):
        """
        Generates the user data (config) file

        :param file str:
            The location (path) of the user data file
        :param usr str:
            The username of the user
        :param name str:
            The name of the user

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        
        config=self.configparser()
        config.read(file)
        
        section="user"
        config.add_section(section)

        config.set(section,"name",name)
        config.set(section,"username",usr)
        config.set(section,"created",str(self.datetime.datetime.utcnow())) # time in gb not in us
        config.set(section,"lastsession",str())
        
        with open(file,"w") as f:
            config.write(f)

        return True

    def getSessionData(self):
        """
        Retrieves the data from the session file
        
        :returns: A dictionary of the data
        :rtype: dict
        """
        
        self.logger.info("Retrieving session file data")
        with open(self.sessionFile,"r") as f:
            lines=f.read()
            if lines == "": # if there are no lines in the file
                self.logger.warning("Session file is empty")
                dat={}
            else:
                dat={line.split(":")[0]:line.split(":")[1] for line in [x.strip("\n") for x in lines.split("\n")]}
        self.logger.info("Session file data retrieved")
        return dat


    def generateFolderStructure(self,folders):
        for folder in folders:
            if self.os.path.isdir(folder):
                self.logger.warning(f"Folder {folder} to create already exists, ignoring")
                continue
            try:
                self.os.makedirs(folder)
            except OSError as e:
                self.logger.exception(e)
                raise OSError(	
                      e)

    def generateFileStructure(self,files):
        for file in files:
            if self.os.path.exists(file):
                self.logger.warning(f"File {file} to create already exists, copying file to recovery directory in Kraken files and clearing file")
                raise Exception
            try:
                with open(file,"w") as f:
                    f.close()
            except OSError as e:
                self.logger.exception(e)
                raise OSError(
                      e)

    def createNewSite(self,siteName):
        self.logger.info(f"Generating a new site for user {self.username}")

        sitePath="data/user/{self.username}/sites/{siteName}"

        if self.os.path.exists(sitePath):
            self.logger.warning(f"Site with this name ({siteName}) already exists")
            return False

        siteConfigFile=f"{sitePath}/site.ini"

        folderStructure=[
            f"{sitePath}",
            f"{sitePath}/output",
        ]

        fileStructure=[
            siteConfigFile,
        ]

        self.generateFolderStructure(folderStructure)
        self.generateFileStructure(fileStructure)
        
        self.logger.info(f"Generated a new site with name {siteName} for user {self.username}")

if __name__ == "__main__":
    Kraken()
