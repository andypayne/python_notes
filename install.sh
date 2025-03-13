#!/bin/bash

pipx install pip-tools

python -m venv env
. env/bin/activate
pip install -U pip setuptools wheel

pip-compile
pip install -r requirements.txt

