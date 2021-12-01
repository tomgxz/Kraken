class Kraken():
    def __init__(self):

        import os,time,threading
        self.os=os
        self.time=time
        self.threading=threading
        self.threads=[]

        import tkinter
        from tkinter.font import Font
        from tkinter import ttk
        self.tkinter=tkinter
        self.tkinterFont=Font
        self.ttk=ttk

        from PIL import ImageTk, Image
        self.pilImageTk=ImageTk
        self.pilImage=Image
        
        self.init()

        self.introScreen()

        self.root.mainloop()

    def init(self):
        self.root=self.tkinter.Tk()

        self.initGraphics()

        self.root.title("Kraken")
        self.root.tk.call("wm","iconphoto",self.root._w,self.tkinter.PhotoImage(file="assets/images/icon/512-512/kraken-icon-png-primary-512-512.png"))
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry(f"{int(self.w/1.5)}x{int(self.h/1.5)}")
        self.root.minsize(int(self.w/2),int(self.h/2))
        self.root.state("zoomed")

        self.root.configure(bg=self.bgcolor)

    def initGraphics(self):
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

        self.captionFont=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="20"
        )

        self.captionFontItalic=self.tkinterFont(
            family=self.fontPrimary["family"],
            size="20",
            slant="italic"
        )

        self.bodyFont=self.tkinterFont(
            family=self.fontPrimary["family"],
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

    def generateImage(self,path,w,h):
        img=self.pilImage.open(path)
        img=img.resize((w,h),self.pilImage.ANTIALIAS)
        return self.pilImageTk.PhotoImage(img)

    def introScreen(self):
        self.introScreenContainer=self.tkinter.Frame(self.root,bg=self.bgcolor,width=int(self.root.winfo_width()/2),height=int(self.root.winfo_height()/2))
        self.introScreenContainer.place(relx=0.5,rely=0.5,anchor="center")

        def titleTextThread(self):
            text1="Kraken - Loading"
            text2="Kraken - Loading."
            text3="Kraken - Loading.."
            text4="Kraken - Loading..."
            texts=[text1,text2,text3,text4]
            itera=0
            while self.introScreenTitleTextThread:
                self.introScreenTitleTextVariable.set(texts[itera])
                self.time.sleep(0.2)
                itera+=1
                if itera > len(texts)-1:
                    itera=0

        def introBarThread(self):
            for i in range(99):                
                self.introScreenProgressBar.step()        
                self.root.update()
                self.time.sleep(0.05)
                
    
        self.introScreenTitleTextVariable=self.tkinter.StringVar(self.introScreenContainer,"Kraken - Loading")
        self.introScreenTitleTextThread=True
        
        self.introScreenTitleText=self.tkinter.Label(self.introScreenContainer,textvariable=self.introScreenTitleTextVariable,bg=self.bgcolor,font=self.titleFont)
        self.introScreenTitleText.place(relx=0.5,rely=0.5,anchor="center")

        self.introScreenProgressBar=self.ttk.Progressbar(self.introScreenContainer,orient="horizontal",length=200,mode="determinate",takefocus=True,maximum=100,style='white.Horizontal.TProgressbar')
        self.introScreenProgressBar.place(relx=0.5,rely=0.7,anchor="center")

        self.introScreenImageObject=self.generateImage(self.icon["gradient"]["256"],100,100)
        self.introScreenImage=self.tkinter.Canvas(self.introScreenContainer,width=100,height=100,bg=self.bgcolor,bd=0)
        self.introScreenImage.place(relx=0.5,rely=0.3,anchor="center")
        self.introScreenImage.create_image(52,52,image=self.introScreenImageObject,anchor=self.tkinter.CENTER)

        self.introScreenThread1=self.threading.Thread(target=titleTextThread, args=[self])
        self.threads.append(self.introScreenThread1)
        self.introScreenThread1.start()

        self.introScreenThread2=self.threading.Thread(target=introBarThread, args=[self])
        self.threads.append(self.introScreenThread2)
        self.introScreenThread2.start()

        

        
        

Kraken()





















