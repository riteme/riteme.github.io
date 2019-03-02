/* loadJS from https://github.com/filamentgroup/loadJS/blob/master/loadJS.js */
(function( w ){
	var loadJS = function( src, cb, ordered ){
		"use strict";
		var tmp;
		var ref = w.document.getElementsByTagName( "script" )[ 0 ];
		var script = w.document.createElement( "script" );

		if (typeof(cb) === 'boolean') {
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

renderMath = function(e) {
    if (e == null) {
        e = $("#comments")[0];
    }

    mode = Cookies.get("math-renderer");

    try {
        if (renderer == 'mathjax') {
            renderWithMathJax(e);
        } else if (renderer == 'katex') {
            renderWithKaTeX(e);
        } else if (renderer == "katex&mathjax") {
            renderWithMathJax(e);
            renderWithKaTeX(e);
        }
    } catch {}
}

if (Cookies.get('math-renderer') == null) {
    Cookies.set('math-renderer', 'katex', { expires: 65536 });
}

startup = function() {
    renderer = Cookies.get('math-renderer');
    if (renderer == 'mathjax') {
        loadJS("/math-renderer/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML", function() {
            MathJax.Hub.Config( { tex2jax: { inlineMath: [['$','$']] }, "HTML-CSS": { scale: 95, fonts: ["TeX"] }, CommonHTML: { scale: 95, fonts: ["TeX"] }, SVG: { scale: 95, fonts: ["TeX"] } } );
            MathJax.Hub.Configured();
        });
    } else if (renderer == 'katex') {
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
                    MathJax.Hub.Config( { tex2jax: { inlineMath: [['$','$']] }, "HTML-CSS": { scale: 95 } } );
                    MathJax.Hub.Configured();
                });
            });
        });
    }

    if (renderer == 'mathjax') {
        document.mathopt.sel[0].checked = true;
    } else if (renderer == 'katex') {
        document.mathopt.sel[1].checked = true;
    } else if (renderer == "katex&mathjax") {
        document.mathopt.sel[2].checked = true;
    } else {
        console.log('No math formula renderer selected!');
    }

    document.mathopt.sel[0].onclick = function() {
        Cookies.set('math-renderer', 'mathjax', { expires: 65536 });
        location.reload();
    }

    document.mathopt.sel[1].onclick = function() {
        Cookies.set('math-renderer', 'katex', { expires: 65536 });
        location.reload();
    }

    document.mathopt.sel[2].onclick = function() {
        Cookies.set('math-renderer', 'katex&mathjax', { expires: 65536 });
        location.reload();
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
        target.classList.add("highlight")
        setTimeout(function () {
            target.classList.remove("highlight")
        }, 3000)
    }
}

function highlight_target() {
    if (document.location.hash.length)
        highlight(document.getElementById(document.location.hash.slice(1)))
}

window.addEventListener("load", highlight_target)
window.addEventListener("hashchange", highlight_target)