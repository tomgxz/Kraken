## Appendix B - Testing

### References to testing in the report

Any testing will either be recorded during the development process or recorded in Appendix B, such as different platforms used in the UI design, or invalid inputs entered when checking user input.

The elements could now be resized using the resize handles that are rendered when an element is hovered or selected. The element cannot be resized to larger than the grid due to the `closestValInArray` being only snapping to the extremes as a maximum, and how the `grid-position` property is handled in CSS. The handles have a invisible area around them that also responds to the `mousemove` and `mouseup` events, so that it can still be moved if the user moves their cursor outside of the handle's area (by going vertically or moving too fast). The testing evidence of this can be found in Appendix B.

The asynchronous function `saveContent` will be called whenever the save button is pressed in the editor, and whenever the autosave process is triggered. It uses the jQuery function `ajax` to send a `POST` method request to the server, on the URL `/<username>/<sitename>/save/<pagename>`, with the content `siteroot().outerHTML` - i.e. the content of the editor. The paramaters `error` and `success` define the functions to be called when the request is finished, based on the outcome. As of now, they simply write to the console. Testing of this using DevTools's Network Conditions functionality can be found in Appendix B.

In Appendix B, I used DevTools' Network Conditions throttling settings to test how it worked on lower connections, including when the site was offline.

### Signup Form Validation

#### Client-Side

The signup form has validation using the same function both client-side and server-side. This is the testing data used for the client-side validation.

|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
|-|-|-|-|-|-|
|Name|`Aaaaa`|Check it says valid|Valid|Valid|Pass
|Name|`Aaa Bbb`|Check it allows spaces|Valid|Valid|Pass
|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Valid|Fail
|Name|null|Check that it requires name|Invalid|Invalid|Pass
|Email|`a@b.cc`|Check it says valid|Valid|Valid|Pass
|Email|`ab12@f42.x7`|Check it says valid|Valid|Valid|Pass
|Email|`@b.cc`|Check it recognises the area before `@`|Invalid|Invalid|Pass
|Email|`a@.cc`|Check it recognises the area after `@`|Invalid|Invalid|Pass
|Email|`a@b.c`|Check it requires a top level domain longer than 1|Invalid|Invalid|Pass
|Email|`a@b.cdef`|Check it requires a top level domain shorter than 4|Invalid|Invalid|Pass
|Email|`a b@ccc.uk`|Check it doesn't allow spaces|Invalid|Invalid|Pass
|Email|null|Check that it requires email|Invalid|Invalid|Pass
|Username|`Aaa`|Check it says valid|Valid|Valid|Pass
|Username|`Aaa bbb`|Check it doesn't allow spaces|Invalid|Invalid|Pass
|Username|`A-._+c`|Check it allows special characters not given in the list|Valid|Valid|Pass
|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Valid|Fail
|Username|null|Check it requires username|Invalid|Invalid|Pass
|Password|`aaa`|Check it has a minimum length of 8|Invalid|Invalid|Pass
|Password|`Aaaaaa_1`|Data to work off for next tests|Valid|Valid|Pass
|Password|`aaaaaa_1`|Check it requires an uppercase character|Invalid|Invalid|Pass
|Password|`AAAAAA_1`|Check it requires a lowercase character|Invalid|Invalid|Pass
|Password|`Aaaaaa_a`|Check it requires a number|Invalid|Invalid|Pass
|Password|`Aaaaaaa1`|Check it requires a special character|Invalid|Invalid|Pass
|Password|null|Check it requires password|Invalid|Invalid|Pass
|Passwords|`Aaaaaa_1` in both fields|Check both fields have to match|Valid|Valid|Pass
|Passwords|`Aaaaaa_1` in one field, `ABCDEF` in the second|Check both fields have to match|Invalid|Invalid|Pass

As you can see from the table, two of the validation checks failed. These are listed here:

|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
|-|-|-|-|-|-|
|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Valid|Fail
|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Valid|Fail

These were both to do with verifying special characters, and, when I revisited the code, I saw that the error was when I tried to iterate through the characters in a string like you do can do in python. Hence, I modified the line `for (var char in specialChar)` to function properly, and both tests came out as invalid.

|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
|-|-|-|-|-|-|
|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Invalid|Pass
|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Invalid|Pass

#### Server-Side

The same set of data was used to check the server-side validation, to ensure that they both returned the same results.

|Field|Test Data|Reason|Expected Outcome|Actual Outcome|Pass/Fail|
|-|-|-|-|-|-|
|Name|`Aaaaa`|Check it says valid|Valid|Valid|Pass
|Name|`Aaa Bbb`|Check it allows spaces|Valid|Valid|Pass
|Name|`Aaa%bbb`|Check that it doesn't allow special chars|Invalid|Invalid|Pass
|Name|None|Check that it requires name|Invalid|Invalid|Pass
|Email|`a@b.cc`|Check it says valid|Valid|Valid|Pass
|Email|`ab12@f42.x7`|Check it says valid|Valid|Valid|Pass
|Email|`@b.cc`|Check it recognises the area before `@`|Invalid|Invalid|Pass
|Email|`a@.cc`|Check it recognises the area after `@`|Invalid|Invalid|Pass
|Email|`a@b.c`|Check it requires a top level domain longer than 1|Invalid|Invalid|Pass
|Email|`a@b.cdef`|Check it requires a top level domain shorter than 4|Invalid|Invalid|Pass
|Email|`a b@ccc.uk`|Check it doesn't allow spaces|Invalid|Invalid|Pass
|Email|None|Check that it requires email|Invalid|Invalid|Pass
|Username|`Aaa`|Check it says valid|Valid|Valid|Pass
|Username|`Aaa bbb`|Check it doesn't allow spaces|Invalid|Invalid|Pass
|Username|`A-._+c`|Check it allows special characters not given in the list|Valid|Valid|Pass
|Username|`%&{}\\<>*?/$!'\":@+`|Check it doesn't allow these special characters|Invalid|Invalid|Pass
|Username|None|Check it requires username|Invalid|Invalid|Pass
|Password|`aaa`|Check it has a minimum length of 8|Invalid|Invalid|Pass
|Password|`Aaaaaa_1`|Data to work off for next tests|Valid|Valid|Pass
|Password|`aaaaaa_1`|Check it requires an uppercase character|Invalid|Invalid|Pass
|Password|`AAAAAA_1`|Check it requires a lowercase character|Invalid|Invalid|Pass
|Password|`Aaaaaa_a`|Check it requires a number|Invalid|Invalid|Pass
|Password|`Aaaaaaa1`|Check it requires a special character|Invalid|Invalid|Pass
|Password|None|Check it requires password|Invalid|Invalid|Pass
|Passwords|`Aaaaaa_1` in both fields|Check both fields have to match|Valid|Valid|Pass
|Passwords|`Aaaaaa_1` in one field, `ABCDEF` in the second|Check both fields have to match|Invalid|Invalid|Pass