#!/usr/bin/env python3
# 用于生成单个页面

import os

import info
import tag
import parser
import breadcrumb
import navigater

import markdown2

MARKDOWN_EXT = ["code-friendly", "fenced-code-blocks", "footnotes", "tables"]


def generate(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File not found")

    reader = parser.Parser()
    reader.load_syntax(parser.PanelBeginSyntax)
    reader.load_syntax(parser.PanelEndSyntax)
    with open(filepath) as md:
        mdinfo, mdtext = reader.process(md)

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
    content = markdown2.markdown(content, extras=MARKDOWN_EXT)

    navigater.handle("favicon", "favicon.png")
    navigater.handle("home", "index.html")
    navigater.handle("strapdown", "strapdown/strapdown.js")
    navigater.home_folder = os.path.dirname(filepath)

    mathjax = navigater.get_mathjax()
    favicon = navigater.get_path("favicon")
    strapdown = navigater.get_path("strapdown")
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

    bread.append("DETAILS", "#", is_alive=True)

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
            strapdown=strapdown,
            home=home
        ))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("No input file.")
        exit(-1)

    filepath = sys.argv[1]
    generate(filepath)
