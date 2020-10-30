import os
from flask_restful import Resource, reqparse
from flask import send_file


class Index(Resource):
    def get(self):
        return "Pagina de API DOC"


class Document(Resource):
    def get(self, name):
        url = f"C:/Users/5154/Documents/{name}"

        return send_file(url, as_attachment=True)
