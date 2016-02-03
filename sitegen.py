#!/usr/bin/env python3
# 重新生成整个网站

import os
import json
import hashlib
import pagegen


def hash(obj):
    obj = str(obj).encode("ASCII")
    return hashlib.md5(obj).hexdigest()

if __name__ != "__main__":
    exit(0)

UPDATE_MAP_FILE = "./map.json"
TEMPLATE_FILE = "./template.html"

update_map = {}
update_all = False

template_token = hash(TEMPLATE_FILE)
template_time = hash(int(os.path.getmtime(TEMPLATE_FILE)))

if os.path.exists(UPDATE_MAP_FILE):
    with open(UPDATE_MAP_FILE) as fp:
        update_map = json.load(fp)

if template_token not in update_map:
    update_map[template_token] = template_time
else:
    if update_map[template_token] != template_time:
        update_map[template_token] = template_time
        update_all = True

if update_all:
    print("(info) Template changed.")

for root, dirs, files in os.walk(os.path.abspath(".")):
    for name in files:
        if name.endswith(".md") or name.endswith(".markdown"):
            path = os.path.join(root, name)

            path_token = hash(path)
            time_token = hash(int(os.path.getmtime(path)))

            if not update_all:
                if path_token in update_map:
                    if update_map[path_token] == time_token:
                        continue
                else:
                    update_map[path_token] = time_token

            print("(info) Generating {}...".format(path))
            pagegen.generate(path)
            update_map[path_token] = time_token

with open(UPDATE_MAP_FILE, "w") as fp:
    json.dump(update_map, fp, indent=4, sort_keys=True)