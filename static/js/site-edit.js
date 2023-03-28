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

// endsource

function addSection(html) {

    try {siteroot().insertAdjacentHTML("beforeend",html)}
    catch {siteroot().innerHTML += html}

    sectionEventListeners()
    elementEventListeners()

    createResizeBoxes()
}

function sectionEventListeners() {
    clearSelectedSections()

    for (var section of sections()) {
        section.addEventListener("click",((e)=>{

            var x = e.target.parentElement
            while (!(x.hasAttribute("data-kraken-section"))) x = x.parentElement

            clearSelectedSections()
            x.setAttribute("data-kraken-section-selected","")
            sectionEditActions.classList.add("shown")
            selectedSection=x;
        }))

        //section.querySelector(".resize-handle").addEventListener("mousedown",e=>{console.log("hi")})
    }
}

function elementEventListeners() {
    clearSelectedElements()
    
    for (var element of elements()) {
        element.addEventListener("click",((e)=>{

            clearSelectedElements()
            e.target.parentElement.setAttribute("data-kraken-element-selected","")
            selectedElement=e.target.parentElement
        }))
    }
}

function clearSelectedSections() {
    for (var section of sections()) section.removeAttribute("data-kraken-section-selected")
    sectionEditActions.classList.remove("shown")
}

function clearSelectedElements() {
    for (var element of elements()) element.removeAttribute("data-kraken-element-selected")
}

function addElement(parent,name,src,css,js,type,order) {
    // (int) parent refers to the id of the element that contains this one. If set to none, the code assumes it is in the top level (ie it is a section div).
    // (str) name is used to refer to this element in the gui. It does not have to be unique
    // (str) src refers to the html code of this element, in the form of a url starting in /static/data/
    // (str) css refers to the css code of this element, in the form of a url starting in /static/data/
    // (str) js refers to the js code of this element, in the form of a url starting in /static/data/
    // (str) type refers to the class of element that this is (eg section, headline, table, quote, image)
    // (int) order is an integer defining how far down in the parent element this element is. Used in conjunction with the other children elements in the parent. If two have the same order, it will then refer to their element id. 0 will mean it is at the top.

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

function addSectionModal_setNavbar(text) {
    text=text.split(/[\r\n]+/g);out="";
    for (var i=0; i<text.length; i++) {
        out=out+addSectionModal_navItem
          .replace("[i]",number2words(i+1).replace(" ",""))
          .replace("[n1]",text[i].replace(" ",""))
          .replace("[n2]",capitalizeWords(text[i]))
    }
    addSectionModal_nav.querySelector("ul.section-selector-nav-list").innerHTML=out;
}

var siteroot = function() { return document.querySelector("[data-content-parentview]")}
var builder = document.getElementById("contains_site");
var addSectionBtn = document.getElementById("localnav_add_section_btn");
var addSectionModal_selectedNavItem="one";
var addSectionModal_selectedNavItemInt=1;
var addSectionModal_container=document.querySelector(".application-content .section-selector-container");
var addSectionModal_list=document.getElementById("section_selector_list");
var addSectionModal_styleElement=document.getElementById("section_selector_style")
var addSectionModal_getAllTemplates = function() { return addSectionModal_list.childNodes }
var addSectionModal_nav=document.getElementById("section_selector_nav");
var addSectionModal_navItem=`<li class="section-selector-nav-item [i]"><a class="link unformatted" id="section_sele  ctor_nav_[n1]"><span class="text bold">[n2]</span></a></li>`;
var addSectionModal_data = {}
var addSectionModal_headers = []
var sectionEditActions = document.querySelector(".section-edit-actions")
var user;
var site;
var siteinfo;
var currentsitename="Home";
var currentpage;
var selectedSection;
var selectedElement;
var sections = function() {
    var x=[]
    siteroot().childNodes.forEach((e)=>{try { if (e.hasAttribute("data-kraken-section")) x.push(e) } catch (er) {return} })
    return x};
var elements = function() {
    return document.querySelectorAll("[data-kraken-element]")
};

function addSectionModal_show() {
    addSectionModal_container.classList.add("shown");
    document.querySelector(".lightbox-mask").classList.add("shown")
}

function addSectionModal_hide() {
    document.querySelector(".application-content .section-selector-container").classList.remove("shown")
    document.querySelector(".lightbox-mask").classList.remove("shown")
}

// event listener for the add section button
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

// section action event listeners
document.getElementById("section_edit_action_settings").addEventListener("click",e=>{ console.log("settings") })
document.getElementById("section_edit_action_duplicate").addEventListener("click",e=>{ addSection(selectedSection.outerHTML) })
document.getElementById("section_edit_action_lock").addEventListener("click",e=>{ selectedSection.setAttribute("data-kraken-locked","") })
document.getElementById("section_edit_action_delete").addEventListener("click",e=>{ selectedSection.remove() })

async function run() {
    user = window.location.pathname.split("/")[1]
    site = window.location.pathname.split("/")[2]
    siteinfo = await fetch(`../../../static/data/userData/${user}/sites/${site}/siteDat.json`).then(response => { return response.json(); })
    currentpage = siteinfo.pages[currentsitename]
    await loadcurrentpage()
}

async function loadcurrentpage() {
    return sethtml(await loadhtmlfile(`../../../static/data/userData/${user}/sites/${site}/files/${currentpage}`))
}

async function loadhtmlfile(path) {
    return await fetch(path)
    .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
    .then( text => { return text })
}

function sethtml(html) {
    builder.innerHTML=html;
}

async function loadsections() {

    await fetch("../../../static/html/sections/classes")
        .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
        .then( text => {addSectionModal_setNavbar(text),addSectionModal_headers.push(text)} )

    var path
    var files

    for (var header of addSectionModal_headers) {
        addSectionModal_data[header] = {css:"",sections:[]}
        path=`../../../static/html/sections/${header}`

        await fetch(path+"/css.css")
            .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
            .then( text => addSectionModal_data[header].css=text )

        await fetch(path+"/files")
            .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
            .then( text => files=text.split(/[\r\n]+/g).filter(function(value, index, arr){ return value != "" }) )

        for (var file of files) {

            await fetch(path+"/"+file)
                .then( response => { if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) } return response.text(); })
                .then( text => addSectionModal_data[header].sections.push(text))

        }

    }
}

function stripPreviewTags(html) {
    return html.replaceAll("data-preview"," ")
}

function addSectionModal_clearCurrentPreviews() {
    addSectionModal_getAllTemplates().forEach((e)=>{ if (!(e == addSectionModal_styleElement)) e.remove() })
}

function addSectionModal_populate(data) {
    addSectionModal_styleElement.innerHTML = data.css

    addSectionModal_clearCurrentPreviews()

    var i=1

    for (var section of data.sections) {
        //addSectionModal_list.innerHTML += section
        addSectionModal_list.insertAdjacentHTML("beforeend",section)
        var e = document.querySelector(".--headline.--type-"+i)

        e.addEventListener("click",function() { addSection(stripPreviewTags(section));addSectionModal_hide() })

        i++
    }
}

function resizable() { return document.querySelectorAll("[data-kraken-resizable]:not([data-kraken-locked])") } 
function draggable() { return document.querySelectorAll("[data-kraken-draggable]:not([data-kraken-locked])") }
function draggableResizable() { return document.querySelectorAll("[data-kraken-resizable][data-kraken-draggable]:not([data-kraken-locked])") }

function createResizeBoxes() {
    for (var element of draggableResizable()) {
        element.appendChild(createResizeBoxContainerElement())
    }
}

function createResizeBoxContainerElement() {
    container = document.createElement("div")
    container.classList.add("element-resize-container")
    container.appendChild(createResizeBoxCornersElement())
    container.appendChild(createResizeBoxEdgesElement())
    return container
}

function createResizeBoxEdgesElement() {
    outline = document.createElement("div")
    outline.classList.add("element-outline")
    return outline
}

function createResizeBoxCornersElement() {
    root = document.createElement("div")
    root.classList.add("resize-corners")
    root.appendChild(createResizeBoxCornerElement("top-left"))
    root.appendChild(createResizeBoxCornerElement("top-right"))
    root.appendChild(createResizeBoxCornerElement("bottom-left"))
    root.appendChild(createResizeBoxCornerElement("bottom-right"))
    return root
}

function createResizeBoxCornerElement(loc) {
    corner = document.createElement("div")
    corner.classList.add("resize-corner")
    corner.classList.add(`resize-corner-${loc}`)
    trigger = document.createElement("div")
    trigger.classList.add("resize-corner-visual-element")
    corner.appendChild(trigger)
    return corner
}

run()
loadsections()