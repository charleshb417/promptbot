#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source $DIR/../env/bin/activate
python $DIR/../promptbot/app.py
