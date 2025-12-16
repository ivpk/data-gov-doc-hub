# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Valstybės duomenų dokumentacija'
copyright = '2025, Valstybės skaitmeninių sprendimų agentūra'
author = 'Valstybės skaitmeninių sprendimų agentūra'
release = "'0.1'"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',  # Pridėkite šią eilutę!
]

templates_path = ['_templates']
exclude_patterns = []

language = 'lt'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}