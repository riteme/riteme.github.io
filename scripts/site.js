/* loadJS from https://github.com/filamentgroup/loadJS/blob/master/loadJS.js */
(function( w ){
	var loadJS = function( src, cb, ordered ){
		"use strict";
		var tmp;
		var ref = w.document.getElementsByTagName( "script" )[ 0 ];
		var script = w.document.createElement( "script" );

		if (typeof(cb) === "boolean") {
			tmp = ordered;
			ordered = cb;
			cb = tmp;
		}

		script.src = src;
		script.async = !ordered;
		ref.parentNode.insertBefore( script, ref );

		if (cb && typeof(cb) === "function") {
			script.onload = cb;
		}
		return script;
	};
	// commonjs
	if( typeof module !== "undefined" ){
		module.exports = loadJS;
	}
	else {
		w.loadJS = loadJS;
	}
}( typeof global !== "undefined" ? global : this ));

renderWithMathJax = function(e) {
    MathJax.Hub.Queue(["Typeset", MathJax.Hub, e]);
}

renderWithKaTeX = function(e) {
    renderMathInElement(
        e, options = {
            delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "$", right: "$", display: false }
            ]
        }
    );
}

function mathAlignLeft(target) {
    target.style["text-align"] = "left"
    target.style["padding-left"] = "4em"
}

function mathAlignCenter(target) {
    target.style["text-align"] = "center"
    target.style["padding-left"] = "0"
}

function toggler(target) {
    return function() {
        if (target.style["text-align"] == "left") mathAlignCenter(target)
        else mathAlignLeft(target)
    }
}

function refreshMathAlign(e) {
    if (e) {
        if (!e.classList.contains(".katex-display")) return
        e = tex[i].getElementsByClassName("katex")[0]
        if (math_align == "center") mathAlignCenter(e)
        else mathAlignLeft(e)
    } else {
        math_align = Cookies.get("math-align")
        tex = document.querySelectorAll("tex .katex-display")
        if (!tex) return
        for (i = 0; i < tex.length; i++) {
            e = tex[i].getElementsByClassName("katex")[0]
            if (math_align == "center") mathAlignCenter(e)
            else mathAlignLeft(e)
        }
    }
}

function registerToggler(e) {
    if (e.classList.contains(".katex-display")) tex = e
    else tex = e.querySelectorAll("tex .katex-display")
    if (!tex) return
    for (i = 0; i < tex.length; i++)
        tex[i].onclick = function() {
            target = this.getElementsByClassName("katex")[0]
            target.onclick = toggler(target)
        }
}

function renderMath(e) {
    if (e == null) {
        e = $("#comments")[0];
    }

    mode = Cookies.get("math-renderer");

    try {
        if (renderer == "mathjax") {
            renderWithMathJax(e);
        } else if (renderer == "katex") {
            renderWithKaTeX(e);
        } else if (renderer == "katex&mathjax") {
            renderWithKaTeX(e);
            renderWithMathJax(e);
        }
    } catch {}
}

if (Cookies.get("math-renderer") == null)
    Cookies.set("math-renderer", "katex", { expires: 65536 })
if (Cookies.get("math-align") == null)
    Cookies.set("math-align", "left", { expires: 65536})

function startup() {
    renderer = Cookies.get("math-renderer")
    if (renderer == "mathjax") {
        loadJS("/math-renderer/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML", function() {
            MathJax.Hub.Config( { tex2jax: { inlineMath: [["$","$"]] }, "HTML-CSS": { scale: 95, fonts: ["TeX"] }, CommonHTML: { scale: 95, fonts: ["TeX"] }, SVG: { scale: 95, fonts: ["TeX"] } } );
            MathJax.Hub.Configured();
        });
    } else if (renderer == "katex") {
        loadJS("/math-renderer/katex/katex.min.js", function() {
            loadJS("/math-renderer/katex/auto-render.min.js", function() {
                renderWithKaTeX(document.body);
            });
        });
    } else if (renderer == "katex&mathjax") {
        loadJS("/math-renderer/katex/katex.min.js", function() {
            loadJS("/math-renderer/katex/auto-render.min.js", function() {
                renderWithKaTeX(document.body);
                loadJS("/math-renderer/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML", function() {
                    MathJax.Hub.Config( { tex2jax: { inlineMath: [["$","$"]] }, "HTML-CSS": { scale: 95 } } );
                    MathJax.Hub.Configured();
                });
            });
        });
    }

    // Math Formula Rendering
    var observer = new MutationObserver(function(muts) {
        muts.forEach(function(mut) {
            for (i = 0; i < mut.addedNodes.length; i++) {
                var x = mut.addedNodes[i]
                if (x.nodeName != "#text")
                    renderMath(x)
            }
        })
    })
    containers = document.getElementsByClassName("article")
    for (i = 0; i < containers.length; i++)
        observer.observe(containers[i], {childList: true, subtree: true})

    if (document.mathopt) {
        if (renderer == "mathjax") {
            document.mathopt.sel[0].checked = true;
        } else if (renderer == "katex") {
            document.mathopt.sel[1].checked = true;
        } else if (renderer == "katex&mathjax") {
            document.mathopt.sel[2].checked = true;
        } else {
            console.log("No math formula renderer selected!");
        }

        document.mathopt.sel[0].onclick = function() {
            Cookies.set("math-renderer", "mathjax", { expires: 65536 });
            location.reload();
        }

        document.mathopt.sel[1].onclick = function() {
            Cookies.set("math-renderer", "katex", { expires: 65536 });
            location.reload();
        }

        document.mathopt.sel[2].onclick = function() {
            Cookies.set("math-renderer", "katex&mathjax", { expires: 65536 });
            location.reload();
        }
    }

    mathopt_align = document.getElementById("mathopt-align")
    if (mathopt_align) {
        math_align = Cookies.get("math-align")
        if (math_align == "center") mathopt_align.checked = true
        mathopt_align.onclick = function() {
            if (math_align == "center") Cookies.set("math-align", "left", { expires: 65536})
            else Cookies.set("math-align", "center", { expires: 65536})
            refreshMathAlign(null)
        }
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startup);
} else {
    startup();
}

// Target Highlighting
function isScrolledIntoHalfView(x) {
    var rect = x.getBoundingClientRect();
    return (rect.top >= 0) && (rect.bottom <= window.innerHeight / 3);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

async function highlight(target) {
    if (target) {
        while (!isScrolledIntoHalfView(target))
            await sleep(200)
        target.classList.add("jump-highlight")
        setTimeout(function () {
            target.classList.remove("jump-highlight")
        }, 3000)
    }
}

function highlight_target() {
    if (document.location.hash.length)
        highlight(document.getElementById(document.location.hash.slice(1)))
}

window.addEventListener("load", function() {
    highlight_target()
    registerToggler(document.body)
    refreshMathAlign(null)
})
window.addEventListener("hashchange", highlight_target)
