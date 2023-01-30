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

    ./new-presentation MY_PRESENTATION

   Replace `MY_PRESENTATION` with the name of your presentation.
   This needs to be done for the rest of the steps below as well.

   You can look in `MY_PRESENTATION/source/conf.py` if you want to
   customize your configuration.

4. Write your presentation, starting in `MY_PRESENTATION/source/index.rst`.
   To get a working example do the following from the repository root directory:

    cp example-files/* MY_PRESENTATION/source/

5. Build the presentation.

   Go to presentation root directory:

    cd MY_PRESENTATION

   For building in a directory:

    make revealjs

   For building a single index.html:

    make dirrevealjs

6. See result using Firefox (dirrevealjs version):

    firefox build/dirrevealjs/index.html

   In the browser window you can use '?' to get list of keyboard short-cuts.

Plugins
=======

sphinx-revealjs
   Gives slides from reStructuredText.
   https://sphinx-revealjs.readthedocs.io/en/stable/

spinx-design
   Provides layout directives to the reStructuredText format.
   https://sphinx-design.readthedocs.io/en/alabaster-theme/index.html

sphinxcontrib.drawio
   Renders .drawio files directly in reStructuredText documents.
   https://github.com/Modelmat/sphinxcontrib-drawio

sphinxcontrib.plantuml
   Specify plantuml code directly in reStructuredText documents.
   https://github.com/sphinx-contrib/plantuml/

