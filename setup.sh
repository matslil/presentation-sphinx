#!/bin/bash

# This script need to be sourced to work

if [[ -d $PWD/venv ]]; then
    . "$PWD"/venv/bin/activate
else
    mkdir "$PWD/venv"
    python3 -m venv $PWD/venv
    . "$PWD"/venv/bin/activate
    pip install -r "$PWD"/requirements.txt
    curl -Lo "$PWD"/venv/bin/plantuml.jar https://github.com/plantuml/plantuml/releases/download/v1.2023.0/plantuml-1.2023.0.jar
    echo "java -jar $PWD/venv/bin/plantuml.jar" > "$PWD"/venv/bin/plantuml
    chmod +x "$PWD"/venv/bin/plantuml
fi

