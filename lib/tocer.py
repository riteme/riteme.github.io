TOC_BEGIN = "<div class=\"toc\">"
TOC_END = "</div>"
TOC_TEMPLATE = """
<div class="mdl-card mdl-shadow--3dp sidebar-card">
  <div class="mdl-card__actions sidebar-title">目录</div>
  <div class="mdl-card__supporting-text">
    {toc}
  </div>
</div>
<br/>
"""

def cut(content):
    if content.startswith(TOC_BEGIN):
        toc, remain = content.split(TOC_END, maxsplit=1)

        return (TOC_TEMPLATE.format(toc = toc + TOC_END), remain)
    else:
        return ("", content)
