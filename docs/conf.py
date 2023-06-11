# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import molsysmt

# -- Project information -----------------------------------------------------

project = 'MolSysMT'
copyright = ''
#copyright = ("2022, UIBCDF Lab at the Mexico City Childrens Hospital Federico Gomez and authors."
#             "Computational Molecular Science Python Cookiecutter version 1.5")
author = 'Liliana M. Moreno Vargas & Diego Prada Gracia'
author = """
Liliana M. Moreno Vargas & Diego Prada Gracia | <a href= "mailto:uibcdf@gmail.com">Contáctanos</a>.
<br>
<a href="https://uibcdf.org">Unidad de Investigación en Biología Computacional y Diseño de Fármacos</a> del <a href=
"http://himfg.com.mx">Hospital Infantil de México Federico Gómez.</a>
"""


# The short X.Y version
version = molsysmt.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags
release = molsysmt.__version__

print(f'version {version}, release {release}')

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinxcontrib.bibtex',
    'sphinx.ext.extlinks',
    'sphinx_copybutton',
    'sphinx_remove_toctrees',
    'sphinx_design',
    'sphinx_favicon',
    'myst_nb',
    'nbsphinx',
]

# Myst extensions and options

myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'colon_fence'
]

myst_heading_anchors = 3

# Autosummary options

autosummary_generate = True

# Napoleon settings
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# sphinxcontrib-bibtex
bibtex_bibfiles = ['bibliography.bib'] # list of *.bib files
bibtex_default_style = 'alpha'
bibtex_encoding = 'utf-8-sig'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

source_parsers={
}

source_suffix = ['.rst', '.md', '.ipynb']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language was edited to use sphinx-intl
language = 'en'
# These next two variables were incluede to use sphinx-intl
locale_dirs =  ['_locale/']
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints', 'old_api', 'freezer']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# Remove from toctrees
remove_from_toctrees = []
for directory in os.walk('api'):
    if directory[0].endswith('/autosummary'):
        remove_from_toctrees.append(directory[0]+'/*')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/uibcdf/MolSysMT",
            "icon": "fa-brands fa-github",
        },
    ],
    "use_edit_page_button": False,
}

html_show_sourcelink = False

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "_static/logo.svg"

favicons = ["favicon-16x16.png",
            "favicon-124x124.png",
            "favicon-128x128.png",
            "favicon-192x192.png",
            "icon.svg"]

html_context = {
    "github_user": "uibcdf",
    "github_repo": "MolSysMT",
    "github_version": "main",
    "doc_path": "docs",
}


# Custom css

html_css_files = [
    'custom.css',
]


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'molsysmtdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
]


# -- 1 for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
]



# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

