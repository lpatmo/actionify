/*function openPage() {
  browser.tabs.create({
    url: "https://developer.mozilla.org"
  });
}

browser.browserAction.onClicked.addListener(openPage);
console.log("hi");*/

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('RecommendBtn').addEventListener('click', recommendActions);
    document.getElementById('SubmitBtn').addEventListener('click', submitActions);      
    document.getElementById('CancelBtn').addEventListener('click', cancelActions);
    let currentTab = browser.tabs.query({active: true, currentWindow:true});     	
    let urltxt = document.getElementById('newsURL');
    
    currentTab.then(setURL)
    function setURL(tab){
    	urltxt.value=tab[0].url;

    }

});

function recommendActions(){
	document.getElementById("TakeAction").style.display="none";
	document.getElementById("SubmitForm").style.display="block";
	document.querySelector("body").style.width="230px";
}
function cancelActions(){
	document.getElementById("TakeAction").style.display="block";
	document.getElementById("SubmitForm").style.display="none";
	document.querySelector("body").style.width="100%";
}
function submitActions(){
	//form stuff
	cancelActions();
}