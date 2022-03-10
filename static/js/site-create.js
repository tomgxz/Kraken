function checkFormSubmitButton() {
  if (!(formName.getAttribute("data-form-input-display") == "success" || formName.getAttribute("data-form-input-display") == "warning")){formSubmit.setAttribute("disabled","");return}
  if (!(formPrivacy1.checked) && !(formPrivacy2.checked)){formSubmit.setAttribute("disabled","");return}
  formSubmit.removeAttribute("disabled"); return;
}

var allowedChars = "qwertyuiopasdfghjklzxcvbnm-._1234567890";
var formSubmit = document.getElementById("new_site_form_submit");
var formName = document.getElementById("new_site_name");
var formPrivacy1 = document.getElementById("new_site_privacy_visible");
var formPrivacy2 = document.getElementById("new_site_privacy_hidden");

formName.addEventListener("keyup",(event) => {
    formName.setAttribute("data-form-input-display",verifyNameField())
    checkFormSubmitButton();
})

formPrivacy1.addEventListener("click",checkFormSubmitButton)
formPrivacy2.addEventListener("click",checkFormSubmitButton)

formSubmit.addEventListener("click",(event)=>{
    console.log(formSubmit.getAttribute("disabled"))
    if (!(formSubmit.getAttribute("disabled"))) {
        formSubmit.children[0].innerHTML = "CREATING SITE..."
    }
})
