#!/bin/bash


[ -d ./env ] || ./setup.sh

source ./env/bin/activate
python ./app.py
