try:
    from assets.screen.screen import Screen
except ModuleNotFoundError:
    from screen import Screen

class LoginScreen(Screen):
    def __init__(self,master,root,titleTextA="Kraken",titleTextB="Form"):
        super().__init__(master,root)

        self.master.logger.info("Generating login screen")

        self.container=self.tkinter.Frame(self.root,bg=self.bgcolor,width=self.internalWidth,height=self.internalHeight)
        self.container.place(relx=0.5,rely=0.5,anchor="center")

        self.imageObject=self.generateImage(self.icon["secondary"]["512"],100,100)
        self.image=self.tkinter.Canvas(self.container,width=100,height=100,bg=self.bgcolor,bd=0)
        self.image.place(relx=0.5,rely=0,anchor="n")
        self.image.create_image(52,52,image=self.imageObject,anchor="center")

        self.titleText=self.tkinter.Label(self.container,text="Kraken - Login / Signup",bg=self.bgcolor,font=self.titleFont)
        self.titleText.place(relx=0.5,rely=0.2,anchor="n")

        self.optionSelect=self.tkinter.Frame(self.container,bg=self.bgcolor,width=320,height=36)
        self.optionSelect.place(relx=0.5,rely=0.4,anchor="center")

        self.optionLogin=self.tkinter.Label(self.optionSelect,font=self.subheaderFont,text="Login",bg=self.bgcolor,fg=self.colors["secondary"]["normal"])
        self.optionLogin.place(relx=0,rely=0.5,anchor="w")

        self.optionSignup=self.tkinter.Label(self.optionSelect,font=self.subheaderFont,text="Signup",bg=self.bgcolor)
        self.optionSignup.place(relx=1,rely=0.5,anchor="e")
        self.optionSignup.bind("<Button-1>",self.onSignupOptionClickEvent)

        self.form=self.tkinter.Frame(self.container,bg=self.bgcolor,width=600,height=200)
        self.form.place(relx=0.5,rely=0.55,anchor="center")
        
        self.usernameContainer,self.usernameLabel,self.usernameTextVar,self.usernameEntry,_=self.generateEntryInput(self.form,"Username",entryColor=self.colors["secondary"]["dark"])
        self.passwordContainer,self.passwordLabel,self.passwordTextVar,self.passwordEntry,self.passwordEye=self.generateEntryInput(self.form,"Password",hidden=True,entryColor=self.colors["primary"]["light"])

        self.passwordEye.bind("<Button-1>",self.onPasswordShowClickEvent)
        self.passwordEye.bind("<ButtonRelease-1>",self.onPasswordShowUnclickEvent)

        self.submitBtn=self.tkinter.Button(
            self.container,
            text="Submit",
            font=self.subheaderFont,
            bg=self.colors["secondary"]["normal"],
            activebackground=self.colors["secondary"]["dark"],
            bd=5,
            relief="groove",
            height=1,
            command=lambda x=self: self.master.loginVerify(x)
        )

        self.submitBtn.place(relx=0.5,rely=0.75,anchor="center")

        self.master.logger.info("Login screen generated")

    def onSignupOptionClickEvent(self,e=None):
        try:
            from assets.screen.signupscreen import SignupScreen
        except ModuleNotFoundError:
            from signupscreen import SignupScreen
        SignupScreen(self.master,self.root)
        self.master.logger.info("Login screen cleared")
        self.clear()
        
    def onPasswordShowClickEvent(self,e=None):
        self.passwordShow=self.tkinter.Entry(self.passwordContainer,textvariable=self.passwordTextVar,width=32,fg=self.passwordEntry["fg"],relief="solid")
        self.passwordShow.grid(row=0,column=1)

    def onPasswordShowUnclickEvent(self,e=None):
        self.passwordShow.destroy()
        del self.passwordShow
