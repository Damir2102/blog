"use strict"

function showActiveLink(menu) {
    const links = document.getElementById(menu)
        .querySelectorAll("a.nav-link")
    const pageURL = document.location.href
    for (const link of links){
        if(link.href=== pageURL){
            link.classList.add("active")
        }
    }
}


showActiveLink("menu")