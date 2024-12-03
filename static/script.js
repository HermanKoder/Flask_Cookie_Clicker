
let Cookies = 0;

printCookies()

function printCookies(){
    document.getElementById("showCookies").innerHTML = Cookies + " Cookies In Stock"
}

function clickCookie(){
    Cookies = Cookies + 1
    printCookies()
}