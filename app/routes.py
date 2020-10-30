from flask_restful import Api
from app.resources import index


def init_app(app):
    api = Api(app, prefix="/doc-api")

    api.add_resource(index.Index, "/")
    api.add_resource(index.Document, "/get_document/<name>")
