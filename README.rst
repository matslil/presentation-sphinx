========================
Presentation infrastructure
========================

This repository gives an infrastructure for making presentations as code, for those who are fed up with PowerPoint.

It uses a browser for doing the presentation, and support things like speaker window (becomes a separate browser window), zoom parts of the slide, and code highlightning.

The presentations are written using restructured text, diagrams use plantuml inline in the text and drawings can be made using draw.io and the .drawio can then be imported directly in the slide.

Pre-requisites
==============

You need to install drawio binary. For Ubuntu you can use snaps for this:

    sudo snap install drawio

Making a new presentation
=========================

0. First setup your environment, must be run for each new shell:

    ./setup.sh

1. Setup directory structure:

    sphinx-quickstart my-new-presentation

   Use separate build and source directory.

2. Update your conf.py:

    sed -i "s/extensions =.*/extensions = ['sphinxcontrib.plantuml','sphinxcontrib.drawio','sphinx_revealjs']/" my-new-presentation/source/conf.py
    echo "plantuml = 'java -jar $PWD/venv/bin/plantuml.jar'" >> my-new-presentation/source/conf.py

3. Perform configuration
   Below example gives 's' for a separate window with the speaker view, code highlighting and ctrl-mouse-click for zoom:

    cat <<EOF  >> my-new-presentation/source/conf.py
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
    EOF

4. Write your presentation, starting in `my-new-presentation/source/index.rst`.
   See `test/source/index.rst` for an example.

5. Build the presentation.

   Go to presentation root directory:

    cd my-new-presentation

   For building in a directory:

    make revealjs

   For building a single index.html:

    make dirrevealjs

6. See result using Firefox (dirrevealjs version):

    firefox build/dirrevealjs/index.html
