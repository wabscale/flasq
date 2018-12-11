#!/bin/bash

PORT=5000

[ -d ./env ] || ./setup.sh
source ./env/bin/activate

python dev.py
#gunicorn -b 0.0.0.0:5000 -w 4 web:app
