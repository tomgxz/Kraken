try:
    from assets.tk.popup import Popup
except ModuleNotFoundError:
    from popup import Popup

class DangerPopup(Popup):
    def __init__(self,screen,title="Error",msg="Please check what you just did was ok",btnText="back",command=None,w=int(1920/4),h=int(1080/4)):
        super().__init__(screen,title,msg,btnText,screen.colors["danger"],command,w,h)
