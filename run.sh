#!/bin/bash
file=$1
echo $file

export FLASK_APP=$file
export FLASK_ENV=development
python -m flask run --host=0.0.0.0
