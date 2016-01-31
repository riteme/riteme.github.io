# 用于生成单个页面

import os

import info
import tag
import parser
import breadcrumb
import navigater


def generate(filepath):
    if not os.path.exists(filepath):
        raise ValueError("File not found")

    reader = parser.Parser()
    reader.load_all_syntax()
    with open(filepath) as md:
        information, content = reader.process(md)

    title = info.generate_title(information["title"])
    create_time = info.generate_time(*split(
        information["create"], ".")
    )
    modified_time = info.generate_time(*split(
        information["modified"], ".")
    )
