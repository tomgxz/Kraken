try:
    from assets.screen.loadingscreen import LoadingScreen
except ModuleNotFoundError:
    from loadingscreen import LoadingScreen

class LoginLoadingScreen(LoadingScreen):
    """ The tkinter post-login loading screen for Kraken. Inherits from :class: Screen. """
    def __init__(self,master,root,titleTextA="Kraken",titleTextB="Logging you in"):
        """
        Constructs a :class: 'LoadingScreen <LoadingScreen>'

        :param master object:
            Reference to the master of this class, which should be the main application object
        :param root object:
            The tkinter root
        :param titleTextA str:
            (Optional, "Kraken") Defines the first part of the title being displayed on screen
        :param titleTextB str:
            (Optional, "Logging you in") Defines the second part of the title being displayed on screen
        """
        
        super().__init__(master,root,titleTextA=titleTextA,titleTextB=titleTextB,progBarRandomMin=0.0001,progBarRandomMax=0.001)

        
    def next(self):
        """ Move the window to the next screen, defined in the function. """
        self.clear()
        self.clearAll()

        return
        try:
            from assets.screen.loginscreen import LoginScreen
        except ModuleNotFoundError:
            from loginscreen import LoginScreen
        LoginScreen(self.master,self.root)
        self.master.logger.info("Loading screen cleared")
        self.clear()

if __name__ == "__main__":
    raise Exception(
        "This module is to be used in conjunction with the Kraken application and not as a standalone module.")
