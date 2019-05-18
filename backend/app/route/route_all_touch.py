# coding=utf-8
from app.api.base import base_name as names
from app.api.src.all_touch.processor import AllProcessor
from app.api.base.base_router import BaseRouter
import json


class AllTouch(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.ORIGIN_X, names.ORIGIN_Y, names.DESTINATION_Y,
                     names.DESTINATION_X, names.TIME, names.PRIORITY]

    def get(self):
        #self._read_args()
        answer = AllProcessor(self.data)
        return answer
