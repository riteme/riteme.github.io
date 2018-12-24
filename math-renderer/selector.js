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
    Cookies.set('math-renderer', 'mathjax', { expires: 65536 });
}

renderer = Cookies.get('math-renderer');
if (renderer == 'mathjax') {
    loadJS("/math-renderer/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML", function() {
        MathJax.Hub.Config( { tex2jax: { inlineMath: [['$','$']] }, "HTML-CSS": { scale: 95 } } );
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

document.addEventListener("DOMContentLoaded", function() {
    renderer = Cookies.get('math-renderer');
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
});
