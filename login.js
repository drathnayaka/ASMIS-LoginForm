//this login.js file used to get user credentials form login form
//and if  validation has done, the home page will be dispayed
function check_pwd() {
  // get data
  var data = new FormData(document.getElementById("login-form"));

  fetch("login.py", { method:"_POST", body:data })
  .then((res) => { return res.text(); })
  .then((txt) => {
    if (txt == "OK") { location.href = "home.html"; }
    else { alert(txt); }
  });
  return false;
}
