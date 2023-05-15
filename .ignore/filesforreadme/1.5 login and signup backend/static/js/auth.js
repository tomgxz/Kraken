// Function called for each field to make sure it is in the correct format, takes a few arguments as flags for what makes it valid
function verifyField(field,fieldName,mustHaveChar=true,minLen=3,canHaveSpace=false,canHaveSpecialChar=true,isPassword=false) {
  // List of special characters for the canHaveSpecialChar flag
  specialChar="%&{}\\<>*?/$!'\":@+`|="

  // Make sure that the input given is a string
  if (typeof field != "string") {throw new Error("HEY! that's not a string?")}

  // Check through all the flags given and throw an appropriate error message if input is invalid
  if (field.length == 0 && mustHaveChar) {return `${fieldName} is not filled out.`}
  if (field.length < minLen) {return `${fieldName} must be greater than ${minLen-1} characters.`}
  if (!canHaveSpace && field.includes(" ")) {return `${fieldName} cannot contain spaces.`}
  if (!canHaveSpecialChar) {
    // Iterate through each character in specialChar to see if its in the input
    // I didn't use regex for this as I wanted to be able to tell the user which character wasn't allowed
    var char;
    for (var i=0;i<specialChar.length;i++) {
      char=specialChar[i]
      if (field.includes(char)) {
        return `${fieldName} cannot contain '${char}'`
      }
    }
  }
  // If the given input is a password
  if (isPassword) {
    // If it doesnt match the given regular expression for password checks
    if (!field.match(/(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_%&{}\\<>*?\/$!'\":@+`|=]).{8,}/)) {
      return `${fieldName} must contain at least 1 of each: uppercase character, lowercase character, number, and special character`
    }
  }

  /*
  Regex pattern breakdown
    (?=.*?[A-Z]) = contains an uppercase character
    (?=.*?[a-z]) = contains a lowercase character
    (?=.*?[0-9]) = contains a digit
    (?=.*?[#?!@$%^&*-_%&{}\\<>*?\/$!'\":@+`|=]) = contains a special character
    .{8,} = has a minimum length of 8 and no upper limit
  */

  return ""
}

// Initialise the code for the all seeing eyes to enable viewing the password
function initAllSeeingEye(element,reveal) {
  // Add onclick event to given element (the eye element)
  element.addEventListener("click", e=> {
    // toggle input type of given input between password and text
    reveal.setAttribute('type',reveal.getAttribute('type') === 'password' ? 'text' : 'password');
    // toggle the fa-eye-slash class for the eye (this sets the icon displayed)
    element.classList.toggle('fa-eye-slash');
  })
}

// Function takes a string and returns a boolean determining whether it is in a valid email format, using regex
function isEmail(email) {
  return email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)
}

// fetch warning element and disable submit bottom
warningSpan = document.querySelector(".field-container .field-warning")
document.querySelector(".field-submit").disabled = true
