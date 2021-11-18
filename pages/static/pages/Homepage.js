/*makes nav bar sticky*/

// When the user scrolls the page, execute function
window.onscroll = function() {stickyNavBar()};

// Get the header
var header = document.getElementById("navidiv");

// returns position of header from the top
var sticky = header.offsetTop;

// Add sticky class to header when you reach its scroll position and remove when you leave the scroll position
function stickyNavBar() {
  if (window.pageYOffset > sticky) { //pageYOffset is vertical axis of window; if user scrolls after position of header
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}