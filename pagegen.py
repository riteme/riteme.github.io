#!/usr/bin/env python3
# 用于生成单个页面

import os
import hashlib
import argparse
import datetime

import lib.info as info
import lib.tag as tag
import lib.tocer as tocer
import lib.parser as parser
import lib.navigater as navigater
import lib.logging as logging
from lib.logging import warn
from lib.utility import *
from preferences import *

import bs4
import markdown
try:
    from css_html_js_minify import html_minify
except:
    html_minify = None


# 初始化 Markdown 扩展
for i in range(len(MARKDOWN_EXTENSIONS)):
    if MARKDOWN_EXTENSIONS[i].startswith("#"):
        MARKDOWN_EXTENSIONS[i] = eval("%s()" % MARKDOWN_EXTENSIONS[i][1:])

preproc = parser.Parser()
preproc.load_syntax(parser.PanelBeginSyntax)
preproc.load_syntax(parser.PanelEndSyntax)
preproc.load_syntax(parser.IncludeSyntax)

def generate(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File not found")

    parser = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_CONFIG
    )
    with open(filepath) as md:
        content, temp = preproc.process(md.read())
        if temp:
            warn("This is a temporary post. Skipped.")
            return
        content = content.replace(chr(8203), '')
        content = parser.convert(content)

    metalost = False
    try:
        mdinfo = parser.Meta
    except AttributeError:
        metalost = True

    if metalost or len(mdinfo) == 0:
        warn("No metadata. Skipped.")
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
    index_title = escape_string(title)
    index_text = escape_string(bs4.BeautifulSoup(content, BEAUTIFUL_SOUP_PARSER).text)
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
    pageurl = SITE_DOMAIN + os.path.relpath(
        os.path.abspath(filepath), start=os.path.abspath("."))[
        :-3] + ".html"

    # 写入文件
    template_file = "templates/%s.html" % DEFAULT_TEMPLATE
    if "template" in mdinfo:
        template_file = "templates/%s.html" % mdinfo["template"][0]
    with open(template_file) as ftemplate:
        template = ftemplate.read()

    new_file = os.path.splitext(filepath)[0] + ".html"
    with open(new_file, "w") as writer:
        html_dom = template.format(
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
        )
        if html_minify:
            writer.write(html_minify(html_dom))
        else:
            writer.write(html_dom)

    # 返回索引信息
    if "index" not in mdinfo or mdinfo["index"][0] in ['true', 'True', '1']:
        return (index_title, index_text, index_tags, index_url)
    return index_title


if __name__ == "__main__":
    argpr = argparse.ArgumentParser(description="Convert specific Markdown file to HTML page")
    log_group = argpr.add_mutually_exclusive_group()
    log_group.add_argument("-v", "--verbose", action="count", help="show more messages", default=0)
    log_group.add_argument("-q", "--quiet", action="count", help="show less messages", default=0)
    argpr.add_argument("-n", "--new", action="store_true", help="set to create a new document instead of converting")
    argpr.add_argument("file", help="path to file that will be converted")

    args = argpr.parse_args()
    if args.verbose:
        logging.LOGGING_LEVEL = logging.LoggingLevel.DEBUG
    else:
        levels = [logging.LoggingLevel.INFO, logging.LoggingLevel.WARN,
            logging.LoggingLevel.ERROR, logging.LoggingLevel.FATAL, logging.LoggingLevel.NONE]
        logging.LOGGING_LEVEL = levels[min(args.quiet, len(levels) - 1)]

    if args.new:
        date = datetime.datetime.now()
        now = "%s.%s.%s" % (date.year, date.month, date.day)
        target = os.path.join(BLOG, now.replace('.', '-'))
        if not os.path.exists(target):
            os.mkdir(target)
        target = os.path.join(target, "%s.md" % args.file)
        with open(DEFAULT_DOCUMENT, "r") as reader:
            content = reader.read()
        if os.path.exists(target):
            warn("'%s' already exists! pagegen will overwrite it." % target)
        with open(target, "w") as writer:
            writer.write(content.format(today=now))
        logging.info("New document created in '%s'." % target)
    else:
        generate(args.file)
