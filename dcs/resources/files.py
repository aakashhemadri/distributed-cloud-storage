from flask_restful import Resource
from dcs.config import config

class Files(Resource):
    def get(self):
        return {}, 200
    def post(self):
        return {}, 200
    def delete(self):
        return "Delete", 200

class FilesList(Resource):
    def get(self):
        return {}, 200
    def post(self):
        return {}, 200


