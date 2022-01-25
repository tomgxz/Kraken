class Screen():
    """ The tkinter screen for Kraken """
    
    def __init__(self,master,root):
        """
        Constructs a :class: 'Screen <Screen>'

        :param master object:
            Reference to the master of this class, which should be the main application object
        :param root object:
            The tkinter root
        """
                
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
        """ Initialize the screen graphics """
        
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

        self.images={
            "kraken_tentacles_one":"assets/images/kraken_tentacles_one.png"
        }

        self.bgcolor=self.colors["light"]

        self.fontPrimary={"family":"Lexend"}
        self.fontSecondary={"family":"Roboto"}

        self.fafonts={
            "brands":"Font Awesome 6 Brands Regular",
            "duotone":"Font Awesome 6 Duotone Light",
            "light":"Font Awesome 6 Pro Light",
            "regular":"Font Awesome 6 Pro Regular",
            "solid":"Font Awesome 6 Pro Solid",
            "thin":"Font Awesome 6 Pro Thin"
        }

        self.fasizes={"massive":48,"large":"36","medium":"26","caption":"18","small":"12"}

        #self.fatkinterfonts=[]

        for key in self.fafonts:
            for size in self.fasizes:
                exec(f"self.fa{key}{size}=self.tkinterFont(family=self.fafonts['{key}'],size='{self.fasizes[size]}')")
                #eval(f"self.fatkinterfonts.append(self.fa{key}{size})")

        #print(self.fatkinterfonts)
        

        self.falightlarge=self.tkinterFont(
            family=self.fafonts["light"],
            size="36"
        )

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

        self.root.configure(bg=self.bgcolor)

    def clearAll(self):
        """
        Destroys all tkinter elements except for the main root window

        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        for child in self.root.winfo_children():
            child.destroy()
        self.master.logger.info("Cleared all tkinter widgets")
        return True

    def generateImage(self,path,w,h):
        """
        Generate a tkinter image that can be inserted into a tkinter canvas widget

        :param path str:
            The location (path) of the image
        :param w int:
            The desired width of the image
        :param h int:
            The desired height of the imaeg

        :returns: a tkinter image object
        :rtype: object
        """
        
        self.master.logger.info("Generating tkinter image")
        img=self.pilImage.open(path)
        img=img.resize((w,h),self.pilImage.ANTIALIAS)
        img=self.pilImageTk.PhotoImage(img)
        self.master.logger.info("Tkinter image generated")
        return img

    def loadingText(self,obj,x="Kraken",y="Loading"):
        """
        Starts running a loading text loop. It is advisable to only use this in a thread

        :param obj object:
            A reference to the tkinter StringVar widget
        :param x str:
            (Optional, "Kraken") The first part of the text to be displayed. If set to None, it will only display :param: y
        :param y str:
            (Optional, "Loading") The second part of the text to be displayed. If set to None, it will only display :param: x
        """
        
        self.master.logger.info("Loading text started")
        texts=[
            f"{x} - {y}",
            f"{x} - {y}.",
            f"{x} - {y}..",
            f"{x} - {y}...",
        ]

        if x == None:
            texts=[
                f"{y}",
                f"{y}.",
                f"{y}..",
                f"{y}...",
            ]

        if y == None:
            texts=[
                f"{x}",
                f"{x}.",
                f"{x}..",
                f"{x}...",
            ]

        itera=0
        while True:
            obj.set(texts[itera])
            self.time.sleep(0.2)
            itera+=1
            if itera > len(texts)-1:
                itera=0

    def generateProgressBar(self,parent,length,style="white"):
        """
        Generates a tkinter progress bar widget

        :param parent object:
            A reference to the parent tkinter widget
        :param length int:
            The length of the progress bar
        :param style str:
            (Optional, "white") A string reffering to the custom style of the progressbar

        :returns: the unplaced tkinter widget
        :rtype: object
        """
        
        return self.ttk.Progressbar(parent,orient="horizontal",length=length,mode="determinate",takefocus=True,maximum=100,style=f'{style}.Horizontal.TProgressbar')

    def generateEntryInput(self,parent,name,entryColor="black",hidden=False):
        """
        Generates a tkinter entry widget

        :param parent object:
            A reference to the parent tkinter widget
        :param name str:
            The name to be displayed next to the entry
        :param length int:
            The length of the entry
        :param entryColor str:
            (Optional, "black") The color of the entry text. Can be a hex code or a valid color name
        :param hidden bool:
            (Optional, False) Determines whether the entry is hidden, such as a password field

        :returns: All of the components of the entry: the container, label, stringvar, entry and label containing the reveal button. The label contianing the reveal button will be empty if :param: hidden is false (or unchanged)
        :rtype: object, object, object, object, object
        """
        
        container=self.tkinter.Frame(parent,bg=self.bgcolor)
        container.pack(side="top",anchor="e")

        label=self.tkinter.Label(container,bg=self.bgcolor,text=name,font=self.captionFontItalic)
        label.grid(row=0,column=0,ipadx=10)

        textvar=self.tkinter.StringVar()

        showCharOld="█"

        if hidden:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid",show="_")
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="👁",font=self.tkinterFont(size="14"))
            label2.grid(row=0,column=2)
        else:
            entry=self.tkinter.Entry(container,textvariable=textvar,width=32,fg=entryColor,relief="solid")
            label2=self.tkinter.Label(container,bg=self.bgcolor,text="⠀⠀",font=self.captionFontItalic)
            label2.grid(row=0,column=2,padx=0.4)

        entry.grid(row=0,column=1)
            

        return container,label,textvar,entry,label2

    def progressBarThread(self,x,command=None,randomMin=0.001,randomMax=0.05):
        """
        Starts running a progress bar loop. It is advisable to only use this in a thread

        :param x object:
            A reference to the progress bar object
        :param command:
            (Optional, None) A command to be run when the progress bar finishes. Will not run anything if set to none.
        :param randomMin float:
            (Optional, 0.001) The minimum wait time between progress bar steps
        :param randomMax float:
            (Optional, 0.05) The maximum wait time between progress bar steps            
        """
        
        self.master.logger.info("Progress bar started")
        threadTime="random"
        threadSleep=0.1
            
        for i in range(99):
            x.step()
            self.root.update()
            self.time.sleep(threadSleep if threadTime=="set" else self.random.uniform(randomMin,randomMax))
        if command is not None:
            command()

    def onElementHover(self,e,color):
        e.widget.config(bg=self.colors[color]["dark"])

    def onElementHoverExit(self,e,color):
        e.widget.config(bg=self.colors[color]["normal"])

    def onTextHover(self,e,color,colored=True):
        if colored:
            e.widget.config(fg=self.colors[color]["dark"])
        else:
            e.widget.config(fg=self.colors["grey"]["800"])

    def onTextHoverExit(self,e,color,colored=True):
        if colored:
            e.widget.config(fg=self.colors[color]["normal"])
        else:
            e.widget.config(fg=self.colors["dark"])

    def initElementHover(self,e,color):
        e.bind("<Enter>", lambda event, color=color: self.onElementHover(event,color))
        e.bind("<Leave>", lambda event, color=color: self.onElementHoverExit(event,color))

    def initTextHover(self,e,color,colored=True):
        e.bind("<Enter>", lambda event, color=color, colored=colored: self.onTextHover(event,color,colored))
        e.bind("<Leave>", lambda event, color=color, colored=colored: self.onTextHoverExit(event,color,colored))

    def clear(self):
        """ Clear the screen """
        try:
            self.container.destroy()
        except:
            self.clearAll()
        self.master.logger.info("Screen deleted")
        del self

if __name__ == "__main__":
    import dis

    dis.dis(Screen)
    
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
