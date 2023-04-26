# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ntt'
copyright = '2023, Romain Vuillemot'
author = 'Romain Vuillemot'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx_gallery.gen_gallery',
]

templates_path = ['_templates']

# Sphinx gallery configuration
sphinx_gallery_conf = {
    'examples_dirs': ['../../gallery'],
    'gallery_dirs': ['gallery']
}

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
# https://sphinx-themes.org/sample-sites/sphinx-theme/
html_theme = 'stanford_theme'
html_theme_path = [sphinx_theme.get_html_theme_path('stanford_theme')]

html_static_path = ['_static']
