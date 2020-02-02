#!/bin/bash
export FLASK_APP=balancer
export FLASK_ENV=development
pipenv run flask run --port 5000 &&