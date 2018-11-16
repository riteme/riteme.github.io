#!/usr/bin/env python3
# 用于生成单个页面

from __future__ import absolute_import
from __future__ import unicode_literals

import os
import hashlib

import lib.info as info
import lib.tag as tag
import lib.tocer as tocer
import lib.parser as parser
import lib.navigater as navigater

import bs4

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

WORDS_PER_MINUTE = 250
BEAUTIFUL_SOUP_PARSER = "lxml"
GITHUB_LOCATION = "https://github.com/riteme/riteme.github.io/blob/master"

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

MARKDOWN_EXT = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
    "markdown.extensions.codehilite",
    "markdown.extensions.toc",
    "markdown.extensions.smart_strong",
    "markdown.extensions.nl2br",
    "markdown.extensions.meta",
    "markdown.extensions.smarty",
    latex_friendly(),
    # new_tab_on_links(),
    tasklist(),
    del_ins()
]

MARKDOWN_CONFIG = {
    "markdown.extensions.codehilite": {
        "linenums": True,
        "guess_lang": False
    }
}


def convert_string(s):
    S = []
    for c in s:
        if c in "\n\r":
            S.append("<br/>")
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

def generate(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File not found")

    reader = parser.Parser()
    reader.load_syntax(parser.PanelBeginSyntax)
    reader.load_syntax(parser.PanelEndSyntax)
    reader.load_syntax(parser.IncludeSyntax)
    converter = markdown.Markdown(
        extensions=MARKDOWN_EXT,
        extension_configs=MARKDOWN_CONFIG
    )
    with open(filepath) as md:
        content, temp = reader.process(md.read())
        if temp:
            print("(warn) This is a temporary post. Stopped.")
            return

        content = content.replace(chr(8203), '')
        content = converter.convert(content)

    metalost = False
    try:
        mdinfo = converter.Meta
    except AttributeError:
        metalost = True

    if metalost or len(mdinfo) == 0:
        print("(info) No metadata. Skipped.")
        return

    toc, content = tocer.cut(content)

    title = info.generate_title(mdinfo["title"][0])

    create_time = info.generate_time(
        *mdinfo["create"][0].split(".")
    )

    modified_time = info.generate_time(
        *mdinfo["modified"][0].split(".")
    )

    tags = tag.TagGroup()
    for x in mdinfo["tags"]:
        tags.append(x)

    # 生成索引信息
    index_title = convert_string(title)
    index_text = convert_string(bs4.BeautifulSoup(content, BEAUTIFUL_SOUP_PARSER).text)
    index_tags = mdinfo["tags"]
    navigater.handle("myself", filepath)
    navigater.home_folder = os.path.abspath(".")
    index_url = navigater.get_path("myself")
    index_url = index_url.rsplit(".", 1)[0] + ".html"
    filename = os.path.basename(filepath)
    words = len(index_text)

    # 处理特殊信息
    pagetitle = mdinfo["title"][0].strip().replace("\"", " ")
    pagekey = hashlib.md5(pagetitle.encode("utf8")).hexdigest()
    pageurl = "http://riteme.github.io/" + os.path.relpath(
        os.path.abspath(filepath), start=os.path.abspath("."))[
        :-3] + ".html"

    # 写入文件
    with open("template.html") as ftemplate:
        template = ftemplate.read()

    new_file = os.path.splitext(filepath)[0] + ".html"

    with open(new_file, "w") as writer:
        writer.write(template.format(
            title=title,
            create=create_time,
            modified=modified_time,
            time='%s 字 / 约 %s' % (words, convert_time(words // WORDS_PER_MINUTE)),
            tags=str(tags),
            toc=toc,
            content=content,
            page_key=pagekey,
            page_title=pagetitle,
            page_url=pageurl,
            mdname=filename,
            github_location=os.path.join(GITHUB_LOCATION, os.path.dirname(index_url), filename)
        ))

    # 返回索引信息
    return (index_title, index_text, index_tags, index_url)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No input file.")
        exit(-1)

    filepath = sys.argv[1]
    generate(filepath)
