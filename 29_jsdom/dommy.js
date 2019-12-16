// By Kevin Cai and Henry Liu <team halfApress>
// SoftDev1 pd9
// K29 -- jsdom
// 2019-12-11

var baseHeader = document.getElementById("h").innerHTML;

var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e['target']['innerHTML'];
};

var removeItem = function(e) {
    // get list then remove target child
    document.getElementById('thelist').removeChild(e['target'])
};

var restoreText = function(e){
    // header does back to inital state
    var h = document.getElementById("h")
    h.innerHTML = baseHeader;
};

var lis = document.getElementsByTagName("li");

for (var i=0; i < lis.length; ++i) {
    // map events to funcs
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', restoreText);
    lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
    // adds new element to list
    var list = document.getElementById('thelist');
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', restoreText);
    item.addEventListener('click', removeItem);
    list.appendChild( item );
};

// every time button with id 'b' is pressed, add new item
var button = document.getElementById("b");
button.addEventListener('click', addItem);

//Dynamic Programming ftw
var gudFib = function(e){
    var fblist = document.getElementById('fiblist');
    var numbers = fblist.childNodes;
    var length = numbers.length;
    var output = document.createElement('li');
    //console.log(length);
    //if not enough numbers in the list, default to 1. Otherwise add the two ending ones
    output.innerHTML = (length < 3) ? 1 : parseInt(numbers[length - 1].innerHTML , 10) + parseInt(numbers[length - 2].innerHTML, 10);
    fblist.appendChild(output); // adding item
};

var fb = document.getElementById("fb");
fb.addEventListener("click", gudFib);
