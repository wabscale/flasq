#!/bin/bash

ENV_NAME=env # env name 
PYTHON_I=$(which python3) # python inerpreter

if [ -d $ENV_NAME ]; then
    echo "removing old enviorment..."
    rm -rf $ENV_NAME
fi

if [ -n "$(which virtualenv)" ]; then
    pip install virtualenv
fi

virtualenv -p ${PYTHON_I} ${ENV_NAME}

source ${ENV_NAME}/bin/activate
sudo pip install -r requirements.txt

echo "source $ENV_NAME/bin/activate" > activate
