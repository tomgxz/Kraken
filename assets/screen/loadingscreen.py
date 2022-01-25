try:
    from assets.screen.screen import Screen
except ModuleNotFoundError:
    from screen import Screen

class LoadingScreen(Screen):
    """ The tkinter loading screen for Kraken. Inherits from :class: Screen. """
    
    def __init__(self,master,root,titleTextA="Kraken",titleTextB="Loading",progBarRandomMin=0.001,progBarRandomMax=0.05):
        """
        Constructs a :class: 'LoadingScreen <LoadingScreen>'

        :param master object:
            Reference to the master of this class, which should be the main application object
        :param root object:
            The tkinter root
        :param titleTextA str:
            (Optional, "Kraken") Defines the first part of the title being displayed on screen
        :param titleTextB str:
            (Optional, "Loading") Defines the second part of the title being displayed on screen
        """
        
        super().__init__(master,root)

        self.master.logger.info("Generating loading screen")

        self.titleTextA=titleTextA
        self.titleTextB=titleTextB

        self.container=self.tkinter.Frame(self.root,bg=self.bgcolor,width=self.internalWidth,height=self.internalHeight)
        self.container.place(relx=0.5,rely=0.5,anchor="center")

        self.imageObject=self.generateImage(self.icon["gradient"]["512"],100,100)
        self.image=self.tkinter.Canvas(self.container,width=100,height=100,bg=self.bgcolor,bd=0,highlightthickness=0)
        self.image.place(relx=0.5,rely=0.3,anchor="center")
        self.image.create_image(52,52,image=self.imageObject,anchor="center")

        self.titleTextVar=self.tkinter.StringVar(self.container,f"{self.titleTextA} - {self.titleTextB}")

        self.titleText=self.tkinter.Label(self.container,textvariable=self.titleTextVar,bg=self.bgcolor,font=self.titleFont)
        self.titleText.place(relx=0.5,rely=0.4,anchor="n")

        self.textThread=self.threading.Thread(target=self.loadingText,args=[self.titleTextVar,self.titleTextA,self.titleTextB])
        self.threads.append(self.textThread)
        self.textThread.start()

        self.progbar=self.generateProgressBar(self.container,200,style="white")
        self.progbar.place(relx=0.5,rely=0.7,anchor="center")

        self.progbarThread=self.threading.Thread(target=self.progressBarThread,args=[self.progbar,self.next,progBarRandomMin,progBarRandomMax])
        self.threads.append(self.progbarThread)
        self.progbarThread.start()

        self.activateLoadThread()

        self.master.logger.info("Loading screen generated")

    def next(self):
        """ Move the window to the next screen, defined in the function. """
        try:
            from assets.screen.loginscreen import LoginScreen
        except ModuleNotFoundError:
            from loginscreen import LoginScreen
        LoginScreen(self.master,self.root)
        self.master.logger.info("Loading screen cleared")
        self.clear()

    def loadThread(self):
        return None

    def activateLoadThread(self):
        self.t=self.threading.Thread(target=self.loadThread)
        self.threads.append(self.t)
        self.t.start()

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
