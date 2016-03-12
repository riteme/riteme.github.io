#!/usr/bin/env python3
# 用于生成单个页面

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import hashlib

import info
import tag
import parser
import breadcrumb
import navigater

import markdown
import markdown.extensions.codehilite

from markdown import Extension
from markdown.inlinepatterns import \
    LinkPattern, ReferencePattern, AutolinkPattern, AutomailPattern, \
    LINK_RE, REFERENCE_RE, SHORT_REF_RE, AUTOLINK_RE, AUTOMAIL_RE

import re

# from markdown.extensions import Extension
# from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor


# Mathjax Extension
class MathJaxPattern(markdown.inlinepatterns.Pattern):

    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(
            self,
            r'(?<!\\)(\$\$?)(.+?)\2'
        )

    def handleMatch(self, m):
        node = markdown.util.etree.Element('mathjax')
        node.text = markdown.util.AtomicString(
            m.group(2) + m.group(3) + m.group(2))
        return node


class MathJaxExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important in
        # LaTeX
        md.inlinePatterns.add('mathjax', MathJaxPattern(), '<escape')


def latex_friendly(configs=[]):
    return MathJaxExtension(configs)

# New Tab Extension
# pylint: disable=invalid-name, too-few-public-methods


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


MARKDOWN_EXT = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
    "markdown.extensions.codehilite",
    "markdown.extensions.toc",
    "markdown.extensions.smart_strong",
    latex_friendly(),
    new_tab_on_links(),
    tasklist()
]

MARKDOWN_CONFIG = {
    "markdown.extensions.codehilite": {
        "linenums": True,
        "guess_lang": True
    }
}


def generate(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File not found")

    reader = parser.Parser()
    reader.load_syntax(parser.PanelBeginSyntax)
    reader.load_syntax(parser.PanelEndSyntax)
    with open(filepath) as md:
        mdinfo, mdtext, temp = reader.process(md)

    if temp:
        print("(warn) This is a temporary post. Stopped.")
        return

    title = info.generate_title(mdinfo["title"])

    create_time = info.generate_time(
        *mdinfo["create"].split(".")
    )

    modified_time = info.generate_time(
        *mdinfo["modified"].split(".")
    )

    tags = tag.TagGroup()
    for x in mdinfo["tags"].split(" "):
        tags.append(x)

    content = "\n".join(mdtext)
    content = markdown.markdown(
        content,
        extensions=MARKDOWN_EXT,
        extension_configs=MARKDOWN_CONFIG
    )

    navigater.handle("favicon", "favicon.png")
    navigater.handle("home", "index.html")
    navigater.handle("css", "css/site.css")
    navigater.handle("mathjax", "mathjax/MathJax.js")
    navigater.home_folder = os.path.dirname(filepath)

    mathjax = navigater.get_path("mathjax")
    favicon = navigater.get_path("favicon")
    css = navigater.get_path("css")
    home = navigater.get_path("home")

    pagetitle = mdinfo["title"].strip()
    pagekey = hashlib.md5(pagetitle.encode("utf8")).hexdigest()
    pageurl = "http://riteme.github.io/" + \
        os.path.relpath(os.path.abspath(filepath), start=os.path.abspath("."))[
            :-3] + ".html"
    duoshuo = """<script type="text/javascript">
var duoshuoQuery = {short_name:"riteme"};
(function() {
    var ds = document.createElement('script');
    ds.type = 'text/javascript';ds.async = true;
    ds.src = (
        document.location.protocol == 'https:' ? 'https:' : 'http:'
    ) + '//static.duoshuo.com/embed.js';
    ds.charset = 'UTF-8';
    (document.getElementsByTagName('head')[0]
     || document.getElementsByTagName('body')[0]).appendChild(ds);
})();
</script>"""

    bread = breadcrumb.Breadcrumb()
    relative = os.path.relpath(
        os.path.dirname(os.path.abspath(filepath)),
        start=os.path.abspath(".")
    )
    nodes = [x.upper()
             for x in os.path.split(relative) if x.strip() not in ["", "."]]
    bread.append("HOME", home)
    for x in nodes:
        bread.append(x, "#")

    bread.append(mdinfo["title"].upper(), "#", is_alive=True)

    with open("template.html") as ftemplate:
        template = ftemplate.read()

    with open("printable-template.html") as fprintable:
        printable = fprintable.read()

    new_file = os.path.splitext(filepath)[0] + ".html"
    new_printable = os.path.splitext(filepath)[0] + "-printable.html"
    printable_path = os.path.basename(new_printable)

    with open(new_file, "w") as writer:
        writer.write(template.format(
            title=title,
            create=create_time,
            modified=modified_time,
            tags=str(tags),
            content=content,
            breadcrumb=str(bread),
            favicon=favicon,
            mathjax=mathjax,
            css=css,
            home=home,
            page_key=pagekey,
            page_title=pagetitle,
            page_url=pageurl,
            duoshuo_code=duoshuo,
            printable=printable_path
        ))

    with open(new_printable, "w") as writer:
        writer.write(printable.format(
            title=title,
            content=content,
            mathjax=mathjax,
            css=css
        ))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No input file.")
        exit(-1)

    filepath = sys.argv[1]
    generate(filepath)
