SCROLL_OFFSET = 30

function getPositionTop(x) {
    cur = 0
    do {
        cur += x.offsetTop
    } while (x = x.offsetParent)
    return cur
}

function jump(target) {
    if (target) {
        window.scrollTo({top: getPositionTop(target) - SCROLL_OFFSET, behavior: "smooth"})
        target.classList.add("highlight")
        setTimeout(function () {
            target.classList.remove("highlight")
        }, 3500)
    }
}

function jumper(id) {
    return function () {
        target = document.getElementById(id)
        jump(target)
        return false
    }
}

process_jumpers = function () {
    li = document.querySelectorAll("a[href^='#']")
    for (i = 0; i < li.length; i++) {
        a = li[i]
        a.onclick = jumper(a.getAttribute("href").slice(1))
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", process_jumpers);
} else {
    process_jumpers();
}

window.addEventListener("load", function () {
    if (document.location.hash.length)
        jump(document.getElementById(document.location.hash.slice(1)))
})