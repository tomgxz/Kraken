class Kraken():
    def __init__(self):

        import os,time,threading
        self.os=os
        self.time=time
        self.threading=threading
        self.threads=[]

        import tkinter
        from tkinter.font import Font
        from tkinter import ttk
        self.tkinter=tkinter
        self.tkinterFont=Font
        self.ttk=ttk

        from PIL import ImageTk, Image
        self.pilImageTk=ImageTk
        self.pilImage=Image

        from encryption import Encryption
        self.Encryptor=Encryption()

        self.init()

        self.loginScreen()

        self.root.mainloop()

    def init(self):
        self.root=self.tkinter.Tk()

        self.initGraphics()

        self.root.title("Kraken")
        self.root.tk.call("wm","iconphoto",self.root._w,self.tkinter.PhotoImage(file="assets/images/icon/512-512/kraken-icon-png-primary-512-512.png"))
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry(f"{int(self.w/1.5)}x{int(self.h/1.5)}")
        self.root.minsize(int(1920/2),int(1080/2))
        self.root.state("zoomed")

        self.root.configure(bg=self.bgcolor)

    def initGraphics(self):
        primary   = {"light":"#58a1ee","accent":"#338ceb","normal":"#1c7fe9","dark":"#1263ba"}
        secondary = {"light":"#dd51e1","accent":"#cc23d1","normal":"#a91dae","dark":"#88188c"}
        accent1   = {"light":"#6acbf1","accent":"#57c4ef","normal":"#27b3eb","dark":"#118bbb"}
        accent2   = {"light":"#3a0dbf","accent":"#2e0b99","normal":"#270982","dark":"#1d075f"}
        
        grey = {"100":"#dee2e6","200":"#ced4da","300":"#adb5bd","400":"#81888F","500":"#8d959d","600":"#495057","700":"#343a40","800":"#212529"}

        self.colors={
            "light":"#f8f9fa",
            "dark":"#e9ecef",

            "danger":"#EA5D5C",
            "warning":"#ffc107",
            "success":"#4dbd74",
            
            "primary":primary,
            "secondary":secondary,
            "accent1":accent1,
            "accent2":accent2,
            
            "grey":grey,
        }

        gradientIcon={"64":"assets/images/icon/64-64/kraken-icon-png-gradient-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-gradient-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-gradient-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-gradient-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-gradient.svg"}
        primaryIcon={"64":"assets/images/icon/64-64/kraken-icon-png-primary-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-primary-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-primary-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-primary-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-primary.svg"}
        secondaryIcon={"64":"assets/images/icon/64-64/kraken-icon-png-secondary-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-secondary-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-secondary-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-secondary-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-secondary.png"}

        self.icon={
            "gradient":gradientIcon,
            "primary":primaryIcon,
            "secondary":secondaryIcon,
            "black":"assets/images/icon/svg/kraken-icon-svg-black.svg"
        }

        self.bgcolor=self.colors["light"]

        self.fontPrimary={"family":"Lexend"}
        self.fontSecondary={"family":"Roboto"}

        self.titleFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="36",
            weight="bold"
        )

        self.headerFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="26"
        )

        self.headerFontBold=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="26",
            weight="bold"
        )

        self.subheaderFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="18",
            weight="bold"
        )

        self.captionFontItalic=self.tkinterFont(
            family=self.fontSecondary["family"],
            size="12",
            slant="italic"
        )

        self.bodyFont=self.tkinterFont(
            family=self.fontSecondary["family"],
            size="12"
        )

        self.style = self.ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure(
            "white.Horizontal.TProgressbar",
            borderradius="5",
            troughcolor=self.bgcolor,
            bordercolor=self.bgcolor,
            background=self.colors["primary"]["normal"],
            lightcolor=self.colors["primary"]["light"],
            darkcolor=self.colors["primary"]["light"]
        )

    def generateImage(self,path,w,h):
        img=self.pilImage.open(path)
        img=img.resize((w,h),self.pilImage.ANTIALIAS)
        return self.pilImageTk.PhotoImage(img)

    def introScreen(self):

        def titleTextThread(self):
            text1="Kraken - Loading"
            text2="Kraken - Loading."
            text3="Kraken - Loading.."
            text4="Kraken - Loading..."
            texts=[text1,text2,text3,text4]
            itera=0
            while self.introScreenTitleTextThread:
                self.introScreenTitleTextVariable.set(texts[itera])
                self.time.sleep(0.2)
                itera+=1
                if itera > len(texts)-1:
                    itera=0

        def introBarThread(self):
            for i in range(99):                
                self.introScreenProgressBar.step()        
                self.root.update()
                self.time.sleep(0.03)
            self.clearIntroScreen()
            self.loginScreen()

        self.introScreenContainer=self.tkinter.Frame(self.root,bg=self.bgcolor,width=int(1920/2),height=int(1080/2))
        self.introScreenContainer.place(relx=0.5,rely=0.5,anchor="center")   
                
        self.introScreenTitleTextVariable=self.tkinter.StringVar(self.introScreenContainer,"Kraken - Loading")
        self.introScreenTitleTextThread=True
        
        self.introScreenTitleText=self.tkinter.Label(self.introScreenContainer,textvariable=self.introScreenTitleTextVariable,bg=self.bgcolor,font=self.titleFont)
        self.introScreenTitleText.place(relx=0.5,rely=0.5,anchor="center")

        self.introScreenProgressBar=self.ttk.Progressbar(self.introScreenContainer,orient="horizontal",length=200,mode="determinate",takefocus=True,maximum=100,style='white.Horizontal.TProgressbar')
        self.introScreenProgressBar.place(relx=0.5,rely=0.7,anchor="center")

        self.introScreenImageObject=self.generateImage(self.icon["gradient"]["256"],100,100)
        self.introScreenImage=self.tkinter.Canvas(self.introScreenContainer,width=100,height=100,bg=self.bgcolor,bd=0)
        self.introScreenImage.place(relx=0.5,rely=0.3,anchor="center")
        self.introScreenImage.create_image(52,52,image=self.introScreenImageObject,anchor=self.tkinter.CENTER)

        self.introScreenThread1=self.threading.Thread(target=titleTextThread, args=[self])
        self.threads.append(self.introScreenThread1)
        self.introScreenThread1.start()

        self.introScreenThread2=self.threading.Thread(target=introBarThread, args=[self])
        self.threads.append(self.introScreenThread2)
        self.introScreenThread2.start()

    def clearIntroScreen(self):
        self.introScreenContainer.destroy()

    def loginScreen(self):

        def onSignupOptionClickEvent(e,self):
            self.clearLoginScreen()
            self.signupScreen()

        def onPasswordShowClickEvent(e,self):
            self.loginScreenPasswordEntryShow=self.tkinter.Entry(self.loginScreenPasswordContainer,textvariable=self.loginScreenPasswordTextVar,width=32,fg=self.loginScreenPasswordEntry["fg"],relief="solid")
            self.loginScreenPasswordEntryShow.grid(row=0,column=1)
            
        def onPasswordShowUnclickEvent(e,self):
            self.loginScreenPasswordEntryShow.destroy()
        
        self.loginScreenContainer=self.tkinter.Frame(self.root,bg=self.bgcolor,width=int(1920/2),height=int(1080/2))
        self.loginScreenContainer.place(relx=0.5,rely=0.5,anchor="center")

        self.loginScreenTitleText=self.tkinter.Label(self.loginScreenContainer,text="Kraken - Login / Signup",bg=self.bgcolor,font=self.titleFont)
        self.loginScreenTitleText.place(relx=0.5,rely=0.2,anchor="n")

        self.loginScreenImageObjectSecondary=self.generateImage(self.icon["secondary"]["256"],100,100)
        self.loginScreenImageSecondary=self.tkinter.Canvas(self.loginScreenContainer,width=100,height=100,bg=self.bgcolor,bd=0)
        self.loginScreenImageSecondary.place(relx=0.5,rely=0,anchor="n")
        self.loginScreenImageSecondary.create_image(52,52,image=self.loginScreenImageObjectSecondary,anchor=self.tkinter.CENTER)

        self.loginScreenForm=self.tkinter.Frame(self.loginScreenContainer,bg=self.bgcolor,width=600,height=200)
        self.loginScreenForm.place(relx=0.5,rely=0.55,anchor="center")

        self.loginScreenUsernameContainer,self.loginScreenUsernameLabel,self.loginScreenUsernameTextVar,self.loginScreenUsernameEntry,_=self.generateEntryInput(self.loginScreenForm,"Username",entryColor=self.colors["secondary"]["dark"])

        self.loginScreenPasswordContainer,self.loginScreenPasswordLabel,self.loginScreenPasswordTextVar,self.loginScreenPasswordEntry,self.loginScreenPasswordEye=self.generateEntryInput(self.loginScreenForm,"Password",hidden=True,entryColor=self.colors["primary"]["light"])

        self.loginScreenPasswordEye.bind("<Button-1>",lambda event, self=self: onPasswordShowClickEvent(event,self))
        self.loginScreenPasswordEye.bind("<ButtonRelease-1>",lambda event, self=self: onPasswordShowUnclickEvent(event,self))

        

        self.loginScreenSubmitButton=self.tkinter.Button(
            self.loginScreenContainer,
            text="Submit",
            font=self.subheaderFont,
            bg=self.colors["primary"]["normal"],
            activebackground=self.colors["primary"]["dark"],
            bd=5,
            relief="groove",
            height=1,
            command=self.loginVerify,
        )

        self.loginScreenSubmitButton.place(relx=0.5,rely=0.75,anchor="center")

        self.loginScreenOptionSelector=self.tkinter.Frame(self.loginScreenContainer,bg=self.bgcolor,width=320,height=36)
        self.loginScreenOptionSelector.place(relx=0.5,rely=0.4,anchor="center")

        self.loginScreenLoginOption=self.tkinter.Label(self.loginScreenOptionSelector,font=self.subheaderFont,text="Login",fg=self.colors["primary"]["normal"],bg=self.bgcolor)
        self.loginScreenLoginOption.place(relx=0,rely=0.5,anchor="w")

        self.loginScreenSignupOption=self.tkinter.Label(self.loginScreenOptionSelector,font=self.subheaderFont,text="Sign Up",bg=self.bgcolor)
        self.loginScreenSignupOption.place(relx=1,rely=0.5,anchor="e")

        self.loginScreenSignupOption.bind("<Button-1>",lambda event, self=self: onSignupOptionClickEvent(event,self)) 

    def clearLoginScreen(self):
        self.loginScreenContainer.destroy()

    def signupScreen(self):

        def onLoginOptionClickEvent(e,self):
            self.clearSignupScreen()
            self.loginScreen()

        def onPasswordShow1ClickEvent(e,self):
            self.signupScreenPassword1EntryShow=self.tkinter.Entry(self.signupScreenPassword1Container,textvariable=self.signupScreenPassword1TextVar,width=32,fg=self.signupScreenPassword1Entry["fg"],relief="solid")
            self.signupScreenPassword1EntryShow.grid(row=0,column=1)
            
        def onPasswordShow1UnclickEvent(e,self):
            self.signupScreenPassword1EntryShow.destroy()

        def onPasswordShow2ClickEvent(e,self):
            self.signupScreenPassword2EntryShow=self.tkinter.Entry(self.signupScreenPassword2Container,textvariable=self.signupScreenPassword2TextVar,width=32,fg=self.signupScreenPassword2Entry["fg"],relief="solid")
            self.signupScreenPassword2EntryShow.grid(row=0,column=1)
            
        def onPasswordShow2UnclickEvent(e,self):
            self.signupScreenPassword2EntryShow.destroy()
            
        
        self.signupScreenContainer=self.tkinter.Frame(self.root,bg=self.bgcolor,width=int(1920/2),height=int(1080/2))
        self.signupScreenContainer.place(relx=0.5,rely=0.5,anchor="center")

        self.signupScreenTitleText=self.tkinter.Label(self.signupScreenContainer,text="Kraken - Login / Signup",bg=self.bgcolor,font=self.titleFont)
        self.signupScreenTitleText.place(relx=0.5,rely=0.2,anchor="n")

        self.signupScreenImageObjectSecondary=self.generateImage(self.icon["secondary"]["256"],100,100)
        self.signupScreenImageSecondary=self.tkinter.Canvas(self.signupScreenContainer,width=100,height=100,bg=self.bgcolor,bd=0)
        self.signupScreenImageSecondary.place(relx=0.5,rely=0,anchor="n")
        self.signupScreenImageSecondary.create_image(52,52,image=self.signupScreenImageObjectSecondary,anchor=self.tkinter.CENTER)

        self.signupScreenForm=self.tkinter.Frame(self.signupScreenContainer,bg=self.bgcolor,width=600,height=200)
        self.signupScreenForm.place(relx=0.5,rely=0.6,anchor="center")

        self.signupScreenNameContainer,self.signupScreenNameLabel,self.signupScreenNameTextVar,self.signupScreenNameEntry,_=self.generateEntryInput(self.signupScreenForm,"Name",entryColor=self.colors["secondary"]["dark"])

        self.signupScreenUsernameContainer,self.signupScreenUsernameLabel,self.signupScreenUsernameTextVar,self.signupScreenUsernameEntry,_=self.generateEntryInput(self.signupScreenForm,"Username",entryColor=self.colors["secondary"]["dark"])

        self.signupScreenPassword1Container,self.signupScreen1PasswordLabel,self.signupScreenPassword1TextVar,self.signupScreenPassword1Entry,self.signupScreenPassword1Eye=self.generateEntryInput(self.signupScreenForm,"Password",hidden=True,entryColor=self.colors["primary"]["light"])
        self.signupScreenPassword2Container,self.signupScreen2PasswordLabel,self.signupScreenPassword2TextVar,self.signupScreenPassword2Entry,self.signupScreenPassword2Eye=self.generateEntryInput(self.signupScreenForm,"Repeat Password",hidden=True,entryColor=self.colors["primary"]["light"])

        self.signupScreenPassword1Eye.bind("<Button-1>",lambda event, self=self: onPasswordShow1ClickEvent(event,self))
        self.signupScreenPassword1Eye.bind("<ButtonRelease-1>",lambda event, self=self: onPasswordShow1UnclickEvent(event,self))

        self.signupScreenPassword2Eye.bind("<Button-1>",lambda event, self=self: onPasswordShow2ClickEvent(event,self))
        self.signupScreenPassword2Eye.bind("<ButtonRelease-1>",lambda event, self=self: onPasswordShow2UnclickEvent(event,self))

        self.signupScreenSubmitButton=self.tkinter.Button(
            self.signupScreenContainer,
            text="Submit",
            font=self.subheaderFont,
            bg=self.colors["primary"]["normal"],
            activebackground=self.colors["primary"]["dark"],
            bd=5,
            relief="groove",
            height=1,
            command=self.signupVerify,
        )

        self.signupScreenSubmitButton.place(relx=0.5,rely=0.8,anchor="center")

        self.signupScreenOptionSelector=self.tkinter.Frame(self.signupScreenContainer,bg=self.bgcolor,width=320,height=36)
        self.signupScreenOptionSelector.place(relx=0.5,rely=0.4,anchor="center")

        self.signupScreenLoginOption=self.tkinter.Label(self.signupScreenOptionSelector,font=self.subheaderFont,text="Login",bg=self.bgcolor)
        self.signupScreenLoginOption.place(relx=0,rely=0.5,anchor="w")

        self.signupScreenSignupOption=self.tkinter.Label(self.signupScreenOptionSelector,font=self.subheaderFont,text="Sign Up",fg=self.colors["primary"]["normal"],bg=self.bgcolor)
        self.signupScreenSignupOption.place(relx=1,rely=0.5,anchor="e")

        self.signupScreenLoginOption.bind("<Button-1>",lambda event, self=self: onLoginOptionClickEvent(event,self)) 

    def clearSignupScreen(self):
        self.signupScreenContainer.destroy()

    def loginVerify(self):
        u=self.loginScreenUsernameTextVar.get()
        p=self.loginScreenPasswordTextVar.get()

        if not self.Encryptor.usernameExists(u):
            self.errorMessage("Verification Error","Username not recognised.")
            return False
        
        if not self.Encryptor.credentialsExist(u,p):
            self.errorMessage("Verification Error","Incorrect password.")
            return False

        self.successMessage("Login Successful","You are being logged in")


    def verifyField(self,field,fieldName,mustHaveChar=True,minLen=4,canHaveSpace=False,canHaveSpecialChar=True):
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
            

    def signupVerify(self):
        n=self.signupScreenNameTextVar.get()
        u=self.signupScreenUsernameTextVar.get()
        p1=self.signupScreenPassword1TextVar.get()
        p2=self.signupScreenPassword2TextVar.get()


        res,out=self.verifyField(n,"Name",canHaveSpace=True,canHaveSpecialChar=False)
        
        if res==False:
            self.errorMessage("Validation Error",out)
            return False
        
        res,out=self.verifyField(u,"Usernae",canHaveSpecialChar=False)

        if res==False:
            self.errorMessage("Validation Error",out)
            return False
        
        res,out=self.verifyField(p1,"Password",minLen=8)

        if res==False:
            self.errorMessage("Validation Error",out)
            return False

        if p1 != p2:    
            self.errorMessage("Validation Error","Passwords do not match.")
            return False

        if not self.Encryptor.verify(u):
            self.errorMessage("Validation Error","An account with this username already exists.")
            return False
        
        self.Encryptor.store(self.Encryptor.encrypt(u),self.Encryptor.encrypt(p1))

        self.successMessage("Sign up successful","You can now log in",command=self.loginScreen)

    def errorMessage(self,title,msg):
        def onErrorBackClick(self):
            self.errorBorder.destroy()
        
        self.errorBorder=self.tkinter.Frame(self.root,width=int(1920/4),height=int(1080/4),bg=self.colors["danger"])
        borderWidth=6 # must be even
        self.errorContainer=self.tkinter.Frame(self.errorBorder,bg=self.colors["grey"]["100"],bd=2,width=int(1920/4)-borderWidth,height=int(1080/4)-borderWidth)
        
        self.errorContainer.place(relx=0.5,rely=0.5,anchor="center")
        self.errorBorder.place(relx=0.5,rely=0.5,anchor="center")

        self.errorTitle=self.tkinter.Label(self.errorContainer,text=title,font=self.subheaderFont,bg=self.colors["grey"]["100"])
        self.errorTitle.place(relx=0.5,rely=0.1,anchor="n")

        self.errorMessageText=self.tkinter.Label(self.errorContainer,text=msg,font=self.captionFontItalic,bg=self.colors["grey"]["100"],fg=self.colors["grey"]["600"])
        self.errorMessageText.place(relx=0.5,rely=0.3,anchor="center")

        self.errorBack=self.tkinter.Button(self.errorContainer,text="back",font=self.bodyFont,bg=self.colors["danger"],command=lambda self=self: onErrorBackClick(self))
        self.errorBack.place(relx=0.05,rely=0.95,anchor="sw")

    def successMessage(self,title,msg,command=None):
        def onSuccessBackClick(self):
            self.successBorder.destroy()
            if command is not None:
                command()

        self.successBorder=self.tkinter.Frame(self.root,width=int(1920/4),height=int(1080/4),bg=self.colors["primary"]["normal"])
        borderWidth=6 # must be even
        self.successContainer=self.tkinter.Frame(self.successBorder,bg=self.colors["grey"]["100"],bd=2,width=int(1920/4)-borderWidth,height=int(1080/4)-borderWidth)
        
        self.successContainer.place(relx=0.5,rely=0.5,anchor="center")
        self.successBorder.place(relx=0.5,rely=0.5,anchor="center")

        self.successTitle=self.tkinter.Label(self.successContainer,text=title,font=self.subheaderFont,bg=self.colors["grey"]["100"])
        self.successTitle.place(relx=0.5,rely=0.1,anchor="n")

        self.successMessageText=self.tkinter.Label(self.successContainer,text=msg,font=self.captionFontItalic,bg=self.colors["grey"]["100"],fg=self.colors["grey"]["600"])
        self.successMessageText.place(relx=0.5,rely=0.3,anchor="center")

        self.successBack=self.tkinter.Button(self.successContainer,text="Click here to continue",font=self.bodyFont,bg=self.colors["primary"]["normal"],command=lambda self=self: onSuccessBackClick(self))
        self.successBack.place(relx=0.5,rely=0.5,anchor="c")
        
        
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


       


Kraken()




















