# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full list see
# the documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory, add
# these directories to sys.path here. If the directory is relative to the documentation
# root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# Import so that autodoc can find code
import ixmp

# -- Project information ---------------------------------------------------------------

project = "ixmp"
copyright = "2017–2023, IIASA Energy, Climate, and Environment (ECE) program"
author = "ixmp Developers"


# -- General configuration -------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions coming
# with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "ixmp.utils.sphinx_linkcode_github",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinxcontrib.bibtex",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories to
# ignore when looking for source files. This pattern also affects html_static_path and
# html_extra_path.
exclude_patterns = ["_build", "README.rst", "Thumbs.db", ".DS_Store"]

# A string of reStructuredText that will be included at the beginning of every source
# file that is read.
version = ixmp.__version__
rst_prolog = r"""
.. |MESSAGEix| replace:: MESSAGE\ :emphasis:`ix`

.. |ixmp| replace:: :emphasis:`ix modeling platform`

.. |version| replace:: {}

.. role:: strike

.. role:: underline

""".format(
    version
)

# -- Options for HTML output -----------------------------------------------------------

# A list of CSS files.
html_css_files = ["custom.css"]

html_favicon = "_static/favicon.svg"

# The name of an image file (relative to this directory) to place at the top of the
# sidebar.
html_logo = "_static/combined-logo-white.png"

# Add any paths that contain custom static files (such as style sheets) here, relative
# to this directory. They are copied after the builtin static files, so a file named
# "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The theme to use for HTML and HTML Help pages.
html_theme = "sphinx_rtd_theme"

# -- Options for sphinx.ext.extlinks ---------------------------------------------------

extlinks = {
    "issue": ("https://github.com/iiasa/ixmp/issue/%s", "#%s"),
    "pull": ("https://github.com/iiasa/ixmp/pull/%s", "PR #%s"),
}

# -- Options for sphinx.ext.intersphinx ------------------------------------------------

intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/stable/", None),
    "genno": ("https://genno.readthedocs.io/en/latest", None),
    "jpype": ("https://jpype.readthedocs.io/en/latest", None),
    "message_ix": ("https://docs.messageix.org/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pint": ("https://pint.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sparse": ("https://sparse.pydata.org/en/stable/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
}

# -- Options for sphinx.ext.linkcode / ixmp.utils.sphinx_linkcode_github ---------------

linkcode_github_repo_slug = "iiasa/ixmp"

# -- Options for sphinx.ext.todo -------------------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for sphinxcontrib.bibtext -------------------------------------------------

bibtex_bibfiles = ["references.bib"]
