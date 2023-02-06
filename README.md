## Table of Contents
  - [Mark Scheme](#mark-scheme)
  >

  - [Analysis](#analysis)
    - [Problem identification](#problem-identification)
    - [Stakeholders](#stakeholders)
    - [Why it is suited to a computational approach](#why-it-is-suited-to-a-computational-approach)
    - [Research](#research)
      - [Existing solution - Squarespace](#existing-solution---squarespace)
      - [Existing solution - Zyro](#existing-solution---zyro)
    - [Key features of the solution](#key-features-of-the-solution)
    - [Limitations of the solution](#limitations-of-the-solution)
    - [Meeting with the stakeholders](#meeting-with-the-stakeholders)
    - [Hardware and Software Requirements](#hardware-and-software-requirements)
      - [Hardware Requirements](#hardware-requirements)
      - [Software Requirements](#software-requirements)
    - [Stakeholder requirements](#stakeholder-requirements)
    - [Success Criteria](#success-criteria)
  >

  - [Design](#design)
    - [URL Navigation](#url-navigation)
    - [User Interface Design](#user-interface-design)
    - [Usability](#usability)
      - [Accessibility](#accessibility)
      - [ARIA](#aria)
    - [Stakeholder input :D](#stakeholder-input-d)
    - [Website structure and backend](#website-structure-and-backend)
    - [Data storage](#data-storage)
    - [Algorithms](#algorithms)
      - [Drag-and-drop editor algorithms](#drag-and-drop-editor-algorithms)
      - [Multi-user system algorithms](#multi-user-system-algorithms)
    - [Diagram showing how the subroutines link](#diagram-showing-how-the-subroutines-link)
    - [Subroutines](#subroutines)
      - [Multi-user system - login system](#multi-user-system---login-system)
      - [Multi-user system - creating a new site](#multi-user-system---creating-a-new-site)
      - [Multi-user system - user settings](#multi-user-system---user-settings)
      - [Utility subroutines](#utility-subroutines)
    - [Explanation and justification of this process](#explanation-and-justification-of-this-process)
    - [Inputs and Outputs](#inputs-and-outputs)
    - [Key variables](#key-variables)
    - [Validation](#validation)
    - [Testing method](#testing-method)
  >

  - [Development and Testing](#development-and-testing)
    - [Stage 1 - Setting up the website](#stage-1---setting-up-the-website)
    - [Stage 2 - Creating and implementing the database](#stage-2---creating-and-implementing-the-database)

## Mark Scheme
  3.1. Analysis of the problem (10 marks)||
  :-|-
  3.1.1 Problem identification | Describe and justify the features that make the problem solvable by computational methods
  ||Explain why the problem is amendable to a computational approach
  3.1.2 Stakeholders | Identify and describe those who will have an interest in the solution explaining how the solution is appropriate to their needs (this may be named individuals, groups or persona that describes the target end user).
  3.1.3 Research the problem | Research the problem and solutions to similar problems to identify and justify suitable approaches to a solution
  ||Describe the essential features of a computational solution explaining these choices.
  ||Explain the limitations of the proposed solution
  3.1.4 Specify the proposed solution | Specify and justify the solution requirements including hardware and software configuration (if appropriate).
  ||Identify and justify measurable success criteria for the proposed solution.

  3.2 Design of the solution (15 marks)||
  :-|-
  3.2.1 Decompose the problem | Break down the problem into smaller parts suitable for computational solutions justifying any decisions made
  3.2.2 Describe the solution | Explain and justify the structure of the solution
  ||Describe the parts of the solution using algorithms justifying how these algorithms form a complete solution to the problem.
  ||Describe usability features to be included in the solution.
  ||Identify key variables / data structures / classes justifying choices and any necessary validation.
  3.2.3 Describe the approach to testing | Identify the test data to be used during the iterative development and post development phases and justify the choice of this test data

  3.3 Developing the solution (25 marks)||
  :-|-
  3.3.1 Iterative development process | Provide annotated evidence of each stage of the iterative development process justifying any decision made.
  ||Provide annotated evidence of prototype solutions justifying any decision made.
  3.3.2 Testing to inform development | Provide annotated evidence for testing at each stage justifying the reason for the test.
  ||Provide annotated evidence of any remedial actions taken justifying the decision made.

  3.4 Evaluation (20 marks)||
  :-|-
  3.4.1 Testing to inform evaluation | Provide annotated evidence of testing the solution of robustness at the end of the development process.
  ||Provide annotated evidence of usability testing (user feedback).
  3.4.2 Success of the solution | Use the test evidence from the development and post development process to evaluate the solution against the success criteria from the analysis.
  3.4.3 Describe the final product | Provide annotated evidence of the usability features from the design, commenting on their effectiveness
  3.4.4 Maintenance and development | Discuss the maintainability of the solution.
  ||Discuss potential further development of the solution.

## Analysis

### Problem identification
  With the internet constantly growing and more and more people relying on it, the demand for websites is constantly increasing. They can range in style from business portfolios and online stores to games. Regardless of who you are or what you do, a website is often expected of you, especially for businesses. However, the problem of creating a professional and functional website can be a daunting task for many individuals and small businesses, especially those who need more technical expertise or resources. Existing website builders may be difficult to navigate, require extensive coding knowledge, or lack the necessary design flexibility to create a unique and effective online presence. Furthermore, many website builders are geared toward certain industries or types of websites, making it difficult for users to find a platform that meets their specific needs. The task of manually programming it can seem very daunting.

  The main aim of this project is to develop a website that allows clients to produce their website via a simple user interface, which alleviates the technical intricacies of HTML, CSS, and JavaScript and allows them to focus on creating a website that reflects their brand and meets their business goals. Clients can select from various styles and themes (or create their own), upload media such as images and videos, and then interact with a drag-and-drop interface to organise a webpage. Each website they create would have a page dedicated to it, with options to customise the styles of the site, the ability to create, organise, and link together pages of the website, preview the website in a variety of display sizes, and add pre-made elements and edit the parameters of the elements in the site.

  A drag-and-drop website builder that is easy to use is increasingly important in today's digital age, where having an online presence is crucial for businesses, organisations, and individuals. A user-friendly website builder that offers a wide range of customisable design options would greatly benefit users who may not have the technical know-how to create a website on their own.

  Moreover, the rise of mobile devices and the increasing importance of responsive design have made it crucial for websites to be optimised for different screen sizes and devices. As such, this project would also be geared towards easily creating mobile-friendly websites to ensure optimal user experience.

  The requirements for a client to be able to use it would also be low due to the entire application being contained within the website: this means that the client would only need a web browser and an internet connection. They do not need to install software onto their computer, nor do they need to worry about software updates.

  In summary, the problem that this website builder aims to solve is to provide an easy-to-use, drag-and-drop website builder for individuals and small businesses, which can be easily customised to their specific needs and optimised for different devices without requiring technical expertise. This will greatly benefit users by allowing them to create a professional and functional website that meets their business goals and reflects their brand without needing a background in technology or coding.

### Stakeholders
  The clients for this solution could be a wide range of individuals or organisations looking to create a website without the need for technical competency or dedicating large amounts of time to it.

  Some potential clients could include:
  - Individuals: People who want to create a personal website, such as a blog, portfolio, or online resume.
  - Small businesses: Owners or managers of small businesses who want to create a website for their business, such as an online store or service provider website.
  - Entrepreneurs: Entrepreneurs who want to create a website for their startup or new business venture.
  - Non-profit organisations: Non-profit organisations that want to create a website to promote their mission and raise awareness.
  - Freelancers: Freelancers and independent contractors who want to create a website to showcase their work and promote their services.

#### Initial talks with stakeholders

  <img alt="404 no stakeholders" src="https://lh5.googleusercontent.com/4uvZ_jq6raFf03ail16FfgqLPm9JP5gdU8V-y3wZAfbUpKUVSNls_AyQkpSCeZ10CrUPHeXBtRubFjCSOWe2scR_DFF6y7YcZc2VesnJbeRY-9vynC5GyrSNOOH4g_Px8H1jbhP-i_bE8n_1Z6K6Rg"/>

### Why it is suited to a computational approach
  This problem is suitable for a computational approach because it automates many technical and design tasks typically associated with creating a website. This is achieved by breaking down the website-building process into smaller, more manageable tasks that a computer program can easily handle.

  For example, it can implement a drag-and-drop interface to allow users to easily add and arrange elements on a webpage, such as text, images, and videos, without coding. The website builder can also include a visual editor that allows users to easily customise the design and layout of their website, such as selecting from a variety of pre-designed templates or themes. The website builder can also apply pre-defined styles and formatting to the website and organise and link the pages together.

  In addition, the solution can also use computational algorithms to optimise the website for different devices and screen sizes, ensuring that the website is responsive and easy to navigate on any device. This can be done by using CSS media queries, which can change the website's layout based on the screen's width, and JavaScript libraries that can detect the device and size of the screen and adjust the layout accordingly.

  Using a computational approach can also ensure that the website is secure, fast, and reliable. It can use techniques like minifying, compression, and caching to make the website load faster and use authentication and authorisation mechanisms to ensure the website is secure.

  The solution will be accessible through a server that hosts a website, which requires a computer to use. No alternative would not require a computer to be able to create a website, as at some point, the user will need to write and host the code that they have produced. This solution would act as a bridge between the client and the code, making it easy for users to create a website without needing to understand the technical details of coding.

#### Computational methods that the solution lends itself to:

##### Problem recognition
  This solution is suitable for problem recognition because it addresses a specific problem that many individuals and small businesses face: the difficulty of creating a professional and functional website without technical expertise or resources. By providing a user-friendly, drag-and-drop interface, a website builder allows users to easily create and edit their website without the need for coding or technical expertise. This addresses the problem of users not having the technical skills or resources to create a website themselves.

  Furthermore, a website builder can also use computational algorithms to optimise the website for different devices and screen sizes, ensuring that the website is responsive and easy to navigate on any device. This addresses the problem of the rise of mobile devices and the increasing importance of responsive design in today's digital age.

##### Problem decomposition
  The problem can be broken down into smaller tasks that must be programmed for the program to operate effectively.
  - Creating an account system and a database to store the user's data.
  > The account system would allow many users to access the server and edit their sites. The data would be stored in a server-side SQL database. The sites would be stored separately on the server.
  - Creating a menu system for users to navigate to access different sites.

  - Storing a list of template elements the user can preview and use in their site.
  > I need to decide on how to store the template elements, display them to the user, and then implement them into a user's site while still allowing them to edit them.
  - Creating a simple drag-and-drop interface that is easy to use and understand.
  > This will probably be based on the grid-based positioning system that many existing website builders use or the constraint system that applications such as android studio use; however, the constraint system may not work with how HTML is created.
  - Creating an effective way of storing the users' sites on the server.
  > They would either be stored in HTM, CSS, and JS files, which would remove the need to convert them, or they could be stored all in XML files, which would make accessing the files easier: the program could convert the XML elements into HTML, CSS, and JS to allow it to be shown. This would allow for the storage of more information about the site and elements and would mean it could all be in one file, including all the separate pages.
  - Converting the user's site into runnable HTML, CSS, and JavaScript so they can download and use it.
  > There would need to be a way for JavaScript to do it so that the user can edit the site in the editor and a way for the server (written in Python) to do it as well

##### Divide and conquer
  These smaller steps are all doable on their own, and combining them would make a divide-and-conquer approach. The advantage of it being coded in a modular way is that each part can be tested and built on its own without relying on other parts of the project.

##### Abstraction
  The program uses abstraction as it removes the complex process of programming code by transferring it into a simpler, graphical interface - it provides a high-level interface for users to create a website while hiding the underlying implementation details. This removes the need for the client to have knowledge and experience in programming, opening the market to a much larger audience.

  For example, the proposed drag-and-drop interface abstracts the implementation details of adding and arranging elements on a webpage using HTML and CSS code.

### Research

#### Existing solution - Squarespace
  Their template list gives the option to preview the website, with all of its functionality in a separate page. They allow their users to view it in different sizes as well.

  <img alt="Squarespace research image: template preview" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace12.png?raw=true" height="360"/>

  When first editing the site, Squarespace offers an assistant with some basic first steps to creating the website, making it easier for the client to understand how the editor works and how to use it effectively.

  <img alt="Squarespace research image: assistant" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace3.png?raw=true" height="360"/>

  Their design options include styles, browser icons, 404 pages, and custom CSS. They can change the fonts, colour scheme, global animations, spacing, and default styles for certain widgets.

  <img alt="Squarespace research image: design menu" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace13.png?raw=true" height="360"/>

  Their editor works in the conventional way of a grid-based system, where the user can place elements anywhere on the grid. It will then assign the item the style property `grid-area:row-start/col-start/row-end/col-end` or `grid-area:y/x/height/width` to define the position of the element. They have different attributes for different screen sizes, and the user can edit both styles separately by switching between laptop and phone modes.

  <img alt="Squarespace research image: element drag and drop" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace6.png?raw=true" width="640"/>

  <img alt="Squarespace research image: grid positioning CSS" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace7.png?raw=true" height="360"/>

  The website is split into sections, where each section contains a content wrapper with the grid positioning system inside.

  <img alt="Squarespace research image: construction diagram" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace14.png?raw=true"/>

  Selecting text gives the user a popup that displays the text formatting options. Whenever the user clicks on an element, they get a different popup that displays the design options for said element.

  <img alt="Squarespace research image: text edit and style popup" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchSquarespace11.png?raw=true" width="640"/>

##### Parts I can apply to my project
  This solution will have the option to preview and use templates similarly to how Squarespace does it, along with their grid positioning system, which is, for lack of a better phrase, an "industry standard." There will also be a similar formatting option setup, but it will be docked on the right-hand side with all the formatting settings in the same place.

  Squarespace also offers a variety of features such as e-commerce integration, SEO tools, analytics, 24/7 customer support, and a Content Management System (CMS) that allows users to update and manage their website's content easily. Although these features are useful in a website builder, I intend not to include them in the solution's first release due to the timeframe for it and how long these features would take to make. This solution would have a CMS, but not at the scale or capability of Squarespace.

#### Existing solution - Zyro
  Zyro also uses an assistant to help the user understand how to use their editor.

  <img alt="Zyro research image: assistant image 1" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro1.png?raw=true" height="360"/>

  <img alt="Zyro research image: assistant image 2" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro2.png?raw=true" height="360"/>

  Zyro has two ways of positioning objects; one is very similar to the way Squarespace does, with a grid positioning system, and the second is a smart layout. It instead uses only columns to position, and the elements can be moved up and down said columns freely and snap to other elements, like how many editors like photoshop might do. The user can toggle the snapping to other elements in section settings.

  <img alt="Zyro research image: grid positioning system" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro3.png?raw=true" width="360"/>

  <img alt="Zyro research image: smart layout positioning system" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro4.png?raw=true" width="360"/>
  <img alt="Zyro research image: snap to guides setting" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro5.png?raw=true" width="360"/>

  Their image resizing system is good. It uses the `object-fit: cover` property in the style of the image and changes the width and height attributes when being dragged, as explained later.

  <img alt="Zyro research image: image resize animation" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro6.gif?raw=true" width="360"/>

  Something else Zyro does is have all of their style attributes defined in one class, which relies on variables such as `--grid-row`,`--m-grid-column`, and `--element-width` that are defined in `element.style` (the style attribute of the HTML object), which have presumably been put there by JavaScript.

  The CSS class with all of the variable references:

  <img alt="Zyro research image: css: positioning variable usage" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro7.png?raw=true" width="360"/>

  The HTML style attribute with all of the variable declarations in it:

  <img alt="Zyro research image: positioning variable declaration" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro8.png?raw=true" width="360"/>

  When moving elements around the layout, Zyro adds four variables to the element, `top`, `left`, `width`, and `height`, which they use to render the element positioning while you are moving it. When the user releases the element, these values are removed. This positioning will be done in JavaScript by taking the position of the cursor when the user clicks on the element, getting the element's position when they click on it, and then offsetting the element's position by the amount they move the cursor. Then, when the user releases the cursor, it runs the code to calculate the new grid positioning of the element. They also have a max width for desktop mode, where the element cannot be moved further.

  <img alt="Zyro research image: live position variable declaration" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/research/ResearchZyro9.png?raw=true" width="640"/>

##### Parts I can apply to my project
  Like Squarespace, Zyro uses a grid positioning system that will be implemented in this project. Their system for moving elements around with temporary `element.style` declarations is also a good way of implementing it that will be used as well.

  Zyro also includes a built-in AI-based website creation tool called Zyro AI Writer, which can help users easily create website content. Similar to the Squarespace e-commerce system, this will not fit into the timeframe of the initial release of this solution, so it will not be implemented.

### Key features of the solution
  <!--TODO: rewrite-->

  This solution will be a web-based, multi-user program where the user uses a grid-based, drag-and-drop system using pre-defined template elements that they can customise. There will be a tutorial for creating a site to help new users understand the system. The user will be able to customise styles for their site, organise pages, access a library of pre-defined templates for widgets such as text, buttons, or links, and control the styling of each element in their pages.

  The aim is to have an easy learning curve and a low entry bar for understanding so that anybody can use it. Ease of use is also key - the cognitive load on the user should be low enough that it allows them to focus on designing the website due to

### Limitations of the solution
  The main limitation is that, as a server-side application, the user will always need an active internet connection to access it, and if the server goes down, there will be no way of using the program.

#### Meeting with the stakeholders
  I should probably contact the "stakeholders" at this point as I'm developing ideas on how the website builder would function.

### Hardware and Software Requirements

#### Hardware Requirements
  The client will need a computer capable of accessing the internet.

  In terms of the server side, hardware requirements may include the following:
  - A server to host the website builder application and handle user requests. This server could be physical or virtual and run on any operating system that can also run Python (as it is the language I will be using to program the backend).
  - The server will require a CPU with enough processing power: it may need a high number of cores and a fast clock speed to handle high traffic and many concurrent users.
  - The server will need enough memory (RAM) to handle the requests and processes of the application.
  - The server will require a sufficient amount of storage to store the website builder application and the images and files uploaded by the users to the CMS.
  - The server will need a high-speed network connection to handle incoming and outgoing traffic between itself and the users. The faster the connection, the better the user's experience will be.

  In addition to the above hardware requirements, it should be designed with scalability in mind so it can be adjusted if the application size or the number of users increases.

#### Software Requirements
  The client will need a JavaScript-compatible web browser and an active internet connection.

  For the server, software requirements may include the following:
  - The operating system used on the server should be able to run Python alongside other software listed below.
  - Python - it will need to be able to run Python in order to host the website builder.
  - A file structure system to store the code and assets for the website builder.
  - A database or file structure system to manage and store the data and media uploaded by the users to the CMS.
  - Firewall software to monitor incoming and outgoing traffic and stop potential threats from corrupting the system.
  - Load balancer software may be required when the user base increases to manage server resources and route traffic to available servers.

### Stakeholder requirements

### Success Criteria

#### Essential Features
  - Login system
  - the ability to view the password with the all-seeing eye
  - Signup fields to be name, email, username, and two passwords to make sure they get it correct
  - SQL database that stores user and site information
  - fully functional error checking on all fields as follows
  >- All fields must not be empty
  >- Name can have spaces and non-alphanumeric characters and must be longer than 2.
  >- Email must be in an email format.
  >- Username cannot have non-alphanumeric characters and must be longer than 2.
  >- Password must be longer than 8.
  >- The repeated password must be identical to password.
  >- Email cannot already be in the database.
  >- Username cannot already be in the database.

  - The homepage, when there are no sites, displays a prompt to create a new site
  - The homepage, when the user has created sites, lists all of them along with a "create new site" button
  - When creating a site, the user will get the following options
  >- Website Name: at least four characters, and any illegal characters are converted into dashes. The user is given a preview of what their site name will look like when it does not match the criteria.
  >- Description: optional
  >- Whether the site is public or private: determines who has access to the site URLs

  - Sites can be accessed with the URL: `/<username>/<sitename>`, and, if public, can be viewed (but not edited) by anyone from this URL. If private, other users will be told this and redirected home.
  - The site will have a config file, where it stores all of its global variables - mostly style choices - which have been selected when creating the site. These can also be edited at any time on the site's homepage.
  > These variables include primary, secondary, accent, and grey colours, primary and secondary fonts, and animation types.

  - File storage system to store user site files
  - CMS system for users to be able to upload custom content
  >

  - The site page (`/<username>/<sitename>`) can be programmatically assigned due to the Python backend: it can take both parameters, search for them in the database, make sure that the current user has permissions, and display the appropriate site.
  - On the site page, the user will get a preview of the website, along with customisability options for the website: the ability to edit the site, reorganise the site structure (which pages go where), edit site settings (such as default colours), and export the site.
  - When editing the site, the organisation will look like this
  >- A navigation bar on the left that contains the options: "website pages", where you can navigate to a different page, "add section", where you can add another template section to the current page, "website styles", where you can change global settings such as fonts and colours, and "add element", where you can drag and drop individual elements into the canvas to edit.
  >- A central canvas where the actual web page can be previewed
  >- A popup modal for the centre which appears when the user needs to select a section or element to add to the page
  >- A styling section on the right-hand side where the user can edit all of the styling properties for a selected element


  - The central canvas will import the raw HTML and CSS files from the server and rely on data tags in the HTML element to understand what does what and how to edit it.
  - Whenever a widget is selected, a box will be drawn around it, with the ability to resize it. The style menu on the right will also populate with style options for the selected element that can be changed in real-time and previewed when hovered over so that the user can easily understand what certain buttons will do.
  - Whenever a widget is selected and held, an outline of the parent section's grid system is previewed, and the element can be moved around. It does this by tracking the cursor's position and relating that to the start position of the cursor on the widget (the anchor point) to render it in the correct place using left, right, top, and bottom CSS tags. When released, the widget will snap into the nearest grid space to where it was released. A similar thing happens when the user selects and holds one of the resize elements on the outline, where it tracks the cursor and then snaps into the closest grid space to resize it.
  - The position parameters, that are changed as described above, are separate for the desktop and mobile views of the web page. Changing the position when the page is in desktop mode will not affect the position in mobile mode and vice versa.
  - When a widget is right-clicked, it will show useful commands such as copy, paste, delete and duplicate.
  >

#### Desirable Features
  - Ability to (export and) import sites in a zip file so you can transfer them between sites, which is different to downloading a usable copy of the website. An export function may not be necessary as it is given in the site settings.
  >

  - When creating the site, the user can select options that allow them to change the default styling properties of the site.
  > These will be the options for colour palettes and font families.

  - The site owner can assign other users the ability to edit public or private sites, but there cannot be two people editing simultaneously. (This is because it would be more complicated to program)
  >

  - To export the site, the user will have two options that will be clearly defined in the UI
  - They can download the site, which will download a zip file containing all the required HTML, CSS, and JavaScript code, so that they can unpack the archive and run the webpage by simply opening the HTML file.
  - They can export the site, which will download a different zip file that contains all of the internal files that Kraken uses to run the editor for the page. This means the user can download backups and send their websites to others.
  >

## Design

### URL Navigation

  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TB
      a((Root)) --> o(Login):::g
      a --> p(Signup):::g
      a --> b(Account):::o
      a --> j("&lt;username&gt;"):::g
      a --> q(Home):::o
      b --> c(Settings):::o
      b --> i(Logout):::o
      c --> d(Profile):::o
      c --> e(Admin):::o
      c --> f(Looks):::o
      c --> g(Sites):::o
      c --> h(Code):::o
      j --> v("&lt;sitename&gt;\n (public)"):::g
      j --> k("&lt;sitename&gt;\n (private)"):::r
      v --> l(Home):::g
      k --> w(Home):::r
      w --> m
      w --> n
      l --> m(Edit):::r
      l --> n(Settings):::r
      q --> r(New):::o --> s(1):::o
      r --> t(2):::o
      r --> u(Generate):::o
      classDef g fill:#030
      classDef o fill:#630
      classDef r fill:#600
  ```

  The different nodes are colour coded based on the permission required to access those pages. If a user does not have the required permission, the user will be redirected to the nearest parent node that the user has access to. If they are signed out, most of the pages will redirect the user to the Login page. The colour coding is as such:
  - Green: Any user can access this page, and they do not need to be signed in; it is public.
  - Orange: You need to be logged in to access this page. This mostly relates to account-based pages such as the settings menu or creating a new site.
  - Red: You need to be the owner of this website, or have sufficient permissions granted by the owner. This only applies to the user websites that are set to private.

### User Interface Design

  ![Main Page Template diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/MainPageTemplate.png?raw=true)

  This is the main "template" on which all pages are built, where the main content will be displayed inside. Defining this in a separate file beforehand (`/templates/base.html`) means that the website has a more unified feel and allows the user to go home and access the navigation menu. Defining it in a separate file also removes redundancy, as the code for it only appears once.

  Home Button
  >The Home button is placed in the top left-hand corner so that it is easy to find and matches how other websites do it; it conforms to the established design patterns and standardised expectations that the user will be familiar with.

  Hamburger
  >The navigation menu has been hidden behind a hamburger at the bottom of the sidebar. This is because, due to the navbar being docked on the side, having lots of links on it would look messy and be hard to read. Therefore, the user can click the hamburger, and a modal will appear with all those links. Clicking the hamburger again, or anywhere else on the screen, will close the modal. The reason why the navbar is on the side of the screen is not only a design choice, but it means that the website builder has more space vertically.

  Main Content
  >This area is where most of the interactive elements will be. These can be seen in the following diagrams.

#### Login and Signup Pages

  ![Login/Signup page diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/LoginFormTemplate.png?raw=true)

  This shows the layout of the login and signup pages. Built inside the main template, it contains the following:
  - The header to tell the user what they are doing
  - The buttons to toggle between login and sign up
  - A warning message area for incorrect credentials or invalid input
  - The form area, which is populated by inputs with labels next to them
  - The submit button at the bottom

#### Homepage

  ![Homepage diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/HomepageTemplate.png?raw=true)

  This shows the layout of the homepage once the user has logged in, if the user already has created a website. If the user has not made any websites yet, it will look similar to this but without the grid of their websites. Built inside the main template, it contains the following:
  - The header, saying "Welcome, `<username>`" so that they know that it is the homepage
  - A grid of all of their current sites.
  > The grid will programmatically change the number of columns based on the display size. It contains square `div`s, each showing the title of the website, an icon informing the user as to whether it is public or private, and is coloured based on the primary colour of said website. The text colour redefines itself based on what the background colour of the `div` is, to make sure it is easy to read

  - A create new site button with the same dimensions as the site `div`s, at the end of the grid layout.

#### Site Home

  ![Site home diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/SiteHomeTemplate.png?raw=true)

  This shows the layout of the site page for the owner (when they visit `/<username>/<sitename>`). Built inside the main template, it contains the following:
  - The header displays the site's name so that the user knows which site they are editing.
  - Navigation options, a list of links that allow the user to navigate the menu system
  > The links include:
  >- Home, which will display a preview of the website in the content window
  >- Edit site, which links to the editor
  >- Site preferences, site styles, and site settings all open setting menus in the content window.

  - The main content window will display content based on what is selected in the navigation options. By default, it will display a preview of the website but can also display setting menus as well.

#### Site Edit

  ![Site edit diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/SiteEditTemplate.png?raw=true)

  This shows the layout of the site editor. Built inside the main template, it contains the following:
  - The navigation bar, docked to the left, contains icons for different links. When hovered, these icons will display a label for what they will open.
  > Some of these options will be: Add section, add element, website pages, website styles, and website settings

  - The display options bar, docked to the top, will contain some settings for how the editor is shown and are put here so the user can easily access them.
  > These will include display size, switching between desktop, tablet, and mobile aspect ratios, previewing the website, and other settings.

  - The selected element options, docked to the top, will contain quick-access site settings until an element is selected in the content window. When an element is selected, it will display style settings.
  >  

  - The content window will display the site so the user can edit it. There is more information on the mechanics of this section in other parts of the report.

### User Settings Pages

  ![User settings diagram](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/templates/SettingsTemplate.png?raw=true)

  This shows the layout of the settings for the logged-in user. Built inside the main template, it contains the following:
  - The header displays "Settings" to inform the user of what page they are on.
  - Settings navigation options, a list of links that separate different categories of settings
  > The links include:
  >- Public Profile - settings that dictate how your profile will appear to other people, such as name, profile picture, and bio.
  >- Account - account based settings, most of which have warnings next to them, such as change username, export account data, archive account and delete account.
  >- Appearance & Accessibility - Accessibility settings such as high contrast mode, and utility settings such as tab preference for writing code.
  >- My Websites - A table of the users websites. Contains a link to the website, how large the size of the website is, the name of the site, and its privacy status.
  >- Custom Code & Elements - A beta option for storing custom code and elements, in a similar fashion to the above website menu.
  >- Help and Documentation - Documentation and a help guide for the application.

  - The options content window will display content based on what is selected in the settings navigation options.

### Usability
  The usability features I have considered ensure that the program is easy to use for as many users as possible, including those with accessibility issues. All of the buttons in the designs are large and easy to notice. When font selection or styling is used, previews for what the font looks like are shown so the user can clearly see what it will look like. This functionality is borrowed by other styling and positioning functions in the editor.

  To make it easier for users to navigate and reduce cognitive load on users, the site will have a deliberately simple structure, with many features hidden behind modals or popup boxes. Elements such as the home button will be placed in conventional positions to make it easier for the user to find.

#### Accessibility
  All colours will be checked to ensure a large enough contrast ratio so that people with colour deficiencies will see an adequate contrast between the text and the background. This includes elements such as colour pickers, where the label text that shows the hex code will change colour depending on the background to ensure that it is still readable. [WebAIM](https://webaim.org/resources/contrastchecker/), a website used to improve accessibility on the internet, will be used to ensure that there is enough contrast in the text. Furthermore, links in text blocks will also be checked to ensure that they have at least a 3:1 contrast ratio with the surrounding text and are visible enough. Quoted from [WebAIM](https://webaim.org/intro/#types),
  > "Often, these [accessibility features] promote overall usability, beyond people with disabilities. Everyone benefits from helpful illustrations, logically-organised content and intuitive navigation. Similarly, while users with disabilities need captions and transcripts, they can be helpful to anyone who uses multimedia in silent or noisy environments."

  The basic accessibility requirements that are suggested, and that could apply to this project, include the following:

  |Requirement|Explanation|
  |:---:|---|
  |Provide equivalent alternative text|Provides text for non-text elements. It is especially helpful for people who are blind and rely on a screen reader to have the content of the website read to them.|
  |Create logical document structure|Headings, lists, and other structural elements provide meaning and structure to web pages. They can also facilitate keyboard navigation within the page.|
  |Ensure users can complete and submit all forms|Every form element (such as text fields, checkboxes, and dropdown lists) needs a programmatically-associated label. Some text may not be focused by tabbing through the form. Users must be able to submit the form.|
  |Write links that make sense out of context|Every link should make sense when read out of context, as screen reader users may choose to read only the links on a web page.|
  |Do not rely on colour alone to convey meaning|Colour can enhance comprehension but cannot alone convey meaning. That information may not be available to a person who is colour-blind and will be unavailable to screen reader users.|
  |Make sure content is clearly written and easy to read|Write clearly, use clear fonts, and use headings and lists logically.|
  |Design to standards|Valid and conventional HTML & CSS promote accessibility by making code more flexible and robust. It also means that screen readers can correctly interpret some website elements.|

#### ARIA
  ARIA (Accessible Rich Internet Applications) attributes will be used throughout the website to allow screen readers to navigate the website. These attributes can be used by assistive technologies, such as screen readers, to provide a more detailed and customised user experience. It is particularly useful for improving the accessibility of dynamic content and advanced user interface controls, such as those used in rich internet applications.

### Stakeholder input :D  

### Website structure and backend

#### Flask
  I have decided to use the Flask Python library as the backend for this website, as I have prior experience in using it, and it suits this project. It is well-documented online, relatively lightweight, and easy to use. Although it does not include as many built-in features as other libraries (such as Django), there are plenty of other Python libraries, such as `flask-login` and `flask-sqlalchemy`, that can add in all of the functionality that is missing from the framework.

#### Jinja
  I have decided to use the Jinja2 template syntax for storing the HTML files, as it has in-built functionality with Flask via the `flask.render_template()` function. All of the HTML files used for the website will be stored in the `templates/` folder in the server directory.

  Jinja is a template system built for Python and Flask (other frameworks have different template systems). It uses templates to reduce duplicated code and make it easier to develop. It enables logic operations in the template file, with functionality for `if`, `while`, `for`, and variable declaration and usage.

  An example system of a Jinja file structure might look like this:

  ##### base.html
  ```jinja
  <html>
    <head>
      <title>Jinja Example</title>
    </head>
    <body>

      {% block content %}
      {% endblock %}

    </body>
  </html>
  ```
  ##### itemlist.html
  ```jinja
  {% extends "base.html" %}

  {% block content%}

  <h1>A list of items</h1>
  <ul>
  {% for item in items %}
    <li>{{ item }}</li>
  {% endfor %}

  {% endblock %}
  ```
  ##### main.py
  ```python
  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
      items = ["apple", "banana", "cherry"]
      return render_template("itemlist.html", items=items)
  ```

  In `base.html`, you can see the `{% ... %}`, which states that this is a control statement. In this case, it defines that the `block` referenced as `content` is to be inserted here. Jinja can have multiple blocks with different names so that a child file can add multiple blocks of content in different places throughout the template.

  In `itemlist.html`, you can see that it `extends base.html`, meaning that it is using `base.html` as a template and looking at that file to find where to insert the code inside `block content`. It also uses a `for` loop to programmatically add list items to the website, based on the list `items` imported in `main.py`, in the `render_template()` command. The `{{ ... }}` indicates that the contents are a Jinja expression.

#### HTML, CSS and JavaScript
  As with many websites, this project will be built using HTML (via Jinja's template generation), CSS, and JavaScript. This is because they are all web standards and are therefore supported by all modern web browsers and devices (although devices are not much of an issue as it is designed to be run on a high-resolution landscape display). It will allow for SEO compatibility, is open source (and therefore free), is highly versatile, and can accomplish a lot. I am also very competent with HTML, CSS & JavaScript and have lots of experience programming with them.

### Data storage
  There will be two different methods of storing information for the website:
  - The multi-user system, including the information about the users' sites, will be stored in an SQL database using the `flask_sqlalchemy` Python library so that it can easily be integrated into the Flask backend.
  - The server will store the users' sites, including the HTML, CSS, and JavaScript code.

#### SQL database storage
  This project will use SQL to store the multi-user information as I have previous experience using SQL, so it will be easy to set up and use. It is also useful due to its entity-relationship capability, meaning it will be well-suited for storing information about users' sites. It also has a Python library that integrates into the current backend library that is being used, Flask. This means there will be less work, as most of the functionality needed is already built-in and tested.

  This is the planned entity relationship diagram for the SQL database. It contains two entities, `USER` and `SITE`, connected with a one-to-many relationship with `user_id` being the foreign key in `SITE`.

  ```mermaid
  %%{init: {'theme':'dark', 'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  erDiagram
      USER ||--o{ SITE : has
      USER {
          string user_id
          string name
          string email
          string password
          string bio
          string url
          bool archived
          int tabpreference
      }

      SITE {
          int site_id
          string user_id
          string name
          datetime datecreated
          bool private
          bool deleted
          text sitepath
      }
  ```

  To incorporate a multi-user editing system for certain sites, the entity relationship diagram for the database will look like this. However, this may not be implemented due to time constraints.

  It contains three entities, `USER`, `SITE`, and `LINK`. It is similar to the previous one, with a linking table added between the two original entities, allowing multiple users to edit multiple sites. Each `LINK` also contains information about the `USER`'s permissions for the `SITE`.

  ```mermaid
  %%{init: {'theme':'dark', 'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  erDiagram  

      USER ||--o{ LINK: has
      USER {
          string user_id
          string name
          string name
          string email
          string password
          string bio
          string url
          bool archived
          int tabpreference
      }

      LINK {
          string user_id
          int site_id
          string role
          bool canedit
          bool canview
      }

      SITE ||--o{ LINK: "to"
      SITE {
          int site_id
          string user_id
          string name
          datetime datecreated
          bool private
          bool deleted
          text sitepath
      }
  ```

#### Server-side file storage
  For the actual user website files, server-side storage will be used as it cannot be easily stored in SQL. It is all stored server-side so the user can access their files from any computer with an internet connection. The way I intend to store the site information is shown below:

  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TB
      a(userData) --> b("&lt;username&gt;") --> c(sites) --> d("&lt;sitename&gt;") --> e(files) & f(site.ini) & g(siteDat.json)
      e --> h(1.html) & i(2.html) & j(3.html)
  ```

  The `username` and `sitename` folders will be named by the primary keys of the data in the SQL database to avoid duplicate folder names.

  The `files` folder will contain all the HTML files, named sequentially, and any custom CSS and JavaScript files the user has added.

  The `siteDat.json` file will contain all the information about the site file structure, referencing which page requires which HTML file in the `files` folder and which CSS and JavaScript code blocks need to be imported.
  > The server will have a store of CSS and JavaScript that will format every template element and section.

  The `site.ini` config file will contain all of the information about the site settings, theming, and preferences.

### Algorithms
  The main parts of this solution are using a SQL database to store information about the multi-user system, the UI design and interactivity, and the actual drag-and-drop editor, with the drag-and-drop editor being the most complex.

<!--TODO: add algorithms for hidden navigation bar -->

#### Drag-and-drop editor algorithms
  The main things that the drag-and-drop editor should be able to do are:
  - Display a resize box around a clicked element.
  - Resize an element when its resize box is dragged.
  - Preview a live display of a dragged element (moving with the cursor), along with the resize box rendering where the element will land when dropped (snapping to the grid).
  - Display a set of styling features in the right-hand menu for a selected element or section.
  - Display a set of options next to a selected element.
  - Display a text editor for a selected element with editable text.
  - Display options in the bottom corner of a selected section.
  - Preview a live display of a dragged section, and renumber the sections into their new positions when dropped.

  In the JavaScript code, each element will have a set of event listeners on them, defined by data tags in the HTML elements:
  - `data-kraken-resizable`
  - `data-kraken-draggable`
  - `data-kraken-editable-text`
  - `data-kraken-editable-style`
  - `data-kraken-locked`

  These will define which functionalities can be used for each element.
  For all of the below diagrams, if the element has the tag `data-kraken-locked`, it will only show a button next to the element/section to unlock it.

  When an element is selected, depending on its function, it will be tagged with one of these attributes so that the JavaScript can easily edit it:
  - `data-kraken-selected-text`
  - `data-kraken-selected-style`
  - `data-kraken-selected-resize`
  - `data-kraken-selected-drag`

##### Resize box
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(data-kraken-resizable is clicked) --> B(Render resize box) --> a("In the parent element of\n the selected element, add\n 12 elements with absolute\n positions") & C("For each corner,\n add event listers")
  ```
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    a("In the parent element of\n the selected element, add\n 12 elements with absolute\n positions") --> b("Using CSS, make four\n of them edges, and\n eight of them boxes") & c("Using JS, position them\n so that they create a\n bounding box around\n the element")
  ```
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    C("For each corner,\n add event listers") --> E("When resize box corner\nis clicked (and held)") --> F("Store cursor's current\n position to work out the\n new positioning values") & H("When the cursor's\n position changes") & K("When the cursor is released")
    F --> G("Add temporary width, height,\n and positioning attributes to\n the resize box elements\n and the element itself")
    H --> I("Update the size of the\n resize box elements so that\nit snaps to the grid box\n closest to the cursor") & J("Update the content of\n the element to match the\n resize box's new size")
    K --> L("Take the temporary variables\n and store them as the new\n width, height, and position\n for the element")
  ```

##### Dragging and dropping elements
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(data-kraken-draggable is clicked) --> B(Render resize box) --> D("For each edge,\n add event listeners") --> M("When resize box edge\nis clicked (and held)") --> N("Store cursor's current\n position to work out the\n new positioning values") --> O("Add temporary positioning\n attributes (left right top and\n bottom) to the resize box\n elements and the element itself")
    M --> P("When the cursor's\n position changes") --> Q("Update the position of the\n resize box so that it snaps\n to the nearest grid box") & R("Update the position of\n the element so that it\n follows the cursor")
    M --> S("When the cursor is released") --> T("Set the element's position\n to the closest grid box to\n the cursor, and re-render\n the resize box to match")
  ```

##### Dragging and dropping sections
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(data-kraken-section & data-kraken-draggable is clicked and held) --> B("Add drop shadow until\n dropped to make it clear\n that it's being moved") & C("Store cursor's current\n position to work out the\n new positioning values") & E("When the cursor's\n position changes") & G("When the cursor is released")
    B --> b("It could possibly also\n be scaled down a bit")
    C --> D("Add temporary positioning\n attributes (left right top and\n bottom) to the section")
    E --> F("Update the position of\n the section so that it\n follows the cursor")
    G --> H("Using the mouse\n positions that were\n recorded") --> I("Work out what the new\n order of the sections\n are and renumber them\n accordingly") & J("Restructure the HTML\n file so that the sections\n are in the new order")
    G --> K("Remove any temporary\n styling applied by the\n drag-and-drop feature")
  ```

##### Displaying element and section options
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(data-kraken-editable-style is clicked) --> B("Lookup the class of the\n element that was selected") --> C("Using this, load the relevant\n styling options in the\n right-hand option menu") --> E("When a style option\n is hovered") & F("When a style option\n is un-hovered") & G("When a style option\n is changed") & I("When the element\n is deselected") & H("When the apply\n changes button\n is clicked")
    E --> e("Update this change in\n the element.style of the\n selected element, and\n listen for when it is\n un-hovered")
    F --> f("If the style option was\n not clicked, remove the\n style attribute from the\n element.style of the\n selected element")
    G --> g("Update this change\n in the element.style\n of the selected element")
    H & I--> J("Take all of the newly-added styles in\n element.style and add them to the\n elements style bank")
  ```

##### Displaying text editors
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(data-kraken-editable-text is clicked) --> B("Style the element\n appropriately") & E("Inside the text element\n of the selected element\n (h1, p, etc), append a text\n input element") & G("When the input\n loses focus")
    E --> F("Remove the text from the\n element and set it as the\n content for the input")
    B --> C("Add a coloured underline\n to the text to indicate\n that it is selected for\n text editing") --> D("Copy all styling of the\n text into the newly generated\n input so that it is seamless")
    G --> H("Fetch the content\n of the input") --> I("Remove the input\n and replace it with the\n stored content")
  ```

#### Multi-user system algorithms
  A lot of the SQL and multi-user algorithms are handled by libraries that are being used, which means that function calls can be used, such as `login_user(user)` from the `flask_login` library or `user = self.User.query.filter_by(user_id=username).first()` that uses an inherited class in the `models.py` file to perform an SQL query. As such, it will reduce a lot of the programming work required, as I can call a function from a different module to do it for me.

  The main things that the multi-user system should be able to do are:
  - Read and write to an SQL database that contains information on the users and their sites
  - Use the database to allow the user to log in
  - Use the database to allow a new user to sign up
  - Verify the user's inputs to make sure they are valid
  - Use the database to organise sites and permissions
  - Use the database to store and create sites for the users
  - Generate folders and files on the server to store user and site information
  - Import and export sites that are stored in the database and on the server

##### Login page
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(User submits login information) --> B("Fetch inputs username and\n password from request.form") --> C("Run the SQL query\n &quot;SELECT user_id FROM User\n WHERE user_id=username&quot;\n to fetch the user") --> D("If no user is\n returned, prompt the\n user to try again") & E("If one user is returned")
    E --> F("Hash and check the\n password given against\n that in the database") --> G("If the hashes do\n not match, prompt\n the user to try again") & H("If the hashes match,\n run the login_user\n subroutine and redirect\n them to the homepage")
  ```

##### Signup page
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(User submits signup information) --> B("Fetch the inputs from\n request.form: name,\n email, username,\n password1, password2") --> C("Use the function verifyField\n to check each input") --> D("name:\n canHaveSpace=true,\n canHaveSpecialChar=True") & E("email:\n minLen=0,\n canHaveSpace=false,\n canHaveSpecialChar=true") & F("username:\n canHaveSpecialChar=false") & G("password1:\n minLen=8") --> H("If any of these return\n an error, prompt the\n user to try again") --> h("Else, continue to the next\n phase of validation") --> I("Check email to make sure\n it is formatted correctly") & J("Check that password1 doesn't\n equal password2") & K("Using the SQL query\n &quot;SELECT user_id FROM User\n WHERE user_id=username&quot;\n to see whether any other users\n with this username exist") --> L("If any of these return\n an error, prompt the\n user to try again") --> M("Else, run the createUser\n function, sign them in,\n and redirect to home")
  ```

##### Field verification
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(verifyField Function) --> B("Takes variables:") --> a("field:\n the content\n of the field") & b("fieldname:\n the name \nof the field") & c("mustHaveChar:\n whether field\n has to have\n content,\n default=true") & d("minLen:\n the minimum\n length of\n field,\n default=3") & e("canHaveSpace:\n whether field\n can have\n whitespace,\n default=false") & f("canHaveSpecialChars:\n whether field can\n have any of a list of\n special characters,\n default=true")
    A --> C("For each of the\n given options,\n check to see\n whether field\n matches the\n criteria") --> D("If it does,\n return an\n empty string") & E("If not, return\n a string\n containing the\n error message")
  ```

##### Creating a new user
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A(createUser Function) --> B("Takes variables:") --> a("username:\n the user's\n username") & b("email:\n the user's\n email address") & c("name:\n the user's name") & d("password:\n the user's\n hashed password")
    A --> C("Insert a new user\n into the User table\n using the given variables") --> D("Generate the user's\n folder structure in the\n server storage")
  ```

##### Creating a new site
  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A("User clicks on the\n create new site option") --> B("Redirect the user\n to the first site create\n page and take them through\n a set of options, seen below") & F("If the user tries to\n go to one of the option\n pages without doing them\n in chronological order,\n they will be redirected\n back to the first page")
    B --> C("When the user\n completes these\n options") & G("When the user completes \na page of options, they will\n be stored in flask.session.\n This means that the \nvariables can be carried over\n into the next page")
    C --> D("They will be\n redirected to the \nhomepage of the\n site") & E("The Flask backend will\n fetch the site settings\n from flask.session,\n and append them to a\n dictionary")
    E --> H("It will then call the\n createSiteStructure subroutine\n to create the site and add\n all of the siteSettings to it")
  ```

  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A("Option Page 1 - General Settings")
    A --> B("The option to import\n an exported site")
    A --> C("The name of the\n new website") --> c("The user will be\n told what the\n criteria are") --> d("If it meets the\n criteria, the input\n box will have a\n green border") & e("If it is too\n short, the input\n box will have a\n red border") & f("If it has any\n illegal characters,\n the input box will\n have an orange\n border")
    f --> g("The user will still be able\n to submit the form,\n but they will be shown\n what the site name will\n look like: any\n illegal characters will\n be replaced with dashes") & h("Illegal characters\n are any character\n that are not lowercase,\n alphanumeric, dashes,\n underscores or periods")
    A --> D("The description\n for the website\n (the user is shown\n that it is optional)") & E("Whether they want\n to set the website to\n public or private") & G("When all options are\n valid, the &quot;Create Site&quot;\n button will become\n clickable")
    E --> F("The user will be\n told that they can\n change this later")
  ```

  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A("Option Page 2 - Colour Scheme") --> C("Whether the user\n wants light or\n dark mode for\n their website") & D("What the light\n and dark bounds\n are (how dark\n should the darkest\n colour be, and\n vice versa)") & E("What the monochromatic\n colour temperature\n should be (using a slider)") & F("What the primary,\n secondary, and accent\n colours are (using\n colour pickers)") --> G("All of these options will affect a set of\n preview boxes showing what the different colours will be") --> H("When they are finished,\n the user can click continue\n to move to the next page")
  ```

  ```mermaid
  %%{init: {'theme':'dark', 'flowchart': {'curve': 'linear'},'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  graph TD
    A("Option Page 3 - Font Family") --> C("The user will be displayed a\n list of font groups") --> D("Each group will have a main,\n large font, and a smaller font\n (with the label paragraph text)") --> E("The font names will be\n displayed in their\n respective fonts") --> F("The user can click on a\n font pair to select it,\n and then click continue\n to finish")
  ```

##### User Settings algorithms

  <!--TODO: user settings algorithms-->

### Diagram showing how the subroutines link

  <!--

  MERMAID MINDMAP DOESN'T WORK IN GITHUB MARKDOWN YET, SO USE AN IMAGE INSTEAD

  ```mermaid
  %%{init:{
    "theme": "base",
    "themeVariables": {
      "primaryColor": "#98c4e4",
      "secondaryColor": "#b3c3ff",
      "tertiaryColor": "#ccd7ff"
    }
  }}

  mindmap
    root((MAIN))

      (Editor Opened)
          (Check for user permissions)
              (If editor, run as normal)
              (If viewer, direct to the preview page)
              (If private, display an error screen)
          (Load files from the server)
              (Necessary files will be listed in the siteDat JSON file)
              (HTML will be populated with kraken data attributes)
              (Apply all of the necessary CSS and JavaScript)
                  (Use dedicated style and script tags instead of importing them)

      (Action taken)
          (Store action in action log)
              (This can be accessed for undos, redos and saves)

      (Editor Saved)
          (If an element is selected, prompt to deselect to save)
          (Fetch HTML from the editor)
              (Remove imported CSS and JavaScript from HTML block)
              (Remove any current selected tags)
              (Update any changed HTML files in the server storage)
          (Look at the action log for any changes to imported files)
              (If changes, update sideDat JSON file as necessary)

      (Display settings changed)
          (If the aspect ratio has been altered)
              (Append necessary data attributes to container element)
              (Resize container as necessary)
              (Update JavaScript display size variables)
                  (So that it knows what CSS and HTML to update, if necessary, and which subroutines to call on event listeners)


      (Element Selected)
          (If locked, pass)
              (Display unlock button)
          (Check for attributes to determine functionality)
              (If styleable, populate the style area with relevant options)
                  (Listen for hovers and selects to add styling)
                  (Listen for deselection of the element to update styles)
              (If draggable, draw a bounding box)
                  (Listen for click and hold)
              (If resizable, draw a bounding box with resize points)
                  (Listen for click and hold)
          (Append necessary selected tags)

      (Section Selected)
          (If locked, pass)
              (Display unlock button)
          (Check for attributes to determine functionality)
              (If styleable, populate the style area with relevant options)
                  (Listen for hovers and selects to add styling)
                  (Listen for deselection of element to update styles)
              (If draggable, listen for click and hold)
              (If resizable, listen for hover over the bottom border)
                  (Display a resize toggle and listen for click and hold)
              (Append necessary selected tags)
  ```

  -->

  ![Diagram showing how the subroutines link](https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/diagrams/mermaid-mindmap-subroutines.svg?raw=true)

### Subroutines
  Now that I have a rough idea of what the subroutines will do and how they will fit together, I can start planning them in pseudocode. The multi-user subroutines will be written in Python, as it is used for the backend, whereas the subroutines for the website builder will be written in JavaScript and imported into the HTML.

  <!--TODO: Talk about how the JavaScript subroutines will be organised in the files.-->

#### Multi-user system - login system

##### auth_login_post
  The Flask backend will call this subroutine when the user submits the login form. The subroutine can fetch input data from the form using the `flask` `request` import. The password it receives will already have been hashed on the client's side so that it is being sent over the internet encrypted.

  ```python
  flask.route("login",method=post)
  def auth_login_post(): # run when the user submits the login form

    # fetch inputs from the form using the ids of the inputs
    username = flask.request.form.get("username")
    password = flask.request.form.get("password")
    remember = flask.request.form.get("remember")

    # fetch a list of users that match the username from the database
    user = db.query(f"SELECT * from USER where user_id={username}").fetchall()

    # if the list of users is empty
    # or the user's hashed password doesn't match the inputted hashed password
    if user.length = 0 || user[0].password == password:
      # flash() passes a message to the next request (next page the user will see)
      flash("Please check your login details and try again")
      # redirect the user to the login page and ask them to try again
      return flask.redirect(flask.url_for("auth_login"))

    flask.login_user(user,remember=remember) # login the user
    return flask.redirect(flask.url_for("main_home"))
  ```

##### auth_signup_post
  The Flask backend will call this subroutine when the user submits the signup form. It uses similar functionality to the `auth_login_post` function, including the passwords being hashed client-side. It uses the `verifyField` and `isEmailFormat` subroutines to check that fields are valid and the `createUser` subroutine to insert a new user into the database and add them to the server storage. Both subroutines are shown later.

  ```python
  flask.route("signup",method=post)
  def auth_signup_post(): # run when the user submits the signup form

    # fetch inputs from the form using the ids of the inputs
    name = flask.request.form.get("name")
    email = flask.request.form.get("email")
    username = flask.request.form.get("username")
    password1 = flask.request.form.get("password")
    password2 = flask.request.form.get("password-repeat")

    # Use the verifyField function to check the inputs are valid.
    #It returns an empty string if valid or an error message if not.
    out = verifyField(name,"Name",canHaveSpace=True,canHaveSpecialChar=True)

    if out.length > 0:
      flash([True,out,"",email,username])
      return flask.redirect(flask.url_for("auth_signup"))

    out = verifyField(email,"Email",minLen=0,canHaveSpace=False,
    canHaveSpecialChar=True)

    if out.length > 0:
      flash([True,out,name,"",username])
      return flask.redirect(flask.url_for("auth_signup"))

    # Check to see whether the email is in a valid format
    if not isEmailFormat(email):
      flash([True,"Email is not in a recognised format",name,"",username])
      return flask.redirect(flask.url_for("auth_signup"))

    # Run an SQL query to check whether this email already has an account
    user = db.query(f"SELECT * from USER where email={username}").fetchall()

    if user:
        flash([True,"That email is already in use",name,"",username])
        return flask.redirect(flask.url_for("auth_signup"))

    out = verifyField(username,"Username",canHaveSpecialChar=False)

    if out.length > 0:
      flash([True,out,name,email,""])
      return flask.redirect(flask.url_for("auth_signup"))

    out = verifyField(password1,"Password",minLen=8)

    if out.length > 0:
      flash([True,out,name,email,username])
      return flask.redirect(flask.url_for("auth_signup"))

    # Make sure the passwords match
    if password1 != password2:
      flash([True,"Passwords do not match",name,email,username])
      return flask.redirect(flask.url_for("auth_signup"))


    # run the createUser function to insert a user into the database
    createUser(username,email,name,password)

    # redirect to the home page
    return flask.redirect(flask.url_for("main_home"))
  ```

  <!--TODO: talk about how the flashes for the error messages work-->

##### verifyField
  This subroutine will be called from `auth_signup_post` to ensure that all of the fields the user inputted are valid. It takes four variables, the requirements that the field has to meet, along with the field's content and name for any error messages. It will return an empty string if the field meets all the requirements and an error message if it does not.

  ```python
  def verifyField(field,fieldName,mustHaveChar=True,minLen=3,
    canHaveSpace=False,canHaveSpecialChar=True):
    # field, required, string, the content of the field
    # fieldName, required, string, the name of the field inputted
    # mustHaveChar, optional (default=true), boolean, whether or not field must
    # contain characters
    # minLen, optional (default=3), integer, the minimum length of field
    # canHaveSpace, optional (default=false), boolean, whether or not field can
    # contain whitespace
    # canHaveSpecialChar, optional (default=true), boolean, whether or not field
    # can contain any of a list of special characters

    # the list of special characters that canHaveSpecialChar refers to
    specialChar = "%&{}\\<>*?/$!'\":@+`|="

    # Make sure that field is the correct datatype
    if field.type is not str:
      raise Exception(
      f"Invalid data type for field. Expected string, received {field.type}")

    # If field is empty and mustHaveChar is true
    if field.length == 0 and mustHaveChar:
      return f"{fieldName} is not filled out."

    # If field is shorter than minLen
    if field.length < minLen:
      return f"{fieldName} must be greater than {minLen-1} characters."

    # If field contains spaces and canHaveSpace is false
    if not canHaveSpace and " " in field:
      return f"{fieldName} cannot contain spaces."

    # If the field contains any of the specialChars and canHaveSpecialChar is false
    if not canHaveSpecialChar:
      for char in specialChar:
        if char in field:
          return f"{fieldName} cannot contain '{char}'"

    # Everything's good; return an empty string
    return ""
  ```

##### createUser
  This subroutine will be called from `auth_signup_post` when it wants to add a new user to the system. Using the arguments given, it will insert a new user into the database and generate the required folder structure for the user using the subroutine `generateFolderStructure`. It is a procedure, so it will not return anything.

  ```python
  def createUser(username,email,name,password):
    # generate the model for a new user
    newUser = db.User(
      user_id=username,
      name=name,
      email=email,
      password=password,
      bio="",
      url="",
      archived=False,
      tabpreference=4,
    )

    # the base path for where the folders should be created
    prefix="static/data/userData/"

    # using the os.path module, get the absolute paths of the required folders
    folderStructure=[os.path.abspath(f"{prefix}{u}"),
                     os.path.abspath(f"{prefix}{u}/sites/")]

    # create all the required folders
    generateFolderStructure(folderStructure)

    # using the generated model, commit it to the database
    db.session.add(newUser)
    db.session.commit()
  ```

##### Diagram showing how these subroutines link

#### Multi-user system - creating a new site
  <!--TODO: add the algorithms for creating the sites-->

##### Diagrams showing how these subroutines link

#### Multi-user system - user settings
  <!--TODO: add the subroutines for user settings-->

##### Diagrams showing how these subroutines link

#### Utility subroutines
  These subroutines are called in different parts of the Python files to perform specific actions. This means that it removes duplicate code for procedures that may need to be used many times throughout

  <!--TODO: add subroutines relating to user settings-->

##### generateFolderStructure
  This subroutine is called whenever the code needs to generate a list of folders. It makes use of the in-built `os` library in Python. It is called when a new user is created or when a user creates a new site.

  ```python
  def generateFolderStructure(folders):
    for folder in folders: # iterate through the list of folders
      if os.path.isdir(folder): # if the folder already exists
        continue
      try:
        os.makedirs(folder)
      except OSError as e: # error catching if required
        raise OSError(e)
  ```

##### generateFileStructure
  This subroutine is called whenever the code needs to generate a list of files. It makes use of the in-built `os` library in Python. It is called when a user creates a new site.

  ```python
  def generateFileStructure(files):
    for file in files: # iterate through the list of files
      if os.path.exists(file): # if the file already exists
        continue
      try:
        with open(file,"w") as f: f.close() # write a new, empty file
      except OSError as e: # error catching if required
        raise OSError(e)
  ```

  <!--TODO: pseudocode for a multi-user permission system for the sites-->

  <!--TODO: JavaScript pseudocode for drag and drop editor-->

### Explanation and justification of this process
  The initial concept seems large and complicated, but the way it is broken down above into separate parts will make the development easier and faster, and will aid the testing and maintaining of the code due to it's modularity.

  The program will be split into three main sections: the multi-user system (including the login system and the creation of sites), the site edit system (including the drag-and-drop editor and the styling system), and the user interface.

  The multi-user part of the program will integrate with the SQL database and the server-side file storage. It is mostly made of sequential algorithms that are either called when the user performs a certain interaction, or when another algorithm calls them.

  The diagrams above can be used to explain this. The `auth_signup_post` subroutine is called when the user completes the signup form, which then calls the `verifyField`, `isEmailFormat`, and `createUser` subroutines.

  Breaking it down like this ensures that the program is modularised in such a way that all of the subroutines can interact with each other. If there is a bug that needs fixing, or a change that needs implementing, it is easy to find the code that needs editing and change it without breaking the rest of the program.

  The code will be very modular, which will help with development and any changes that will be made later. This will be achieved by following this design and separating the multi-user system, editing system, and user interface. If another developer were to take over the programming, this design would make it easier to understand and make ammendments. The two different programming languages, Python and JavaScript, will communicate via Flask's `session` and `flash` features to make sure that the two languages can interact with each other. The functions will be containied in a class, that will be initialised when ran, to make use of the `self` variable communication so that all of the subroutines can use the same variables. It will also use variables and `return` statements for some subroutines where necessary.

### Inputs and Outputs
  |Input|Process|Output|
  |---|---|---|
  |Login submit button| `auth_login_post` to verify user input.| Log in the user to the session, or providing a suitable error message.|
  |Signup submit button| `auth_login_signup` to verify user input, insert the new user into the database and generating the new folder structure for the user.| Log in the user to the session, or provide a suitable error message.|
  |Create site inputs (when the user goes through the new site creation pages)|Store the inputs in the session, and generate a new site in the database & file structure from the inputs given.| Redirect the user to the site page.|
  |Home button| Redirect the user to the homepage.| Redirect the user to the homepage.|
  |Menu hamburger| Darken the main content and display the menu items over them.| Show the user the menu items.|
  |Hamburger open and anything else selected| Remove the darkening of the main content and hide the menu items.| Hide the menu items.|
  |Site edit option (Add Section, Website Pages, etc)| A modal will open over the main content with the main content being darkened, with the content relating to the selected option.| A modal with relevant options is displayed.|
  |Display size option.| The site container will change width to match the option selected. The elements in the container will have the necessary data tags appended.| The editing window will change size to match the selected option.|
  |Element selected| Fetch element data tags to perform appropriate tasks. Listen for events such as dragging the element, or the resize box, if necessary.| Display appropriate style settings in right hand dock. Display resize box. Display text editor if necessary.|
  |Section selected| Fetch section data tags to perform appropriate tasks. Listen for events such as dragging the section up and down, or dragging on the bottom to resize, if necessary.| Display appropriate style settings in right hand dock. Display resize bar on bottom when hovered.|
  |Style option hovered| Apply the hovered style to the selected element.| Render what the element will look like with the hovered style.|
  |Style option selected| Apply the selected style to the selected element.| Add the selected style option to the element.|

### Key variables
  These are the main variables that the Python program will use:
  |Name|Data Type|How it is used|
  |---|---|---|
  |`host`| string, in the format `x.x.x.x`| Defines the host the server uses|
  |`port`| integer| Defines the port the server uses
  |`db`| `flask_sqlalchemy.SQLAlchemy` object| Access the SQL database|
  |`loginManager`| `flask_login.LoginManager` object| Manage the user login system|
  |`app`| `flask.Flask` object| Manage the site routing|

  These are the main variables that the JavaSript code will use:
  |Name|Data Type|How it is used|
  |---|---|---|
  |`requiredChars`| string| A set of characters of which at least one must be in a site name for it to be valid.|
  |`allowedChars`| string| A set of characters that are allowed in the site name when creating a new site.|
  |`defaultColors`| dictionary of strings| The default colour scheme when generating a new site.|
  |`colors`| dictionary of strings| The selected colour options when generating a new site.|
  |`colorDisplay`| dictionary of lists of elements| The colour preview elements when generating a new site - the first one is the element that changes colour, the second one is the text element that displays the current hex colour.|
  |`colors`| dictionary of strings| The selected colour options when generating a new site.|
  |`textOptions`| list of elements| A list of the text options when generating a new site - they get given event listeners for when they are selected.|
  |`sectionSelectorNavSelected`| string| A written number referring to the selected section category in the `Add Section` modal.|
  |`sectionSelectorNavSelectedInt`| integer| An integer version of the previous variable. A written number is used to insert it into classes, as integers are not allowed.|
  |`sectionSelectorNavItem`| string| Template for a section link element for the section navigation bar in the `Add Section` modal.|
  |`selectedElement`| element| The currently selected element.|
  |`fonts`| list of dicts| A list of all of the fonts that the style settings use.|
  |`fontDropdownItem`| string| Template for a font dropdown element for the font family dropdown in the style modal.|

### Validation
  To make sure that the program is robust and will not throw critical errors, validation will be used throughout the code to ensure that the data entered by users is accurate, complete, and conforms to specific rules and constraints. Due to the usage of `<input>`s in the HTML code as the vast majority of the input methods, HTML can make sure that the correct data type is being inputted. However, some text that the user input needs to be validated to make sure that it meets certain requirements. Instances of this include:

##### Login and signup forms
  For the login and signup forms, the text inputted need to have specific parameters. For example, the username must have a minimum length of 3 characters, must not contain special characters, and must be unique in the database. To verify most of this, the `verifyFunction` subroutine is used. This subroutine is outlined earlier in the document. For specific things like checking that the username is unique, or that the password matches the given user, SQL queries are used to validate the inputs. The data here is verified on the client-side before being sent, and is then checked server-side to double check that the data is valid.

##### Website Name when creating a new site
  The website name must meet these specific requirements:
  - At least four characters
  - At least one alphanumeric character
  - Illegal characters can be inputted, but will be changed

  In the JavaScript, it will take the content of the input and replace any illegal characters into dashes, then display this name to the user. It will also make sure that the form can be submitted until the input matches the given criteria. This process is outlined earlier in the document. This is an example of client-side validation, where the JavaScript checks the data locally before sending it off to the server.

##### Importing an exported site
  When the user attempts to import a zip file containing a website, the zip file will be verified to conform with a specific format that exporting will use. If any malicious files are found, or any extra files that are not supposed to be there, the website will throw an error client-side before sending it to the server. It will also make sure that the HTML files contained are in the correct format.

##### Uploading data to the CMS
  There will be a whitelist for the allowed files that can be uploaded to the CMS, and these will be checked and validated before they are sent to the server.

##### Data Sanitization
  Throughout the code, the user input will be checked and cleaned to remove the risk of potentially dangerous or malicious data before being stored in the database. For example, to negate the possibility of an SQL injection attack, the library used to manage the database removes any usage of SQL queries in the code, meaning the data inputted cannot be used to execute a query. Other attack methods that will be looked into include XSS (cross-site scripting), DDoS (distributed denial of service), and MitM (man in the middle) attacks.

### Testing method
  When developing the project, a lot of the alpha testing done will be white box testing, done by the developers. Unit testing will be used to ensure that all of the subroutines function as expected and intended. By testing each module of the program individually, this means that when they are all combined together, the program will function correct. Integration testing will be performed to make sure the program functions as a whole. This will include checking how different modules interact with each other, and how the front-end interacts with the back-end of the website.

  Different areas of testing when programming will include the input data of the program (for example, the user input on the login form), how the program handles said data, and what the result will be. To ensure that it has suitable error catching throughout, each module should go through destructive testing. For user input, this means using a variety of incorrect entries to see how it handles them. For the editor, this means attempting to perform styling that is invalid, dragging elements outside their boundary region, or making them too large. This will also include security testing; making sure that SQL injection or XSS attacks do not work.

  Usability testing will be done both white-box and black-box - the UI design will be tested during and after development and will be tested with some of the stakeholders to make sure that it is easy to understand and navigate, and that it functions as intended on a variety of devices, resolutions, and browsers. Feedback, criticisms, and suggestions from the stakeholders will be taken after these sessions to ensure that the final product is easy to use and meets their requirements.

  Any testing will be recorded during the development process, such as different platforms used in the UI design, or invalid inputs entered when checking user input.

## Development and Testing

### Stage 1 - Setting up the website

  Before creating the database system, I decided to get the website backend up and running, and design the login and signup pages, to make it easier to test certain elements of the database. This includes setting up the template design for the front-end, creating a form system with verification in JavaScript, and performing validation server-side. The first thing I did was get the flask backend running. For this, I modified some code that I have used before when using Flask as a backend.

##### \_\_init\_\_.py
  ```python
  from flask import Flask

  # Flask is the application object

  # The main class of the application
  class Kraken():
    def __init__(self,host,port):
      # Create the Flask application and set a secret key
      self.app = Flask("Kraken")
      self.app.config["SECRET_KEY"]="secret-key-goes-here"

      # Initialise the website pages
      self.initPages()

      # Run the Flask application
      self.app.run(host=host,port=port)

    def initPages(self):

      # Home page route
      @self.app.route("/")
      def main_index():
        # Display the returned text
        return "This is the homepage!"

  if __name__ == "__main__":
    # Initialise the application on port 1380
    Kraken("0.0.0.0",1380)
  ```

  When run, it would output this to the console:

  <img alt="The console after running this code" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.1_creatingthebackend_console.png?raw=true" width="750"/>

  And look like this in the website:

  <img alt="The website after running this code" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.1_creatingthebackend_browser.png?raw=true" width="750"/>

  Having got the framework for the backend in place, I then created a basic template for the HTML (in Jinja) and some CSS code to work with it, so that I could test some of the functions that I wanted to use. These files were created at `/templates/test.html` and `/static/css/test.css`, and were deleted afterwards when I knew that the system was functioning as intended. To make sure that some of the modules of Flask were working as intended, I used the `render_template` and `flash` functions in Python, ran a loop in the HTML file using Jinja, and used `url_for` to import the CSS file.

<!-- Having got the framework in place... -->

##### changes to \_\_init\_\_.py
  ```python
  from flask import Flask, render_template, redirect, flash

  # Flask is the application object
  # render_template converts a Jinja file to html
  # redirect redirects the website to another root function
  # flash sends messages to the client
  ```
  ```python
  def initPages(self):

    # Home page route
    @self.app.route("/")
    def main_index():
      # flash sends a message to the next site that flask renders
      flash(["Apples","Oranges","Pears",1,2,3])
      # render_template takes the Jinja template file given in the templates folder
      # and turns it into true HTML
      return render_template("test.html")

  ```

##### /templates/test.html
  ```jinja
  <!DOCTYPE html>
  <html>
    <head>
      <title>Kraken Test :)</title>

      <link href="{{url_for('static', filename='css/test.css')}}" rel="stylesheet"
      type="text/css" />
    </head>

    <body>
      <ol>

        {# Iterate through the list in the first flashed message, and create a
           list element for each one #}

        {% for element in get_flashed_messages()[0] %}
          <li>{{element}}</li>
        {% endfor %}

      </ol>
    </body>
  </html>
  ```

##### /static/css/test.css
  ```css
  ol{
    background-color:#e8e8ff;
    font-size:12px;
    font-family:Lexend,sans-serif;
    width:200px;
  }

  li:first-of-type{
    font-size:16px;
  }
  ```

  When run, the website looked like this:

  <img alt="A screenshot of the test page that I programmed" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.2_testingflaskandjinja_browser.png?raw=true" width="750"/>

  As you can see by the image, using the `flash` function, flask successfully sends the list `["Apples","Oranges","Pears",1,2,3]` to the webpage for it to be recieved by the `get_flashed_messages` function. It also successfully managed to iterate through the list using `{% for element in get_flashed_messages()[0] %}`, and used the `url_for` function to import the stylesheet.

  Before creating the database structure, I decided to create the frontend for the login and signup pages, so that it would be easier to test. Due to the above code working successfully, I started off by making a `base.html` template, that all of the other Jinja files would build on top of. I then created the `login.html` and `signup.html` files as well. This was made easier by my previous experience in web design, as I could use a library of CSS code that I have collected to speed up the design process. To be able to view the templates, I added some `app.route` functions to `__init__.py` using the `render_template` function.

<!-- TODO: add icon code -->

<!-- Before creating the database structure... -->

##### changes to \_\_init\_\_.py
  ```python
  def initPages(self):

     # Home page route
     @self.app.route("/")
     def main_home():
       return "Hi o/"

     # Login page route
     @self.app.route("/login/")
     def auth_login():
       return render_template("login.html")

     # Signup page route
     @self.app.route("/signup/")
     def auth_signup():
       return render_template("signup.html")
  ```

##### /templates/base.html
  ```jinja
  <!DOCTYPE html>
  <html>
    <head>
      <meta http-equiv="Content-type" content="text/html; charset=utf-8">
      <meta http-equiv="Content-type" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">

      <title>Kraken</title>

      <!-- Site Meta -->
      <meta name="title" content="Kraken">
      <meta name="robots" content="index, follow">
      <meta name="language" content="English">

      <!-- Site Icons -->
      <link rel="apple-touch-icon" sizes="512x512" href="{{url_for('static',
        filename='img/icon/apple-touch-icon/apple-touch-icon-512-512.png')}}">
      <link rel="icon" type="image/png" sizes="512x512" href="{{url_for('static',
        filename='img/icon/tab-icon/tab-icon-512-512.png')}}">
      <link rel="mask-icon" href="{{url_for('static', filename='
        img/icon/mask-icon/mask-icon.svg')}}">

      <link rel="canonical" href="CanonicalUrl">

      <!-- Font Awesome Imports -->
      <!-- fa is a large icon database which you can import into a site -->
      <script src="https://kit.fontawesome.com/73a2cc1270.js"></script>
      <link rel="stylesheet" href="
        https://pro.fontawesome.com/releases/v6.0.0-beta3/css/all.css">

      <!-- Internal Stylesheet Imports -->
      <link href="{{url_for('static', filename='css/main.css')}}"
        rel="stylesheet" type="text/css" />
      <link href="{{url_for('static', filename='css/build.css')}}"
        rel="stylesheet" type="text/css" />

    </head>
    <body>

      <div class="page">
        <div class="application-container">

          <!-- Navigation bar, docked on the left hand side -->
          <!-- Contains the logo as a link to the homepage at the top, and a
          hamburger at the bottom -->

          <nav class="globalnav globalnav-vertical">
            <div class="globalnav-content">
              <div class="globalnav-list">
                <div class="globalnav-logo">
                  <a class="globalnav-link globalnav-link-home link unformatted"
                    href="{{ url_for('main_home') }}">
                    <img class="globalnav-logo-image" alt="Kraken" src="{{url_for(
                      'static', filename='img/icon/512-512/kraken-icon-png-primary-
                      512-512.png')}}" preserveAspectRatio>
                    <span class="globalnav-link-hidden-text visibly-hidden">
                      Kraken
                    </span>
                  </a>
                </div>
                  <ul class="globalnav-list">
                    <li class="globalnav-item one fake" role="button"></li>
                    <li class="globalnav-item two" role="button">
                      <div class="hamburger hamburger--collapse js-hamburger"
                        id="globalnav-hamburger">
                        <div class="hamburger-box">
                          <div class="hamburger-inner"></div>
                        </div>
                      </div>
                    </li>
                  </ul>
              </div>
            </div>
          </nav>

          <!-- Floating option modal for the navbar, which is opened and closed
          via the hamburger in the navigation bar -->

          <div class="globalnav-floating-options">
            <!-- URL links are left blank for now as the pages have not yet
            been created -->

            <a class="globalnav-floating-option one" href="">
              <span class="globalnav-floating-option-content text header small">
              My Sites</span>
            </a>

            <a class="globalnav-floating-option two" href="">
              <span class="globalnav-floating-option-content text header small">
              Settings</span>
            </a>

            <a class="globalnav-floating-option three" href="">
              <span class="globalnav-floating-option-content text header small">
              Logout</span>
            </a>
          </div>

          <!-- Backdrop behind nav bar modal to apply a darkness filter behind
          the modal -->

          <div class="globalnav-floating-options-backdrop"></div>


          <!-- External Script Imports -->
          <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/
          jquery.min.js"></script>
          <script src="https://code.jquery.com/jquery-3.5.1.min.js"
          crossorigin="anonymous"></script>

          <!-- Internal Script Imports -->
          <script src="{{url_for('static', filename='js/main.js')}}"></script>
          <script src="{{url_for('static', filename='js/globalnav-floating-options.
          js')}}"></script>

          {% block content %}
          {% endblock %}

        </div>
      </div>

    </body>
  </html>
  ```

  For clarity, I have removed some unnecessary elements from the head of `base.html`, such as the open-graph protocol and some of the meta elements.

##### /templates/login.html
  ```jinja
  {% extends "base.html" %}

  {% block content %}

  <link href="{{url_for('static', filename='css/auth.css')}}" rel="stylesheet"
  type="text/css" />

  <div class="application-content">
    <div class="text-header-container">
      <h2 class="text header xl dark one">Kraken - Login</h2>
      <ul class="header-options">
        <li class="header-option header-option-login active notextselect">
          <h4 class="text header bold">Login</h4>
        </li>
        <li class="header-option header-option-signup notextselect"
        onclick="window.location.href=`{{ url_for('auth_signup') }}`">
          <h4 class="text header bold">Signup</h4>
        </li>
      </ul>
    </div>
    <div class="field-container active">

      <!-- Warning area for the form that uses the flashed warning message -->

      <span class="field-warning text italic">
        <!-- TODO: add code for flashed warning msg -->
      </span>

      <form class="field-options" method="post" action="/login/">

        <div class="field-option field-option-username">
          <h4 class="text italic">Username</h4>
          <div class="field-input-container">
            <input class="field-input" placeholder="Username" type="text"
            name="username">
            <span class="eye-spacer"></span>
          </div>
        </div>
        <div class="field-option field-option-password">
          <h4 class="text italic">Password</h4>
          <div class="field-input-container">
            <input class="field-input" placeholder="Password" type="password"
            name="password">
            <span class="eye-reveal">
              <i class="fa-solid fa-eye"></i>
            </span>
          </div>
        </div>
        <div class="field-option field-option-remember">
          <h4 class="text italic">Remember Me</h4>
          <div class="field-input-container">
            <input class="field-input" type="checkbox" name="remember">
            <span class="eye-spacer"></span>
          </div>
        </div>

        <button class="field-submit btn secondary rounded slide" type="submit">
          <span class="btn-content text uppercase secondary">Submit</span>
        </button>

      </form>

    </div>
  </div>

  {% endblock %}
  ```

##### /templates/signup.html
  ```jinja
  {% extends "base.html" %}

  {% block content %}

  <link href="{{url_for('static', filename='css/auth.css')}}" rel="stylesheet"
  type="text/css" />
  <div class="application-content">
    <div class="text-header-container">
      <h2 class="text header xl dark one">Kraken - Signup</h2>
        <ul class="header-options">
          <div class="header-option header-option-login notextselect"
          onclick="window.location.href=`{{ url_for('auth_login') }}`">
            <h4 class="text header bold">Login</h4>
          </div>
          <div class="header-option header-option-signup active notextselect">
            <h4 class="text header bold">Signup</h4>
          </div>
        </ul>
      </div>

      <div class="field-container active">

        <!-- Warning area for the form that uses the flashed warning message -->

        <span class="field-warning text italic">
          <!-- TODO: add code for flashed warning msg -->
        </span>

        <form class="field-options" method="post" action="/signup/">

          <div class="field-option field-option-name">
            <h4 class="text italic">Name</h4>
            <div class="field-input-container">
              <input class="field-input" placeholder="Name" type="name"
              name="name" autofocus>
              <span class="eye-spacer"></span>
            </div>
          </div>

          <div class="field-option field-option-email">
            <h4 class="text italic">Email</h4>
            <div class="field-input-container">
              <input class="field-input" placeholder="name@domain.com"
              type="email" name="email" autofocus>
              <span class="eye-spacer"></span>
            </div>
          </div>

          <div class="field-option field-option-username">
            <h4 class="text italic">Username</h4>
            <div class="field-input-container">
              <input class="field-input" placeholder="Username" type="text"
              name="username" autofocus>
              <span class="eye-spacer"></span>
            </div>
          </div>

          <div class="field-option field-option-password">
            <h4 class="text italic">Password</h4>
            <div class="field-input-container">
              <input class="field-input" placeholder="Password" type="password"
              name="password">
              <span class="eye-reveal">
                <i class="fa-solid fa-eye"></i>
              </span>
            </div>
          </div>

          <div class="field-option field-option-password-repeat">
            <h4 class="text italic">Repeat Password</h4>
            <div class="field-input-container">
              <input class="field-input" placeholder="Again :/" type="password"
              name="password-repeat">
              <span class="eye-reveal">
                <i class="fa-solid fa-eye"></i>
              </span>
            </div>
          </div>

          <button class="field-submit btn secondary rounded slide" type="submit">
            <span class="btn-content text uppercase secondary">Submit</span>
          </button>

        </form>

      </div>
  </div>

  {% endblock %}
  ```

  The files make use of `url_for` to fetch many different URLs, including page icons, stylesheets, images, links to other pages, and scripts.

  For example, the URL for the home button image in `base.html` is defined by `{{url_for('static', filename='img/icon/512-512/kraken-icon-png-'+navbarLogoColor+'-512-512.png')}}`. The variable `navbarLogoColor` is declared in child templates to define which colour should be used.

   I also added some icons to be used as the logo for the website. They are located in `/static/img/icon/<resolution>/` where there are different folders for each resolution of the icon. These were generated by me using a bit of Python code that I have written previously. To add some variation to the site, there are three colours of logo: primary (blue), secondary (magenta) and gradient (a gradient of the two going from top left to bottom right). These colours match up with the primary and secondary colours of the website, defined in the CSS code.

  The inheriting system is displayed here in these files, where you can see `{% block content %} {% endblock %}` in `base.html`, to define where the code block `content` will be inserted into the file, and then `{% extends "base.html" %}` and `{% block content %} {% endblock %}` in `login.html` and `signup.html`, which define what file will be extended, and which block to insert into.

  The CSS and JavaScript for both pages is imported from the `/static/css/` and `/static/js/` directories respectively. `main.css` is my library of CSS code that I have collected (the syntax for classes is shown below), and `build.css` contains the CSS for the `base.html` template. `build.css` contains the code for the floating navigation options, that I tested by appending classes in devtools. This means that the only thing I need to do for it to work is to program the event listeners. The login and signup pages have a CSS file called `auth.css`, that defines the page-specific styling for the login form.

  For JavaScript, I added in some abstract imports to be filled in later: `main.js` for global code, and `globalnav-floating-options.js` for when I code the navigation bar.

<!-- The css and js ... -->

##### Syntax for /templates/main.css
  ```css
  Global classes:
      .notextselect
      .nopointerevents
      .visibly-hidden
      .fake
      .box
      .no-inversion

  Positional Classes:
      .relative
      .sticky
      .fixed
      .abs
      .static

  Text classes:
      .text <light|dark|primary|secondary|accent|grey-100 => grey-800> [italic] [bold|thin] [ellipsis] [xl|large|default-size|small] [header|jumbo] [lowercase|uppercase] [notextselect] [left|center|right|justify]

  Link classes:
      .text .link [classes for text] [disabled] [link-slide] [notformatted]
      (link-slide class requires the css variable --link-slide-width)

  Btn classes:
      .btn <light|dark|primary|secondary|accent> <square|rounded|pill> [slide]
      .btn.slide [from-left|from-right]

      If slide is set, the btn must contain a span element with syntax:
          span .btn-content .text (all text classes apply here)
      which contains the text of the button

      A span like this is recommended even if the .slide class is not present so you can format the text inside separately

  em classes:
      [classes for text]

  /* .section-content.fixed-width will set the width to 1440px, and will set the width to 100% when the viewport width is less than 1440px */
  ```

##### /static/css/build.css
  ```css
  .globalnav {
      background: var(--colors-grey-200);
      position:fixed;
  }

  .globalnav-floating-options {
      transform:scale(0);
      transform-origin:bottom left;
      opacity:0;
      margin:0;
      transition:transform,opacity,margin,visibility;
      transition-delay:130ms;
      transition-duration: 260ms;
      transition-timing-function: ease-in-out;
      background-color:var(--colors-grey-100);
      position:fixed;
      bottom:0;
      left:96px;
      z-index:8;
      padding:16px 8px;
      display:flex;
      flex-direction: column;
      align-items: center;
      border-radius: 10px;
      visibility:hidden;
  }

  .globalnav-floating-options.is-active {
      margin-bottom:16px;
      margin-left:16px;
      transform:scale(1);
      opacity:1;
      visibility:visible;
  }

  .globalnav-floating-option:not(:first-of-type) {
      margin-top:16px;
  }

  .globalnav-floating-options-backdrop {
      z-index:7;
      position:fixed;
      width:calc(100vw - 96px);
      height:100vh;
      background-color: #000;
      top:0;
      right:0;
      opacity:0;
      transition: opacity 260ms 130ms ease-in-out, visibility 260ms 130ms ease-in-out;
      visibility: hidden;
  }

  .globalnav-floating-options-backdrop.is-active {
      opacity:0.4;
      visibility: visible;
  }

  .application-container {
      width:calc(100vw - 96px);
      height:100vh;
      display:flex;
      flex-direction:row;
      margin-left:96px;
  }

  .application-content {
      width:100%;
      height:100%;
      padding: 16px;
  }

  .application-content .text-header-container {
      margin-bottom:64px;
  }

  .main {
      /*height:calc(100% - 79px - 64px);*/
      width:100%;
      display:flex;
      justify-content: center;
  }

  .main-content {
      width:100%;
      height:100%;
  }

  .main-content.thin {
      width:60%
  }
  ```

##### /static/css/auth.css
  ```css
  .application-container {
      width:100vw;
      height:100vh;
      display:flex;
      flex-direction:row;
  }

  .application-content {
      width:100%;
      height:100%;
      padding: 16px;
  }

  .application-content .text-header-container {
      margin-bottom:64px;
      display:flex;
      flex-direction:column;
      align-items: center;
  }

  .application-content .text-header-container .text.one {
      margin-bottom:16px;
  }

  .application-content .header-option {
      position:relative;
      overflow:visible;
  }

  .application-content .header-option::after {
      content: "";
      background-color: var(--colors-grey-500);
      width: 70%;
      height: 4px;
      border-radius: 5px;
      position: absolute;
      bottom: -5px;
      right: -8px;
      opacity:1;
      transition:background-color 200ms ease-in-out,width 200ms ease-in-out,height 200ms ease-in-out,bottom 200ms ease-in-out,right 200ms ease-in-out,opacity 200ms ease-in-out;
  }

  .application-content .header-option.active::after {
      background-color: var(--colors-secondary-dark);
  }

  .application-content .header-option:hover::after {
      background-color: var(--colors-grey-300);
      width: 100%;
      height: 100%;
      bottom: 0;
      right: 0;
      opacity: 0.2;
  }

  .application-content .header-option.active:hover::after {
      background-color: var(--colors-secondary);
  }

  .application-content .section-header-item:not(:last-child) {
      margin-bottom: 16px
  }

  .application-content .header-options {
      width:50%;
      display:flex;
      justify-content: space-evenly
  }

  .application-content .header-option {
      cursor:pointer;
  }

  .application-content .header-option:active {
      opacity:.8;
  }

  .application-content .header-option.active {
      color:var(--colors-secondary);
  }

  .application-content .field-container {
      display: flex;
      flex-direction: column;
      align-items: center;
  }

  .application-content .field-container .field-submit {
      margin-top:32px;
      align-self: center;
  }

  .application-content .field-container .field-options {
      width:360px;
      display:flex;
      flex-direction:column;
  }

  .application-content .field-container .field-option:not(:last-child) {
      margin-bottom:8px
  }

  .application-content .field-container .field-option {
      display:flex;
      flex-direction: row;
      justify-content: space-between;
  }

  .application-content .field-container .field-option .field-input-container {
      display:flex;
      flex-direction: row;
  }

  .application-content .field-container .field-option .field-input {
      font-family: var(--font-body);
  }

  .application-content .field-container .field-option .field-input-container .eye-reveal,
  .application-content .field-container .field-option .field-input-container .eye-spacer {
      width:19px;
      height:19px;
      display:flex;
      justify-content: center;
      align-items: center;
      margin-left:8px;
  }

  .application-content .field-container .field-option .field-input-container .eye-reveal:active {
      color:var(--colors-secondary);
  }

  .application-content .field-container .field-warning {
      color:#e63832;
      margin-bottom:8px;
      max-width: 360px;
      text-align: center;
  }
  ```

  After running the website, the login and signup pages looked like this:

  <img alt="A screenshot of the login page" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.3_loginfrontend_logincssdesign.png?raw=true" width="750"/>
  <img alt="A screenshot of the signup page" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.3_loginfrontend_signupcssdesign.png?raw=true" width="750"/>

  <!-- TODO: redo these screenshots -->

  Currently, when you click the submit button, it redirects to a page saying "Method not allowed", as the post functions have not been added to `__init__.py` yet.

  The next step was to set up the front-end programming for the login and signup pages, and the navigation bar. Starting with the navigation bar, I needed to set event listeners for the hamburger and background darkener `div`. These listeners would add or remove the `is-active` class to the hamburger, options list, and background, so that the website renders correctly. The file is already imported into `base.html` via `<script src="{{url_for('static', filename='js/globalnav-floating-options.js')}}">`.

<!-- Front end prog - globalnav hide -->

##### /static/js/globalnav-floating-options.js
  ```js
  document.getElementById("globalnav-hamburger").addEventListener("click",()=>{
      document.getElementById("globalnav-hamburger").classList.toggle('is-active');
      document.querySelectorAll(".globalnav-floating-options").forEach((e)=>{e.classList.toggle("is-active")});
      document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{e.classList.toggle("is-active")});
  });

  document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{
      e.addEventListener("click",()=>{
          document.getElementById("globalnav-hamburger").classList.remove('is-active');
          document.querySelectorAll(".globalnav-floating-options").forEach((e)=>{e.classList.remove("is-active")});
          document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{e.classList.remove("is-active")});
      })
  });
  ```

  After running the website, the floating navigation options looked like this:

  <img alt="A screenshot of the floating navigation options when closed" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.3_loginfrontend_floatingnav.png?raw=true" width="360"/>

  There is validation of the inputs both client-side and server-side, so I needed to implement that into the JavaScript for the login and signup pages. I also need to add code so that when the all-seeing eye is pressed, the password field is miraculously revealed. For the validation, I will use the `verifyField` function that I have written in pseudocode (which will also be used in the Python backend). Because of this, there will be three files, `auth.js`, `login.js` and `signup.js` so that there is less duplicated code. There will also be a function `isEmail`, which uses a regex validation check to make sure that the email given is in a valid format.

##### /static/js/auth.js
  ```js
  // Function called for each field to make sure it is in the correct format, takes a few arguments as flags for what makes it valid
  function verifyField(field,fieldName,mustHaveChar=true,minLen=3,canHaveSpace=false,canHaveSpecialChar=true,isPassword=false) {
    // List of special characters for the canHaveSpecialChar flag
    specialChar="%&{}\\<>*?/$!'\":@+`|="

    // Make sure that the input given is a string
    if (typeof field != "string") {throw new Error("HEY! that's not a string?")}

    // Check through all the flags given and throw an appropriate error message if input is invalid
    if (field.length == 0 && mustHaveChar) {return `${fieldName} is not filled out.`}
    if (field.length < minLen) {return `${fieldName} must be greater than ${minLen-1} characters.`}
    if (!canHaveSpace && field.includes(" ")) {return `${fieldName} cannot contain spaces.`}
    if (!canHaveSpecialChar) {
      // Iterate through each character in specialChar to see if its in the input
      // I didn't use regex for this as I wanted to be able to tell the user which character wasn't allowed
      var char;
      for (var i=0;i<specialChar.length;i++) {
        char=specialChar[i]
        if (field.includes(char)) {
          return `${fieldName} cannot contain '${char}'`
        }
      }
    }
    // If the given input is a password
    if (isPassword) {
      // If it doesnt match the given regular expression for password checks
      if (!field.match(/(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_%&{}\\<>*?\/$!'\":@+`|=]).{8,}/)) {
        return `${fieldName} must contain at least 1 of each: uppercase character, lowercase character, number, and special character`
      }
    }

    /*
    Regex pattern breakdown
      (?=.*?[A-Z]) = contains an uppercase character
      (?=.*?[a-z]) = contains a lowercase character
      (?=.*?[0-9]) = contains a digit
      (?=.*?[#?!@$%^&*-_%&{}\\<>*?\/$!'\":@+`|=]) = contains a special character
      .{8,} = has a minimum length of 8 and no upper limit
    */

    return ""
  }

  // Initialise the code for the all seeing eyes to enable viewing the password
  function initAllSeeingEye(element,reveal) {
    // Add onclick event to given element (the eye element)
    element.addEventListener("click", e=> {
      // toggle input type of given input between password and text
      reveal.setAttribute('type',reveal.getAttribute('type') === 'password' ? 'text' : 'password');
      // toggle the fa-eye-slash class for the eye (this sets the icon displayed)
      element.classList.toggle('fa-eye-slash');
    })
  }

  // Function takes a string and returns a boolean determining whether it is in a valid email format, using regex
  function isEmail(email) {
    return email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)
  }

  // fetch warning element and disable submit bottom
  warningSpan = document.querySelector(".field-container .field-warning")
  document.querySelector(".field-submit").disabled = true
  ```

##### /static/js/login.js
  ```js
  // function called when an input is changed, to check whether all inputs are valid
  function verifyAllFields() {
    if (fields["Username"].value.length < 1) {
      warningSpan.innerText = "Username is not filled out"
      document.querySelector(".field-submit").disabled = true
      return
    }

    if (fields["Password"].value.length < 1) {
      warningSpan.innerText = "Password is not filled out"
      document.querySelector(".field-submit").disabled = true
      return
    }

    warningSpan.innerText = ""
    document.querySelector(".field-submit").disabled = false
  }

  // Dictionary of all fields in the form
  fields={
    "Username":document.querySelector(".field-option-username .field-input"),
    "Password":document.querySelector(".field-option-password .field-input")
  }

  initAllSeeingEye(document.querySelector(".field-option-password .eye-reveal i"),document.querySelector(".field-option-password .field-input"))
  document.querySelectorAll(".field-input").forEach(field=>{console.log(field);field.addEventListener("change",verifyAllFields)})
  ```

##### /static/js/signup.js
  ```js
  // function called when an input is changed, to check whether all inputs are valid
  function verifyAllFields() {
    verifyOutput=verifyField(fields["Name"].value,"Name",true,3,true,false)

    if (verifyOutput.length > 0) {
      warningSpan.innerText = verifyOutput
      document.querySelector(".field-submit").disabled = true
      return
    }

    verifyOutput=verifyField(fields["Email"].value,"Email",true,0)

    if (verifyOutput.length > 0) {
      warningSpan.innerText = verifyOutput
      document.querySelector(".field-submit").disabled = true
      return
    }

    // check for email in the correct format
    if (!isEmail(fields["Email"].value)) {
      warningSpan.innerText = "Email is not a valid email address"
      document.querySelector(".field-submit").disabled = true
      return
    }

    verifyOutput=verifyField(fields["Username"].value,"Username",true,3,false,false)

    if (verifyOutput.length > 0) {
      warningSpan.innerText = verifyOutput
      document.querySelector(".field-submit").disabled = true
      return
    }

    console.log("Password")
    verifyOutput=verifyField(fields["Password"].value,"Password",true,8,false,true,true)

    if (verifyOutput.length > 0) {
      warningSpan.innerText = verifyOutput
      document.querySelector(".field-submit").disabled = true
      return
    }

    // Make sure passwords match
    if (fields["Password"].value!=fields["Repeat Password"].value) {
      warningSpan.innerText = "Passwords do not match"
      document.querySelector(".field-submit").disabled = true
      return
    }

    // If no errors are called, then enable the button and clear the warning message
    warningSpan.innerText = ""
    document.querySelector(".field-submit").disabled = false
  }

  // Dictionary of all fields in the form
  fields={
    "Name":document.querySelector(".field-option-name .field-input"),
    "Email":document.querySelector(".field-option-email .field-input"),
    "Username":document.querySelector(".field-option-username .field-input"),
    "Password":document.querySelector(".field-option-password .field-input"),
    "Repeat Password":document.querySelector(".field-option-password-repeat .field-input")
  }

  initAllSeeingEye(document.querySelector(".field-option-password .eye-reveal i"),document.querySelector(".field-option-password .field-input"))
  initAllSeeingEye(document.querySelector(".field-option-password-repeat .eye-reveal i"),document.querySelector(".field-option-password-repeat .field-input"))
  document.querySelectorAll(".field-input").forEach(field=>{console.log(field);field.addEventListener("change",verifyAllFields)})
  ```

  This is an image of the all-seeing eye in action:

  <img alt="A screenshot of the all-seeing eye doing its magic" src="https://github.com/Tomgxz/Kraken/blob/report/.readmeassets/screenshots/development/1.4_loginfrontend_allseeingeye.png?raw=true" width="360"/>

  After implementing the client-side validation, I then tested each field with a variety of different inputs to make sure the validation code was functioning properly

  |Test Type|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
  |-|-|-|-|-|-|-|
  |Valid|Name|`Aaaaa`|Check it says valid|Valid|Valid|Pass
  |Valid|Name|`Aaa Bbb`|Check it allows spaces|Valid|Valid|Pass
  |Invalid|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Valid|Fail
  |Invalid|Name|null|Check that it requires name|Invalid|Invalid|Pass
  |Valid|Email|`a@b.cc`|Check it says valid|Valid|Valid|Pass
  |Valid|Email|`ab12@f42.x7`|Check it says valid|Valid|Valid|Pass
  |Invalid|Email|`@b.cc`|Check it recognises the area before `@`|Invalid|Invalid|Pass
  |Invalid|Email|`a@.cc`|Check it recognises the area after `@`|Invalid|Invalid|Pass
  |Invalid|Email|`a@b.c`|Check it requires a top level domain longer than 1|Invalid|Invalid|Pass
  |Invalid|Email|`a@b.cdef`|Check it requires a top level domain shorter than 4|Invalid|Invalid|Pass
  |Invalid|Email|`a b@ccc.uk`|Check it doesn't allow spaces|Invalid|Invalid|Pass
  |Invalid|Email|null|Check that it requires email|Invalid|Invalid|Pass
  |Valid|Username|`Aaa`|Check it says valid|Valid|Valid|Pass
  |Invalid|Username|`Aaa bbb`|Check it doesn't allow spaces|Invalid|Invalid|Pass
  |Valid|Username|`A-._+c`|Check it allows special characters not given in the list|Valid|Valid|Pass
  |Invalid|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Valid|Fail
  |Invalid|Username|null|Check it requires username|Invalid|Invalid|Pass
  |Invalid|Password|`aaa`|Check it has a minimum length of 8|Invalid|Invalid|Pass
  |Valid|Password|`Aaaaaa_1`|Data to work off for next tests|Valid|Valid|Pass
  |Invalid|Password|`aaaaaa_1`|Check it requires an uppercase character|Invalid|Invalid|Pass
  |Invalid|Password|`AAAAAA_1`|Check it requires a lowercase character|Invalid|Invalid|Pass
  |Invalid|Password|`Aaaaaa_a`|Check it requires a number|Invalid|Invalid|Pass
  |Invalid|Password|`Aaaaaaa1`|Check it requires a special character|Invalid|Invalid|Pass
  |Invalid|Password|null|Check it requires password|Invalid|Invalid|Pass
  |Valid|Passwords|`Aaaaaa_1` in both fields|Check both fields have to match|Valid|Valid|Pass
  |Invalid|Passwords|`Aaaaaa_1` in one field, `ABCDEF` in the second|Check both fields have to match|Invalid|Invalid|Pass

  As you can see from the table, two of the validation checks failed. These are listed here:

  |Test Type|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
  |-|-|-|-|-|-|-|
  |Invalid|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Valid|Fail
  |Invalid|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Valid|Fail

  These were both to do with verifying special characters, and, when I revisited the code, I saw that the error was when I tried to iterate through the characters in a string like you do can do in python. Hence, I modified the line `for (var char in specialChar)` to function properly, and both tests came out as invalid.

  |Test Type|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
  |-|-|-|-|-|-|-|
  |Invalid|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Invalid|Pass
  |Invalid|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Invalid|Pass

##### changes to /static/js/auth.js
  ```js
  function verifyField(...)
  ```
  ```js
    if (!canHaveSpecialChar) {
      var char;
      for (var i=0;i<specialChar.length;i++) {
        char=specialChar[i]
        if (field.includes(char)) {
          return `${fieldName} cannot contain '${char}'`
        }
      }
    }
  ```

  I then implemented the server-side validation, which re-checks all of the validation performed client-side (using the same `verifyField` function), to ensure that the inputs are valid and weren't tampered with client-side. Flask retrieves the values of the form via the `requests` import. The database checking has not yet been implemented at this point, as I wanted to get the login and signup pages fully completed before creating the database. This also involved adding code to the templates to interpret the flashed error message.

<!-- Implemented server-side validation -->

##### changes to \_\_init\_\_.py
  ```python
  from flask import Flask, render_template, redirect, flash, request

  # Flask is the application object
  # render_template converts a Jinja file to html
  # redirect redirects the website to another root function
  # flash sends messages to the client
  # request allows the code to handle form inputs
  ```
  ```python
  # Login post route
  @self.app.route("/login/", methods=["post"])
  def auth_login_post():
    # Get the filled-in items from the login form
    username = request.form.get("username")
    password = request.form.get("password")
    remember = True if request.form.get('remember') else False

    # TODO: get the user from the database. if there's no user it returns none
    if False:
      # Flashes true to signify an error, the error message, the username given, and the remember flag given
      flash([True,'Please check your login details and try again.'])
      return redirect(url_for('auth_login'))

    # TODO: check for correct password
    if False:
      flash([True,'Please check your login details and try again.'])
      return redirect(url_for('auth_login'))

    # TODO: login user
    return redirect(url_for("main_home"))

  ```
  ```python
  # Signup post route
  @self.app.route("/signup/", methods=["post"])
  def auth_signup_post():
    # Get the filled-in items from the signup form
    name=request.form.get("name")
    email=request.form.get("email")
    username=request.form.get("username")
    password1=request.form.get("password")
    password2=request.form.get("password-repeat")

    # the verifyField function returns either an empty string if the field meets the requirements
    # defined by the arguments, or an error message. So, if len(verifyOutput) > 0, that
    # means that the field is invalid

    # Verify the name input and return an error message if invalid
    verifyOutput=self.verifyField(name,"Name",canHaveSpace=True,canHaveSpecialChar=True)

    if len(verifyOutput) > 0:
      # Flashes true to signify an error, and the error message
      flash([True,verifyOutput])
      return redirect(url_for("auth_signup"))

    # Verify the email input and return an error message if invalid
    verifyOutput=self.verifyField(email,"Email",minLen=0,canHaveSpace=False,canHaveSpecialChar=True)

    if len(verifyOutput) > 0:
      # Flash an error message
      flash([True,verifyOutput])
      return redirect(url_for("auth_signup"))

    # Verify the username input and return an error message if invalid
    verifyOutput=self.verifyField(username,"Username",canHaveSpecialChar=False)

    if len(verifyOutput) > 0:
      # Flash an error message
      flash([True,verifyOutput])
      return redirect(url_for("auth_signup"))

    # Verify the password input and return an error message if invalid
    verifyOutput=self.verifyField(password1,"Password",minLen=8)

    if len(verifyOutput) > 0:
      # Flash an error message
      flash([True,verifyOutput])
      return redirect(url_for("auth_signup"))

    # Return an error message if the passwords do not match
    if password1!=password2:
      # Flash an error message
      flash([True,"Passwords do not match"])
      return redirect(url_for("auth_signup"))

    # TODO: check whether this email already has an account

    if False:
      flash([True,"That email is already in use"])
      return redirect(url_for("auth_signup"))

    # TODO: check whether this username already exists

    if False:
      flash([True,"That username is already in use"])
      return redirect(url_for("auth_signup"))

    # TODO: create a new user in the database

    return redirect(url_for("auth_login"))
  ```
  ```python
  def verifyField(self,field,fieldName,mustHaveChar=True,minLen=3,canHaveSpace=False,canHaveSpecialChar=True):
      # List of special characters for the canHaveSpecialChar flag
      specialChar="%&{}\\<>*?/$!'\":@+`|="

      # Make sure that the input given is a string, raise an exception if its not
      if type(field) != str: Exception("HEY! that's not a string?")

      # Check through all the flags given and throw an appropriate error message if input is invalid
      if len(field) == 0 and mustHaveChar: return f"{fieldName} is not filled out."
      if len(field) < minLen: return f"{fieldName} must be greater than {minLen-1} characters."
      if not canHaveSpace and " " in field: return f"{fieldName} cannot contain spaces."
      if not canHaveSpecialChar:
        for char in specialChar:
          if char in field:
            return f"{fieldName} cannot contain '{char}'"

      return "" # Return an empty string if the input is valid
  ```

##### changes to /templates/login.html and /templates/signup.html
  ```jinja
  {% set messages = get_flashed_messages()[0] %}
  ```
  ```jinja
  <span class="field-warning text italic">
    {% if messages[0] %}
      {{ messages[1] }}
    {% endif %}
  </span>
  ```

  At the suggestion of one of the stakeholders, I also added a feature so that when you submit the form, and it throws an error, the form values are carried over so that the user doesn't have to fill them out again. I implemented this using the `flash` function, flashing a list containing the inputs that they had given. To make sure that this didn't cause any issues when opening the page for the first time, the `auth_login` and `auth_signup` functions also flash a list (`[False,"","","",""]`) to prevent any index errors.

<!-- Carrying inputs over -->

##### changes to \_\_init\_\_.py
  ```python
  # Login page route
  def auth_login():
    # Flash an empty list of values to stop errors in the Jinja code
    flash([False,"","","",""])
    return render_template("login.html")
  ```
  ```python
  # Signup page route
  def auth_signup():
    # Flash an empty list of values to stop errors in the Jinja code
    flash([False,"","","",""])
    return render_template("signup.html")
  ```
  ```python
  # Login post route
  def auth_login_post():
  ```
  ```python
    # Flashes true to signify an error, the error message, the username given, and the remember flag given
    flash([True,'Please check your login details and try again.',username,remember])
    return redirect(url_for('auth_login'))
  ```
  ```python
  # Signup post route
  def auth_signup_post():
  ```
  ```python
    if len(verifyOutput) > 0:
      # Flashes true to signify an error, the error message, the name given (removed due to error), the email given, and the username given
      flash([True,verifyOutput,"",email,username])
      return redirect(url_for("auth_signup"))
  ```
  ```python
      # Flash an error message and the filled in values
      flash([True,verifyOutput,name,"",username])
  ```
  ```python
      flash([True,verifyOutput,name,email,""])
  ```
  ```python
      flash([True,verifyOutput,name,email,username])
  ```
  ```python
    # Return an error message if the passwords do not match
    if password1!=password2:
      # Flash an error message and the filled in values
      flash([True,"Passwords do not match",name,email,username])
      return redirect(url_for("auth_signup"))
  ```

##### changes to /templates/login.html
  ```jinja
  <input class="field-input" placeholder="Username" type="text" name="username" value="{{messages[2]}}">
  ```
  ```jinja
  <input class="field-input" type="checkbox" name="remember"  value={{messages[3]}}>
  ```

##### changes to /templates/signup.html
  ```jinja
  <input class="field-input" placeholder="Name" type="name" name="name" autofocus value="{{ messages[2]}}">
  ```
  ```jinja
  <input class="field-input" placeholder="name@domain.com" type="email" name="email" autofocus value="{{ messages[3]}}">
  ```
  ```jinja
  <input class="field-input" placeholder="Username" type="text" name="username" autofocus value="{{ messages[4]}}">
  ```

  To finish the design of the login and signup pages, I added a jinja variable that defines the colour of the logo in the sidebar, and added another variable that defines whether or not the hamburger and subsequent option modal is visible or not. This is because, although it will be required for other sites (such as the homepage), the navigation bar is not necessary here as all of the links in the navigation bar will redirect to `/login` as the user is not signed in.

<!-- Logo color and navbar toggle -->

##### changes to /templates/base.html
  ```jinja
  <!-- navbarLogoColor is a jinja variable that is defined in files that extend from this one. It defines what colour the logo should be - primary, secondary, or gradient -->
  <link rel="apple-touch-icon" sizes="512x512" href="{{url_for('static', filename='img/icon/512-512/kraken-icon-png-'+navbarLogoColor+'-128-128.png')}}">
  <link rel="icon" type="image/png" sizes="128x128" href="{{url_for('static', filename='img/icon/128-128/kraken-icon-png-'+navbarLogoColor+'-128-128.png')}}">
  ```
  ```jinja
  <img class="globalnav-logo-image" alt="Kraken" src="{{url_for('static', filename='img/icon/512-512/kraken-icon-png-'+navbarLogoColor+'-512-512.png')}}" preserveAspectRatio>
  ```
  ```jinja
  {% if navbarOptionsEnabled %}
    <ul class="globalnav-list">
      <li class="globalnav-item one fake" role="button"></li>
      <li class="globalnav-item two" role="button">
        <div class="hamburger hamburger--collapse js-hamburger" id="globalnav-hamburger">
          <div class="hamburger-box">
            <div class="hamburger-inner"></div>
          </div>
        </div>
      </li>
    </ul>
  {% endif %}
  ```
  ```jinja
  {% if navbarOptionsEnabled %}

  <!-- Floating option modal for the navbar, which is opened and closed via the hamburger in the navigation bar -->

  <div class="globalnav-floating-options">
      <a class="globalnav-floating-option one" href="">
          <span class="globalnav-floating-option-content text header small dark">My Sites</span>
      </a>

      <a class="globalnav-floating-option two" href="">
          <span class="globalnav-floating-option-content text header small dark">Settings</span>
      </a>

      <a class="globalnav-floating-option three" href="">
          <span class="globalnav-floating-option-content text header small dark">Logout</span>
      </a>
  </div>

  <!-- Backdrop behind nav bar modal to apply a darkness filter behind the modal -->

  <div class="globalnav-floating-options-backdrop"></div>

  <script src="{{url_for('static', filename='js/globalnav-floating-options.js')}}"></script>

  {% endif %}
  ```

##### changes to /templates/login.html and /templates/signup.html
  ```jinja
  {% set navbarLogoColor = "secondary" %}
  {% set navbarOptionsEnabled = False %}
  ```

  All of the logo images now have the `navbarLogoColor` variable to define which image to fetch. The hamburger and navigation options are now surrounded in `{% if navbarOptionsEnabled %}`. Both of these variables will be defined in files that extend from this file, such as `login.html`. The script import for `/js/globalnav-floating-options.js` has also been moved into the if block to remove unnecessary imports.

### Stage 2 - Creating and implementing the database

  After completing the login and signup pages, I created the dabase, referring to the entity relationship diagram that I had outlined when planning. The two entities are `User` and `Site`, where `user_id` is a foregin key in `Site` to allow them to link together via a one to many relationship. The `User` entity contains some settings information, such as `bio`, `url`, and `tabpreference`, which will be able to be changed in the settings page, that are implemented now to make development down the line easier.

  ```mermaid
  %%{init: {'theme':'dark', 'themeVariables':{'fontFamily':'Lexend,Noto Sans,Helvetica,Arial'}}}%%

  erDiagram
      USER ||--o{ SITE : has
      USER {
          string user_id
          string name
          string email
          string password
          string bio
          string url
          bool archived
          int tabpreference
      }

      SITE {
          int site_id
          string user_id
          string name
          datetime datecreated
          bool private
          bool deleted
          text sitepath
      }
  ```

  The database is managed by the `flask_sqlalchemy.SQLAlchemy` object. In `__init.py`, the object is created (with the variable name `databaseObject`) when the file is run so that `models.py`, the new file that I created which contains the entity classes, can import it. After adding the `databaseObject` object to the class, it imports the two classes from `models.py`, so that the database can interact with them. I also moved all of the flask setup into the function `initFlask` to make the code clearer.

##### changes to \_\_init\_\_.py
  ```python
  from flask_sqlalchemy import SQLAlchemy

  # SQLAlchemy manages the SQL database

  # Create the database object
  databaseObject = SQLAlchemy()

  # The main class of the application
  class Kraken():
    # Global reference to database object
    global databaseObject

    def __init__(self,host,port):
      # Assign the database object to the local db reference
      self.db=databaseObject

      # Initialise the flask application
      self.initFlask()

      # Initialise the SQL database
      self.db.init_app(self.app)

      # Import the User and Site entities from models.py
      from models import User, Site
      self.User=User
      self.Site=Site
  ```
  ```python
    def initFlask(self):
      # Create the Flask application and set a secret key
      self.app = Flask(__name__)
      self.app.config["SECRET_KEY"]="secret-key-goes-here"
      # Set the database file URL to /db.sqlite in the root directory
      self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///db.sqlite"
      self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      # Initialise the website pages
      self.initPages()
  ```

##### models.py
  ```python
  from flask_login import UserMixin

  # Import the SQLAlchemy database object from the main class
  from __init__ import databaseObject as db

  # User class to store the user's information in the database
  class User(UserMixin,db.Model):
    # Set the name of the table in the database to "user"
    __tablename__="user"

    # Define the columns in the table
    # Primary Key user_id as a string
    user_id = db.Column( db.String, primary_key=True )
    # Name as a string
    name = db.Column( db.String )
    # Email as a string, cannot be null and must be unique
    email = db.Column( db.String, nullable=False, unique=True )
    # Password as a string, cannot be null
    password = db.Column( db.String, nullable=False )
    # Bio as a text field
    bio = db.Column( db.Text )
    # URL as a text field
    url = db.Column( db.Text )
    # Archived flag as a boolean, cannot be null (default False)
    archived = db.Column( db.Boolean, nullable=False )
    # Tab preference as a number, cannot be null (default four)
    tabpreference = db.Column( db.Float, nullable=False )

    # Setup the foreign key relationship
    sites = db.relationship("Site")

    # Function to return the primary key
    def get_id(self): return self.user_id

  # Site class to store the User's sites in the database
  class Site(db.Model):
    # Set the name of the table in the database to "site"
    __tablename__="site"

    # Define the columns of the table
    # Primary Key site_id as an integer
    site_id = db.Column( db.Integer, primary_key=True )
    # Foreign Key user_id as a string, referring to user_id in the User table
    user_id = db.Column( db.String, db.ForeignKey("user.user_id") )
    # Name as a string, cannot be null
    name = db.Column( db.String, nullable=False )
    # Datecreated as a datetime format
    datecreated = db.Column( db.DateTime )
    # Private flag as a boolean, cannot be null
    private = db.Column( db.Boolean, nullable=False )
    # Deleted flag as a boolean, cannot be null (default False)
    deleted = db.Column( db.Boolean, nullable=False )
    # Sitepath as a text field
    sitePath = db.Column( db.Text )

    # Function to return the primary key
    def get_id(self): return self.site_id
  ```

  I then ran the following commands in an online SQL editor to create the database, and saved it as `db.sqlite` in the root directory, so that SQLAlchemy could use it.

<!-- I ran the following commands -->

##### db.sqlite commands
  ```SQL
  CREATE TABLE user (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    bio TEXT,
    url TEXT,
    archived BOOLEAN NOT NULL,
    tabpreference INT NOT NULL
  )

  CREATE TABLE site (
    site_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    datecreated DATE,
    private BOOLEAN NOT NULL,
    deleted BOOLEAN NOT NULL,
    user_id TEXT,
    sitePath TEXT,
    CONSTRAINT fk_user_id,
      FOREIGN KEY (user_id) REFERENCES user(user_id)
  )
  ```

  I now added the authentication code to `auth_login_post` and `auth_signup_post` so that they could query the new database. This also included importing the `werkzeug.security` module to implement the hashing of passwords, and the `flask_login` module to implement the logging in system

<!-- Login auth -->

##### changes to \_\_init\_\_.py
  ```python
  from flask_login import LoginManager, login_user

  # LoginManager is the object that manages signed in users
  # login_user logs in a give user

  from werkzeug.security import generate_password_hash, check_password_hash

  # generate_password_hash and check_password_hash are used when generating and authenticating users
  ```
  ```python
    def __init__(self,host,port):
  ```
  ```python
      # Initialise the login manager
      self.loginManager=LoginManager()
      self.loginManager.login_view="auth_login" # set which function routes to the login page
      self.loginManager.init_app(self.app)

      # Fetches a row from the User table in the database
      @self.loginManager.user_loader
      def loadUser(user_id): return self.User.query.get(user_id)
  ```
  ```python
    def auth_login_post():
  ```
  ```python
      # Fetch the user from the database. if there's no user it returns none
      user = self.User.query.filter_by(user_id=username).first()

      if user is None:
        # Flashes true to signify an error, the error message, the username given, and the remember flag given
        flash([True,'Please check your login details and try again.',username,remember])
        return redirect(url_for('auth_login'))

      # TODO: check for correct password
      if not check_password_hash(user.password,password):
        flash([True,'Please check your login details and try again.',username,remember])
        return redirect(url_for('auth_login'))

      # Log in the user and redirect them to the homepage
      login_user(user,remember=remember)
      return redirect(url_for("main_home"))
  ```
  ```python
    def auth_signup_post():
  ```
  ```python
      # Check whether this email already has an account
      if self.User.query.filter_by(email=email).first():
        flash([True,"That email is already in use",name,"",username])
        return redirect(url_for("auth_signup"))

      # Check whether this username already exists
      if self.User.query.filter_by(user_id=username).first():
        flash([True,"That username is already in use",name,email,""])
        return redirect(url_for("auth_signup"))
  ```

  Next, I created the function `createUser`, that would be called when all of the validation in `auth_signup_post` is complete. It takes the variables `username`,`email`,`name`, and `password`. The function creates a new entry in the database, and creates the users file structure in the server-side storage, making use of the `generateFolderStructure` function.

<!-- createUser fn -->

##### changes to \_\_init\_\_.py
  ```python
  def __init__(host,port):
     import os
     self.os=os
  ```
  ```python
  def auth_signup_post():
  ```
  ```python
    # create a new user in the database and send to the login page
    self.createUser(username,email,name,password1)
    return redirect(url_for("auth_login"))
  ```
  ```python
  def createUser(self,u,e,n,p):

    # Create a new User object using the variables given
    newUser = self.User(
      user_id=u,
      name=n,
      email=e,
      password=generate_password_hash(p,method='sha256'),
      bio="",
      url="",
      archived=False,
      tabpreference=4,
    )

    # Server-side folder generation

    prefix="static/data/userData/"

    # List of all folders to create
    folderStructure=[self.os.path.abspath(f"{prefix}{u}"),self.os.path.abspath(f"{prefix}{u}/sites/")]

    self.generateFolderStructure(folderStructure)

    # Create new user and commit to database
    self.db.session.add(newUser)
    self.db.session.commit()

  def generateFolderStructure(self,folders):
    # Iterate through given list of folders
    for folder in folders:
      # Ignore if folder already exists
      if self.os.path.isdir(folder): continue
      # Create folder, and catch any errors
      try: self.os.makedirs(folder)
      except OSError as e:
        raise OSError(
              e)
  ```

  I then modified the `auth_signup_post` function so that it logs you in as soon as the user creates their account.

##### changes to \_\_init\_\_.py
  ```python
  def auth_signup_post():
  ```
  ```python
    # create a new user in the database and server-side storage
    self.createUser(username,email,name,password1)

    # Log in the new user and redirect them to the homepage
    login_user(self.User.query.filter_by(user_id=username).first(),remember=False)
    return redirect(url_for("auth_login"))
  ```

### Features
  To assemble the web pages, the users can drag and drop pre-designed elements categorised into groups such as headlines, quotes, forms, footers, and more. The elements can be previewed in a sidebar next to the main canvas of the page, displayed with the correct styles of the website, from which they can be placed on the webpage. The website would be divided into sections. The user can drag and drop whole sections into the page or add individual elements into an existing section, such as text elements or images. After placing the elements into the canvas, the user can select the element to be able to interact with them by moving them around, changing their styling (such as padding, size, colouring, transparency, position, font size, and many more) in a panel called the inspector panel, adding children to the element, or writing custom element-specific HTML, CSS, or JavaScript code that can be translated into the preview in real-time. These custom elements/pieces of code will then be saved in the user's account so that they can be used in other projects or published so that other users can use them. The canvas will highlight elements with a border when hovered over so that the user can easily see the different elements and how they interact with them. The overall aim of the editor is for someone with very minimal knowledge, even none at all, about web design or programming to be able to interact with it, hence the WYSIWYG intuitiveness.

  The canvas would have options at the top to preview at certain conventional dimensions (for example, 375px for phones and 768px for tablets) or custom widths. This is so the user can view how the elements interact with each other at custom resolutions. The inspector panel elements will also have options to change parameters at different screen resolutions (in the functionality of `@media screen and (max-width: 375px)`). There will also be an option to preview the site in its full functionality, where the user can view all the pages without the extra clutter of the canvas and side panels.

  The styling of the website will be able to be edited in a side panel, where the colour scheme, element preferences, and font face can be changed. There will be custom pre-selected pairings of colours and fonts, but the user would also be able to use their fonts, given they could provide a google fonts link or an OFT/TTF file. The colours could be changed using a colour pricer and certain sliders. The website code itself (when rendering the colours) will reference variables defined at the top of the code in the format --colors-<name>-[light|dark]-[rgb], such as --colors-secondary-dark. The website will generate light and dark variants, but users can select the main colours (primary, secondary, and accent). There will also be a light and dark colour, and grey 100 through 900, generated by the code from user input of minimum darkness, maximum lightness, and colour temperature parameters. All colour variables will be stored in hex format, and there will be three-integer versions in RGB format. There will be a body, header, and jumbo font variable for font variables, where the jumbo font defaults to the header font unless specified otherwise by the user. There will also be sans-serif and serif font variables to define the other variables, as each font will have a "backup" font if it cannot be imported. An example of the variable declaration would look like this:
  ```--colors-primary-light: #58a1ee;
  --colors-primary: #1c7fe9;
  --colors-primary-dark: #1263ba;
  --colors-secondary-light: #dd51e1;
  --colors-secondary: #a91dae;
  --colors-secondary-dark: #88188c;
  --colors-accent-light: #6acbf1;
  --colors-accent: #27b3eb;
  --colors-accent-dark: #118bbb;
  --colors-light: #f8f9fa;
  --colors-dark: #121212;
  --colors-primary-light-rgb: 88, 161, 238;
  --colors-primary-rgb: 28, 127, 233;
  --colors-primary-dark-rgb: 18, 99, 186;
  --colors-secondary-light-rgb: 221, 81, 225;
  --colors-secondary-rgb: 169, 29, 174;
  --colors-secondary-dark-rgb: 136, 24, 140;
  --colors-accent-light-rgb: 106, 203, 241;
  --colors-accent-rgb: 39, 179, 235;
  --colors-accent-dark-rgb: 17, 139, 187;
  --colors-light-rgb: 248, 249, 250;
  --colors-dark-rgb: 18, 18, 18;
  --colors-grey-100: #dee2e6;
  --colors-grey-200: #ced4da;
  --colors-grey-300: #adb5bd;
  --colors-grey-400: #81888F;
  --colors-grey-500: #8d959d;
  --colors-grey-600: #495057;
  --colors-grey-700: #343a40;
  --colors-grey-800: #212529;
  --colors-grey-900: #1f1f1f;
  --font-sans-serif: "Helvetica", "Arial", sans-serif;
  --font-serif: serif;
  --font-body: "Roboto", var(--font-sans-serif);
  --font-header: "Lexend", var(--font-sans-serif);
  --font-jumbo: var(--font-header);
  ```

  The user's designs will be stored on the server, which can be recoverable and editable on any computer until the website is complete. The server will create regular backups of the site that can be recoverable in case the user wants to retrieve a previous version of the site. Users can download websites anytime in a structure that will allow them to host the website easily.

  The user could share the website with other users, giving them viewing permissions (if the website is private) and the ability to download and edit the site. The user could also transfer the site's ownership to someone else.

  To access the website builder, the URL functions like this: `/<username>/<sitename>/`, where the backend interprets the URL to send the correct information to the user to load the site. It will check for permissions for the user to send the appropriate site to them.
