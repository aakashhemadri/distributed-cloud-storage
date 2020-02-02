from flask import redirect
from flask_restful import Resource
from balance import balance

url_ = "http://127.0.0.1:500"

class Node(Resource):
    def get():
        nodes = balance() #[(,),(,),]
        location = "http://127.0.0.1:500" + str(node) + request.script_root + request.path
        resp = requests.get(location)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    def put():
        nodes = balance()
        location = "http://127.0.0.1:500" + str(node) + request.script_root + request.path
        resp = requests.put(location,json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    def post():
        nodes = balance()
        location = "http://127.0.0.1:500" + str(node) + request.script_root + request.path
        resp = requests.post(location,json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    def delete():
        nodes = balance()
        location = "http://127.0.0.1:500" + str(node) + request.script_root + request.path
        resp = requests.delete(location).content
        response = Response(resp.content, resp.status_code, headers)
        return response