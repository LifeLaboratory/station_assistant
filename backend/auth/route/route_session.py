# coding=utf-8
from base import base_errors as errors, base_name as names
from auth.api.src.Authentication import auth
from flask_restful import Resource


class Session(Resource):
    args = [names.LOGIN, names.PASSWORD, names.PAGE]

    def post(self):
        error, data = self.parse_data()
        if error == errors.OK:
            error, answer = auth(data)
            if error == errors.OK:
                return answer, {'Access-Control-Allow-Origin': '*'}
        return {names.SESSION: None}, {'Access-Control-Allow-Origin': '*'}

    def options(self):
        return "OK", errors.OK, {'Access-Control-Allow-Origin': '*',
                                 'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
                                 'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type'}
