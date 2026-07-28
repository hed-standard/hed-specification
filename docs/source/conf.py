# Configuration file for the Sphinx documentation builder.


# -- Project information -----------------------------------------------------
project = "HED specification"
copyright = "2025, HED Working Group"
author = "HED Working Group"
version = "4.0"
release = "4.0.0"


# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Configure source file suffixes
source_suffix = [".rst", ".md"]

# Disable automatic section numbering
html_secnumber_suffix = ""
html_use_index = True

# Disable numbering completely
numfig = False
toc_object_entries_show_parents = "hide"

# Completely disable section numbering
html_use_smartypants = True
html_add_permalinks = ""

# -- Options for HTML output ------------------------------------------------
html_theme = "furo"
html_title = "HED specification"
html_logo = "_static/images/croppedWideLogo.png"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["gh_icon_fix.js"]

# Furo theme options
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#0969da",
        "color-brand-content": "#0969da",
    },
    "dark_css_variables": {
        "color-brand-primary": "#58a6ff",
        "color-brand-content": "#58a6ff",
    },
    "source_repository": "https://github.com/hed-standard/hed-specification/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "navigation_with_keys": True,
}

# Configure sidebar to show logo, search, navigation, and quick links
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "quicklinks.html",
        "sidebar/scroll-end.html",
    ]
}

# -- Autodoc configuration --------------------------------------------------
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "show-inheritance": True,
}


# -- MyST Configuration -----------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
]

# Configure MyST to parse headings for navigation
myst_heading_anchors = 4

# Disable automatic numbering in MyST
myst_number_code_blocks = []
myst_title_to_header = False

# -- Intersphinx mapping ---------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# -- Napoleon settings -----------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
