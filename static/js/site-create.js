String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

function checkFormSubmitButton() {
  if (!(formName.getAttribute("data-form-input-display") == "success" || formName.getAttribute("data-form-input-display") == "warning")){formSubmit.setAttribute("disabled","");return}
  if (!(formPrivacy1.checked) && !(formPrivacy2.checked)){formSubmit.setAttribute("disabled","");return}
  formSubmit.removeAttribute("disabled"); return;
}

function editFormMessage(nameInput,val) {
  messageContainer.classList.remove("visibly-hidden")
  newInner=val.toLowerCase()
  for (var i=0; i<newInner.length; i++) {
    var letter=newInner[i];
    if (!(allowedChars.includes(letter))) {
      newInner=newInner.replaceAt(i,"-")
    }
  }
  if (hasRepeatedDashes(newInner)) { newInner=replaceRepeatedDashes(newInner) }
  messageSpan.innerHTML=newInner
}

function hideFormMessage() {
  messageContainer.classList.add("visibly-hidden")
  messageSpan.innerHTML=""
}

function hasRepeatedDashes(val) {
  for (var i=0;i<val.length;i++) {
    if (val[i] == "-" && val[i+1] == "-") {
      return true
    }
  }
  return false
}

function replaceRepeatedDashes(val) {
  return listToStr(replaceRepeatedDashesRecursion(val.split("")))
}

function listToStr(lst) {
  var out=""
  for (var i=0;i<lst.length;i++) {
    out=out+lst[i]
  }
  return out
}

function replaceRepeatedDashesRecursion(val) {
  for (var i=0;i<val.length;i++) {
    if (val[i] == "-" && val[i+1] == "-") {
      val.splice(i+1,1)
      val=replaceRepeatedDashesRecursion(val)
    }
  }
  return val
}

var requiredChars = "qwertyuiopasdfghjklzxcvbnm1234567890"
var allowedChars = "qwertyuiopasdfghjklzxcvbnm-._1234567890";
var formSubmit = document.getElementById("new_site_form_submit");
var formName = document.getElementById("new_site_name");
var formDesc = document.getElementById("new_site_desc");
var formPrivacy1 = document.getElementById("new_site_privacy_visible");
var formPrivacy2 = document.getElementById("new_site_privacy_hidden");
var messageContainer = document.querySelector(".new-site-form .form-input-container.one .message-container");
var messageSpan = document.querySelector(".new-site-form .form-input-container.one .message-container .message-container-jsedit");

formName.addEventListener("keyup",(event) => {
    formName.setAttribute("data-form-input-display",verifyNameField())
    checkFormSubmitButton();
})

formPrivacy1.addEventListener("click",checkFormSubmitButton)
formPrivacy2.addEventListener("click",checkFormSubmitButton)

formSubmit.addEventListener("click",(event)=>{
    if (!(formSubmit.getAttribute("disabled"))) {
        formSubmit.children[0].innerHTML = "CREATING SITE..."
    }
})
