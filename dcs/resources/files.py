from flask import make_response, Response, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import json, uuid, os
from flask_restful import Resource
from dcs.config import config

class Files(Resource):
    def put(self):
        id_ = uuid.uuid4()
        id_ = str(id_)
        with open(config['storage_directory'] + "/metadata.json") as json_file:
            metadata = json.load(json_file)
        file = request.files['file']
        filename = secure_filename(file.filename)
        for iter_file in metadata:
            if(iter_file['file_name'] == filename):
                return Response("File Already Exists", 409, mimetype="text/plain")
        file.save(config['storage_directory'] + "/" +filename)
        metadata.append({
            "file_name": filename,
            "id": id_,
        })
        with open(config['storage_directory'] +  "/metadata.json", 'w') as outfile:
            json.dump(metadata, outfile)
        response = Response(id_, 200, mimetype="text/plain")
        return response

    def get(self, id):
        with open(config['storage_directory']+ "/metadata.json") as json_file:
            metadata = json.load(json_file)
        id = str(id)
        for it in metadata:
             if(it['id'] == id or it['file_name'] == id ):
                 return send_file('../uploads/' + it['file_name'])
        res = "requested object " + str(id) + " is not found"
        return res, 404

    def post(self):
        return {}, 200

    def delete(self, id):
        with open(os.path.join(config['storage_directory'], "metadata.json")) as json_file:
            metadata = json.load(json_file)
        id = str(id)
        temp = metadata
        for it in metadata:
            if(it['file_name'] == id or it['id'] == id):
                    temp = [i for i in metadata if not (i['id'] == id or i['file_name'] == id )]
                    os.remove(os.path.join(config['storage_directory'],it['file_name']))
                    with open(config['storage_directory'] +  "/metadata.json", 'w') as outfile:
                        json.dump(temp, outfile)
                    return ("object " + id + " deleted successfully"), 200
        return ("Requested object " + id + " is not found") , 404

class FilesList(Resource):
    def get(self):
        with open(os.path.join(config['storage_directory'], "metadata.json")) as json_file:
            metadata = json.load(json_file)
        if(metadata == []):
            return "", 200
        return metadata, 200
    def post(self):
        return {}, 200


