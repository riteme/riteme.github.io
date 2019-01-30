SCROLL_OFFSET = 80

function getPositionTop(x) {
    cur = 0
    do {
        cur += x.offsetTop
    } while (x = x.offsetParent)
    return cur
}

function jump(target) {
    if (target) window.scrollTo({top: getPositionTop(target) - SCROLL_OFFSET, behavior: "smooth"})
}

function jumper(id) {
    return function () {
        target = document.getElementById(id)
        jump(target)
        return false
    }
}

window.addEventListener("load", function () {
    li = document.querySelectorAll("a[href^='#']")
    for (i = 0; i < li.length; i++) {
        a = li[i]
        a.onclick = jumper(a.getAttribute("href").slice(1))
    }
    jump(document.querySelector(":target"))
})