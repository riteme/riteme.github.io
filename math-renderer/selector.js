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

    if (renderer == 'mathjax') {
        renderWithMathJax(e);
    } else if (renderer == 'katex') {
        renderWithKaTeX(e);
    } else if (renderer == "katex&mathjax") {
        renderWithMathJax(e);
        renderWithKaTeX(e);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    if (Cookies.get('math-renderer') == null) {
        Cookies.set('math-renderer', 'mathjax', { expires: 65536 });
    }

    renderer = Cookies.get('math-renderer');

    if (renderer == 'mathjax') {
        document.mathopt.sel[0].checked = true;
        MathJax.Hub.Configured();
    } else if (renderer == 'katex') {
        document.mathopt.sel[1].checked = true;
        renderWithKaTeX(document.body);
    } else if (renderer == "katex&mathjax") {
        document.mathopt.sel[2].checked = true;
        MathJax.Hub.Configured();
        renderWithKaTeX(document.body);
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
