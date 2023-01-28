#!/bin/bash

# This script need to be sourced to work

readonly TOP=$PWD

readonly VENV=$TOP/venv

if [[ -d $VENV ]]; then
    . "$VENV"/bin/activate
else
    mkdir "$VENV"
    python3 -m venv $VENV
    . "$VENV"/bin/activate
    pip install -r "$TOP"/requirements.txt
    curl -Lo "$VENV"/bin/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2023.0/plantuml-1.2023.0.jar
fi

