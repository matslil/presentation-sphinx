# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2023, Mats'
author = 'Mats'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.plantuml','sphinxcontrib.drawio','sphinx_revealjs']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
plantuml = 'java -jar /home/mats/git/presentationer/venv/bin/plantuml.jar'
revealjs_style_theme='night'
revealjs_notes_from_comments = True,
revealjs_script_plugins = [
  { "name": "RevealHighlight", "src": "revealjs4/plugin/highlight/highlight.js", },
  { "name": "RevealNotes", "src": "revealjs4/plugin/notes/notes.js", },
  { "name": "RevealZoom", "src": "revealjs4/plugin/zoom/zoom.js", }
  ]
revealjs_script_conf = """
{
  controls: false,
  controlsTutorial: false,
  controlsLayout: 'bottom-right',
  controlBackArrows: 'faded',
  progress: true,
}
"""
