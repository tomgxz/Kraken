try:
    from assets.screen.screen import Screen
except ModuleNotFoundError:
    from screen import Screen

class MenuScreen(Screen):
    """ The tkinter login screen for Kraken. Inherits from :class: Screen. """

    def __init__(self,master,root):
        """
        Constructs a :class: 'MenuScreen <MenuScreen>'

        :param master object:
            Reference to the master of this class, which should be the main application object
        :param root object:
            The tkinter root
        """

        super().__init__(master,root)

        self.master.logger.info("Generating menu screen")

        self.sidebarBg=self.colors["grey"]["100"]
        self.sidebar=self.tkinter.Frame(self.root,bg=self.sidebarBg,width=100,height=self.master.h)
        self.sidebar.pack(expand=False,fill="both",side="left",anchor="nw")

        self.master.sidebarLogo=self.tkinter.Canvas(self.sidebar,width=100,height=100,bg=self.sidebarBg,bd=0,highlightthickness=0)
        self.master.sidebarLogo.pack()
        self.master.sidebarLogo.create_image(52,52,image=self.master.sidebarLogoObject,anchor="center")

        self.settingsIcon=self.tkinter.Label(self.sidebar,text="\uf013",font=self.falightmassive,fg=self.colors["primary"]["normal"],bg=self.sidebarBg)
        self.settingsIcon.place(relx=0.5,rely=0.95,anchor="s")
        self.settingsIconClicked=False
        self.settingsIcon.bind("<Button-1>",self.onSettingsIconClickEvent)

        self.columnpad1=self.tkinter.Frame(self.root,bg=self.bgcolor,width=32,height=self.master.h)
        self.columnpad1.pack(expand=False,fill="both",side="left",anchor="nw")

        self.content=self.tkinter.Frame(self.root,bg=self.bgcolor,width=int(self.master.minwidth-100),height=self.master.minheight)
        self.content.pack(expand=True,fill="both",side="right")

        text="Welcome, user"
        sessionDat=self.master.getSessionData()
        if "username" in sessionDat:
            text=f"Welcome, {sessionDat['username']}"

        self.title=self.tkinter.Label(self.content,text=text,font=self.titleFont,bg=self.bgcolor)
        self.title.grid(row=0,column=0,sticky="nw")

        if not self.master.userhassites:
            self.emptyContainer=self.tkinter.Frame(self.content,bg=self.bgcolor,width=468,height=int(self.master.minwidth/2))
            self.emptyContainer.place(relx=0.5,rely=0.5,anchor="center")

            self.master.emptyImage=self.tkinter.Canvas(self.emptyContainer,bg=self.bgcolor,width=468,height=211,highlightthickness=0)
            self.master.emptyImage.pack()
            self.master.emptyImage.create_image(int(468/2),int(211/2),image=self.master.emptyImageObject,anchor="center")

            self.emptyText1=self.tkinter.Label(self.emptyContainer,text="Looks Pretty Empty Here...",font=self.headerFontBold,bg=self.bgcolor,width=468)
            self.emptyText1.pack()

            self.emptyText2=self.tkinter.Label(self.emptyContainer,text="Maybe you should create a new site?",font=self.subheaderFont,bg=self.bgcolor,width=468,fg=self.colors["primary"]["normal"])
            self.emptyText2.pack()

            self.emptyText2.bind("<Button-1>",self.createNewSiteBtnClick)

            self.initTextHover(self.emptyText2,color="primary")

        if self.master.userhassites:
            self.contentHeaderContainer=self.tkinter.Frame(self.content,bg=self.bgcolor)
            self.contentHeaderContainer.grid(row=1,column=0,sticky="n")

            self.caption=self.tkinter.Label(self.contentHeaderContainer,text="Your sites:",font=self.headerFont,bg=self.bgcolor)
            self.caption.grid(row=1,column=0,sticky="nw")

            self.newSiteBtnContainer=self.tkinter.Frame(self.contentHeaderContainer,bg=self.bgcolor)
            self.newSiteBtnContainer.grid(row=1,column=1,sticky="ne")

            self.newSiteBtn=self.tkinter.Button(self.newSiteBtnContainer,
                text="Create New Site",
                font=self.subheaderFont,
                bg=self.colors["accent1"]["normal"],
                activebackground=self.colors["accent1"]["dark"],
                bd=5,
                relief="groove",
                height=1,
                command=self.createNewSiteBtnClick
            )

            self.newSiteBtn.pack(side="right")

            self.siteList=self.tkinter.Frame(self.content,bg=self.bgcolor)
            self.siteList.grid(row=2,column=0,sticky="n")

            sites=self.master.os.listdir(self.master.usersitesdir)
            for site in enumerate(sites):
                sites[site[0]]=f"{self.master.os.path.abspath(self.master.usersitesdir)}\\{site[1]}\\"
            self.siteListElements={}
            colorItera=[
                self.colors["primary"]["light"],
                self.colors["secondary"]["light"],
                self.colors["accent1"]["normal"]
            ]
            colorIteraHover=[
                self.colors["primary"]["normal"],
                self.colors["secondary"]["normal"],
                self.colors["accent1"]["dark"]
            ]
            itera=0
            for site in sites:
                siteConfig=self.configparser()
                siteConfig.read(f"{site}site.ini")
                sitename=siteConfig.get("site","sitename")
                color=colorItera[itera%3]
                focussedDict=self.siteListElements[siteConfig.get("site","sitename")]={}
                focussedDict["frame"]=self.tkinter.Frame(self.siteList,width=300,height=150,bg=color)
                focussedDict["title"]=self.tkinter.Label(focussedDict["frame"],bg=color,text=sitename,font=self.subheaderFont)
                focussedDict["frame"].bind("<Enter>",lambda event,color=colorIteraHover[itera%3],focussedDict=focussedDict:self.siteElementOnMouseEnter(event,color,focussedDict))
                focussedDict["frame"].bind("<Leave>",lambda event,color=color,focussedDict=focussedDict:self.siteElementOnMouseExit(event,color,focussedDict))
                itera+=1

            for item in self.siteListElements:
                focussed=self.siteListElements[item]
                focussed["frame"].pack(padx=32,pady=16)
                focussed["title"].place(x=4,y=4)

        self.master.logger.info("Menu screen generated")

    def siteElementOnMouseEnter(self,event,color,elementGroup):
        elementGroup["frame"].configure(bg=color)
        elementGroup["title"].configure(bg=color)

    def siteElementOnMouseExit(self,event,color,elementGroup):
        elementGroup["frame"].configure(bg=color)
        elementGroup["title"].configure(bg=color)

    def createNewSiteBtnClick(self,event=None):
        try:self.newSiteBtn.configure(state="disabled",bg=self.colors["grey"]["400"])
        except:pass
        try:self.emptyText2.unbind("<Button-1>")
        except:pass
        self.master.newSitePopup(self)

    def next(self):
        """ Move the window to the next screen, defined in the function. """

        try:
            from assets.screen.loginloadingscreen import LoginLoadingScreen
        except ModuleNotFoundError:
            from loginloadingscreen import LoginLoadingScreen
        LoginLoadingScreen(self.master,self.root)
        self.master.logger.info("Login screen cleared")
        self.clear()

    def onSettingsIconClickEvent(self,event=None):
        if self.settingsIconClicked:
            self.settingsIcon.configure(font=self.falightmassive,fg=self.colors["primary"]["normal"])
        else:
            self.settingsIcon.configure(font=self.fasolidmassive,fg=self.colors["primary"]["dark"])

        self.settingsIconClicked=not self.settingsIconClicked

        return True


if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
