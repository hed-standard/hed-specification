# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------
project = 'HED Specification'
copyright = '2025, HED Working Group'
author = 'HED Working Group'
release = '3.3.0'
version = '3.3.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_design',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Configure source file suffixes
source_suffix = ['.rst', '.md']

# Disable automatic section numbering
html_secnumber_suffix = ""
html_use_index = True

# Disable numbering completely
numfig = False
toc_object_entries_show_parents = 'hide'

# Completely disable section numbering
html_use_smartypants = True
html_add_permalinks = ""

# -- Options for HTML output ------------------------------------------------
html_theme = 'sphinx_book_theme'
html_title = 'HED Specification'
html_logo = '_static/images/croppedWideLogo.png'

html_theme_options = {
    'repository_url': 'https://github.com/hed-standard/hed-specification',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_edit_page_button': True,
    'path_to_docs': 'docs/source',
    'show_toc_level': 2,
    'navigation_with_keys': False,
    'show_navbar_depth': 1,
    'use_download_button': True,
    'toc_title': None,
    'use_fullscreen_button': False,
}

# Force the sidebar to use toctree titles instead of page titles
html_sidebars = {
    "**": ["navbar-logo", "search-field", "sbt-sidebar-nav.html", "quicklinks.html"]
}

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for LaTeX output -----------------------------------------------
latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': r'''
        \usepackage[utf8]{inputenc}
        \usepackage{fancyhdr}
        \usepackage{graphicx}
        \usepackage{longtable}
        \usepackage{booktabs}
        \usepackage{array}
        \pagestyle{fancy}
        \fancyhf{}
        \fancyhead[L]{HED Specification}
        \fancyhead[R]{\thepage}
        \renewcommand{\headrulewidth}{0.4pt}
        \setcounter{tocdepth}{2}
    ''',
    'fncychap': '\\usepackage[Bjornstrup]{fncychap}',
    'printindex': '\\footnotesize\\raggedright\\printindex',
    'extraclassoptions': 'openany,oneside',
    'babel': '\\usepackage[english]{babel}',
}

latex_documents = [
    ('index', 'HEDSpecification.tex', 'HED Specification',
     'HED Working Group', 'manual'),
]

latex_show_pagerefs = False
latex_show_urls = 'footnote'
latex_use_xindy = False

# -- MyST Configuration -----------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "attrs_inline",
]

# Configure MyST to parse headings for navigation
myst_heading_anchors = 4

# Disable automatic numbering in MyST
myst_number_code_blocks = []
myst_title_to_header = False
