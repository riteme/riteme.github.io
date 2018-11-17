#!/usr/bin/env python3

import os
import sys
import shutil

HELP_DOCUMENT = """{command_line}: Setup this site to local server.
    Usage: {command_line} [--quick] [--install-to=PATH] [--help/-h]

    --quick: Copy smallest required files to the server.
    --install-to=PATH: Set the server location.
    --help -h: Show this help.
"""

INSTALL_TO = "/var/www/html/"

SMALLEST_UPDATE_FOLDERS = [
    "blog"
]

SMALLEST_UPDATE_FILES = [
    "index.html",
    "posts.html",
    "css/site.css",
    "tipuesearch/tipuesearch_content.js"
]

def setup_quick():
    global INSTALL_TO
    global SMALLEST_UPDATE_FOLDERS
    global SMALLEST_UPDATE_FILES

    print("(warn) Quick setup enabled")

    print("(info) Removing previous files...")

    for target in SMALLEST_UPDATE_FOLDERS:
        path = os.path.join(INSTALL_TO, target)
        if os.path.exists(path):
            shutil.rmtree(path)

    for target in SMALLEST_UPDATE_FILES:
        path = os.path.join(INSTALL_TO, target)
        if os.path.exists(path):
            os.remove(path)

    print("(info) Copying new files...")

    for target in SMALLEST_UPDATE_FOLDERS:
        src = os.path.join(os.getcwd(), target)
        dest = os.path.join(INSTALL_TO, target)
        shutil.copytree(src, dest)

    for target in SMALLEST_UPDATE_FILES:
        src = os.path.join(os.getcwd(), target)
        dest = os.path.join(INSTALL_TO, target)
        shutil.copy2(src, dest)

def setup():
    global INSTALL_TO

    print("(info) Removing previous files...")

    if os.path.exists(INSTALL_TO):
        shutil.rmtree(INSTALL_TO)

    print("(info) Copying new files...")

    shutil.copytree(os.getcwd(), INSTALL_TO)
    os.system("chmod 755 /var/www/html -R")

if __name__ == "__main__":
    handler = setup

    for param in sys.argv[1:]:
        if param.startswith("--help") or param.startswith("-h"):
            print(HELP_DOCUMENT.format(command_line = sys.argv[0]))
            exit()
        elif param.startswith("--quick"):
            handler = setup_quick
        elif param.startswith("--install-to="):
            pre, INSTALL_TO = param.split("=")
        else:
            print("(error) Unrecognized parameter '{param}'".format(param = param))
            exit(-1)

    handler()
