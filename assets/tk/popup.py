class Popup():
    """ Custom tkinter popup widget for Kraken """
    
    def __init__(self,screen,title="title",msg="msg",btnText="back",color="#000000",command=None,w=int(1920/4),h=int(1080/4)):
        """
        Constructs a :class: 'Popup <Popup>'

        :param screen :
        """
        self.command=command

        self.bgcolor=screen.colors["grey"]["100"]
        
        borderWidth=6 # must be even
        self.border=screen.tkinter.Frame(screen.root,width=w,height=h,bg=color)
        self.container=screen.tkinter.Frame(self.border,bg=self.bgcolor,width=w-borderWidth,height=h-borderWidth)

        self.border.place(relx=0.5,rely=0.5,anchor="center")
        self.container.place(relx=0.5,rely=0.5,anchor="center")

        self.title=screen.tkinter.Label(self.container,text=title,font=screen.subheaderFont,bg=self.bgcolor)
        self.title.place(relx=0.5,rely=0.1,anchor="n")

        self.text=screen.tkinter.Label(self.container,text=msg,font=screen.captionFontItalic,bg=self.bgcolor,fg=screen.colors["grey"]["600"])
        self.text.place(relx=0.5,rely=0.3,anchor="center")

        self.back=screen.tkinter.Button(self.container,text=btnText,font=screen.bodyFont,bg=color,command=self.onBackClick)
        self.back.place(relx=0.05,rely=0.95,anchor="sw")

    def onBackClick(self):
        self.border.destroy()
        if self.command is not None:
            self.command()
        del self

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
