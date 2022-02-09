try:
    from assets.tk.popup import Popup
except ModuleNotFoundError:
    from popup import Popup

class NewSitePopup(Popup):
    def __init__(self,screen,w=int(1920/4),h=int(1080/4)):
        """
        Constructs a :class: 'NewSitePopup <NewSitePopup>'
        """
        self.screen=screen
        self.popupColor=self.screen.colors["accent1"]["normal"]

        self.bgcolor=self.screen.colors["grey"]["100"]

        super().__init__(self.screen,"Create New Site","You will never see this","cancel",self.popupColor,None,w,h)
        self.text.place_forget()

        self.submit=self.screen.tkinter.Button(self.container,text="create",font=self.screen.bodyFont,bg=self.popupColor,command=self.submit)
        self.submit.place(relx=0.95,rely=0.95,anchor="se")

        self.form=self.screen.tkinter.Frame(self.container,bg=self.bgcolor)
        self.form.place(relx=0.5,rely=0.5,anchor="center")

        self.entryContainer,self.entryLabel,self.entryTextVar,self.entryEntry,_=self.screen.generateEntryInput(self.form,"Site Name",entryColor=self.screen.colors["secondary"]["dark"],spacer=False)
        self.entryContainer.configure(bg=self.bgcolor)
        self.entryLabel.configure(bg=self.bgcolor)
        self.entryEntry.configure(bg=self.bgcolor)
        _.configure(bg=self.bgcolor)

    def submit(self):
        self.text.place_forget()
        content=self.entryTextVar.get()

        if len(content) < 4:
            self.text.configure(fg=self.screen.colors["danger"],text="Site names must be at least 4 characters long.")
            self.text.place(relx=0.5,rely=0.3,anchor="center")
            return False

        result=self.screen.master.generateNewSite(content)

        if not result:
            self.text.configure(fg=self.screen.colors["danger"],text="A site with this name already exists!!1")
            self.text.place(relx=0.5,rely=0.3,anchor="center")
            entryText=self.entryTextVar.get()
            suffix="-1"
            if entryText[-2] == "-" and entryText[-1].isdigit():
                suffix=str(int(suffix)-1)
                entryText=entryText[:-2]
            self.entryTextVar.set(entryText+suffix)

        return True

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
