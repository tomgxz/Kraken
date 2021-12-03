from screen import Screen

class SignupScreen(Screen):
    def __init__(self,master,root,titleTextA="Kraken",titleTextB="Form"):
        super().__init__(master,root)

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

        self.optionLogin=self.tkinter.Label(self.optionSelect,font=self.subheaderFont,text="Login",bg=self.bgcolor)
        self.optionLogin.place(relx=0,rely=0.5,anchor="w")
        self.optionLogin.bind("<Button-1>",self.onLoginOptionClickEvent)

        self.optionSignup=self.tkinter.Label(self.optionSelect,font=self.subheaderFont,text="Signup",bg=self.bgcolor,fg=self.colors["secondary"]["normal"])
        self.optionSignup.place(relx=1,rely=0.5,anchor="e")

        self.form=self.tkinter.Frame(self.container,bg=self.bgcolor,width=600,height=200)
        self.form.place(relx=0.5,rely=0.6,anchor="center")

        self.nameContainer,self.nameLabel,self.nameTextVar,self.nameEntry,_=self.generateEntryInput(self.form,"Name",entryColor=self.colors["secondary"]["dark"])
        self.usernameContainer,self.usernameLabel,self.usernameTextVar,self.usernameEntry,_=self.generateEntryInput(self.form,"Username",entryColor=self.colors["secondary"]["dark"])
        
        self.password1Container,self.password1Label,self.password1TextVar,self.password1Entry,self.password1Eye=self.generateEntryInput(self.form,"Password",hidden=True,entryColor=self.colors["primary"]["normal"])
        self.password2Container,self.password2Label,self.password2TextVar,self.password2Entry,self.password2Eye=self.generateEntryInput(self.form,"Repeat Password",hidden=True,entryColor=self.colors["primary"]["normal"])

        self.password1Eye.bind("<Button-1>",self.onPassword1ShowClickEvent)
        self.password1Eye.bind("<ButtonRelease-1>",self.onPassword1ShowUnclickEvent)

        self.password2Eye.bind("<Button-1>",self.onPassword2ShowClickEvent)
        self.password2Eye.bind("<ButtonRelease-1>",self.onPassword2ShowUnclickEvent)

        self.submitBtn=self.tkinter.Button(
            self.container,
            text="Submit",
            font=self.subheaderFont,
            bg=self.colors["secondary"]["normal"],
            activebackground=self.colors["secondary"]["dark"],
            bd=5,
            relief="groove",
            height=1,
            command=self.master.loginVerify,
        )

        self.submitBtn.place(relx=0.5,rely=0.8,anchor="center")

    def onLoginOptionClickEvent(self,e):
        from loginscreen import LoginScreen
        LoginScreen(self.master,self.root)
        self.clear()
        
    def onPassword1ShowClickEvent(self,e):
        self.password1Show=self.tkinter.Entry(self.password1Container,textvariable=self.password1TextVar,width=32,fg=self.password1Entry["fg"],relief="solid")
        self.password1Show.grid(row=0,column=1)

    def onPassword1ShowUnclickEvent(self,e):
        self.password1Show.destroy()
        del self.password1Show

    def onPassword2ShowClickEvent(self,e):
        self.password2Show=self.tkinter.Entry(self.password2Container,textvariable=self.password2TextVar,width=32,fg=self.password2Entry["fg"],relief="solid")
        self.password2Show.grid(row=0,column=1)

    def onPassword2ShowUnclickEvent(self,e):
        self.password2Show.destroy()
        del self.password2Show

