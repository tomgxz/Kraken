class Popup():
    def __init__(self,screen,title="title",msg="msg",btnText="back",color="#000000",command=None,w=int(1920/4),h=int(1080/4)):
        self.command=command
        
        borderWidth=6 # must be even
        self.border=screen.tkinter.Frame(screen.root,width=w,height=h,bg=color)
        self.container=screen.tkinter.Frame(self.border,bg=screen.colors["grey"]["100"],width=w-borderWidth,height=h-borderWidth)

        self.border.place(relx=0.5,rely=0.5,anchor="center")
        self.container.place(relx=0.5,rely=0.5,anchor="center")

        self.title=screen.tkinter.Label(self.container,text=title,font=screen.subheaderFont,bg=screen.colors["grey"]["100"])
        self.title.place(relx=0.5,rely=0.1,anchor="n")

        self.text=screen.tkinter.Label(self.container,text=msg,font=screen.captionFontItalic,bg=screen.colors["grey"]["100"],fg=screen.colors["grey"]["600"])
        self.text.place(relx=0.5,rely=0.3,anchor="center")

        self.back=screen.tkinter.Button(self.container,text=btnText,font=screen.bodyFont,bg=color,command=self.onBackClick)
        self.back.place(relx=0.05,rely=0.95,anchor="sw")

    def onBackClick(self):
        self.border.destroy()
        if self.command is not None:
            self.command()
        del self