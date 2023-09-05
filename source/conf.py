# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
latex_elements = {
    'sphinxsetup': "verbatimforcewraps, verbatimmaxunderfull=0",
}



project = '2023级NKU操作系统实验指导书'
copyright = '2023, NKU OS LAB'
author = 'NKU助教团队'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
source_suffix = ['.rst', '.md']


templates_path = ['_templates']
exclude_patterns = []
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'zh_CN'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


