class Kraken():
    def __init__(self):

        import os,time,threading,random,datetime
        self.os=os
        self.time=time
        self.threading=threading
        self.threads=[]
        self.random=random
        self.datetime=datetime

        import tkinter
        from tkinter.font import Font
        from tkinter import ttk
        self.tkinter=tkinter
        self.tkinterFont=Font
        self.ttk=ttk

        from PIL import ImageTk, Image
        self.pilImageTk=ImageTk
        self.pilImage=Image

        from configparser import ConfigParser
        self.configparser=ConfigParser

        from encryption import Encryption
        self.Encryptor=Encryption()

        self.init()

        from assets.screen.loadingscreen import LoadingScreen
        from assets.screen.loginscreen import LoginScreen
        from assets.screen.signupscreen import SignupScreen

        from assets.tk.dangerpopup import DangerPopup
        from assets.tk.successpopup import SuccessPopup

        self.dangerPopup=DangerPopup
        self.successPopup=SuccessPopup
        
        LoadingScreen(self,self.root)

        self.root.mainloop()

    def init(self):
        self.root=self.tkinter.Tk()

        self.root.title("Kraken")
        self.root.tk.call("wm","iconphoto",self.root._w,self.tkinter.PhotoImage(file="assets/images/icon/512-512/kraken-icon-png-primary-512-512.png"))
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry(f"{int(self.w/1.5)}x{int(self.h/1.5)}")
        self.root.minsize(int(1920/2),int(1080/2))
        self.root.state("zoomed")

    def clearAll(self):
        for child in self.root.winfo_children():
            child.destroy()


    def loginVerify(self,origin):
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
        
        
    def generateEntryInput(self,parent,name,entryColor="black",hidden=False):
        container=self.tkinter.Frame(parent,bg=self.bgcolor)
        container.pack(side="top",anchor="e")

        label=self.tkinter.Label(container,bg=self.bgcolor,text=name,font=self.captionFontItalic)
        label.grid(row=0,column=0,ipadx=10)

        textvar=self.tkinter.StringVar()

        showCharOld="█"

        if hidden:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid",show="_",)
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="👁",font=self.tkinterFont(size="14"))
            label2.grid(row=0,column=2)
        else:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid")
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="⠀⠀",font=self.captionFontItalic)
            label2.grid(row=0,column=2,padx=0.4)

        entry.grid(row=0,column=1)
            

        return container,label,textvar,entry,label2

    def generateUser(self,usr,name):

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


Kraken()

