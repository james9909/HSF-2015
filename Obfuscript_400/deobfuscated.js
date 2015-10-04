var _0x6cab = ["", "controlPanel", "getElementById", "userString", "userNumber", "userBool", "onclick", "b1", "b2", "thank mr. skeletal", "b3", "fromCharCode", "b4", "b5", "getTime", "length", "c", "split", "random", "floor", "b6", "b7", "b8", "b9", "b10", "b11", "b12", "divr", "join", "color", "style", "helper", "blue", "innerHTML", "Correct!", "zIndex", "cancan", "723", "initialize", "run", "addCat", "slice", "wat", "sort", "j", " ", "replace", "ct", "gh", "[", "4", "map", "10", "0xf", "string",
    "0"];
var keyString = "";
var keyNumber = 0;
var keyBool = false;
var counter = 0;
var controlPanel = document["getElementById"]("controlPanel");
var userString = document["getElementById"]("userString");
var userNumber = document["getElementById"]("userNumber");
var userBool = document["getElementById"]("userBool");
document["getElementById"]("b1")["onclick"] = function() {
    counter += 1;
};
document["getElementById"]("b2")["onclick"] = function() {
    updateKey(0, keyString + "thank mr. skeletal");
};
document["getElementById"]("b3")["onclick"] = function() {
    updateKey(0, "MEOW");
};
document["getElementById"]("b4")["onclick"] = function() {
    updateKey(1, keyNumber << counter);
};
document["getElementById"]("b3")["onclick"] = function() {
    updateKey(1, (new Date)["getTime"]() % 2 == 0 ? (new Date)["getTime"]() : Math["floor"](Math["random"]() * 30));
};
document["getElementById"]("b6")["onclick"] = function() {
    updateKey(0, keyString + "number"[counter]);
};
document["getElementById"]("b7")["onclick"] = function() {
    updateKey(1, parseInt(keyNumber) - 1);
};
document["getElementById"]("b8")["onclick"] = function() {
    updateKey(0, keyString + String["fromCharCode"](counter));
};
document["getElementById"]("b9")["onclick"] = function() {
    counter = 0;
};
document["getElementById"]("b10")["onclick"] = function() {
    updateKey(2, keyBool || (Math["floor"](Math["random"]() * 100) % 2 == 0 || !keyBool));
};
document["getElementById"]("b11")["onclick"] = function() {
    updateKey(0, keyString + "[object Object]"[counter]);
};
document["getElementById"]("b12")["onclick"] = function() {
    updateKey(1, parseInt(keyNumber) / 2);
};
function updateKey(recurring, m1) {
    switch(recurring) {
        case 0:
            keyString = m1;
            userString["innerHTML"] = m1;
            break;
        case 1:
            keyNumber = Math["floor"](parseInt(m1));
            userNumber["innerHTML"] = "" + Math["floor"](parseInt(m1));
            break;
        case 2:
            keyBool = m1;
            userBool["innerHTML"] = "" + m1;
            break;
    }
    if (keyString == "truest10fr34-511") {
        if ((keyNumber % 2 == 0) &&
                (keyNumber % 24 == 18) &&
                (keyNumber > 0) &&
                (~keyNumber < 285)))) {
               if (keyBool == false) {
                   // le flag
               } else {
                   wrong();
               }
           } else {
               wrong();
           }
    } else {
        wrong();
    }
};
