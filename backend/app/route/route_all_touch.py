# coding=utf-8
from app.api.base import base_name as names
from app.api.src.all_touch.processor import AllProcessor
from app.api.base.base_router import BaseRouter
from app.config.config import HEADER
import json


class AllTouch(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.ORIGIN_X, names.ORIGIN_Y, names.DESTINATION_Y,
                     names.DESTINATION_X, names.TIME, names.PRIORITY]

    def get(self):
        #self._read_args()
        answer = AllProcessor(self.data)
        return answer, HEADER

    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*',
                                 'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
                                 'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type'}