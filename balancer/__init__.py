import os

from flask import Flask, Blueprint, json
from flask_restful import Resource, Api
from node import Node

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['UPLOAD_FOLDER'] = config['storage_directory']

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    api.add_resource(Node, '/files', '/files/<string:id>', '/files/list')
    app.register_blueprint(api_bp)
    APP = app
    return app