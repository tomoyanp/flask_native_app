function createHtml() {


	var titleElem = document.getElementById("title");
	var contentElem = document.getElementById("blog-content");

    var outputContents = ""
    titleTmp = titleElem.value;
	titleTmp = "<p id=\"blog-title\">" + titleTmp + "</p>";

    outputContents += titleTmp + "\n"

    contentTmp = contentElem.value;
    contentTmp = contentTmp.split("\n");

    for(var i = 0; i < contentTmp.length; i++) {
    	console.log("####");
    	contentTmp[i] = "<p id=\"inner-blog\">" + contentTmp[i] + "</p>";
    	outputContents += contentTmp[i] + "\n";
    }


    var outputDiv = document.getElementById("output");
    outputDiv.value = outputContents;

}