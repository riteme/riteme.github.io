import re
import hashlib

import markdown.extensions.codehilite

from markdown import Extension
from markdown.inlinepatterns import \
    LinkPattern, ReferencePattern, AutolinkPattern, AutomailPattern, \
    LINK_RE, REFERENCE_RE, SHORT_REF_RE, AUTOLINK_RE, AUTOMAIL_RE
from markdown.postprocessors import Postprocessor


TOC_BEGIN = "<div class=\"toc\">"
TOC_END = "</div>"
TOC_TAIL = '<ul><li><a href="#comments">评论区</a></li></ul>'
TOC_TEMPLATE = """
<div class="mdl-card mdl-shadow--2dp sidebar-card">
  <div class="mdl-card__actions sidebar-title">目录</div>
  <div class="mdl-card__supporting-text">
    {toc}
  </div>
</div>
<br/>
"""


# LaTeX Extension
class LaTeXPattern(markdown.inlinepatterns.Pattern):
    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(
            self,
            r'(?<!\\)(\$\$?)(.+?)\2'
        )

    def handleMatch(self, m):
        node = markdown.util.etree.Element('tex')
        node.text = markdown.util.AtomicString(
            m.group(2) + m.group(3) + m.group(2))
        return node


class LaTeXExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important in
        # LaTeX
        md.inlinePatterns.add('tex', LaTeXPattern(), '<escape')

def latex_friendly(configs=[]):
    return LaTeXExtension(configs)

# New Tab Extension
class NewTabMixin(object):
    def handleMatch(self, match):
        elem = super(NewTabMixin, self).handleMatch(match)
        if elem is not None and not elem.get('href').startswith('#'):
            elem.set('target', '_blank')
        return elem

class NewTabLinkPattern(NewTabMixin, LinkPattern):
    pass

class NewTabReferencePattern(NewTabMixin, ReferencePattern):
    pass

class NewTabAutolinkPattern(NewTabMixin, AutolinkPattern):
    pass

class NewTabAutomailPattern(NewTabMixin, AutomailPattern):
    pass

class NewTabExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns['link'] = \
            NewTabLinkPattern(LINK_RE, md)
        md.inlinePatterns['reference'] = \
            NewTabReferencePattern(REFERENCE_RE, md)
        md.inlinePatterns['short_reference'] = \
            NewTabReferencePattern(SHORT_REF_RE, md)
        md.inlinePatterns['autolink'] = \
            NewTabAutolinkPattern(AUTOLINK_RE, md)
        md.inlinePatterns['automail'] = \
            NewTabAutomailPattern(AUTOMAIL_RE, md)

def new_tab_on_links(configs=None):
    if configs is None:
        configs = {}
    return NewTabExtension(configs=configs)

# Tasklist Extension
def tasklist(configs=None):
    if configs is None:
        return ChecklistExtension()
    else:
        return ChecklistExtension(configs=configs)

class ChecklistExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('checklist', ChecklistPostprocessor(md),
                              '>raw_html')

class ChecklistPostprocessor(Postprocessor):
    """
    adds checklist class to list element
    """
    pattern = re.compile(r'<li>\[([ Xx])\]')

    def run(self, html):
        html = re.sub(self.pattern, self._convert_checkbox, html)
        before = '<ul>\n<li><input type="checkbox"'
        after = before.replace('<ul>', '<ul class="checklist">')
        return html.replace(before, after)

    def _convert_checkbox(self, match):
        state = match.group(1)
        checked = ' checked' if state != ' ' else ''
        return '<li><input type="checkbox" disabled%s>' % checked

# DelIns Extension
from markdown.inlinepatterns import SimpleTagPattern

DEL_RE = r"(\~\~)(.+?)(\~\~)"
INS_RE = r"(\+\+)(.+?)(\+\+)"

class DelInsExtension(markdown.extensions.Extension):

    """Adds del_ins extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.inlinePatterns.add(
            'del', SimpleTagPattern(DEL_RE, 'del'), '<not_strong')
        md.inlinePatterns.add(
            'ins', SimpleTagPattern(INS_RE, 'ins'), '<not_strong')

def del_ins(configs={}):
    return DelInsExtension(configs=dict(configs))

def hash(obj):
    obj = str(obj).encode("ascii")
    return hashlib.md5(obj).hexdigest()

def escape_string(s):
    S = []
    for c in s:
        if c in "\n\r":
            S.append("\\n")
        elif c == "\t":
            S.append("\\t")
        elif c == "\"":
            S.append("\\\"")
        elif c == "\\":
            S.append("\\\\")
        elif c == "%":
            S.append("% ")
        elif ord(c) == 8203:  # ZERO WIDTH SAPCE, it fucks KaTeX
            pass
        else:
            S.append(c)

    return "".join(S)

def convert_time(m):
    h = m // 60
    m %= 60
    if h:
        return '%s 小时 %s 分钟' % (h, m)
    return '%s 分钟' % m

def generate_time(year, month, day):
    return "{}.{:0>2}.{:0>2}".format(year, month, day)

class Tag(object):
    """表示一个标签"""

    def __init__(self, text):
        super(Tag, self).__init__()
        self.text = text
        self._style = "<a href=\"/search.html?q={tag}\"><span class=\"label\">{tag}</span></a>"

    def __str__(self):
        return self._style.format(tag=self.text)

class TagGroup(object):
    """表示一个标签组"""

    def __init__(self):
        super(TagGroup, self).__init__()
        self.tags = []

    def __str__(self):
        code = [str(tag) for tag in self.tags]

        return " ".join(code)

    def append(self, text):
        if text.strip() == "":
            return

        self.tags.append(Tag(text))

def cut_toc(content):
    if content.startswith(TOC_BEGIN):
        toc, remain = content.split(TOC_END, maxsplit=1)
        return (TOC_TEMPLATE.format(toc = toc + TOC_TAIL + TOC_END), remain)
    else:
        return ("", content)
