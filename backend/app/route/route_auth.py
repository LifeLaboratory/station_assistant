# coding=utf-8
from app.api.base import base_name as names
from app.api.src.authentication import auth
from app.api.base.base_router import BaseRouter


class Auth(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD]

    def post(self):
        self._read_args()
        answer = auth(self.data)
        return answer
