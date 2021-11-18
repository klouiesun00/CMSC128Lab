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