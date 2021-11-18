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

/*Creates the pop-up modal boxes for book summaries*/
// Get all the modals
var modal1 = document.getElementById("modal1");
var modal2 = document.getElementById("modal2");
var modal3 = document.getElementById("modal3");
var modal4 = document.getElementById("modal4");
var modal5 = document.getElementById("modal5");
var modal6 = document.getElementById("modal6");
var modal7 = document.getElementById("modal7");
var modal8 = document.getElementById("modal8");
var modal9 = document.getElementById("modal9");
var modal10 = document.getElementById("modal10");

// Get the triggers for the modal
var btn1 = document.getElementById("CRA");
var btn2 = document.getElementById("CoS");
var btn3 = document.getElementById("AtBP");
var btn4 = document.getElementById("IGYtS");
var btn5 = document.getElementById("TPoBaW");
var btn6 = document.getElementById("THG");
var btn7 = document.getElementById("EaP");
var btn8 = document.getElementById("L");
var btn9 = document.getElementById("ED");
var btn10 = document.getElementById("TLT");

// for the (x) of each modal
var span1 = document.getElementById("close1");
var span2 = document.getElementById("close2");
var span3 = document.getElementById("close3");
var span4 = document.getElementById("close4");
var span5 = document.getElementById("close5");
var span6 = document.getElementById("close6");
var span7 = document.getElementById("close7");
var span8 = document.getElementById("close8");
var span9 = document.getElementById("close9");
var span10 = document.getElementById("close10");

// When the user clicks on the img, open the modal
btn1.onclick = function() {
  modal1.style.display = "block";
}

btn2.onclick = function() {
  modal2.style.display = "block";
} 

btn3.onclick = function() {
  modal3.style.display = "block";
}

btn4.onclick = function() {
  modal4.style.display = "block";
}

btn5.onclick = function() {
  modal5.style.display = "block";
}

btn6.onclick = function() {
  modal6.style.display = "block";
}

btn7.onclick = function() {
  modal7.style.display = "block";
}

btn8.onclick = function() {
  modal8.style.display = "block";
}

btn9.onclick = function() {
  modal9.style.display = "block";
}

btn10.onclick = function() {
  modal10.style.display = "block";
}

// When the user clicks on (x), close the modal
span1.onclick = function() {
  modal1.style.display = "none";
}

span2.onclick = function() {
  modal2.style.display = "none";
}

span3.onclick = function() {
  modal3.style.display = "none";
}

span4.onclick = function() {
  modal4.style.display = "none";
}

span5.onclick = function() {
  modal5.style.display = "none";
}

span6.onclick = function() {
  modal6.style.display = "none";
}

span7.onclick = function() {
  modal7.style.display = "none";
}

span8.onclick = function() {
  modal8.style.display = "none";
}

span9.onclick = function() {
  modal9.style.display = "none";
}

span10.onclick = function() {
  modal10.style.display = "none";
}


// When the user clicks anywhere outside of modal, close it
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }else if (event.target == modal2) {
  	modal2.style.display = "none";
  }else if (event.target == modal3) {
  	modal3.style.display = "none";
  }else if (event.target == modal4) {
  	modal4.style.display = "none";
  }else if (event.target == modal5) {
  	modal5.style.display = "none";
  }else if (event.target == modal6) {
  	modal6.style.display = "none";
  }else if (event.target == modal7) {
  	modal7.style.display = "none";
  }else if (event.target == modal8) {
  	modal8.style.display = "none";
  }else if (event.target == modal9) {
  	modal9.style.display = "none";
  }else if (event.target == modal10) {
  	modal10.style.display = "none";
  }
}
