function revealOption(e) { e.style.opacity=1;e.style.visibility="visible" }
function hideFromLeft() { fromLeftOptions.style.opacity=0;fromLeftOptions.style.visibility="hidden" }

function makeSlide() { document.querySelectorAll(buttonsPrefix+":not(.slide-or-static) .btn").forEach((e)=>{ e.classList.add("slide") }) }
function makeStatic() { document.querySelectorAll(buttonsPrefix+":not(.slide-or-static) .btn").forEach((e)=>{ e.classList.remove("slide") }) }

function makeSquare() { document.querySelectorAll(buttonsPrefix+":not(.corner-options) .btn").forEach((e)=>{ removeClasses(e,["rounded","pill"]);addClass(e,"square") }) }
function makeRounded() { document.querySelectorAll(buttonsPrefix+":not(.corner-options) .btn").forEach((e)=>{ removeClasses(e,["square","pill"]);addClass(e,"rounded") }) }
function makePill() { document.querySelectorAll(buttonsPrefix+":not(.corner-options) .btn").forEach((e)=>{ removeClasses(e,["rounded","square"]);addClass(e,"pill") }) }

function makeThin() { document.querySelectorAll(buttonsPrefix+".left-or-right .btn").forEach((e)=>{ e.classList.add("thin") }) }
function makeThick() { document.querySelectorAll(buttonsPrefix+".left-or-right .btn").forEach((e)=>{ e.classList.remove("thin") }) }

function enableSubmit() { document.querySelector(".new-site-form.four .field-submit").removeAttribute("disabled") }
function disableSubmit() { document.querySelector(".new-site-form.four .field-submit").setAttribute("disabled","") }

function updateStored() {
    var out="sliding:"+slidingPreference+",cornerType:"+squaredPreference+",thin:"+thinPreference+",fromLeft:"+fromLeftPreference
    stored.value=out
}

var slidingPreference = null;
var squaredPreference = null
var thinPreference = null;
var fromLeftPreference = null;
var canOpenFromLeft = false;
var hasOpenFromLeft = false;

var slidingOptions = document.querySelector(".new-site-form.four .button-option.slide-or-static")
var squaredOptions = document.querySelector(".new-site-form.four .button-option.corner-options")
var thinOptions = document.querySelector(".new-site-form.four .button-option.thin-or-large")
var fromLeftOptions = document.querySelector(".new-site-form.four .button-option.left-or-right")
var buttonsPrefix = ".new-site-form.four .button-option"
var stored=document.getElementById("style-option-output")

slidingOptions.querySelector(".option-true").addEventListener("click",(e)=>{
    slidingPreference=true;
    revealOption(squaredOptions);
    makeSlide();
    canOpenFromLeft=true;
    if(hasOpenFromLeft){revealOption(fromLeftOptions)}
    if(thinPreference!=null){revealOption(fromLeftOptions)}
    if(fromLeftPreference==null){disableSubmit()}
    updateStored();
})
slidingOptions.querySelector(".option-false").addEventListener("click",(e)=>{
    slidingPreference=false;
    revealOption(squaredOptions);
    makeStatic();
    canOpenFromLeft=false;
    hideFromLeft();
    updateStored();
})

squaredOptions.querySelector(".square").addEventListener("click",(e)=>{
    squaredPreference="square";
    revealOption(thinOptions);
    makeSquare();
    updateStored();
})
squaredOptions.querySelector(".rounded").addEventListener("click",(e)=>{
    squaredPreference="rounded";
    revealOption(thinOptions);
    makeRounded();
    updateStored();
})
squaredOptions.querySelector(".pill").addEventListener("click",(e)=>{
    squaredPreference="pill";
    revealOption(thinOptions);
    makePill();
    updateStored();
})

thinOptions.querySelector(".option-true").addEventListener("click",(e)=>{
    thinPreference=true;
    if(canOpenFromLeft){revealOption(fromLeftOptions);hasOpenFromLeft=true};
    makeThin();
    if(!(slidingPreference)){enableSubmit()}
    updateStored();
})
thinOptions.querySelector(".option-false").addEventListener("click",(e)=>{
    thinPreference=false;
    if(canOpenFromLeft){revealOption(fromLeftOptions);hasOpenFromLeft=true};
    makeThick();
    if(!(slidingPreference)){enableSubmit()}
    updateStored();
})

fromLeftOptions.querySelector(".option-true").addEventListener("click",(e)=>{
    fromLeftPreference=true;
    enableSubmit();
    updateStored();
})
fromLeftOptions.querySelector(".option-false").addEventListener("click",(e)=>{
    fromLeftPreference=false;
    enableSubmit();
    updateStored();
})
