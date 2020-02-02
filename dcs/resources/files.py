import json, uuid, os

from flask import make_response, Response, flash, request, redirect, url_for, send_file
from flask_restful import Resource
from werkzeug.utils import secure_filename

from dcs.config import config
from dcs.utils import read_metadata, write_metadata

class Files(Resource):
    def put(self):
        id_ = uuid.uuid4()
        id_ = str(id_)
        metadata = read_metadata()
        file = request.files['file']
        filename = secure_filename(file.filename)
        if(filename == ""):
            return "No file sent", 200
        for iter_file in metadata:
            if(iter_file['file_name'] == filename):
                return Response("File Already Exists", 409, mimetype="text/plain")
        file.save(config['storage_directory'] + '/' + filename)
        metadata.append({
            "file_name": filename,
            "id": id_,
        })
        write_metadata(metadata)
        return Response(id_, 200, mimetype="text/plain")

    def get(self, id):
        metadata = read_metadata()
        id = str(id)
        for it in metadata:
             if(it['id'] == id or it['file_name'] == id ):
                 return send_file('../uploads/' + it['file_name'])
        return Response("requested object " + str(id) + " is not found", 404)

    def delete(self, id):
        metadata = read_metadata()
        id = str(id)
        for it in metadata:
            if(it['file_name'] == id or it['id'] == id):
                    metadata = [i for i in metadata if not (i['id'] == id or i['file_name'] == id )]
                    os.remove(os.path.join(config['storage_directory'],it['file_name']))
                    write_metadata(metadata)
                    return Response(("object " + id + " deleted successfully"), 200)
        return Response(("Requested object " + id + " is not found") , 404)

class FilesList(Resource):
    def get(self):
        metadata = read_metadata()
        if(metadata == []):
            return "", 200
        return metadata, 200


