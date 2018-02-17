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
        renderMathInElement(
            document.body,
            options = {
                delimiters: [
                    { left: "$$", right: "$$", display: true },
                    { left: "$", right: "$", display: false }
                ]
            }
        )
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
});
