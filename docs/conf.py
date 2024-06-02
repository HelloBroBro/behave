# -*- coding: utf-8 -*-
# =============================================================================
# SPHINX CONFIGURATION: behave documentation build configuration file
# =============================================================================

from __future__ import print_function
import os.path
import sys
import importlib

# -- ENSURE: Local workspace is used (for sphinx apidocs).
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

# ------------------------------------------------------------------------------
# DETECT BUILD CONTEXT
# ------------------------------------------------------------------------------
ON_READTHEDOCS = os.environ.get("READTHEDOCS", None) == "True"
USE_SPHINX_INTERNATIONAL = True


# ------------------------------------------------------------------------------
# EXTENSIONS CONFIGURATION
# ------------------------------------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "1.3"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named "sphinx.ext.*") or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.ifconfig",
    "sphinx.ext.extlinks",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]
optional_extensions = [
    # -- DISABLED: "sphinxcontrib.youtube",
    # http://www.sphinx-doc.org/en/stable/faq.html
    "rinoh.frontend.sphinx",    # ALTERNATIVE FOR: LATEX-PDF
    "rst2pdf.pdfbuilder",       # PDF

]
for optional_module_name in optional_extensions:
    try:
        importlib.import_module(optional_module_name)
        extensions.append(optional_module_name)
    except ImportError:
        pass


extlinks = {
    "this": ("https://github.com/behave/behave/blob/main/%s", "%s"),  # AKA: this_repo
    "behave": ("https://github.com/behave/behave", None),
    "behave.example": ("https://github.com/behave/behave.example", None),
    "issue":  ("https://github.com/behave/behave/issues/%s", "issue #%s"),
    "pull":  ("https://github.com/behave/behave/issues/%s", "PR #%s"),
    "github": ("https://github.com/%s", "github:/"),
    "pypi": ("https://pypi.org/project/%s", "%s"),
    "youtube": ("https://www.youtube.com/watch?v=%s", "youtube:video=%s"),

    # -- CUCUMBER RELATED:
    "cucumber": ("https://github.com/cucumber/common/", None),
    "cucumber.issue": ("https://github.com/cucumber/common/issues/%s", "cucumber issue #%s"),
}

intersphinx_mapping = {
    "python": ('https://docs.python.org/3', None)
}

# -- SUPPORT: Documentation variation-points with sphinx.ext.ifconfig
def setup(app):
    # -- VARIATION-POINT: supports_video
    # BASED-ON: installed("sphinxcontrib-youtube") and output-mode
    # TODO: Check for output-mode, too (supported on: HTML, ...)
    supports_video = "sphinxcontrib.youtube" in extensions
    app.add_config_value("supports_video", supports_video, "env")


# -----------------------------------------------------------------------------
# BASIC CONFIGURATION
# -----------------------------------------------------------------------------
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# -- MULTI-LANGUAGE SUPPORT: en, ...
# SEE: https://pypi.org/project/sphinx-intl/
# SEE: https://github.com/sphinx-doc/sphinx-intl/
if USE_SPHINX_INTERNATIONAL:
    locale_dirs = ["locale/"]   # path is example but recommended.
    gettext_compact = False     # optional.
    print("USE SPHINX-INTL: locale_dirs=%s" % ",".join(locale_dirs))

# STEPS:
#   make gettext
#       -- Create *.po files in "../build/docs/locale/"
#   sphinx-intl update -p ../build/docs/locale -l de -l ja
#       -- Create *.po files in "gettext/de/", "gettext/ja/" dirs.
#
# -----------------------------------------------------------------------------
# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
project = u"behave"
authors = u"Jens Engel, Benno Rice and Richard Jones"
copyright = u"2012-2024, %s" % authors

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from behave import __version__
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ""
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, "()" will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# -- PYGMENTS_STYLE: The name of the Pygments (syntax highlighting) style to use.
# LIGHT THEME CANDIDATES: tango, stata-light, default, vs
# DARK  THEME CANDIDATES: lightbulb, monokai, stata-dark, zenburn
pygments_style = "tango"
pygments_dark_style = "lightbulb"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# ------------------------------------------------------------------------------
# OPTIONS FOR: HTML OUTPUT
# ------------------------------------------------------------------------------
# The theme to use for HTML and HTML Help pages.
# SEE: https://www.sphinx-doc.org/en/master/usage/theming.html
# SEE: https://sphinx-themes.org
# DISABLED: html_theme = "bootstrap"
# DISABLED: html_theme = "sphinx_nefertiti"
html_theme = "furo"

# -- DISABLED: Use html_theme = "furo" now.
# if ON_READTHEDOCS:
#    html_theme = "default"

if html_theme == "furo":
    # -- SEE: https://pradyunsg.me/furo/customisation/
    html_theme_options = {
        "navigation_with_keys": True,
        # DISABLED: "light_logo": "behave_logo1.png",
        # DISABLED: "dark_logo": "behave_logo2.png",
    }
elif html_theme == "sphinx_nefertiti":
    pygments_style = "vs"
    pygments_dark_style = "monokai"
    html_theme_options = {
        "style": "blue",
        "sans_serif_font": "Arial",
        "monospace_font": "Ubuntu Mono",
        "doc_headers_font": "Arial",
        "monospace_font_size": "1.05rem",
        "documentation_font_size": "1.05rem",
        # -- SHOW: REPO INFO
        "repository_url": "https://github.com/behave/behave",
        "repository_name": "behave/behave",
        "versions": [
            # ("latest", "https://github.com/behave/behave/"),
            ("v1.2.7.dev5", "https://github.com/behave/behave/releases/tag/v1.2.7.dev5"),
            ("v1.2.7.dev4", "https://github.com/behave/behave/releases/tag/v1.2.7.dev4"),
            ("v1.2.6", "https://pypi.org/project/behave/v1.2.6/"),
        ]
    }
elif html_theme == "bootstrap":
    # See sphinx-bootstrap-theme for documentation of these options
    # https://github.com/ryan-roemer/sphinx-bootstrap-theme
    import sphinx_bootstrap_theme
    html_theme_options = {
        'navbar_site_name': 'Document',
        'navbar_pagenav': True
    }

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/behave_logo1.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not "", a "Last updated on:" timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%m-%d"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ""

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = ".html"

# ------------------------------------------------------------------------------
# OPTIONS FOR: HTML HELP
# ------------------------------------------------------------------------------
# Output file base name for HTML help builder.
htmlhelp_basename = "behave.doc"


# ------------------------------------------------------------------------------
# OPTIONS FOR: LATEX OUTPUT
# ------------------------------------------------------------------------------
latex_elements = {
    # The paper size ("letterpaper" or "a4paper").
    "papersize": "a4paper",

    # The font size ("10pt", "11pt" or "12pt").
    # "pointsize": "10pt",

    # Additional stuff for the LaTeX preamble.
    # "preamble": "",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ("index", "behave.tex", u"behave Documentation", authors, "manual"),
]

# latex_logo = None

# ------------------------------------------------------------------------------
# OPTIONS FOR: MANUAL PAGE (man page) OUTPUT
# ------------------------------------------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "behave", u"behave Documentation", [authors], 1)
]



# ------------------------------------------------------------------------------
# OPTIONS FOR: Texinfo output
# ------------------------------------------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ("index", "behave", u"behave Documentation", authors,
   "behave", "A test runner for behave (feature tests).", "Miscellaneous"),
]

# -----------------------------------------------------------------------------
# RST2PDF OUTPUT CONFIGURATION: builder=pdf   (prepared)
# -----------------------------------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.
pdf_documents = [
    ('index', project, project, authors),
]
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']
# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed = True
# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
pdf_language = "en_US"
# Mode for literal blocks wider than the frame. Can be overflow, shrink or truncate
pdf_fit_mode = "shrink"
# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
# pdf_break_level = 0 XXX
pdf_break_level = 1

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True
# verbosity level. 0 1 or 2
#pdf_verbosity = 0
# If false, no index is generated.
#pdf_use_index = True
# If false, no modindex is generated.
#pdf_use_modindex = True
pdf_use_modindex = False

# If false, no coverpage is generated.
#pdf_use_coverpage = True
# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'
# Documents to append as an appendix to all manuals.
#pdf_appendices = []
# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = True XXX
pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72
# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
pdf_page_template = 'cutePage'
