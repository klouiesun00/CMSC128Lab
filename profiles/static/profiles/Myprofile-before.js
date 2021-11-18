/* validate form information */

/* var uname1 = document.forms["log-in-form"]["uname"].value;
var pwrd1 = document.forms["log-in-form"]["password"].value;
var email = document.forms["sign-up-form"]["email"].value;
var uname2 = document.forms["sign-up-form"]["uname"].value;
var pwrd2 = document.forms["sign-up-form"]["password"].value;


function validateLogin() {
  if (uname1 == "" || pwrd1 == "") {
    alert("Please fill in all the required fields");
    return false;
  }
}

function validateSignup() {
  if (email == "" || uname2 == "" || pwrd2 == "") {
    alert("Please fill in all the required fields");
    return false;
  }
} */

var pw1 = document.getElementById("id_password1");    // sign up passwords
var pw2 = document.getElementById("id_password2");
var pw3 = document.getElementById("id_password");     // log in password
var togglepw1 = document.getElementById("password-toggle");   // sign up toggle
var togglepw2 = document.getElementById("password-toggle1");  // log in toggle

const togglePasswordSU=(e) => {     //password toggling for sign up form
  if(togglepw1.textContent==="Show password"){   // for sign up
    togglepw1.textContent="Hide password";
    pw1.setAttribute("type", "text");
    pw2.setAttribute("type", "text");
    
  }else{                                        // for sign up
    togglepw1.textContent="Show password";
    pw1.setAttribute("type", "password");
    pw2.setAttribute("type", "password");
  }
}

const togglePasswordLI=(e) => {      //password toggling for sign up form
  if(togglepw2.textContent==="Show password"){    // for log in
    togglepw2.textContent="Hide password";
    pw3.setAttribute("type", "text");
  }else{
    togglepw2.textContent="Show password";
    pw3.setAttribute("type", "password");
  }
}
togglepw1.addEventListener("click", togglePasswordSU);
togglepw2.addEventListener("click", togglePasswordLI);

