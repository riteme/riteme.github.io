# riteme.site
This is riteme personal blog.

Powered by `sitegen.py`.

## `sitegen.py`
### Files
* `sitegen.py`: Generate the site.
* `pagegen.py`: Convert specific post to HTML document.
* `map.json`: Timestamps recorded by `sitegen.py` to avoid duplicated generation (not in GitHub repo, generated at the launch of `sitegen.py`).
* `lib/*.py`: Utilities for `pagegen.py` and `sitegen.py`.

### Requirements
* Python3
* Python Markdown
* Pygments (If not exist, code highlight will be disabled)
* Beautiful Soup 4

### Basic Usage
Write blogs in `blog` folder.

Use `./sitegen.py` to generate site. `./sitegen.py --force` for entire regeneration.

Use `./pagegen.py [PATH TO MARKDOWN]` to compile a specific markdown file.

(For Linux) `./setup.py` (with root privilege) to copy the entire repo into `/var/www/html`. With parameter `--quick` to just copy some of files specified in `setup.py` (`SMALLEST_UPDATE_*` (lists) in the python file).
