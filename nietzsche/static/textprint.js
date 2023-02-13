var typingText = document.querySelector('#result').content;

var typingBool = false;
var typingIdx = 0;

typingText = typingText.split("");

if (typingBool == false && typingText != ''){
    typingBool = true;
    var tyInt = setInterval(typing, 70);
}

function typing(){
    if (typingIdx < typingText.length){
        $('.result-text').append(typingText[typingIdx]);
        typingIdx++;
    } else {
        clearInterval(tyInt);
    }
}
