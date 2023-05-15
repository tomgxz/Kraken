// function called when an input is changed, to check whether all inputs are valid
function verifyAllFields() {
  verifyOutput=self.verifyField(fields["Name"].value,"Name",canHaveSpace=true)

  if (verifyOutput.length > 0) {
    warningSpan.innerText = verifyOutput
    document.querySelector(".field-submit").disabled = true
    return
  }

  verifyOutput=self.verifyField(fields["Email"].value,"Email",minLen=0,canHaveSpace=false)

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

  verifyOutput=self.verifyField(fields["Username"].value,"Username",canHaveSpecialChar=false)

  if (verifyOutput.length > 0) {
    warningSpan.innerText = verifyOutput
    document.querySelector(".field-submit").disabled = true
    return
  }

  verifyOutput=self.verifyField(fields["Password"].value,"Password",minLen=8,passwordCheck=true)

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
