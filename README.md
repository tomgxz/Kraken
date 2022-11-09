
## Analysis
### Problem identification
With the internet constantly growing, and more and more people relying on it, the demand for websites is constantly increasing - it is now expected for businesses to have their own webpage that people can easily access. They can range in style from business portfolios, to online stores, to games. However, a lot of people may find it difficult to create a website for themselves or their organisation, and the task of manually programming it can seem very daunting. The main aim of this project is to develop a website that allows clients to produce their own website via a simple user interface, which alleviates the technical intricacies of HTML, CSS and JavaScript. Clients will be able to select from a variety of styles and themes - or create their own - upload media such as images and videos, and then interact with a drag and drop interface to organise a webpage. Each website they create would have it’s own page dedicated to it, with options to customise the styles of the site, ability to create, organise, and link together pages of the website, preview the website in a variety of display sizes, and of course add pre-made elements and edit the parameters of the elements in the site. The requirements for a client to be able to use it would also be low, due to the entire application being contained within its own website, meaning that the client would only need a web browser and internet connection. This means the client doesn't need to install software onto their computer, nor do they need to worry about software updates.
#### Stakeholders
The clients for this software would be businesses or individuals who require a website but do not have the technical competency or time to build one themselves.

| Stakeholder | Role |Interaction |
|--|--|--|
| | | |
| | | |

<img alt="404 no stakeholders" src="https://lh5.googleusercontent.com/4uvZ_jq6raFf03ail16FfgqLPm9JP5gdU8V-y3wZAfbUpKUVSNls_AyQkpSCeZ10CrUPHeXBtRubFjCSOWe2scR_DFF6y7YcZc2VesnJbeRY-9vynC5GyrSNOOH4g_Px8H1jbhP-i_bE8n_1Z6K6Rg"/>

#### Why it is suited to a computational approach
This problem lends itself to a computational approach due to the fact that websites are inherently computational. The solution will be run from a server that hosts a website, meaning it will need a computer to use. There is no alternative that would not require a computer to be able to create a website, as at one point you will need to write and host the code that you have produced. This program would simply act as a bridge between the client and the code.

#### Computational methods that the solution lends itself to:
##### Problem recognition
##### Problem decomposition
The problem can be broken down into smaller tasks that need to be run for the program can be used effectively.
- Creating an account system, and a database to store the user's data.
> The account system would allow for many different users to access the server and edit their sites. The data would be stored in a server-side SQL database. The sites would be stored separately on the server.
- Creating a menu system for the user to navigate so that they can access different sites.

- Storing a list of template elements that the user can preview and use in their site.
> I would need to decide on how to store the template elements, how to display them to the user, and then how to implement them into a user's site whilst still allowing them to edit them.
- Creating a simple drag and drop interface that is easy to use and understand.
> This would probably be based off of the grid based positioning system that many existing website builders use, or the constraint system that applications such as android studio use, however that may not work with how HTML is created.
- Creating an effective way of storing the users' sites on the server.
> They would either be stored in HTM, CSS, and JS files, which would remove the need to convert them, or they could be stored all in XML files, which would make accessing the files easier: the program could convert the XML elements into HTML, CSS, and JS to allow it to be showed. This would allow for the storage of more information about the site and elements, and would mean it could all be in one file, including all the separate pages. The
- Converting the user's site into runnable HTML, CSS and JavaScript, so that they can download and use it.
> There would need to be a way for JS to do it so that the user can edit the site in the editor, and a way for the server (written in python) to do it as well
##### Divide and conquer
These smaller steps are all doable on their own, and combining them together mould make a divide and conquer approach. The advantage of it being coded in a modular way such as this is that each part can be tested and built on its own, without relying on other parts of the project.
##### Abstraction
The program uses abstraction as it removes the complex process of having to program code by transferring it into a more simple, graphical interface. This removes the need of the client to have knowledge and experience in programming and therefore opening the market to a much larger audience.

### Research
#### Existing solution - Squarespace
In their template list, they also give the option to preview the website, with all of its functionality in a separate page. They allow you to view it in different sizes as well.

<img alt="research-squarespace-4" src="https://lh6.googleusercontent.com/LHJzOfj9A_6wXIMYhHQR0DkdHhVzN4nSDL6LTghu3nUUsvGNFrW--MyvAcaikYt_5rVs_cMYNWHJ6I8Au0KfoqsN03BZ6rbcl7s9dDOFqjbBpaqkUF6Zqjv-YK_bccaihznPTZ7nNlTjejYNybUOsvKTckaHC1ipN8H03MCTuP2AJgFwb5cke2ml" height="360"/>
<img alt="research-squarespace-5" src="https://lh6.googleusercontent.com/4deX5c1Ep9XPrPXPD_VwahIqANJZ4BD7kuAuv3wPYCLB2m5Ee7c7b0mkCNz9FNKT66LvE56sxLwrm_b6HCLGB8u3Yni_M6SI2xy8HPriRcbq_xW9M3tnVyWpKOXtkn3gDyMknPDyG6-5GzNZeP7PHA" height="360"/>

When first starting to edit the site, squarespace offer an assistant with some basic first steps to creating the website, which makes it easier for the client to be able to understand how the editor works and how to effectively use it.

<img alt="research-squarespace-6" src="https://lh4.googleusercontent.com/PGXuevk3IgcYNprwAzUvwxBSuKW7wBpZxZWfwz2s6TCFkmfOMv3V9t6G01B9OVCgWLkHZftd1DWNEvi6syy9tMG2fZxdtFm3Fz_-TC3A0InOLuP-Vz3ndGdkC0KTpGelubJ9nLROLv1lnTGYNzLwfA" height="360"/>

Their design options include the styles, browser icon, 404 page, and custom css options. They can change the fonts, color scheme, global animations, spacing, and default styles for certain widgets.

<img alt="research-squarespace-7" src="https://lh5.googleusercontent.com/zgryJycyYJV2YPL6xErutkA_QbplHhED2QA9wS0z0ROEfVD4BassWMh4O0iE_BU6z_EmHfYba6SbrYZwMmV6jR9rM7FznuKJC6etSVPp5u68bRMq7czWlCk2caYi_uG7utvAdtVvoHqCxv1WBVH73g" height="360"/>
<img alt="research-squarespace-8" src="https://lh5.googleusercontent.com/K8GbumvM658mweDK5wKAUe1wtP9WxKkPHQAHCNxvpUJK2LtwrOwQGXr9X3VZrqzTRggiK6ID5ffxYYwHjmKVpqqHsHgrwDtG217NxGFSeOa2ExQy_PHBkkTAoKBwgwoJ__phgCoNg7bteLyIneFXMf8" height="360"/>

Their editor works in the conventional way of a grid based system, where you can place elements anywhere on the grid. It will then assign the item the style property ```grid-area:row-start/col-start/row-end/col-end```, or ```grid-area:y/x/height/width``` to define the position of the element. They have different attributes for different screen sizes, and you can edit both different styles by switching between laptop mode and phone mode.

<img alt="research-squarespace-9" src="https://lh6.googleusercontent.com/YApgdzdXYzdDGzf9MwE5GFovaajl1mqd1RPN0PC4xRLXweQ58AwLSMzB4Vf4RoBVdz3UaRN8PHxfqbsk96rbsd5QTrqh2FSrpq7bs2d67vWcjLZ6uo3wwSFYn80a2fN9A4VdYpR6ZU6fGGmOoHizFoxS2zYPM1h8R9Cs-bEdKkDQHNbxs00rvamDvg" width="640"/>
<img alt="research-squarespace-10" src="https://lh3.googleusercontent.com/jSX67py4IMFc6OQrQ6o5oTeOg-l6vrrfNL8CYyeM_JgzzVRGf86uoSX_a8g5U90kRLg4VyRDx_AetbDcTuT60m2Q31tvln44fwl410JQpoLY-9OT1hJCVh-EU1BwbuazbaQeeEftVV2Iu2HZHck8Fj3I-hywukOP0_PYtnQOtWbfMe7iDOdXCfuclA" height="360"/>

The website is split into sections, where each section contains a content wrapper with the grid positioning system inside.

<img alt="research-squarespace-11" src="https://lh3.googleusercontent.com/cf-XLNirmnX0qBJrjkLiNOIkbeyYlHB_KrMsb5ARvDERoAm9n7JEG2OcBxSLY9yNAD__O-ojjEVHdGXMFkzaFGX5Yn5qnyN8ty6HYBsHOuJXbZ7JrvRPEHIvhiOW-BMl1ngIeaFt8cJkFqSr9zoxxVMD6VmCUGmzN2u93t84la5xtAWt107xYE4tdQ" width="640"/>
<img alt="research-squarespace-12" src="https://lh4.googleusercontent.com/1AEcECEM1wk74DGWqVbg5gmNWo_Dt2RfCAWYsGhKZrwxzH1uH6j7kR3x_Zo7ASvQawiR1Iw9MG_lzPZVkke-GJq2te6OyAxomxVFsiiAma-2W-uHxXKQF3b9-J4ML6w8xncG2v4lJGFm7virRDFAithmPBkVn6Xv2SVDhrND8agB4ihh2a9G6d-ahg" width="640"/>
<img alt="research-squarespace-13" src="https://lh3.googleusercontent.com/BS4wFAn7mCikSTD8ObNh9PF6J_AMIjUTvY3ceB3vDF8MQoZSuA6_YlixNiLTPSOGyv7b_A3piKPOyKAzAQTA9FCY50FnmBN-HtzlPzGU_I92nVELGq2Y0lY54XFQfyYfUMx5Z04CB8Z4VHMLbDL7zWVCNr7TJdiRsic17qC_X9emTCwltI2z85D7zg" width="640"/>

By selecting text, you get a popup that displays the text formatting options. Whenever you click on an element, you get a different popup that displays the design options for said element

<img alt="research-squarespace-14" src="https://lh3.googleusercontent.com/ev5HPHTQPOsLEgQW5NfRt-sSZQ3uM5pD8cclTsFAjOaMfMQ88n5OF7gRm1mlKnAeD0mhCTwekKXL5DZtyhSas_GvTOG6Qr0DF5indKilMvJLXv9cLgwE6OoBgGlc98sFSU6s6FBTN1o8-sG7-MCU4RjDfMPPOTsduPwuthf8CDzyK4m8eVGCBv22ww" width="640"/>

##### Parts I can apply to my project

My solution will have the option to preview and use templates in a similar way to how Squarespace does it, along with their grid positioning system, which is, for lack of a better phrase, an "industry standard." There will also be a similar formatting option setup, but in will be docked on the right hand side with all of the formatting in the same place.

#### Existing solution - Zyro

Zyro also use an assistant to help the user understand how to use their editor.

<img alt="research-zyro" src="https://lh5.googleusercontent.com/S0OwKYuCciTU8C4I51QQcsDQDKe0lVabMJD2n2Ui7IJzArSoj75-j-ZtjMi5lKPgAa_ceJ1--ye1Om8so6_IYAgfZ2oq_6Zs-zfHoRfAZhuPEK3wXVCIsji2G2cGuqRz_OSxcu55Tr83_jyC1DQY9bRkCbfJV_4G33Xs0neRtib_E04YPDhpai7njA" height="360"/>
<img alt="research-zyro" src="https://lh5.googleusercontent.com/-vItU2Wcqt5wXqsJEOwun3I3FV0-nxIds5YcUWCuSZN2REVyfxGe3NZNopRUWhJjEHlcxUue96C5FlAbcNEihc7g-DCIHwGQown7olWi_zahY2EQhneDWTx4pHqdQKYaEb-0A6ShPD5hGGcI_NJqSu_muxIHVWFRFSkwXderRlTN_20GuyGywRl6Cw" height="360"/>

Zyro have two ways of positioning objects; one of them is very similar to the way squarespace do it, with a grid positioning system, and the second is something they call smart layout. It instead uses only columns to position, and the elements can be moved up and down said columns freely and snap to other elements, like how many editors like photoshop might do. You can toggle the snapping to other elements in section settings

<img alt="research-zyro" src="https://lh4.googleusercontent.com/ROxnCPT2jj-6Ug5JvXI-CjaNcU21iZ-ft--M3lo6c8iyZbGZpk2sBSNMGZpBN4sAxQo_TfPFDJc4YzYx-F4QewOFqq61-AnULblX94yGQ3yqZ2xwpa8y5jP1Y9femHEL9n8Ox5RBEXVNPMGhkJO4wGYbcv84Havc06gtyiU9ykedwRAYczvrEmLDRA" width="360"/>
<img alt="research-zyro" src="https://lh6.googleusercontent.com/KE2qzng016t_fXdGx-TeMWaTWYkE1SNRNm9GMjwa30nXhYXy0tUrWUKZrI9gbWiXGy_hjjPQLYh34hTtaOWSYsVwVXLUcwpBvfFHoVCcG5RVlTExMD3OIOarKeUS3DYsMqVhF6_OB9ioO5oxE7AsGWWrZTIKSXQewR6pHnVqzwvvQEjczZJ9T8DrfQ" width="360"/>
<img alt="research-zyro" src="https://lh6.googleusercontent.com/EtcJ4lja464xzMvE0qx-Gnen8zCXwMXhun60PIY0cMn-QKRUUnifacAO9sToMfSbCCcBpG0b58kTIk2_ChLJ8ylblGG7L6bcz4Xtgyk3GsTyV18ALhk-dvfoLGq1a18ifQ8ZWQSKwiE6ae6PIHrLHeZN_Eq6H0Z--uNyhJXTz3HZAS8iIBmfPMhzOg" width="360"/>

Their image resizing system is nice. It makes use of the ```object-fit:cover``` property in the style of the image, and just changing the width and height attributes when being dragged, as explained later

<img alt="research-zyro" src="https://lh6.googleusercontent.com/T50XFpiRq5sBvajAxl3lIYad4kgz2ykblrH28UB3hlxRzfY3Lr3nrveA305zbsylf9KfyLiPX8Y4APmACEa_vwZ4E675ED68PELTRgvtjbyKOZGLM0eSdCVhFQE6mT32bbXjZS_vTWArv4gJ9DzfVrNncZ6Ej1IUZhLAX64QaPnZaMDV0zat8lvRIg" width="360"/>

Something else zyro does is have all of their style attributes defined in one class, which rely on variables such as ```--grid-row```,```--m-grid-column```, and```--element-width``` that are defined in element.style (the style attribute of the HTML object), which have presumably been put their by JavaScript.

This is the CSS class with all of the variable references:

<img alt="research-zyro" src="https://lh4.googleusercontent.com/X7rGrjfPJxcZP9GrmGuyIrjOCsNrGFrjrJ-bqzdhgxXNLK1IY_hHV5tq-4bZROZ9uYr8CnvydM7Jk9AK37JJE_y04qEdm7vUvjNNnu_fI1QgpICINXxVlW5Uu47Kfktirshq8xm4xWBw4QzyBKZ6WMJN4fu8d0w8j-Lq7HXG3tU5CY2L6EriMYUA7A" width="360"/>

This is the HTML style attribute with all of the variable declarations in it:

<img alt="research-zyro" src="https://lh4.googleusercontent.com/3Bd9HaJjJ0osuEaZOOc0gaV47AllPCGZHU4wpQvH0andtH39rO4_LA3gDPntgIr82QiwKJam0IMXaBSeoHtCeAT8NSRd2S2cTTLVNdXEEBMcBTnkKp8iIGORGxufhbw84cPq60wZNiPv7Vaz89EYkecq22EaQlUEiuVvBcPlAyDuye98B37gKNwA2w" width="360"/>

When moving elements around the layout, Zyro adds four variables to the element, top, left, width, and height, which they use to render the positioning of the element while you are moving it. When you release the element, these values are removed. This positioning would probably be done in JavaScript by taking the position of the cursor when you clicked on the element, getting the position of the element when you click on it, and then offsetting the position of the element by the amount you remove the cursor. Then, when you release the cursor, it runs the code to calculate the new grid positioning of the element. They also have a max width for desktop, where the element cannot be moved further.

<img alt="research-zyro" src="https://lh4.googleusercontent.com/JhjuJvoNGNdeNjPF7M_VITx7KkcEB8yq_rKxjZ1yhtXaB3op08v4jYC9Vy8hfPBqZguR808YCAWWBDYlV4elGNSxsVs6zKfe_xtwyyTjJlPq8TPmZVoLsaO9PY1LomnxTBBoPXq_tLBRtkBQMCaXh_WDviL6wIgCSIPUcGnQY271jdRG_-5IJtmKNw" width="640"/>

### Features
To assemble the web pages, the clients will be able to drag and drop pre-designed elements categorised in groups such as headlines, quotes, forms, footers and more. The elements can be previewed in a sidebar next to the main canvas of the page, displayed with the correct styles of the website, from which they can be placed on the webpage. The website itself would be divided into sections, where you can drag and drop whole sections into the page or add individual elements into an existing section, such as text elements or images. After placing the elements into the canvas, the client can select the element to be able to interact with them, by moving them around, changing their styling (such as padding, size, coloring, transparency, position, font size, and many more) in a panel called the inspector panel, adding children to the element, or writing custom element-specific HTML, CSS, or JavaScript code that can be translated into the preview in real time. These custom elements / pieces of code will then be saved in the clients account, so that they can be used in other projects and/or published so that other clients can use them. The canvas will highlight elements with a border when they are hovered over, so that the client can easily see what the different elements are and how they can interact with them. The overall aim of the editor is for someone with very minimal knowledge, even none at all, about web design or programming to be able to interact with it, hence the WYSIWYG intuitiveness.

The canvas would have options at the top to be able to preview at certain conventional dimensions (375px for phones, 768px for tablets, etc) or at custom widths. This is so that the client can view how the elements interact with each other at custom resolutions. The elements, in the inspector panel, will also have options to change parameters at different screen resolutions (in the functionality of `@media screen and (max-width: 375px)`). There will also be an option to preview the site in its full functionality, where you can view all or the page without the extra clutter of the canvas and side panels.

The styling of the website will be able to be edited in a side panel, where the color scheme, element preferences and font face can be changed. There will be custom pre-selected pairings of colors and of fonts, but the user would also be able to use their own fonts, given they could provide a google fonts link or an otf/ttf file. The colors would be able to be changed using a color pricer and certain sliders. The website code itself (when rendering the colors) will reference variables defined at the top of the code, in the format --colors-<name>-[light|dark]-[rgb], such as --colors-secondary-dark. The light and dark variants will be generated by the website, but the main colors (primary, secondary, and accent) can be selected by the client. There will also be a light and dark color, and grey 100 through 900, generated by the code from user input of parameters of minimum darkness, maximum lightness and color temperature. All color variables will be stored in hex format, and there will be three-integer versions in rgb format. For font variables, there will be a body, header and jumbo font variable, where the jumbo font defaults to the header font unless specified otherwise by the client. There will also be a sans-serif and a serif font variables for use in defining the other variables, as each font will have a “backup” font if it cannot be imported. An example of the variable declaration would look like this:
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

The clients designs will be stored on the server which can be recoverable and editable on any computer until the website is complete. The server will create regular backups of the site that can be recoverable in case the client wants to retrieve a previous version of the site. Websites can be downloadable by the client at any time in a structure that will allow them to host the website easily.

The client would be able to share the website to other clients, giving them viewing permissions (if the website is private), the ability to download the site, and potentially be able to edit the site. The client would also be able to transfer the ownership of the site to someone else.

To access the website builder, the url functions like this: `/u/<User>/<Site>/[]`, where the backend interprets the url to send the correct information to the client as to be able to load the site. It will check for permissions for the client to send the appropriate site to them.
