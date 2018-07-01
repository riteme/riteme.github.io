TOC_BEGIN = "<div class=\"toc\">"
TOC_END = "</div>"
TOC_TEMPLATE = """
<div class="mdl-card mdl-shadow--3dp" style="width: 100%">
  <div class="mdl-card__title mdl-card--border">
    <h4 class="mdl-card__title-text">目录</h4>
  </div>
  <div class="mdl-card__supporting-text">
    {toc}
  </div>
</div>
"""

def cut(content):
    if content.startswith(TOC_BEGIN):
        toc, remain = content.split(TOC_END, maxsplit=1)

        return (TOC_TEMPLATE.format(toc = toc + TOC_END), remain)
    else:
        return ("", content)
