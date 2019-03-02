#!/usr/bin/env python3
# 重新生成整个网站

import os
import sys
import json
import argparse
import traceback

import pagegen
import libs.database as database
import libs.logging as logging
from libs.logging import debug, info, warn, error
from libs.utility import *
from preferences import *


update_map = {}
update_all = False
update_count = 0


def check_template_update(token, current_time):
    global update_map
    global update_all

    if token not in update_map or update_map[token] != current_time:
        update_map[token] = current_time
        update_all = True
        info("Template (%s) changed." % token[:8])

def real_generate(filepath):
    try:
        info("Generating '%s'..." % filepath)
        return pagegen.generate(filepath)
    except Exception as e:
        error("Failed to generate %s." % filepath)
        error("%s" % str(e))
        debug("Python traceback:\n" + "".join(traceback.format_tb(e.__traceback__)))

def generate(root, name):
    global update_map
    global update_all
    global update_count
    global ALL_PATHS

    path = os.path.join(root, name)
    path_token = hash(path)
    time_token = hash(int(os.path.getmtime(path)))

    if path_token not in update_map:
        update_map[path_token] = None
    if update_map[path_token] == time_token and not update_all:
        return

    data = real_generate(path)
    update_count += 1
    update_map[path_token] = time_token

    if type(data) == str:
        database.del_index(data)
    elif data:
        database.add_index(*data)


if __name__ == "__main__":
    argpr = argparse.ArgumentParser(description="Convert specific Markdown file to HTML page")
    log_group = argpr.add_mutually_exclusive_group()
    log_group.add_argument("-v", "--verbose", action="count", help="show more messages", default=0)
    log_group.add_argument("-q", "--quiet", action="count", help="show less messages", default=0)
    argpr.add_argument("-r", "--regenerate", action="store_true", help="force to regenerate the entire site")

    args = argpr.parse_args()
    if args.verbose:
        logging.LOGGING_LEVEL = logging.LoggingLevel.DEBUG
    else:
        levels = [logging.LoggingLevel.INFO, logging.LoggingLevel.WARN,
            logging.LoggingLevel.ERROR, logging.LoggingLevel.FATAL, logging.LoggingLevel.NONE]
        logging.LOGGING_LEVEL = levels[min(args.quiet, len(levels) - 1)]
    if args.regenerate:
        update_all = True
        warn("Force to update all pages.")

    if not update_all:
        database.load_index(DATABASE_LOCATION)
    if os.path.exists(UPDATE_MAP_FILE):
        with open(UPDATE_MAP_FILE) as fp:
            update_map = json.load(fp)
    for root, dirs, files in os.walk(TEMPLATES):
        for file in files:
            path = os.path.join(root, file)
            check_template_update(hash(path), hash(int(os.path.getmtime(path))))

    generate(os.path.abspath("."), "index.md")
    generate(os.path.abspath("."), "posts.md")
    generate(os.path.abspath("."), "about.md")
    generate(os.path.abspath("."), "links.md")
    #generate(os.path.abspath("."), "search.md")

    for root, dirs, files in os.walk(os.path.abspath(BLOG)):
        for name in files:
            if name.endswith(".md") or name.endswith(".markdown"):
                generate(root, name)

    with open(UPDATE_MAP_FILE, "w") as fp:
        json.dump(update_map, fp, indent=4, sort_keys=True)

    if update_count:
        info("Updated %s page(s)." % update_count)
        info("Writing to JSON database '%s'..." % DATABASE_LOCATION)
        database.save_json_index(DATABASE_LOCATION)
        info("Writing to Tipuesearch database '%s'..." % TIPUESEARCH_DATABASE_LOCATION)
        database.save_tipuesearch_index(TIPUESEARCH_DATABASE_LOCATION)
        info("Writing to sitemap '%s'..." % SITEMAP_LOCATION)
        database.save_text_sitemap(SITEMAP_LOCATION)
    else:
        warn("Nothing to update.")
