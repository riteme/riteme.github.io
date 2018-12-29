function jump(target) {
    if (target) window.scrollTo({top: target.offsetTop - 80, behavior: "smooth"})
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