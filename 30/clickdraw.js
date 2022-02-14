// Team HE: Han Zhang, Edwin Zheng
// SoftDev
// K30 -- Canvas Based JS Drawing
// 2022-02-14

//retrieve node in DOM via ID
var c = document.getElementById("slate")

//instantiate a CanvasRenderingContext2D Object
var ctx = c.getContext("2d");

//intit global state var
var mode = "rect";

//var toggleMode = function(e) {
var toggleMode = function(e) {
    console.log("toggling...")
    if ( ) {

    }
    else {

    }
}

var drawRect = function(e) {
    var mouseX = c.offsetX
    var mouseY = c.offsetY
    console.log("mouseclick registered at ", mouseX, mouseY)

}

//var drawCircle = functoin(e) {
var drawCircle = (e) => {

    console.log("mouseclick registered at ", mouseX, mouseY);

}

//var draw = function(e) {
var draw = (e) => {

}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    c.clearRect(0,0, c.clientWidth, c.clientHeight)
}

c.addEventListener("click", draw)
var bToggler = document.
bToggler. ;
var clearB = ;
clearB. ;