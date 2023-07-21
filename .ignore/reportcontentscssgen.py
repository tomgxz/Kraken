x = """ - [File Structure Diagram](#file-structure-diagram) ~~95~~
  - [Code](#code) ~~96~~
    - [Root Directory](#root-directory) ~~96~~
      - [\_\_init\_\_.py](#__init__py) ~~96~~
      - [dbCommands.txt](#dbcommandstxt) ~~107~~
      - [models.py](#modelspy) ~~108~~
      - [requirements.txt](#requirementstxt)
      >

      - [/static](#staticcss) ~~109~~
        - [/css](#staticcss) ~~109~~
          - [auth.css](#staticcssauthcss) ~~109~~
          - [blank.css](#staticcssblankcss) ~~112~~
          - [build.css](#staticcssbuildcss) ~~114~~
          - [default_content_style.css](#staticcssdefault_content_stylescss) ~~116~~
          - [edit.css](#staticcsseditcss) ~~116~~
          - [home.css](#staticcsshomecss) ~~116~~
          - [index.css](#staticcssindexcss) ~~118~~
          - [main.css](#maincss) ~~120~~
          - [preview_override.css](#staticcsspreview_overridecss)
          - [settings.css](#settingscss) ~~121~~
          - [site-create.css](#site-createcss) ~~125~~
          - [site-edit.css](#site-editcss) ~~131~~
        - [/html/sections](#statichtmlsections) ~~135~~
          - [classes](#statichtmlsectionsclasses) ~~135~~
          - [/headline](#statichtmlsectionsheadline) ~~135~~
            - [css.css](#statichtmlsectionsheadlinecsscss) ~~135~~
            - [files](#statichtmlsectionsheadlinefiles) ~~138~~
            - [html_element_headline_1.html](#statichtmlsectionsheadlinehtom_element_headline_1html) ~~138~~
        - [/js](#staticjs) ~~138~~
          - [auth.js](#staticjsauthjs) ~~138~~
          - [colorConversion.js](#staticjscolorconversionjs) ~~140~~
          - [globalnav-floating-options.js](#staticjsglobalnav-floating-optionsjs) ~~142~~
          - [login.js](#staticjsloginjs) ~~143~~
          - [main.js](#staticjsmainjs) ~~143~~
          - [signup.js](#staticjssignupjs) ~~144~~
          - [site-create-options-1.js](#staticjssite-create-options-1js) ~~145~~
          - [site-create-options-2.js](#staticjssite-create-options-2js) ~~151~~
          - [site-create-options-3.js](#staticjssite-create-options-2js) ~~152~~
          - [site-create.js](#staticjssite-createjs) ~~154~~
          - [site-edit.js](#staticjssite-editjs) ~~157~~
        >

      - [/templates](#templates) ~~162~~
        - [base.html](#templatesbasehtml) ~~162~~
        - [home-nosite.html](#templateshome-nositehtml) ~~165~~
        - [home-sites.html](#templateshome-siteshtml) ~~166~~
        - [login.html](#templatesloginhtml) ~~167~~
        - [settings-admin.html](#templatessettings-adminhtml) ~~168~~
        - [settings-base.html](#templatessettings-basehtml) ~~171~~
        - [settings-code.html](#templatessettings-codehtml) ~~173~~
        - [settings-dev.html](#templatessettings-devhtml) ~~174~~
        - [settings-looks.html](#templatessettings-lookshtml) ~~174~~
        - [settings-profile.html](#templatessettings-profilehtml) ~~175~~
        - [settings-sites.html](#templatessettings-siteshtml) ~~176~~
        - [signup.html](#templatessignup) ~~178~~
        - [site-create-base.html](#templatessite-create-basehtml) ~~179~~
        - [site-create-options-1.html](#templatessite-create-options-1html) ~~180~~
        - [site-create-options-2.html](#templatessite-create-options-2html) ~~183~~
        - [site-create-options-3.html](#templatessite-create-options-3html) ~~185~~
        - [site-create.html](#templatessite-createhtml) ~~187~~
        - [site-edit-home.html](#templatessite-edit-homehtml) ~~189~~
        - [site-edit.html](#templatessite-edithtml) ~~190~~
"""

import re

cssq1 = cssq2 = ""

for y in re.findall("\(([^\)]+)\)",x):
    if y == "#": continue
    z = f"a[href=\"{y}\"],"
    cssq1 += z
    if y in ["#analysis","#design","#development","#testing","#evaluation","#appendix-a---code","#appendix-b---testing","#file-structure-diagram","#code"]:
        cssq2 += z
        
cssq1 = cssq1[:-1] + "{color:black}"
cssq2 = (cssq2[:-1] + "{font-weight:600}") if cssq2 != "" else ""

print(cssq1+cssq2)