try:
    from assets.tk.popup import Popup
except ModuleNotFoundError:
    from popup import Popup

class SuccessPopup(Popup):
    def __init__(self,screen,title="Success",msg="You can now do something",btnText="continue",command=None,w=int(1920/4),h=int(1080/4)):
        super().__init__(screen,title,msg,btnText,screen.colors["primary"]["normal"],command,w,h)
        self.back.place(relx=0.5,rely=0.5,anchor="c")
