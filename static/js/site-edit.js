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

function setSectionNavbar(text) {
    text=text.split(/[\r\n]+/g);out="";
    for (var i=0; i<text.length; i++) {
        out=out+sectionSelectorNavItem
          .replace("[i]",number2words(i+1).replace(" ",""))
          .replace("[n1]",text[i].replace(" ",""))
          .replace("[n2]",capitalizeWords(text[i]))
    }
    sectionSelectorNav.querySelector("ul.section-selector-nav-list").innerHTML=out;
}

function sectionNavbarSetSelected() {
    sectionSelectorNav.querySelector(`ul.section-selector-nav-list li a.link`).style.opacity=0.75;
    sectionSelectorNav.querySelector(`ul.section-selector-nav-list li.${sectionSelectorNavSelected} a.link`).style.opacity=1;
    sectionSelectorDisplayPreview();
}

function sectionSelectorDisplayPreview() {
  function layer1(text) {
    path=`../../../static/html/sections/${text.split(/[\r\n]+/g)[sectionSelectorNavSelectedInt-1]}`;

    fetch(path+"/css.css")
        .then( response => {
            if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
            return response.text();})
        .then( text0 => sectionSelectorList.innerHTML = sectionSelectorList.innerHTML + `<style>${text0}</style>`  )

    fetch(path+"/files")
        .then( response => {
            if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
            return response.text();})
        .then( text1 => layer2(path,text1) )
  }

  function layer2(path,text) {
      text=text.split(/[\r\n]+/g).filter(function(value, index, arr){ return value != "" });
      for (var i=0; i<text.length; i++) {
          layer3(`${path}/${text[i]}`)
          //fetch(`${path}/${text[i]}`)
          //    .then( response => {
          //        if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
          //        return response.text();})
          //    .then( text1 => layer3(text1) )
      }
  }

  function layer3(text) {
      fetch(text)
          .then( response => {
              if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
              return response.text();})
          .then( text2 => layer4(text2) )
  }

  function layer4(text) {
      sectionSelectorList.innerHTML = sectionSelectorList.innerHTML + text

      previewSections = sectionSelectorList.querySelectorAll("[data-preview]")
      previewSections.forEach((e)=>{
          e.style.cursor = "pointer"
          e.style.marginBottom = "32px"
      })
  }

  sectionSelectorList.innerHTML = "";

  fetch("../../../static/html/sections/classes")
    .then( response => {
        if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
        return response.text() })
    .then( text => layer1(text) )
}

function parseXml(xml) {
    var parser = new DOMParser();
    return parser.parseFromString(xml,"text/xml");
}

function parseXmlFile(path) {
    fetch(path)
        .then( response => {
            if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
            return response.text() })
        .then( xml => {xml = parseXml(xml);return xml} )
}

function insertWebsite(html) { builder.innerHTML=html; }

var builder = document.getElementById("contains_site");
var addSectionBtn = document.getElementById("localnav_add_section_btn");
var sectionSelectorNavSelected="one";
var sectionSelectorNavSelectedInt=1;
var sectionSelectorContainer=document.querySelector(".application-content .section-selector-container");
var sectionSelectorList=document.getElementById("section_selector_list");
var sectionSelectorNav=document.getElementById("section_selector_nav");
var sectionSelectorNavItem=`<li class="section-selector-nav-item [i]"><a class="link unformatted" id="section_sele  ctor_nav_[n1]"><span class="text bold">[n2]</span></a></li>`;
var sectionClassList="";
var previewSections;

addSectionBtn.addEventListener("click",() => {
    if (!(sectionSelectorContainer.classList.contains("shown"))) {
      sectionSelectorContainer.classList.add("shown");
      document.querySelector(".lightbox-mask").classList.add("shown")
      sectionSelectorNavSelected="one";
      sectionNavbarSetSelected()
    }
});

document.querySelector(".application-content .section-selector-exit-btn").addEventListener("click",() => {
    document.querySelector(".application-content .section-selector-container").classList.remove("shown")
    document.querySelector(".lightbox-mask").classList.remove("shown")
});

document.querySelector(".lightbox-mask").addEventListener("click",() => {
  console.log(1);
    document.querySelector(".application-content .section-selector-container").classList.remove("shown")
    document.querySelector(".lightbox-mask").classList.remove("shown")
});

// section selector navbar content

fetch("../../../static/html/sections/classes")
  .then( response => {
    if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
    return response.text();
  })
  .then( text => setSectionNavbar(text) )

parseXmlFile("../../../static/data/userData/test/sites/testing-site/site.xml");

fetch("../../../static/data/userData/test/sites/testing-site/files/1.html")
  .then( response => {
    if (!response.ok) { throw new Error(`HTTP error: ${response.status}`) }
    return response.text();
  })
  .then( text =>  insertWebsite(text))
