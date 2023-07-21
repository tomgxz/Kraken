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

  // If no errors are called, then enable the button and clear the warning message
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
