/*makes nav bar sticky*/

window.onscroll = function() {stickyNavBar()};
var header = document.getElementById("navidiv");
var sticky = header.offsetTop;

function stickyNavBar() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

/* collapsible effect on book reviews */
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) { //for each element in collapsible class
  coll[i].addEventListener("click", function() {  //if button is clicked add the active class
    this.classList.toggle("active");
    var content = this.nextElementSibling;	// and display/hide the element right after the button, which is its content
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}