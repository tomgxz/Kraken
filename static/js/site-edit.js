/* --------------- CODE FROM OTHER SOURCES --------------- */
// #region

// source https://stackoverflow.com/questions/14766951/transform-numbers-to-words-in-lakh-crore-system Juan Gaitan

var num = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ");
var tens = "twenty thirty forty fifty sixty seventy eighty ninety".split(" ");

function number2words(n){
    if (n < 20) return num[n];
    var digit = n%10;
    if (n < 100) return tens[~~(n/10)-2] + (digit? "-" + num[digit]: "");
    if (n < 1000) return num[~~(n/100)] +" hundred" + (n%100 == 0? "": " and " + number2words(n%100));
    return number2words(~~(n/1000)) + " thousand" + (n%1000 != 0? " " + number2words(n%1000): "");
}

// source https://www.codegrepper.com/profile/code-grepper

function capitalizeWords(string) { return string.replace(/(?:^|\s)\S/g, function(a) { return a.toUpperCase() }) };

// source https://www.grepper.com/answers/17868/javascript+sleep

const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

// endsource

// #endregion

/* --------------- VARIABLES AND CONSTANTS --------------- */
// #region

var builder = document.getElementById("contains_site")
var saveSiteBtn = document.getElementById("localnav_save")
var currentsitename = "Home"

// add section modal variables

var addSectionBtn = document.getElementById("localnav_add_section_btn");
var addSectionModal_selectedNavItem="one";
var addSectionModal_selectedNavItemInt=1;
var addSectionModal_container=document.querySelector(".application-content .section-selector-container");
var addSectionModal_list=document.getElementById("section_selector_list");
var addSectionModal_styleElement=document.getElementById("section_selector_style")
var addSectionModal_nav=document.getElementById("section_selector_nav");
var addSectionModal_navItem=`<li class="section-selector-nav-item [i]"><a class="link unformatted" id="section_selector_nav_[n1]"><span class="text bold">[n2]</span></a></li>`;
var addSectionModal_data = {}
var addSectionModal_headers = []

var addSectionModal_getAllTemplates = function() { return addSectionModal_list.childNodes }

// section edit actions

var sectionEditActions = document.querySelector(".section-edit-actions")

// abstract variables

var user
var site
var siteinfo
var currentpage
var selectedSection
var selectedElement

// query prefixes

queryprefix_sitecontainer = "#contains_site"

queryprefix_notlocked = `:not([data-kraken-locked])`
queryprefix_locked = `[data-kraken-locked]`

queryprefix_section = `${queryprefix_sitecontainer} [data-kraken-section]:not([data-preview])`
queryprefix_sectionselected = `${queryprefix_section}[data-kraken-section-selected]`

queryprefix_element = `${queryprefix_section} [data-kraken-element]`
queryprefix_elementselected = `${queryprefix_element}[data-kraken-element-selected]`
queryprefix_elementresizable = `${queryprefix_element}${queryprefix_notlocked}[data-kraken-resizable]`
queryprefix_elementdraggable = `${queryprefix_element}${queryprefix_notlocked}[data-kraken-draggable]`

// #endregion

/* ------------------- QUERY FUNCTIONS ------------------- */
// #region

function siteroot() { return document.querySelector("[data-content-parentview]")}
function resizable() { return document.querySelectorAll(queryprefix_elementresizable) } 
function draggable() { return document.querySelectorAll(queryprefix_elementdraggable) }
function sections() { return document.querySelectorAll(queryprefix_section) }
function elements() { return document.querySelectorAll(queryprefix_element) }

// #endregion

/* ------------ ADDING ELEMENTS AND LISTENERS ------------ */
// #region

// appends a section to the end of the editor
function addSection(html) {

    try {siteroot().insertAdjacentHTML("beforeend",html)}
    catch {siteroot().innerHTML += html}

    sectionEventListeners()
    elementEventListeners()

    createResizeBoxes()
}

// adds an element :/
function addElement(parent,name,src,css,js,type,order) {
    // (int) parent refers to the id of the element that contains this one. If set to none, the code assumes it is in the top level (ie it is a section div).
    // (str) name is used to refer to this element in the gui. It does not have to be unique
    // (str) src refers to the html code of this element, in the form of a url starting in /static/data/
    // (str) css refers to the css code of this element, in the form of a url starting in /static/data/
    // (str) js refers to the js code of this element, in the form of a url starting in /static/data/
    // (str) type refers to the class of element that this is (eg section, headline, table, quote, image)
    // (int) order is an integer defining how far down in the parent element this element is. Used in conjunction with the other children elements in the parent. If two have the same order, it will then refer to their element id. 0 will mean it is at the top.

    return

    var toplevel=false;
    if (parent == null) { toplevel=true }
    else { if (parent >= siteDat.length) { console.log("Parent ID larger than list of elements");return false; } }

    var id=0;
    if (siteDat.length > 0) { siteDat[siteDat.length-1]["id"]+1;  }

    siteDat.add(
      {
        "name":name,
        "locked":false,
        "src":src,
        "css":css,
        "js":js,
        "type":type,
        "parent":parent,
        "id":id,
        "toplevel":toplevel,
        "order":order,
      }

    )
}

// onclick function for section event listeners
function sectionOnClick(e) {
    var x = e.currentTarget
    //while (!(x.hasAttribute("data-kraken-section"))) x = x.parentElement

    clearSelectedSections()
    x.setAttribute("data-kraken-section-selected","")
    sectionEditActions.classList.add("shown")

    sectionEditActions.style.top = `${x.getBoundingClientRect().top-siteroot().getBoundingClientRect().top}px`

    if (x.hasAttribute("data-kraken-locked")) sectionEditActions_setlock_locked()
    else sectionEditActions_setlock_unlocked()

    selectedSection=x;
}

// onclick function for element event listener
function elementOnClick(e) {
    clearSelectedElements()
    
    setSelectedElement(e.currentTarget)
    createResizeCornerEventListeners()

    createDragEventListeners()
}

// creates the event listeners for all the sections
function sectionEventListeners() {
    clearSelectedSections()

    for (var section of sections()) {
        section.removeEventListener("click",sectionOnClick)
        section.addEventListener("click",sectionOnClick)

        //section.querySelector(".resize-handle").addEventListener("mousedown",e=>{console.log("hi")})
    }
}

// creates the event listeners for every element
function elementEventListeners() {
    clearSelectedElements()
    
    for (var element of elements()) {
        element.removeEventListener("click",elementOnClick)
        element.addEventListener("click",elementOnClick)
    }
}

// #endregion

/* ------------ SELECTED ELEMENTS AND SECTIONS ----------- */
// #region

// removes the data-kraken-section-selected tag from every section
function clearSelectedSections() {
    for (var section of sections()) section.removeAttribute("data-kraken-section-selected")
    sectionEditActions.classList.remove("shown")
}

// removes the data-kraken-element-selected tag from every element
function clearSelectedElements() {
    for (var element of elements()) element.removeAttribute("data-kraken-element-selected")
}

// #endregion

/* ------------------ ADD SECTION MODAL ------------------ */
// #region

// removes all sections from the add section modal
function addSectionModal_clearCurrentPreviews() {
    // remove each template section if it is not the style element
    addSectionModal_getAllTemplates().forEach((e)=>{ if (!(e == addSectionModal_styleElement)) e.remove() })
}

// populates the add section modal with templates based on a dictionary of data
function addSectionModal_populate(data) {
    addSectionModal_styleElement.innerHTML = data.css

    addSectionModal_clearCurrentPreviews()

    var i=1

    for (var section of data.sections) {
        //addSectionModal_list.innerHTML += section
        addSectionModal_list.insertAdjacentHTML("beforeend",section)
        var e = document.querySelector(".--headline.--type-"+i)

        e.parentElement.addEventListener("click",(e) => { 
            addSection(stripPreviewTags(e.currentTarget.outerHTML))
            addSectionModal_hide() 
        })

        i++
    }
}

// add a title to the local add section modal navigation bar
function addSectionModal_setNavbar(text) {
    // format the string based on the content of the string
    out=addSectionModal_navItem
        .replace("[i]",number2words(1)) // TODO work out the correct number
        .replace("[n1]",text.replace(" ",""))
        .replace("[n2]",capitalizeWords(text))

    // append to the local navbar
    addSectionModal_nav.querySelector("ul.section-selector-nav-list").innerHTML+=out;
}

// displays the add section modal
function addSectionModal_show() {
    addSectionModal_container.classList.add("shown");
    document.querySelector(".lightbox-mask").classList.add("shown")
}

// hides the add section modal
function addSectionModal_hide() {
    document.querySelector(".application-content .section-selector-container").classList.remove("shown")
    document.querySelector(".lightbox-mask").classList.remove("shown")

    addSectionModal_clearCurrentPreviews()
}

// loads all section templates from the /static/html/ directory and stores them to the dictionary addSectionModal_data, 
// along with the types of templates being stored in the list addSectionModal_headers
// The function is asynced to allow the use of await functions to fetch the content of the file
async function addSectionModal_loadsections() {

    // load the classes file, which contains all of the template types, and store them in the headers list
    await fetch("../../../static/html/sections/classes")
        // throw an error if there is an issue with the response
        .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
        .then( text => {
            for (line of text.split("\n")) {
                addSectionModal_setNavbar(line)
                addSectionModal_headers.push(line)
            }
        })

    var path
    var files

    // iterate through all the section types
    for (var header of addSectionModal_headers) {

        // add the section type to the data
        addSectionModal_data[header] = {css:"",sections:[]}
      
        // set the root URL for the section type
        path=`../../../static/html/sections/${header}`

        // fetch the custom CSS file for this type of headers
        await fetch(path+"/css.css")
            // throw an error if there is an issue with the response
            .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
            // add to the data dictionary
            .then( text => addSectionModal_data[header].css=text )

        // fetch the file list
        await fetch(path+"/files")
            // throw an error if there is an issue with the response
            .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
            // split the file into lines and filter out any empty lines
            .then( text => files=text.split(/[\r\n]+/g).filter(function(value, index, arr){ return value != "" }) )

        // iterate through all given files
        for (var file of files) {

            // fetch the template HTML
            await fetch(path+"/"+file)
                // throw an error if there is an issue with the response
                .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })      
                // add the template to the sections list
                .then( text => addSectionModal_data[header].sections.push(text))

        }

    }
}

// removes all data-preview tags from a string
function stripPreviewTags(html) {
    return html.replaceAll("data-preview"," ")
}

// event listener for the add section button, uses addSectionModal_show &
addSectionBtn.addEventListener("click",() => {
    // if the add section modal is not already shown
    if (!(addSectionModal_container.classList.contains("shown"))) {
        addSectionModal_show()

        addSectionModal_selectedNavItem="one";
        addSectionModal_selectedNavItemInt=1;

        addSectionModal_nav.querySelector(`ul.section-selector-nav-list li a.link`).style.opacity=0.75;
        addSectionModal_nav.querySelector(`ul.section-selector-nav-list li.${addSectionModal_selectedNavItem} a.link`).style.opacity=1;
        
        addSectionModal_clearCurrentPreviews()
        addSectionModal_populate(addSectionModal_data[addSectionModal_headers[addSectionModal_selectedNavItemInt-1]])

    }
});

// event listener for the close x in the add section modal
document.querySelector(".application-content .section-selector-exit-btn").addEventListener("click",addSectionModal_hide);

// event listener for the dark backround of the modals
document.querySelector(".lightbox-mask").addEventListener("click",addSectionModal_hide);

// #endregion

/* ---------------- SECTION EDIT ACTIONS ----------------- */
// #region

// set the locked icon in the lock button
function sectionEditActions_setlock_locked() {
    document.querySelector("#section_edit_action_lock i").classList.add("fa-unlock")
}

// set the unlocked icon in the lock button
function sectionEditActions_setlock_unlocked() {
    document.querySelector("#section_edit_action_lock i").classList.remove("fa-unlock")
}

// check whether there is a section selected - if not, hide the actions
function sectionEditActions_checkVisibility() {
    try {
        if (!(document.querySelectorAll("[data-kraken-section-selected]").length > 0)) { 
            sectionEditActions.classList.remove("shown")
        }
    } catch (e) {
        sectionEditActions.classList.remove("shown")
    }
}

// section action event listeners
document.getElementById("section_edit_action_settings").addEventListener("click",e=>{ console.log("settings") })
document.getElementById("section_edit_action_duplicate").addEventListener("click",e=>{ addSection(selectedSection.outerHTML) })
document.getElementById("section_edit_action_delete").addEventListener("click",e=>{ selectedSection.parentElement.removeChild(selectedSection) })

// lock event listener requires changing of the symbol depending on whether or not the section is locked
document.getElementById("section_edit_action_lock").addEventListener("click",e=>{
    console.log(selectedSection)
    if (selectedSection.hasAttribute("data-kraken-locked")) {
        selectedSection.removeAttribute("data-kraken-locked","") 
        sectionEditActions_setlock_unlocked()
    } else {
        selectedSection.setAttribute("data-kraken-locked","") 
        sectionEditActions_setlock_locked()
    }
})

// #endregion

/* --------- STARTING THE EDITOR AND LOADING HTML -------- */
// #region

// call on the page being loaded
// loads HTML from the server, starts all required event listeners, 
// creates any required resize boxes, and starts the autosave timer
async function run() {
    // get the username and sitename from the site url
    user = window.location.pathname.split("/")[1]
    site = window.location.pathname.split("/")[2]

    // get the siteinfo dictionary from the server
    siteinfo = await fetch(`../../../static/data/userData/${user}/sites/${site}/siteDat.json`).then(response => { return response.json(); })

    // get the current site page, defaults to "Home" if nothing is set
    currentpage = siteinfo["pages"][currentsitename]

    // load the current page
    await loadcurrentpage(user,site,currentpage)
    
    // create any required event listeners
    sectionEventListeners()
    elementEventListeners()

    // create any required resize boxes for elements and grid previews for sections
    createResizeBoxes()

    // start the autosave process
    saveTimeout()

    addSectionModal_loadsections()
    
    // event listener for the add section button, uses addSectionModal_show &
    saveSiteBtn.addEventListener("click",saveContent);
  
    // constant checks for stuff
    document.querySelector(".site-builder").addEventListener("click",() => {
        sectionEditActions_checkVisibility()
        createGridPreviews()
    })
}

// loads the current page into the editor from a set criteria
async function loadcurrentpage(user,site,currentpage) {
    return sethtml(await loadhtmlfile(`../../../static/data/userData/${user}/sites/${site}/files/${currentpage}`))
}

// loads a file from a path
async function loadhtmlfile(path) {
    return await fetch(path)
    .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
    .then( text => { return text })
}

// sets the content of the editor
function sethtml(html) {
    builder.innerHTML=html;
}

// #endregion

/* ----------------- SAVING USER CONTENT ----------------- */
// #region

// await function used to ensure that multiple saves are not occuring at the same time
async function waitForNotSaving() {
    while (document.querySelector(".localnav.one .localnav-item.four").hasAttribute("data-kraken-savestate")) { await sleep(100) }
    return true
}

// sends a request to the server to save the content of the editor to the server file storage
async function saveContent() {
    // remove all existing timeouts to reduce conflicts
    clearTimeout(saveContent)

    // wait for the current save to finish, if running
    await waitForNotSaving()

    console.log("Saving...")

    // start the save animation
    showSaveLoader()

    //$.post(`../../../${window.location.pathname.split("/")[1]}/${window.location.pathname.split("/")[2]}/save/${siteinfo["pages"][currentsitename]}`, {
    //    data:siteroot().outerHTML // need to strip kraken tags
    //})

    req = $.ajax({
        type:"post",
        url:`../../../${window.location.pathname.split("/")[1]}/${window.location.pathname.split("/")[2]}/save/${siteinfo["pages"][currentsitename]}`,
        data:{content:siteroot().outerHTML},
        datatype:"json",
        error: function(xhr,ajaxOptions,thrownError) { hideSaveLoader(false) },
        success: function(response) { hideSaveLoader(true) },
    })

    // create the new timeout
    saveTimeout()
}

// starts the timeout for the saveContent function
function saveTimeout() {
    clearTimeout(saveContent) // clear any previous timeouts
    setTimeout(saveContent,60000) // run the savecontent function every minute
}

// starts the save loading animation
function showSaveLoader() {
    document.querySelector(".localnav.one .localnav-item.four").setAttribute("data-kraken-savestate","saving")
}

// finishes the save loading animation and shows a success/fail icon, then resets to normal
async function hideSaveLoader(success) {
    document.querySelector(".localnav.one .localnav-item.four").setAttribute("data-kraken-savestate",success?"success":"error")
    await sleep(1500)
    document.querySelector(".localnav.one .localnav-item.four").removeAttribute("data-kraken-savestate")
}

// #endregion

/* --------------------- RESIZE BOXES -------------------- */
// #region

// generates resize boxes for every resizable element
function createResizeBoxes() {
    var r = resizable() // get all resizable elements
    for (var element of r) {
        // remove the current resize box
        element.querySelectorAll(".element-resize-container").forEach((e) => {
            e.parentElement.removeChild(e)
        })
    
        // set the resize type based on the element tags
        type = "corners"
        if (element.hasAttribute("data-kraken-editable-text")) type = "horizontal"

        // create the resize box for resizable and draggable elements
        element.appendChild(createResizeBoxContainerElement(type,element,true))
    }

    // iterate through all draggable elements
    for (var element in draggable()) {
        // if the element is not resizable
        if (!(element in r)) {
            // create the resize box for non-resizable elements
            element.appendChild(createResizeBoxContainerElement("",element,false))
        }
    }
}

// returns a resize box container element with all required things inside
function createResizeBoxContainerElement(type,parent,corners) {
    // create the container element and add required classes
    container = document.createElement("div")
    container.classList.add("element-resize-container")

    if (corners) { // if it requires corners, append a corner container child
        if (type == "corners") container.appendChild(createResizeBoxFourCornersElement())
        if (type == "horizontal") container.appendChild(createResizeBoxHorizontalCornersElement())
    }

    // append an outline child
    container.appendChild(createResizeBoxEdgesElement(parent))

    return container
}

// returns the resize box edges element
function createResizeBoxEdgesElement(parent) {
    // create the outline element and add required classes
    outline = document.createElement("div")
    outline.classList.add("element-outline")

    // set the correct height
    outline.style.height=parent.querySelector("div").offsetHeight+"px"

    return outline
}

// returns an element containing four resize corners
function createResizeBoxFourCornersElement() {
    // create the container element and add required classes
    root = document.createElement("div")
    root.classList.add("resize-corners")

    // append each required corner to the element
    root.appendChild(createResizeBoxCornerElement("top-left"))
    root.appendChild(createResizeBoxCornerElement("top-right"))
    root.appendChild(createResizeBoxCornerElement("bottom-left"))
    root.appendChild(createResizeBoxCornerElement("bottom-right"))

    return root
}

// returns an element containing two horizontal resize corners
function createResizeBoxHorizontalCornersElement() {
    // create the container element and add required classes
    root = document.createElement("div")
    root.classList.add("resize-corners")

    // append each required corner to the element
    root.appendChild(createResizeBoxCornerElement("horizontal-left"))
    root.appendChild(createResizeBoxCornerElement("horizontal-right"))
    return root
}

// reurns a resize corner
function createResizeBoxCornerElement(loc) {
    // create the corner element and add required classes
    corner = document.createElement("div")
    corner.classList.add("resize-corner")
    corner.classList.add(`resize-corner-${loc}`)
    
    // create the visual elemet and add required classes
    trigger = document.createElement("div")
    trigger.classList.add("resize-corner-visual-element")

    // add the visual element as a child of the corner element
    corner.appendChild(trigger)

    return corner
}

// #endregion

/* ------------ DRAG AND DROP EVENT LISTENERS ------------ */
// #region

/*
function closestValInArray(num, arr) {
    var curr = arr[0];
    var diff = Math.abs (num - curr);
    for (var val = 0; val < arr.length; val++) {
        var newdiff = Math.abs (num - arr[val]);
        if (newdiff < diff) {
            diff = newdiff;
            curr = arr[val];
        }
    }
    return curr;
}
*/

function closestValInArray(num, arr) {
    prev = arr[0]
    for (val of arr) {
        if (val > num) return prev
        prev = val
    }
}

function closestValInArray(num, arr) {
    prev = arr[0]
    diff = Math.abs(num - prev)
    for (var val of arr) {
        var newdiff = Math.abs (num - val)
        if (newdiff < diff) {
            diff = newdiff
            prev = val
        }
    }
    return prev
}

// event listener function for element resizing
function elementResize(e2) {
    // get the corner that has been dragged
    current = e2.currentTarget

    // set the selected element and section to the parents of the corner

    parent = current.parentElement
    while (!(parent.hasAttribute("data-kraken-element"))) {
        parent = parent.parentElement
    }

    setSelectedElement(parent)

    while (!(parent.hasAttribute("data-kraken-section"))) {
        parent = parent.parentElement
    }

    setSelectedSection(parent)

    // get the current section's grid and current element
    currentsection = document.querySelector(queryprefix_sectionselected+" section .section-grid")
    currentelement = document.querySelector(queryprefix_elementselected)

    // get the computed styles of said elements and any required parameters
    currentsection_style = getComputedStyle(currentsection)
    currentelement_style = getComputedStyle(currentelement)
    currentsection_columngap = parseInt(currentsection_style.columnGap.replace("px",""))
    currentsection_gridtemplatecolumns = currentsection_style.gridTemplateColumns
    currentsection_startx = currentsection.getBoundingClientRect().left
    currentelement_position = currentelement_style.getPropertyValue("--position").split("/")

    columnlist = []
    cumulative = 0
    snappoints = []

    //console.log(currentelement)
    //console.log(currentsection)

    //console.log(currentsection_columngap)

    // get a list of the template columns as integers
    // eg [0,0,4,4,4,4,4,4,0,0]
    for (var col of currentsection_gridtemplatecolumns.split(" ")) 
        columnlist.push(parseInt(col.replace("px","")))

    // get the cumulative values of the column positions
    // eg [0,0,4,8,12,16,24,32,32,32] when the columngap is 0
    // this gets the offset from the start of the grid, in pixels, of every column
    for (var col of columnlist) {
        snappoints.push(cumulative)
        cumulative += col + currentsection_columngap
    }

    //console.log(snappoints)


    type = ""

    // get the type of resize based on the classes of the handle
    if (classlist.contains("resize-corner-top-left") | classlist.contains("resize-corner-top-right") | classlist.contains("resize-corner-bottom-left") | classlist.contains("resize-corner-bottom-right")) type="xy"
    if (classlist.contains("resize-corner-horizontal-left") | classlist.contains("resize-corner-horizontal-right")) type="x"

    // if its a horizontal resize
    if (type=="x") {
        
        //console.log("Old position variable: ",currentelement_position)

        // get the final x position (from the reference of the start of the viewport)
        endx = e2.clientX
        //console.log("End x position: ",endx)

        // get the final x position (from the reference of the start of the section grid)
        endxoffset = endx-currentsection_startx
        //console.log("End x offset from parent: ", endxoffset)
        //console.log("Column offsets: ", snappoints)

        // get the closest column to the final value
        closestsnappoint = closestValInArray(endxoffset,snappoints)
        //console.log("Closest column offset to end x offset: ", closestsnappoint)

        // get the index of the closest column, ie the column number - 1
        index = snappoints.indexOf(closestsnappoint)
        //console.log("Index of closest column: ", index)

        // set the column number for the position variable
        columnnumber = String(index+1)
        //console.log("Closest column number: ",columnnumber)

        // assign the new position based on the postoken
        currentelement_position[postoken] = columnnumber
        //console.log("New position variable: ",currentelement_position)

        // assign the new position property to the selected element
        currentelement.style.setProperty("--position",currentelement_position.join("/"))

    }
}

// event listener function for element drag-and-drop drop
function elementDrop(e2,endpos) {

    // get the dragged element
    current = e2.currentTarget 

    // get the current section, and any required style paramaters
    currentsection = document.querySelector("[data-kraken-section-selected] section .section-grid")
    currentsection_style = getComputedStyle(currentsection)
    currentsection_columngap = parseInt(currentsection_style.columnGap.replace("px",""))
    currentsection_rowgap = parseInt(currentsection_style.rowGap.replace("px",""))
    currentsection_gridtemplatecolumns = currentsection_style.gridTemplateColumns
    currentsection_gridtemplaterows = currentsection_style.gridTemplateRows
    currentsection_startx = currentsection.getBoundingClientRect().left
    currentsection_starty = currentsection.getBoundingClientRect().top

    // get the elemenets style and position values
    current_style = getComputedStyle(current)
    current_position = current_style.getPropertyValue("--position").split("/")

    //console.log("Position: ",current_position)

    columnlist = []
    cumulative = 0
    columnsnappoints = []

    // get a list of the template columns as integers
    for (var col of currentsection_gridtemplatecolumns.split(" ")) 
        columnlist.push(parseInt(col.replace("px","")))

    // get the cumulative values of the column positions
    // this gets the offset from the start of the grid, in pixels, of every column
    for (var col of columnlist) {
        columnsnappoints.push(cumulative)
        cumulative += col + currentsection_columngap
    }

    // repeat for rows

    rowlist = []
    cumulative = 0
    rowsnappoints = []

    // get a list of the template rows as integers
    for (var row of currentsection_gridtemplaterows.split(" ")) 
        rowlist.push(parseInt(row.replace("px","")))

    // get the cumulative values of the row positions
    // this gets the offset from the top of the grid, in pixels, of every row
    for (var row of rowlist) {
        rowsnappoints.push(cumulative)
        cumulative += row + currentsection_rowgap
    }

    //console.log("Col snap points: ",columnsnappoints)
    //console.log("Row snap points: ",rowsnappoints)

    // get the end x and y positions
    // (endpos is the bounding box of the element when it was dropped)
    endx = endpos.left
    endy = endpos.top

    // get the end x and y positions in relation to the section
    endxoffset = endx-currentsection_startx
    endyoffset = endy-currentsection_starty

    //console.log("End X Offset: ",endxoffset)
    //console.log("End Y Offset: ",endyoffset)

    // get the closest column/row offset point to the end offsets
    closestcolumnsnappoint = closestValInArray(endxoffset,columnsnappoints)
    closestrowsnappoint = closestValInArray(endyoffset,rowsnappoints)

    //console.log("Closest Col snap point ",closestcolumnsnappoint)
    //console.log("Closest Row snap point ",closestrowsnappoint)

    // get the numbers of the column/row 
    columnindex = columnsnappoints.indexOf(closestcolumnsnappoint)
    rowindex = rowsnappoints.indexOf(closestrowsnappoint)

    //console.log("Col index: ",columnindex)
    //console.log("Row index: ",rowindex)

    // set the column and row numbers
    columnnumber = String(columnindex+1)
    rownumber = String(rowindex+1)

    //console.log("Col number: ",columnnumber)
    //console.log("Row number: ",rownumber)

    //console.log("Position: ",current_position)

    // 0 = start row
    // 1 = start column
    // 2 = end row
    // 3 = end column

    // Set the new end positions based on the difference between the original and new position
    current_position[2] = String(parseInt(current_position[2]) + parseInt(rownumber) - parseInt(current_position[0]))
    current_position[3] = String(parseInt(current_position[3]) + parseInt(columnnumber) - parseInt(current_position[1]))

    // set the new start positions
    current_position[1] = columnnumber
    current_position[0] = rownumber

    console.log("Position: ",current_position)

    // set the --position style variable
    current.style.setProperty("--position",current_position.join("/"))

}

// creates event listeners for resize corners on currently selected elements
function createResizeCornerEventListeners() {
    // get all corners of every resizable element
    for (corner of document.querySelectorAll(queryprefix_elementresizable+" .element-resize-container .resize-corner")) {

        // make a copy of the corner - this removes any existing event listeners so that there are not multiple resize events being triggered
        newcorner = corner.cloneNode(true)
        corner.parentNode.replaceChild(newcorner,corner)

        corner=newcorner

        // mouse down event listener
        corner.addEventListener("mousedown",(e1) => {

            // get the clicked element
            current = e1.currentTarget 

            // get the parent section by iterating through every parent element
            parent = current.parentElement
            while (!(parent.hasAttribute("data-kraken-section"))) parent = parent.parentElement

            // render the grid preview element
            parent.querySelectorAll(".section-grid-preview").forEach((e)=>{
                e.setAttribute("data-kraken-visible","")
            })

            type = ""
            classlist = current.classList
            postoken = 0

            // work out whether it is a horizontal resize or a 2D resizes by looking at the classes of the elemenet
            if (classlist.contains("resize-corner-top-left") | classlist.contains("resize-corner-top-right") | classlist.contains("resize-corner-bottom-left") | classlist.contains("resize-corner-bottom-right")) type="xy"
            if (classlist.contains("resize-corner-horizontal-left") | classlist.contains("resize-corner-horizontal-right")) type="x"

            // postoken defines which corner is being dragged, and how the code should change the attributes based on that
            if (classlist.contains("resize-corner-horizontal-left")) postoken=1
            if (classlist.contains("resize-corner-horizontal-right")) postoken=3

            // get the start position of the mouse
            startpos = [e1.clientX,e1.clientY]

            // set the mouse move event listener
            current.addEventListener("mousemove",(e2) => {
                
                // get the clicked element
                current = e2.currentTarget

                // get the new position of the mouse
                newpos = [e2.clientX,e2.clientY]

                // get the full style of the current element
                current_style = getComputedStyle(current)

                // get the current transformation property by converting
                // matrix(a,b,c,d,e,f)
                // into
                // ["a","b","c","d","e","f"]
                current_transform = current_style.transform.replace("matrix(","").replace(")","").replaceAll(" ","").split(",")

                //console.log(e2.clientX,startpos[0],e2.clientX - startpos[0])

                // if it is a horizontal resize
                if (type=="x") {
                    // get the difference in position since the last render
                    diff = newpos[0] - startpos[0]
                    
                    // set the horizontal translation property of the matrix
                    current_transform[4] = String(parseInt(current_transform[4])+diff)

                    // set the new matrix as the transform property
                    current.style.transform = "matrix(" + current_transform.join(",") + ")"

                    // get the outline element of the resize box
                    outline = current.parentNode.parentNode.querySelector(".element-outline")
                    outline_style = getComputedStyle(outline)
                    outline_width = outline_style.width
                    outline_width = parseInt(outline_width.replace("px",""))

                    outline_left = outline_style.left
                    outline_left = parseInt(outline_left.replace("px",""))
                    
                    outline_right = outline_style.right
                    outline_right = parseInt(outline_right.replace("px",""))

                    // if the element is being resized from the left handle
                    if (postoken == 1) {
                        // set the style properties to reflect the transformation
                        outline.style.left = String(outline_left + diff) + "px"
                        outline.style.width = String(outline_width - diff) + "px"
                    }

                    // if the element is being resized from the right handle
                    if (postoken == 3) {
                        // set the style properties to reflect the transformation
                        outline.style.right = String(outline_right + diff) + "px"
                        outline.style.width = String(outline_width + diff) + "px"

                    }
                }

                // set the start position so that the next render resize works properly
                startpos = newpos

            })

            // set the mouse up event listener
            current.addEventListener("mouseup",(e2) => {
                
                // set the new properties for the element
                elementResize(e2)

                // get the parent section by iterating through every parent element
                parent = current.parentElement
                while (!(parent.hasAttribute("data-kraken-section"))) parent = parent.parentElement

                // hide the grid preview element
                parent.querySelectorAll(".section-grid-preview").forEach((e)=>{
                    e.removeAttribute("data-kraken-visible")
                })

                // recreate the resize boxes and event listeners to remove any visual errors and clear the mousemove and mouseup event listeners
                createResizeBoxes()
                createResizeCornerEventListeners()

            })
        })
    }
}

// creates event listeners for all draggable elements
function createDragEventListeners() {
    // get every draggable element
    for (element of draggable()) {

        // create the mouse down eevent listener
        element.addEventListener("mousedown",(e1) => {

            // end the listener if a resize corner is being clicked, because otherwise the drag and resize functions will be happening simultaneously
            if (e1.target.classList.contains("resize-corner") | e1.target.classList.contains("resize-corner-visual-element")) return

            // get the current element, set it as being dragged, and fetch the content
            current = e1.currentTarget
            current.setAttribute("data-kraken-dragging","")
            content = current.querySelector("div")

            // get the starting cursor position
            startpos = [e1.clientX,e1.clientY]

            // get the current --position value
            storedPosition = current.style.getPropertyValue("--position")

            // set the box shadow and background color for the element
            content.style.boxShadow = "0px 0px 8px 3px rgba(0,0,0,0.25"
            content.style.backgroundColor = "var(--colors-light)"

            // get the parent section by iterating through every parent element
            parent = current.parentElement
            while (!(parent.hasAttribute("data-kraken-section"))) parent = parent.parentElement

            // render the grid preview element
            parent.querySelectorAll(".section-grid-preview").forEach((e)=>{
                e.setAttribute("data-kraken-visible","")
            })

            // create the mouse move event listener
            current.addEventListener("mousemove",(e2) => {
                
                // get the selected element
                current = e2.currentTarget

                // store the new cursor position
                newpos = [e2.clientX,e2.clientY]

                // fetch the style of the selected element
                current_style = getComputedStyle(current)

                // get the differences in position
                xdiff = newpos[0] - startpos[0]
                ydiff = newpos[1] - startpos[1]

                // get the bounding boxes of the section and element
                sectionbox = selectedSection.getBoundingClientRect()
                currentbox = current.getBoundingClientRect()

                // get the element's width and height in pixels
                currentwidth = current.offsetWidth
                currentheight = current.offsetHeight

                // get the top and left positions relative to the section boundary
                relativetop = currentbox.top - sectionbox.top + ydiff
                relativeleft = currentbox.left - sectionbox.left + xdiff

                // set the element style so that it follows the cursor
                current.style.position = "absolute"
                current.style.setProperty("--position","")
                current.style.top = String(relativetop) + "px"
                current.style.left = String(relativeleft) + "px"
                current.style.width = String(currentwidth) + "px"
                current.style.height = String(currentheight) + "px"
                current.style.zIndex = "999999"

                // set the start position so that the next render works properly
                startpos = [e2.clientX,e2.clientY]

            })

            // set the mouse up event listener
            current.addEventListener("mouseup",(e2) => {

                // get the dragged element, remove the dragging tag, and get its content
                current = e2.currentTarget
                current.removeAttribute("data-kraken-dragging")
                content = current.querySelector("div")

                // get the dragged element's final position
                endpos = current.getBoundingClientRect()

                // reset the styling used in the dragging animation
                content.style.boxShadow = ""
                content.style.backgroundColor = ""

                current.style.removeProperty("position")
                current.style.removeProperty("top")
                current.style.removeProperty("left")
                current.style.removeProperty("width")
                current.style.removeProperty("height")
                current.style.removeProperty("z-index")

                // set the element position back to what it was while the new one is being calculated
                current.style.setProperty("--position",storedPosition)

                // calculate and set the new position property for the element
                elementDrop(e2,endpos)

                // get the parent section by iterating through every parent element
                parent = current.parentElement
                while (!(parent.hasAttribute("data-kraken-section"))) parent = parent.parentElement

                // hide the grid preview element
                parent.querySelectorAll(".section-grid-preview").forEach((e)=>{
                    e.removeAttribute("data-kraken-visible")
                })

                // duplicate the element to remove all used event listeners
                newcurrent = current.cloneNode(true)
                current.parentNode.replaceChild(newcurrent,current)
                current = newcurrent

                // recreate the element event listeners
                elementEventListeners()

            })
        })

    }
}

// #endregion

/* ------------ SELECTED ELEMENTS AND SECTIONS ----------- */
// #region

function setSelectedElement(element) {
    document.querySelectorAll("[data-kraken-element-selected]").forEach((e)=>{ e.removeAttribute("[data-kraken-element-selected]") })
    element.setAttribute("data-kraken-element-selected","")
}

function setSelectedSection(section) {
    document.querySelectorAll("[data-kraken-section-selected]").forEach((e)=>{ e.removeAttribute("[data-kraken-section-selected]") })
    section.setAttribute("data-kraken-section-selected","")
}

// #endregion

/* ------------------ GRID PREVIEW BOX ------------------- */
// #region

function createGridPreviews() {
    // for every section
    for (var section of document.querySelectorAll(queryprefix_section + " section")) {

        // remove any existing grid previews in the section
        for (var existing of section.querySelectorAll(".section-grid-preview")) {
            existing.parentNode.removeChild(existing)
        }

        // create the grid container element and add required classes
        container = document.createElement("div")
        container.classList.add("section-grid-preview")

        // get the style of the section grid and any required paramaters
        gridstyle = getComputedStyle(section.querySelector(".section-grid"))
        gridstyle_rows = gridstyle.gridTemplateRows.split(" ")
        gridstyle_columns = gridstyle.gridTemplateColumns.split(" ")
        gridstyle_rowgap = parseInt(gridstyle.rowGap.replace("px",""))
        gridstyle_columngap = parseInt(gridstyle.columnGap.replace("px",""))

        columnoffset = parseInt(gridstyle.getPropertyValue("--block-padding-left"))
        rowoffset = parseInt(gridstyle.getPropertyValue("--block-padding-top"))

        //console.log(gridstyle.gridTemplateColumns)

        // for every column in the grid
        for (var columnwidth of gridstyle_columns) {

            // set the rowoffset back to the starting value
            rowoffset = parseInt(gridstyle.getPropertyValue("--block-padding-top"))

            // for every row in the column
            for (var rowheight of gridstyle_rows) {
                //console.log(columnoffset,rowoffset)

                // add a child box with the correct positions
                container.appendChild(createGridPreviewBox(columnwidth,rowheight,rowoffset,columnoffset))

                //console.log(parseInt(rowheight.replace("px","")))

                // increase the row offset by the width of the row and the row gap
                rowoffset = rowoffset + parseInt(rowheight.replace("px","")) + gridstyle_rowgap
            }

            // increase the column offset by the width of the column and the column gap
            columnoffset = columnoffset + parseInt(columnwidth.replace("px","")) + gridstyle_columngap

        }

        // add the grid previeew
        section.appendChild(container)
    }
}

// creates a single box for the grid previews
function createGridPreviewBox(width,height,top,left) {
    // create the box element and add any required classes
    box = document.createElement("div")
    box.classList.add("section-grid-preview-box")

    // set the style to match the arguments
    box.style.width = width
    box.style.height = height
    box.style.top = top+"px"
    box.style.left = left+"px"

    // hide the box if one of the dimensions is 0
    if (width == "0px" || height == "0px") box.style.opacity = "0"

    return box
}

// #endregion

/* ------------------------- RUN ------------------------- */

run()