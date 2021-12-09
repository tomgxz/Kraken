class Generator():
    """ Core interface for HTMLGenerator """

    def __init__(
        self,
        siteName:str="",
        description:str="",
        icon:str="",
        iconType:str="",
        url:str="",
        author:str="",
        publisher:str="",
        copyright:str="",
        audience:str="",
        robots:str="",
        email:str="",
        phone:str="",
        bannerImage:str="",
        bannerImageAlt:str="",
        bannerImageType:str=""
    ):

        """ 
        Constructs a :class: 'Generator <Generator>' 
        
        :param siteName str:
            (Optional, "") Name of the webpage, will be in the title of the site, and the name of the directory.

        :param description str:
            (Optional, "") Description of the webpage.

        :param icon str:
            (Optional, "") Path of the icon of the webpage. Creates a duplicate in the resources. Will default to the icon of the generator.

        :param iconType str:
            (Optional, "") Image type of :param: icon.

        :param url str:
            (Optional, "") Url of the webpage. Used in metadata.

        :param author str:
            (Optional, "") Author of the webpage. Will default to the name of this generator.

        :param publisher str:
            (Optional, "") Publisher of the webpage. Will default to :param: author if left blank.

        :param copyright str:
            (Optional, "") Copyright of the webpage. Will default to :param: publisher if left blank, along with the year of the generation.

        :param audience str:
            (Optional, "") Target audience of the webpage. Will default to 'everyone' if left blank.

        :param robots str:
            (Optional, "") How robots interact with your webpage. Will default to 'index, follow' if left blank.

        :param email str:
            (Optional, "") Contact email of the webpage.

        :param phone str:
            (Optional, "") Contact phone of the webpage.

        :param bannerImage str:
            (Optional, "") Image used in cards. Creates a duplicate in the resources.

        :param bannerImageAlt str:
            (Optional, "") Alt text for :param: bannerImage. Defaults to 'Banner Image'.

        :param bannerImageType str:
            (Optional, "") Image type of :param: bannerImage.
        
        """

        import os,imghdr,datetime
        self.os=os
        self.imghdr=imghdr
        self.datetime=datetime

        self.websiteName=siteName if siteName !="" else "GeneratedPage"
        self.pageName="Home"
        self.url="as"
        self.pageUrl="yfvgbhjlkm"
        self.title=self.websiteName
        self.globalDescription=description if description !="" else None # under 160 char
        self.websiteIcon=icon if icon !="" else None
        self.websiteIconType="image/png"

        self.author="Thomas Lee"
        self.publisher="Thomas Lee"
        self.copyright="Thomas Lee"
        self.audience="Everyone"
        self.robots="index,follow"

        self.contactEmail="aaa@bbb.c"
        self.contactPhone="+44 0000 000000"

        self.primaryColor="#ffffff"

        self.bannerImage="../resources/images/banner.png"
        self.bannerImageType="image/png"
        self.bannerImageAlt="Alt"

        self.jpegTypes=["jpg","jpeg","jfif","jpg","pjpeg","pjp"]
        self.icoTypes=["ico","cur"]

        if self.websiteIcon != None:

            self.fileExistsException(self.websiteIcon)
            self.fileReadableException(self.websiteIcon)
            
            pass

            if self.imghdr.what(self.websiteIcon) not in self.validImageTypes:
                raise Exception("Invalid filepath - file is not an allowed image type.")
            if self.imghdr.what(self.websiteIcon) not in self.validIconTypes:
                raise Exception("Invalid filepath - file is not an allowed icon type.")

        #self.constructDirectory()
        #self.constructFiles()

        self.generateHead()

    def constructDirectory(self):
        """ Constructs all appropriate directories for the intial state of the webpage.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        self.paths=[f"{self.websiteName}",f"{self.websiteName}/resources",f"{self.websiteName}/resources/application",f"{self.websiteName}/resources/audio",f"{self.websiteName}/resources/css",f"{self.websiteName}/resources/css/global",f"{self.websiteName}/resources/css/index",f"{self.websiteName}/resources/image",f"{self.websiteName}/resources/js",f"{self.websiteName}/resources/js/global",f"{self.websiteName}/resources/js/index",f"{self.websiteName}/resources/multipart",f"{self.websiteName}/resources/text",f"{self.websiteName}/resources/video"]

        for path in self.paths:
            try:
                self.os.mkdir(path)
            except OSError:
                return False
        
        return True
    
    def constructFiles(self):
        """ Constructs all appropriate files for the initial state of the webpage. Does not create the contents of the files.
        
        :returns: A boolean determining whether the process was successful
        :rtype: bool
        """
        self.files=[
            f"{self.websiteName}/index.html",

            f"{self.websiteName}/resources/css/global/global.css",
            f"{self.websiteName}/resources/css/index/index.css",

            f"{self.websiteName}/resources/js/global/global.js",
            f"{self.websiteName}/resources/js/index/index.js"
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

        paths=[f"{self.websiteName}/{path}",f"{self.websiteName}/resources/css/{path}",f"{self.websiteName}/resources/js/{path}"]

        files=[f"{self.websiteName}/{path}/index.html",f"{self.websiteName}/resources/css/{path}/index.css",f"{self.websiteName}/resources/js/{path}/index.js"]


        for path in paths:
            try:
                self.os.makedirs(path)
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
        created=None,
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

        created=created if created != None else self.datetime.datetime.now()
        
        self.fileExistsException(path)
        self.fileReadableException(path)
        self.fileWriteableException(path)

        if type.lower() not in self.resourceList():
            raise Exception("Not a recognised file category. Valid categories: application, audio, image, multipart, text, video")

        type=type.lower()
        savePath=f"{self.baseFolderPath}/resources/{type}/{self.os.path.basename(self.path)}"

        savePath=savePath

    def generateHead(self):
        headContentPrefix="\t"
        headContent="\n"
        metaItems=self.generateMeta()

        for item in metaItems:
            headContent+=f"{headContentPrefix}{item}\n"

        print(self.writeElement(element="head",closeTag=True,content=headContent,tabDelimited=True))

    def generateMeta(self):
        metaList=[]
        
        def addMetaElement(element="meta",args={},closeTag=False,content="",tabDelimited=False):
            metaList.append(self.writeElement(element=element,args=args,closeTag=closeTag,content=content,tabDelimited=tabDelimited))

        def addOpenGraphElement(name,content):
            addMetaElement(args={"property":f"og:{name}","content":content})

        def addTwitterGraphElement(name,content):
            addMetaElement(args={"property":f"twitter:{name}","content":content})

        addMetaElement(element="script",closeTag=True,args={"src":"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"})
        addMetaElement(args={"charset":"UTF-8"})

        addMetaElement(element="title",closeTag=True,content=self.websiteName,tabDelimited=True)

        addMetaElement(args={"name":"description","content":self.globalDescription})
        addMetaElement(args={"name":"author","content":f"{self.author}, {self.contactEmail}"})
        addMetaElement(args={"name":"reply-to","content":self.contactEmail})
        addMetaElement(args={"name":"publisher","content":self.publisher})
        addMetaElement(args={"name":"copyright","content":self.copyright})
        addMetaElement(args={"name":"audience","content":self.audience})
        addMetaElement(args={"name":"robots","content":self.robots})
        addMetaElement(args={"name":"viewport","content":"width=device-width, initial-scale=1.0"})
        addMetaElement(args={"name":"language","content":"EN"})

        addMetaElement(args={"name":"apple-mobile-web-app-capable","content":"yes"})
        addMetaElement(args={"name":"apple-touch-fullscreen","content":"yes"})
        addMetaElement(args={"name":"apple-mobile-web-app-status-bar-style","content":"black"})
        addMetaElement(args={"name":"apple-mobile-web-app-title","content":self.websiteName})
        
        addMetaElement(args={"name":"application-name","content":self.websiteName})
        addMetaElement(args={"name":"theme-color","content":self.primaryColor})

        addMetaElement(element="link",args={"rel":"apple-touch-icon","href":self.websiteIcon})
        addMetaElement(element="link",args={"rel":"icon","type":self.websiteIconType,"href":self.websiteIcon})

        addMetaElement(args={"http-equiv":"Page-Enter","content":"RevealTrans(Duration=2.0,Transition=2)"})
        addMetaElement(args={"http-equiv":"Page-Exit","content":"RevealTrans(Duration=3.0,Transition=12)"})
        addMetaElement(args={"http-equiv":"Content-type","content":"text/html; charset=utf-8"})
        addMetaElement(args={"http-equiv":"X-UA-Compatible","content":"IE=edge"})
        addMetaElement(args={"http-equiv":"content-language","content":"en"})

        addOpenGraphElement("site_name",self.websiteName)
        addOpenGraphElement("title",self.pageName)
        addOpenGraphElement("description",self.globalDescription)
        addOpenGraphElement("image:type",self.bannerImageType)
        addOpenGraphElement("image",self.bannerImage)
        addOpenGraphElement("type","website")
        addOpenGraphElement("url",self.pageUrl)
        addOpenGraphElement("email",self.contactEmail)
        addOpenGraphElement("phone_number",self.contactPhone)

        addTwitterGraphElement("card","summary")
        addTwitterGraphElement("site","@rickastley")
        addTwitterGraphElement("title",self.pageName)
        addTwitterGraphElement("description",self.globalDescription)
        addTwitterGraphElement("image:alt",self.bannerImageAlt)
        addTwitterGraphElement("image",self.bannerImage)
        addTwitterGraphElement("url",self.pageUrl)

        return metaList

        # canonical link shows a link which is the same as the current page but this page should take priority over it in seo

    """



    <script src="https://kit.fontawesome.com/73a2cc1270.js"></script>
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v6.0.0-beta3/css/all.css">

    <meta property="twitter:card" content="summary">
    <meta property="twitter:site" content="@efapaudio">
    <meta property="twitter:title" content="Qwibgfit">
    <meta property="twitter:description" content="The ultimate puzzle dodecahedron, now with added sock">
    <meta property="twitter:image" content="../resources/img/satisfied.png">
    <meta property="twitter:url" content="https://www.qwibgift.net/home">
    <link rel="stylesheet" href="../resources/css/new.css">
    <style>*{transition: background-color .5s, background .5s, color .5s;}</style>

"""
    
    def writeElement(
        self,
        element:str="element",
        closeTag:bool=True,
        content:str="",
        args:dict={},
        tabDelimited:bool=False,
    ):
        """Write a html element to a string. Contains no error checking as of now.

        :param str element:
            (Optional, '') The type of element to be written. No error checking.
        :param bool closeTag:
            (Optional, True) Determines whether to append '</{element}>' to the end of the string.
        :param str contents:
            (Optional, '') Adds content into the element. Only has an effect if closeTag is true and contents is not empty.
        :param dict args:
            (Optional, {}) The arguments inputted. They are written to the element. To just write the key, set it to none. No error checking.
        :param bool tabDelimited:
            (Optional, False) Determins whether the element is contained within one line.

        :returns: String containing the element
        :rtype: str
        """
        
        elementInternal=f"{element}"

        for key in args:
            if args[key]==None:
                elementInternal=f"{elementInternal} {key}"
            else:
                elementInternal=f"{elementInternal} {key}=\"{args[key]}\""

        returnContent=f"<{elementInternal}>"

        if closeTag:
            if content=="":
                returnContent=f"{returnContent}</{element}>"
            elif tabDelimited:
                returnContent=f"{returnContent}{content}</{element}>"
            else:
                returnContent=f"{returnContent}\n\t{content}\n</{element}>"

        return returnContent

      
    def fileExists(self,path):
        """ Checks whether a file exists. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file exists.
        :rtype: bool
        """
        return self.os.path.isfile(path)
    
    def fileReadable(self,path):
        """ Checks whether a file is readable. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file is readable.
        :rtype: bool
        """
        return self.os.access(path, self.os.R_OK)
    
    def fileWriteable(self,path):
        """ Checks whether a file is writeable. Returns the result.
        
        :param str path:
            The path of the file.

        :returns: Boolean describing whether the file is writeable.
        :rtype: bool
        """
        return self.os.access(path, self.os.W_OK)

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

    def resourceList(self):
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
