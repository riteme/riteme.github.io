#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""CSS-HTML-JS-Minify.

StandAlone Async single-file cross-platform no-dependency Minifier for the Web.
"""


__version__ = '1.9.1'
__license__ = 'GPLv3+ LGPLv3+'
__author__ = 'Juan Carlos'
__email__ = 'juancarlospaco@gmail.com'
__url__ = 'https://github.com/juancarlospaco/css-html-js-minify'
__source__ = ('https://raw.githubusercontent.com/juancarlospaco/'
              'css-html-js-minify/master/css-html-js-minify.py')


__all__ = ['process_single_html_file', 'process_single_js_file',
           'process_single_css_file', 'html_minify', 'js_minify',
           'css_minify', 'minify']
           
from .minify import (process_single_html_file, process_single_js_file,
                     process_single_css_file, html_minify, js_minify,
                     css_minify)


