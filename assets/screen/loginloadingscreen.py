try:
    from assets.screen.loadingscreen import LoadingScreen
except ModuleNotFoundError:
    from loadingscreen import LoadingScreen

class LoginLoadingScreen(LoadingScreen):
    def __init__(self,master,root,titleTextA="Kraken",titleTextB="Logging you in"):
        print(1)
        super().__init__(master,root,titleTextA=titleTextA,titleTextB=titleTextB,progBarRandomMin=0.0001,progBarRandomMax=0.001)

        
    def next(self):
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
