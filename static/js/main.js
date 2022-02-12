function letterWrapper(query) {
	// takes a html element query and wraps every letter inside with a span <span class="js-wrapped-letter js" style="display:inline-block"></span>
	
    document.querySelectorAll(query).forEach((item) => {
        item.innerHTML=item.textContent.replace(/\w/g, "<span class='js-wrapped-letter js' style='display:inline-block'>$&</span>");
    });
}

function wordWrapper(query) {
	// takes a html element query and wraps every word inside with a span <span class="js-wrapped-word js" style="display:inline-block"></span>
	
    document.querySelectorAll(query).forEach((item) => {
        item.innerHTML=item.textContent.replace(/\w+/g,"<span class='js-wrapped-word js' style='display:inline-block'>$&</span>");
    });
}

function lineWrapper(query) {
	// takes a html element query and wraps every line inside with a span <span class="js-wrapped-line js" style="display:inline-block"></span>
	
    document.querySelectorAll(query).forEach((item) => {
        item.innerHTML=item.textContent.replace(/.+$/gm,"<span class='js-wrapped-line js' style='display:inline-block'>$&</span>");
    });
}

function jsQ(query) {
	// takes a html element query and appends the class "js" to it. Used to recognise which elements have been edited by javascript
	
    try {
        document.querySelectorAll(query).forEach((item) => {item.classList.add("js")});
    } catch(e) {
        console.log(e);
    }
}

function jsE(el) {
	// takes a html element object and appends the class "js" to it. Used to recognise which elements have been edited by javascript
	
    try {
        el.classList.add("js");
    } catch(e) {
        console.log(e);
    }
}

$(document).ready(function () {
    document.body.classList.remove("visibly-hidden");jsE(document.body); // reveal the page when it has been loaded
    
});