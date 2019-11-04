#!/usr/bin/env python3
# 用于生成单个页面

import os
import hashlib
import argparse
import datetime

import libs.parser as parser
import libs.navigater as navigater
import libs.logging as logging
from libs.logging import debug, warn, error
from libs.utility import *
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

def generate(filepath, do_modtime_check=True):
    if not os.path.exists(filepath):
        raise ValueError("File not found")
    with open(filepath) as reader:
        return process_document(filepath, reader.read(), do_modtime_check)

def process_document(filepath, source, do_modtime_check=True):
    # 解析 Markdown 文本
    parser = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_CONFIG
    )
    content, temp = preproc.process(source)
    if temp:
        warn("This is a temporary post. Skipped.")
        return True
    content = parser.convert(content.replace(chr(8203), ""))  # Remove non-width spaces

    # 准备 meta 数据
    try:
        meta = parser.Meta
        if len(meta) == 0:
            raise AttributeError
    except AttributeError:
        warn("No metadata. Skipped.")
        return True
    mdinfo = {}
    for key, val in METAINFO_DEFAULTS.items():
        if val is None and key not in meta:
            error("Missing metainfo '%s'. Stopped." % key)
            return False
        if key not in meta:
            mdinfo[key] = val
        elif type(val) == bool:
            mdinfo[key] = meta[key][0] in ["true", "True", True]
        elif type(val) == list:
            mdinfo[key] = meta[key]
        else:
            mdinfo[key] = meta[key][0]

        # if key in meta:
        #     debug(f'{key}: [{repr(type(meta[key]))}]{repr(meta[key])} → [{repr(type(mdinfo[key]))}]{repr(mdinfo[key])}')
        # else:
        #     debug(f'{key}: [{repr(type(val))}]{repr(val)} → [{repr(type(mdinfo[key]))}]{repr(mdinfo[key])}')

    # 准备页面模板参数
    toc, content = cut_toc(content)
    title = mdinfo["title"]
    create_time = generate_time(*mdinfo["create"].split("."))
    modified_time = generate_time(*mdinfo["modified"].split("."))
    if do_modtime_check and modified_time != generate_date(datetime.datetime.now()):
        warn("Modified time is not updated to today. (%s)" % filepath)
    tags = TagGroup()
    for x in mdinfo["tags"]:
        tags.append(x)
    folder = os.path.abspath(os.path.join(os.path.dirname(filepath), mdinfo["location"]))
    new_file = os.path.join(folder, os.path.splitext(os.path.basename(filepath))[0] + ".html")
    navigater.handle("myself", new_file)
    navigater.handle("md_url", filepath)
    navigater.home_folder = os.path.abspath(".")
    index_title = escape_string(title)
    index_text = escape_string(bs4.BeautifulSoup(content, BEAUTIFUL_SOUP_PARSER).text)
    index_url = navigater.get_path("myself")
    filename = os.path.basename(filepath)
    words = len(index_text)
    pagetitle = mdinfo["title"].strip().replace("\"", " ")
    pagekey = hashlib.md5(pagetitle.encode("utf8")).hexdigest()
    pageurl = SITE_DOMAIN + os.path.relpath(
        os.path.abspath(filepath), start=os.path.abspath("."))[:-3] + ".html"

    # 写入文件
    template_file = os.path.join(TEMPLATES_FOLDER, "%s.html" % mdinfo["template"])
    with open(template_file) as reader:
        template = reader.read()
    os.makedirs(folder, exist_ok=True)
    with open(new_file, "w") as writer:
        html_dom = template.format(
            title=title,
            create=create_time,
            modified=modified_time,
            stat=STAT_TEMPLATE.format(
                word=words, time=convert_time(words // WORDS_PER_MINUTE)),
            tags=str(tags),
            toc=toc,
            content=content,
            page_key=pagekey,
            page_title=pagetitle,
            page_url=pageurl,
            mdname=filename,
            github_location=os.path.join(GITHUB_LOCATION, navigater.get_path("md_url"))
        )
        if html_minify:
            writer.write(html_minify(html_dom))
        else:
            writer.write(html_dom)

    # 返回索引信息
    if mdinfo["index"]:
        return (index_title, index_url, index_text, mdinfo)
    return index_title


if __name__ == "__main__":
    argpr = argparse.ArgumentParser(description="Convert specific Markdown file to HTML page")
    log_group = argpr.add_mutually_exclusive_group()
    log_group.add_argument("-v", "--verbose", action="count", help="show more messages", default=0)
    log_group.add_argument("-q", "--quiet", action="count", help="show less messages", default=0)
    argpr.add_argument("-n", "--new", action="store_true", help="set to create a new document instead of converting")
    argpr.add_argument("-t", "--toc", action="store_true", help="whether to include a table of content in the document", default=False)
    argpr.add_argument("file", help="path to file that will be converted")

    args = argpr.parse_args()
    if args.verbose:
        logging.LOGGING_LEVEL = logging.LoggingLevel.DEBUG
    else:
        levels = [logging.LoggingLevel.INFO, logging.LoggingLevel.WARN,
            logging.LoggingLevel.ERROR, logging.LoggingLevel.FATAL, logging.LoggingLevel.NONE]
        logging.LOGGING_LEVEL = levels[min(args.quiet, len(levels) - 1)]

    if args.new:
        folder = os.path.join(BLOG_FOLDER, today().replace(".", "-"))
        os.makedirs(folder, exist_ok=True)
        target = os.path.join(folder, "%s.md" % args.file)
        if os.path.exists(target):
            warn("'%s' already exists! pagegen will overwrite it." % target)
        with open(target, "w") as writer:
            writer.write(meta_to_string(METAINFO_DEFAULTS))
            if args.toc:
                writer.write("\n[TOC]\n")
        logging.info("New document created in '%s'." % target)
    else:
        generate(args.file)
