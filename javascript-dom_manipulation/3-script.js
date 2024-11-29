document.getElementById("toggle_header").onclick = colorToggle;
function colorToggle() {
  document.querySelector("header").classList.toggle("green");
  document.querySelector("header").classList.toggle("red");

}
