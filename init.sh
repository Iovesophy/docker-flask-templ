#!/bin/sh -eux
pip3 install flask
export FLASK_APP=/app/main.py
flask run --host=0.0.0.0
