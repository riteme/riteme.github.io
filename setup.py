#!/usr/bin/env python3

import os
import shutil

print("Removing last files...")

if os.path.exists("/var/www/html/blog"):
    shutil.rmtree("/var/www/html/blog")

if os.path.exists("/var/www/html/css"):
    shutil.rmtree("/var/www/html/css")

if os.path.exists("/var/www/html/index.html"):
    os.remove("/var/www/html/index.html")

if os.path.exists("/var/www/html/posts.html"):
    os.remove("/var/www/html/posts.html")

if os.path.exists("/var/www/html/search.html"):
    os.remove("/var/www/html/search.html")


print("Copying new files...")
shutil.copytree(os.path.join(os.getcwd(), "blog"), "/var/www/html/blog")
shutil.copytree(os.path.join(os.getcwd(), "css"), "/var/www/html/css")
shutil.copy2(os.path.join(os.getcwd(), "index.html"), "/var/www/html/index.html")
shutil.copy2(os.path.join(os.getcwd(), "posts.html"), "/var/www/html/posts.html")
shutil.copy2(os.path.join(os.getcwd(), "search.html"), "/var/www/html/search.html")

