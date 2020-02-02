#!/bin/bash
export FLASK_APP=dcs
export FLASK_ENV=development
pipenv run flask run --port $(( 5000 + $1 ))