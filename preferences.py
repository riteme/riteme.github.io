# For sitegen.py
UPDATE_MAP_FILE = "map.json"
DATABASE_LOCATION = "content.json"
TIPUESEARCH_DATABASE_LOCATION = "scripts/tipuesearch_content.js"
SITEMAP_LOCATION = "sitemap.txt"
TEMPLATES = "templates/"
BLOG = "blog/"
SITE_DOMAIN = "https://riteme.site/"

# For pagegen.py
WORDS_PER_MINUTE = 250
BEAUTIFUL_SOUP_PARSER = "lxml"
GITHUB_LOCATION = "https://github.com/riteme/riteme.github.io/blob/master"
SITE_DOMAIN = "https://riteme.site/"
DEFAULT_TEMPLATE = "template"
DEFAULT_DOCUMENT = "default.md"

# '#' 开头的项目会调用同名的函数来获得扩展
MARKDOWN_EXTENSIONS = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.tables",
    "markdown.extensions.codehilite",
    "markdown.extensions.toc",
    "markdown.extensions.smart_strong",
    "markdown.extensions.nl2br",
    "markdown.extensions.meta",
    "markdown.extensions.smarty",
    "#latex_friendly",
    #"#new_tab_on_links",
    "#tasklist",
    "#del_ins"
]

MARKDOWN_CONFIG = {
    "markdown.extensions.codehilite": {
        "linenums": True,
        "guess_lang": False
    }
}