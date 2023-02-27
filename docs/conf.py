# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "gowt"
copyright = "2023, chramb"
author = "chramb"
release = "0.0.1rc0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.doctest",  # test code snippets in docs
    "sphinx.ext.autodoc",  # code documentation
    "sphinx.ext.coverage",  # coverage stats in sphinx
    "sphinx.ext.napoleon",  # *.rst documentation
    "sphinx.ext.todo",  # to-do items support
    "sphinx.ext.viewcode",  # add links to highlighted source code
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/__main__.py"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
