function jumper(id) {
    return function () {
        target = document.getElementById(id)
        window.scrollTo({top: target.offsetTop - 80, behavior: "smooth"})
        return false
    }
}

window.addEventListener("load", function () {
    li = document.querySelectorAll("a[href^='#']")
    for (i = 0; i < li.length; i++) {
        a = li[i]
        a.onclick = jumper(a.getAttribute("href").slice(1))
        a.setAttribute("href", "#")
    }
})