class Screen():
    def __init__(self,master,root):
        master.logger.info("Generating screen")
        
        self.master=master
        self.root=root

        import os,time,threading,random,datetime
        self.os=os
        self.time=time
        self.threading=threading
        self.threads=[]
        self.random=random
        self.datetime=datetime

        import tkinter
        from tkinter.font import Font
        from tkinter import ttk
        self.tkinter=tkinter
        self.tkinterFont=Font
        self.ttk=ttk

        from PIL import ImageTk, Image
        self.pilImageTk=ImageTk
        self.pilImage=Image

        from configparser import ConfigParser
        self.configparser=ConfigParser

        self.init()

        self.internalWidth=int(1920/2)
        self.internalHeight=int(1080/2)

        self.master.logger.info("Screen generated")
        
    def init(self):

        self.initGraphics()

        self.root.configure(bg=self.bgcolor)

    def initGraphics(self):
        self.master.logger.info("Initializing screen graphics")
        
        primary   = {"light":"#58a1ee","accent":"#338ceb","normal":"#1c7fe9","dark":"#1263ba"}
        secondary = {"light":"#dd51e1","accent":"#cc23d1","normal":"#a91dae","dark":"#88188c"}
        accent1   = {"light":"#6acbf1","accent":"#57c4ef","normal":"#27b3eb","dark":"#118bbb"}
        accent2   = {"light":"#3a0dbf","accent":"#2e0b99","normal":"#270982","dark":"#1d075f"}
        
        grey = {"100":"#dee2e6","200":"#ced4da","300":"#adb5bd","400":"#81888F","500":"#8d959d","600":"#495057","700":"#343a40","800":"#212529"}

        self.colors={
            "light":"#f8f9fa",
            "dark":"#e9ecef",

            "danger":"#EA5D5C",
            "warning":"#ffc107",
            "success":"#4dbd74",
            
            "primary":primary,
            "secondary":secondary,
            "accent1":accent1,
            "accent2":accent2,
            
            "grey":grey,
        }

        gradientIcon={"64":"assets/images/icon/64-64/kraken-icon-png-gradient-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-gradient-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-gradient-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-gradient-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-gradient.svg"}
        primaryIcon={"64":"assets/images/icon/64-64/kraken-icon-png-primary-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-primary-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-primary-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-primary-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-primary.svg"}
        secondaryIcon={"64":"assets/images/icon/64-64/kraken-icon-png-secondary-64-64.png","128":"assets/images/icon/128-128/kraken-icon-png-secondary-128-128.png","256":"assets/images/icon/256-256/kraken-icon-png-secondary-256-256.png","512":"assets/images/icon/512-512/kraken-icon-png-secondary-512-512.png","svg":"assets/images/icon/svg/kraken-icon-svg-secondary.png"}

        self.icon={
            "gradient":gradientIcon,
            "primary":primaryIcon,
            "secondary":secondaryIcon,
            "black":"assets/images/icon/svg/kraken-icon-svg-black.svg"
        }

        self.bgcolor=self.colors["light"]

        self.fontPrimary={"family":"Lexend"}
        self.fontSecondary={"family":"Roboto"}

        self.titleFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="36",
            weight="bold"
        )

        self.headerFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="26"
        )

        self.headerFontBold=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="26",
            weight="bold"
        )

        self.subheaderFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="18",
            weight="bold"
        )

        self.captionFontItalic=self.tkinterFont(
            family=self.fontSecondary["family"],
            size="12",
            slant="italic"
        )

        self.bodyFont=self.tkinterFont(
            family=self.fontSecondary["family"],
            size="12"
        )

        self.style = self.ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure(
            "white.Horizontal.TProgressbar",
            borderradius="5",
            troughcolor=self.bgcolor,
            bordercolor=self.bgcolor,
            background=self.colors["primary"]["normal"],
            lightcolor=self.colors["primary"]["light"],
            darkcolor=self.colors["primary"]["light"]
        )

    def clearAll(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.master.logger.info("Cleared all tkinter widgets")

    def generateImage(self,path,w,h):
        self.master.logger.info("Generating tkinter image")
        img=self.pilImage.open(path)
        img=img.resize((w,h),self.pilImage.ANTIALIAS)
        img=self.pilImageTk.PhotoImage(img)
        self.master.logger.info("Tkinter image generated")
        return img

    def loadingText(self,obj,x="Kraken",y="Loading"):
        self.master.logger.info("Loading text started")
        texts=[
            f"{x} - {y}",
            f"{x} - {y}.",
            f"{x} - {y}..",
            f"{x} - {y}...",
        ]

        itera=0
        while True:
            obj.set(texts[itera])
            self.time.sleep(0.2)
            itera+=1
            if itera > len(texts)-1:
                itera=0

    def generateProgressBar(self,parent,length,style="white"):               
        return self.ttk.Progressbar(parent,orient="horizontal",length=length,mode="determinate",takefocus=True,maximum=100,style=f'{style}.Horizontal.TProgressbar')

    def generateEntryInput(self,parent,name,entryColor="black",hidden=False):
        container=self.tkinter.Frame(parent,bg=self.bgcolor)
        container.pack(side="top",anchor="e")

        label=self.tkinter.Label(container,bg=self.bgcolor,text=name,font=self.captionFontItalic)
        label.grid(row=0,column=0,ipadx=10)

        textvar=self.tkinter.StringVar()

        showCharOld="█"

        if hidden:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid",show="_",)
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="👁",font=self.tkinterFont(size="14"))
            label2.grid(row=0,column=2)
        else:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid")
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="⠀⠀",font=self.captionFontItalic)
            label2.grid(row=0,column=2,padx=0.4)

        entry.grid(row=0,column=1)
            

        return container,label,textvar,entry,label2

    def progressBarThread(self,x,command=None,randomMin=0.001,randomMax=0.05):
        self.master.logger.info("Progress bar started")
        threadTime="random"
        threadSleep=0.1
            
        for i in range(99):
            x.step()
            self.root.update()
            self.time.sleep(threadSleep if threadTime=="set" else self.random.uniform(randomMin,randomMax))
        if command is not None:
            command()

    def clear(self):
        self.container.destroy()
        self.master.logger.info("Screen deleted")
        del self
