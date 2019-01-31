#!/usr/bin/env python3
# 重新生成整个网站

import os
import sys
import json
import hashlib
import traceback

import lib.tipuesearch as tipuesearch
import pagegen


if __name__ != "__main__":
    exit(0)


UPDATE_MAP_FILE = "./map.json"
TEMPLATES = "templates/"
DOMAIN = "https://riteme.site/"
SITEMAP_LOCATION = "sitemap.txt"
ALL_PATHS = []

update_map = {}
update_all = False


if "--force" in sys.argv:
    update_all = True
    print("(info) Force to update all pages.")

if os.path.exists(UPDATE_MAP_FILE):
    with open(UPDATE_MAP_FILE) as fp:
        update_map = json.load(fp)

def check_template_update(token, current_time):
    global update_map
    global update_all

    if token not in update_map or update_map[token] != current_time:
        update_map[token] = current_time
        update_all = True
        print("(info) Template (%s) changed." % token[:8])

def hash(obj):
    obj = str(obj).encode("ascii")
    return hashlib.md5(obj).hexdigest()

for root, dirs, files in os.walk(TEMPLATES):
    for file in files:
        path = os.path.join(root, file)
        check_template_update(hash(path), hash(int(os.path.getmtime(path))))


def real_generate(filepath):
    try:
        print("(info) Generating {}...".format(filepath))
        return pagegen.generate(filepath)
    except Exception as e:
        print("(error) Failed to generate {}.\n{}".format(filepath, str(e)))
        print('Python traceback:\n' + ''.join(traceback.format_tb(e.__traceback__)))


def generate(root, name):
    global update_map
    global update_all
    global ALL_PATHS

    global pool

    path = os.path.join(root, name)
    ALL_PATHS.append(DOMAIN + (os.path.relpath(path, start="."))[:-2] + "html")

    path_token = hash(path)
    time_token = hash(int(os.path.getmtime(path)))

    if not update_all:
        if path_token in update_map:
            if update_map[path_token] == time_token:
                return
        else:
            update_map[path_token] = time_token

    data = real_generate(path)
    update_map[path_token] = time_token

    if data:
        if type(data) == str:
            tipuesearch.del_index_info(data)
        else:
            tipuesearch.add_index_info(*data)


if __name__ == "__main__":
    tipuesearch.load_index("tipuesearch/content.json")

    generate(os.path.abspath("."), "index.md")
    generate(os.path.abspath("."), "posts.md")
    generate(os.path.abspath("."), "about.md")
    generate(os.path.abspath("."), "links.md")
    # generate(os.path.abspath("."), "search.md")

    for root, dirs, files in os.walk(os.path.abspath("./blog/")):
        for name in files:
            if name.endswith(".md") or name.endswith(".markdown"):
                generate(root, name)

    with open(UPDATE_MAP_FILE, "w") as fp:
        json.dump(update_map, fp, indent=4, sort_keys=True)

    print("(info) Writing to search database...")
    tipuesearch.save_index(
        "tipuesearch/tipuesearch_content.js",
        "tipuesearch/content.json"
    )

    print("(info) Writing to %s..." % SITEMAP_LOCATION)
    with open(SITEMAP_LOCATION, "w") as writer:
        writer.write("\n".join((str(x) for x in ALL_PATHS)))
