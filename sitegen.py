#!/usr/bin/env python3
# 重新生成整个网站

import os
import pagegen

for root, dirs, files in os.walk(os.path.abspath(".")):
    for name in files:
        if name.endswith(".md") or name.endswith(".markdown"):
            path = os.path.join(root, name)
            print("(info) Generating {}...".format(path))
            pagegen.generate(path)
