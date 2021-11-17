import os,imghdr,enum,datetime

class browsers(enum.Enum):
    chrome=0
    edge=1
    firefox=2
    ie=3
    opera=4
    safari=5

class imageCompatibility(enum.Enum):
    apng = [browsers.chrome,browsers.edge,browsers.firefox,            browsers.opera,browsers.safari]
    avif = [browsers.chrome,              browsers.firefox,            browsers.opera                ]
    gif =  [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]
    jpeg = [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]
    png =  [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]
    svg =  [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]
    webp = [browsers.chrome,browsers.edge,browsers.firefox,            browsers.opera,browsers.safari]
    bmp =  [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]
    ico =  [browsers.chrome,browsers.edge,browsers.firefox,browsers.ie,browsers.opera,browsers.safari]

def resourceList():
    """ Returns a list of accepted file types for resources.
               
    :returns: A dictionary containing lists that defines which resources are allowed.
    :rtype: dict
    """
    return {
        "application": [
            "x-executeable",
            "graphql",
            "javascript",
            "json",
            "ld+json",
            "feed+json",
            "msword",
            "pdf",
            "sql",
            "vnd.api+json",
            "vnd.ms-excel",
            "vnd.ms-powerpoint",
            "vnd.oasis.opendocument.text",
            "vnd.openxmlformats-officedocument.presentationml.presentation",
            "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "vnd.openxmlformats-officedocument.wordprocessingml.document",
            "x-www-form-urlencoded",
            "xml",
            "zip",
            "zstd",
            "macbinary"
        ],
        
        "audio": [
            "mpeg",
            "mp3",
            "ogg",
            "wav"
        ],

        "image": [
            "apng",
            "avif",
            "gif",
            "jpeg",
            "png",
            "svg",
            "webp",
            "bmp",
            "ico"
        ],

        "multipart": [
            "form-data"
        ],

        "text": [
            "javascript",
            "css",
            "csv",
            "html",
            "php",
            "plain",
            "xml"
        ],

        "video": [
            "mp4",
            "ogg",
            "webm"
        ]
    }

class Generator():
    """ Core interface for HTMLGenerator """

    def __init__(self,name:str="",title:str="",description:str="",icon:str=""):
        """ Constructs a :class: 'Generator <Generator>' """

        self.name=name if title !="" else "GeneratedPage"
        self.title=title if title !="" else None
        self.description=description if description !="" else None
        self.icon=icon if icon !="" else None

        self.jpegTypes=["jpg","jpeg","jfif","jpg","pjpeg","pjp"]
        self.icoTypes=["ico","cur"]

        if self.icon != None:

            self.fileExistsException(self.icon)
            self.fileReadableException(self.icon)
            
            pass

            if imghdr.what(self.icon) not in self.validImageTypes:
                raise Exception("Invalid filepath - file is not an allowed image type.")
            if imghdr.what(self.icon) not in self.validIconTypes:
                raise Exception("Invalid filepath - file is not an allowed icon type.")

        self.constructDirectory()
        self.constructFiles()


    def fileExists(self,path):
        """ Checks whether a file exists. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file exists.
        :rtype: bool
        """
        return os.path.isfile(path)
    
    def fileReadable(self,path):
        """ Checks whether a file is readable. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file is readable.
        :rtype: bool
        """
        return os.access(path, os.R_OK)
    
    def fileWriteable(self,path):
        """ Checks whether a file is writeable. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file is writeable.
        :rtype: bool
        """
        return os.access(path, os.W_OK)

    def fileExistsException(self,path):
        """ Checks whether a file exists. Throws an exception if it doesn't.
        
        :param str path:
            The path of the file.

        :rtype: None
        """
        if not self.fileExists(path):
            raise Exception("Invalid filepath - no file found.")
    
    def fileReadableException(self,path):
        """ Checks whether a file is readable. Throws an exception if it isn't.
        
        :param str path:
            The path of the file.

        :rtype: None
        """
        if not self.fileReadable(path): 
            raise Exception("Invalid filepath - file is not readable.")

    def fileWriteableException(self,path):
        """ Checks whether a file is writeable. Throws an exception if it isn't.
        
        :param str path:
            The path of the file.

        :rtype: None
        """
        if not self.fileWriteable(path):
            raise Exception("Invalid filepath - file is not writeable.")

    def constructDirectory(self):
        """ Constructs all appropriate directories for the intial state of the webpage.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        self.paths=[f"{self.name}",f"{self.name}/resources",f"{self.name}/resources/application",f"{self.name}/resources/audio",f"{self.name}/resources/css",f"{self.name}/resources/css/global",f"{self.name}/resources/css/index",f"{self.name}/resources/image",f"{self.name}/resources/js",f"{self.name}/resources/js/global",f"{self.name}/resources/js/index",f"{self.name}/resources/multipart",f"{self.name}/resources/text",f"{self.name}/resources/video"]

        for path in self.paths:
            try:
                os.mkdir(path)
            except OSError:
                return False
        
        return True
    
    def constructFiles(self):
        """ Constructs all appropriate files for the initial state of the webpage. Does not create the contents of the files.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        self.files=[
            f"{self.name}/index.html",

            f"{self.name}/resources/css/global/global.css",
            f"{self.name}/resources/css/index/index.css",

            f"{self.name}/resources/js/global/global.js",
            f"{self.name}/resources/js/index/index.js"
        ]

        for file in self.files:
            if self.fileExists(file):
                continue
            try:
                with open(file,"w") as f:
                    pass
            except OSError:
                return False
        
        return True

    def constructNewPage(self,path):
        """ Adds a new page to the resources with appropriate css and js files. Does not create the content of the files.
        
        :param str path:
            The path of the new webpage - formatted '\\xxx\\xxx'. Example '\\about\\legal'.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """

        paths=[f"{self.name}/{path}",f"{self.name}/resources/css/{path}",f"{self.name}/resources/js/{path}"]

        files=[f"{self.name}/{path}/index.html",f"{self.name}/resources/css/{path}/index.css",f"{self.name}/resources/js/{path}/index.js"]


        for path in paths:
            try:
                os.makedirs(path)
            except OSError:
                return False
            self.paths.append(path)
        
        for file in files:
            if self.fileExists(file):
                continue
            try:
                with open(file,"w") as f:
                    pass
            except OSError:
                return False
            self.files.append(file)
    
        return True

    def addResource(
        self,
        path:str,
        type:str="",
        name:str="",
        desc:str="",
        authors:list=[],
        created:datetime.datetime=datetime.datetime.now(),
    ):
        """ Adds a new resource to the generator. 
        
        :param str path:
            The filepath of the resource to be added - formatted '\\xxx\\xxx.xxx'.
        :param str type:
            (Optional, '') The type of file being passed - formatted 'xxx/xxx'.
        :param str name:
            (Optional, '') The name you would like to set the file as. Will also be stored in metadata.
        :param str desc:
            (Optional, '') The description of the file stored in metadata.
        :param list authors:
            (Optional, []) The authors of the file stored in metadata.
        :param datetime.datetime created:
            (Optional, datetime.datetime.now()) The creation time of the file stored in metadata.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """

        if not self.fileExists(path):
            return False
        if not self.fileReadable(path):
            return False
    
    def writeElement(
        self,
        element:str="element",
        closeTag:bool=True,
        contents:str="",
        args:dict={},
    ):
        """Write a html element to a string. Contains no error checking as of now.

        :param str element:
            (Optional, '') The type of element to be written. No error checking.
        :param bool closeTag:
            (Optional, True) Determines whether to append '</{element}>' to the end of the string.
        :param str contents:
            (Optional, '') Adds content into the element. Only has an effect if closeTag is true and contents is not empty.
        :param dict args:
            (Optional, {}) The arguments inputted. They are written to the element. No error checking.

        :returns: String containing the element
        :rtype: str
        """
        
        elementInternal=f"{element}"

        for key in args:
            elementInternal=f"{elementInternal} {key}=\"{args[key]}\""

        returnContent=f"<{elementInternal}>"

        if closeTag:
            returnContent=f"{returnContent}\n\t{contents}\n</{element}>"

        return returnContent