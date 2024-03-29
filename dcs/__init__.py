__author__ = 'Aakash Hemadri <aakashhemadri123gmail.com>'
__version__ = '0.0.1'
__classifiers__ = [
    'Development Status :: Unstable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v2.0',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.8',
]
__copyright__ = "2013, %s " % __author__
__license__ = """
   Copyright %s.
   GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991
 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
""" % __copyright__

__docformat__ = 'restructuredtext en'

__doc__ = """
:abstract: A distributed cloud storage server.
:version: %s
:author: %s
:contact: http://github.com/aakashhemadri
:date: 2020-02-01
:copyright: %s
""" % (__version__, __author__, __license__)

import os

from flask import Flask, Blueprint, json
from flask_restful import Resource, Api
from dcs.resources.files import Files,FilesList
from dcs.resources.hello import HelloWorld
from dcs.config import config
from dcs.utils import read_metadata, write_metadata

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
APP = []
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['UPLOAD_FOLDER'] = config['storage_directory']
    utils.write_metadata([])
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
    
    api.add_resource(Files, '/files', '/files/<string:id>')
    api.add_resource(FilesList, '/files/list')
    api.add_resource(HelloWorld, '/')
    app.register_blueprint(api_bp)
    APP = app
    return app