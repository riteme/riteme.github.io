TOC_BEGIN = "<div class=\"toc\">"
TOC_END = "</div>"

def cut(content):
    if content.startswith(TOC_BEGIN):
        toc, remain = content.split(TOC_END, maxsplit=1)

        return (toc + TOC_END, remain)
    else:
        return ("", content)
