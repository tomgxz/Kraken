function addElement(parent,name,src,css,type) {
    if parent >= siteDat.length { console.log("Parent ID larger than list of elements");return false; }

    var id=0;
    if siteDat.length > 0 { siteDat[siteDat.length-1]["id"]+1;  }

    siteDat.add(
      {
        "name":name,
        "locked":false,
        "src":src,
        "css":css,
        "type":type,
        "parent":parent,
        "id":id,
      }

    )
}

var builder = document.getElementById("contains_site")
