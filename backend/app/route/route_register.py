# coding=utf-8
from app.api.base import base_name as names
from app.api.src.registration import register
from app.api.base.base_router import BaseRouter


class Register(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD, names.NAME]

    def post(self):
        self._read_args()
        answer = register(self.data)
        return answer

    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*',
                                 'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
                                 'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type'}