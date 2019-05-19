# coding=utf-8
from app.api.base import base_name as names
from app.api.src.authentication import auth
from app.api.base.base_router import BaseRouter


class Session(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD]

    def post(self):
        self._read_args()
        answer = auth(self.data)
        return answer

    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*',
                                 'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
                                 'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type'}