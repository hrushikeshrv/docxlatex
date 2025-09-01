# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# ! To build docs, run `make html` in the docs_src/ directory.


project = "docxlatex"
copyright = "2025, Hrushikesh Vaidya (@hrushikeshrv)"
author = "Hrushikesh Vaidya (@hrushikeshrv)"
release = "v1.2.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.googleanalytics",
]
googleanalytics_id = "G-TGM5F6WJNV"

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
