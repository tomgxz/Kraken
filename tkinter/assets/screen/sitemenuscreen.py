try: from assets.screen.screen import Screen
except ModuleNotFoundError: from screen import Screen

class SiteMenuScreen(Screen):
    """ The site options screen for Kraken. Inherits from :class: Screen. """

    def __init__(self,master,root,sitePath):
        """
        Constructs a :class: 'SiteMenuScreen <SiteMenuScreen>'

        :param master object:
            Reference to the master of this class, which should be the main application object
        :param root object:
            The tkinter root
        """

        super().__init__(master,root)

        self.master.logger.info("Generating site menu screen")

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

    def onSettingsIconClickEvent(self,event=None):
        if self.settingsIconClicked: self.settingsIcon.configure(font=self.falightmassive,fg=self.colors["primary"]["normal"])
        else: self.settingsIcon.configure(font=self.fasolidmassive,fg=self.colors["primary"]["dark"])
        self.settingsIconClicked=not self.settingsIconClicked
        return True

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
