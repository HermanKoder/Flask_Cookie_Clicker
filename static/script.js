let cookies = 0;
    
function printCookies() {
    document.getElementById("showCookies").innerHTML = cookies + " Cookies In Stock";
}

function clickCookie() {
    cookies += 1;
    printCookies();
    fetch('/update_cookies', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({cookies: cookies})
    });
}