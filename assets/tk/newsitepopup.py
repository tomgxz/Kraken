try:
    from assets.tk.popup import Popup
except ModuleNotFoundError:
    from popup import Popup

class NewSitePopup(Popup):
    def __init__(self,screen,w=int(1920/4),h=int(1080/4)):
        """
        Constructs a :class: 'NewSitePopup <NewSitePopup>'
        """
        self.popupColor=screen.colors["accent1"]["normal"]
        
        super().__init__(screen,"Create New Site","You will never see this","cancel",self.popupColor,None,w,h)
        self.text.place_forget()
        self.text.destroy()

        self.submit=screen.tkinter.Button(self.container,text="create",font=screen.bodyFont,bg=self.popupColor,command=self.submit)
        self.submit.place(relx=0.95,rely=0.95,anchor="se")

        self.form=screen.tkinter.Frame(self.container,bg=screen.colors["grey"]["100"])
        self.form.place(relx=0.5,rely=0.5,anchor="center")
        
        self.entryContainer,self.entryLabel,self.entryTextVar,self.entryEntry,_=screen.generateEntryInput(self.form,"Site Name",entryColor=screen.colors["secondary"]["dark"],spacer=False)
        self.entryContainer.configure(bg=self.screen.color["primary"]["normal"])
        self.entryEntry.configure(bg=self.bgcolor)


    def submit(self):
        content=self.entryTextVar.get()
        print(content)
        

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
