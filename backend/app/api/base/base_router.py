# coding=utf-8
from flask_restful import Resource, reqparse
from app.api.base import base_name as names
import json


class BaseRouter(Resource):
    _args = []

    def __init__(self):
        self.args = None
        self.data = dict()

        self._parser = reqparse.RequestParser()

    def _read_args(self):
        for arg in self.args:
            self._parser.add_argument(arg)
        self.data = self._parser.parse_args()
        for arg in self.args:
            self.data[arg] = json.loads(self.data.get(arg))

    def get(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def delete(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def put(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*'}

