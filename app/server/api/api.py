from flask_restful import Api, Resource, reqparse
from flask import  Blueprint, jsonify, Response
import json
import os

api_blueprint = Blueprint('api', __name__,)
api = Api(api_blueprint )

class Documentation(Resource):
    def get(self):
        return {
            'command1': '/api/path1',
            'command2': '/api/path2',
            'command3': '/api/path3'
        }

api.add_resource(Documentation, '/api')
