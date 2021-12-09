class Kraken():
    """"""

    def __init__(self):
        """"""
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
            from assets.screen.loginscreen import LoginScreen
            from assets.screen.signupscreen import SignupScreen

            from assets.tk.dangerpopup import DangerPopup
            from assets.tk.successpopup import SuccessPopup
            
        except ModuleNotFoundError as e: # import error
            self.logger.error("Internal module not found - exiting program")
            self.logger.exception(e)
            raise SystemExit
        
        else:
            self.Encryptor=Encryption(self.logger)
            self.dangerPopup=DangerPopup
            self.successPopup=SuccessPopup

        self.logger.info("Classes imported")

        self.init() # generate tkinter

        LoadingScreen(self,self.root) # load up the loading screen

        self.logger.info("Tkinter mainloop started")
        self.root.mainloop()

    def init(self):
        """"""
        self.root=self.tkinter.Tk()

        self.logger.info("Tkinter main root initalised")

        self.root.title("Kraken") # window title
        self.root.tk.call("wm","iconphoto",self.root._w,self.tkinter.PhotoImage(file="assets/images/icon/512-512/kraken-icon-png-primary-512-512.png")) # icon
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry(f"{int(self.w/1.5)}x{int(self.h/1.5)}")
        self.root.minsize(int(1920/2),int(1080/2))
        self.root.state("zoomed") # fullscreen

        self.logger.info("Tkinter main root formatted")

    def initLogger(self):
        """"""
        commands=[] # used to store log commands before the log has been generated, so that they can be appended

        #if not (self.os.path.exists(self.sessionFile) or self.os.path.exists(self.logFile)):
        if self.os.path.exists(self.sessionFile) and self.os.path.exists(self.logFile): # if both files exist, session.txt and latest.log
            with open(self.sessionFile,"r") as f:
                if f.readlines() == []: # if there are no lines in the file
                    commands.append(lambda:self.logger.warning("Session file is empty"))
                self.previousSessionData={line.split(":")[0]:line.split(":")[1] for line in [x.strip("\n") for x in f.readlines()]}
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
        

    def clearAll(self):
        """"""
        for child in self.root.winfo_children():
            child.destroy()

    def loginVerify(self,origin):
        """"""
        u=origin.usernameTextVar.get()
        p=origin.passwordTextVar.get()

        if not self.Encryptor.usernameExists(u):
            self.dangerPopup(origin,"Verification Error","Username not recognised.")
            return False
        
        if not self.Encryptor.credentialsExist(u,p):
            self.dangerPopup(origin,"Verification Error","Incorrect password.")
            return False

        self.successPopup(origin,"Login Successful","You are being logged in",command=self.clearAll)


    def verifyField(self,field,fieldName,mustHaveChar=True,minLen=3,canHaveSpace=False,canHaveSpecialChar=True):
        """"""
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
        """"""
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

        if not self.Encryptor.verify(u):
            self.dangerPopup(origin,"Validation Error","An account with this username already exists.")
            return False
        
        self.Encryptor.store(self.Encryptor.encrypt(u),self.Encryptor.encrypt(p1))

        self.generateUser(u,n)

        self.successPopup(origin,"Sign up successful","You can now log in",command=origin.onLoginOptionClickEvent)
        
    def generateUser(self,usr,name):
        """"""

        userConfigFile=f"data/user/{usr}/user.ini"
        
        folderStructure=[
            f"data/user/{usr}/",
            f"data/user/{usr}/sites/"
        ]

        fileStructure=[
            userConfigFile,
        ]

        for folder in folderStructure:
            if not self.os.path.isdir(folder):
                self.os.makedirs(folder)
        for file in fileStructure:
            with open(file,"w") as f:
                f.close()

        self.generateUserData(userConfigFile,usr,name)

    def generateUserData(self,file,usr,name):
        """"""
        
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

if __name__ == "__main__":
    Kraken()

