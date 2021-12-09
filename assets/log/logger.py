class Logger():
    def __init__(self,sessionFile:str="",logFile:str="",formatting:str="[%(asctime)s] [%(levelname)s]: %(message)s",dateTime:str="%m-%d-%Y %H:%M:%S",*a,**k):
        import os,logging,sys
        self.os=os
        self.logging=logging
        self.sys=sys
        
        self.sessionFile=sessionFile
        self.logFile=logFile
        self.format="%(message)s"
        self.format=formatting
        self.dateTime=dateTime

        if not (self.os.path.exists(self.sessionFile) or os.path.exists(self.logFile)):
            raise Exception(
                "File(s) dont exist")

        self.logger=self.logging.getLogger()
        self.logger.setLevel(self.logging.INFO)
        
        self.loggingFormatter=self.logging.Formatter(self.format,self.dateTime)
        
        self.loggingStdoutHandler=self.logging.StreamHandler(self.sys.stdout)
        self.loggingStdoutHandler.setLevel(self.logging.DEBUG)
        self.loggingStdoutHandler.setFormatter(self.loggingFormatter)

        self.loggingFileHandler=self.logging.FileHandler(self.logFile)
        self.loggingFileHandler.setLevel(self.logging.DEBUG)
        self.loggingFileHandler.setFormatter(self.loggingFormatter)

        self.logger.addHandler(self.loggingFileHandler)
        self.logger.addHandler(self.loggingStdoutHandler)

    def clearLog(self,*a,**k):
        assert self.os.path.exists(self.logFile)
        open(self.logFile,"w").close()

    def log(self,msg,*a,**k):
        self.logger.log(msg,*a,*k)

    def debug(self,msg,*a,**k):
        self.logger.debug(msg,*a,*k)

    def info(self,msg,*a,**k):
        self.logger.info(msg,*a,*k)

    def warning(self,msg,*a,**k):
        self.logger.warning(msg,*a,*k)
    
    def error(self,msg,*a,**k):
        self.logger.error(msg,*a,*k)

    def critical(self,msg,*a,**k):
        self.logger.critical(msg,*a,*k)

    def exception(self,msg,*a,**k):
        self.logger.exception(msg,*a,*k)
