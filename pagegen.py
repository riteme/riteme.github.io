#!/usr/bin/env python3
# 用于生成单个页面

import os

import info
import tag
import parser
import breadcrumb
import navigater

import markdown


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


def makeExtension(configs=[]):
    return MathJaxExtension(configs)


MARKDOWN_EXT = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
    "markdown.extensions.codehilite",
    "markdown.extensions.toc",
    "markdown.extensions.smart_strong",
    makeExtension()
]


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
        exit(0)

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
    content = markdown.markdown(content, extensions=MARKDOWN_EXT)

    navigater.handle("favicon", "favicon.png")
    navigater.handle("home", "index.html")
    navigater.handle("css", "css/site.css")
    navigater.home_folder = os.path.dirname(filepath)

    mathjax = navigater.get_mathjax()
    favicon = navigater.get_path("favicon")
    css = navigater.get_path("css")
    home = navigater.get_path("home")

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

    bread.append(title.upper(), "#", is_alive=True)

    with open("template.html") as ftemplate:
        template = ftemplate.read()

    new_file = os.path.splitext(filepath)[0] + ".html"
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
            home=home
        ))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No input file.")
        exit(-1)

    filepath = sys.argv[1]
    generate(filepath)
