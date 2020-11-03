import os
from flask_restful import Resource, reqparse
from flask import send_file

UPLOAD_DIRECTORY = 'C:/Users/5154/Documents/'


class Index(Resource):
    def get(self):
        files = []

        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)

            if os.path.isfile(path):
                files.append(filename)
        
        return files


class Document(Resource):
    def get(self, name):
        for file in os.listdir(UPLOAD_DIRECTORY):
            if file.split('.')[0] == name:
                document = file
                
                return send_file(f'{UPLOAD_DIRECTORY}/{file}', as_attachment=True)

