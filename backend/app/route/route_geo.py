# coding=utf-8
from app.api.base import base_name as names
from app.api.src.geo.processor import GeoProcessor
from app.api.base.base_router import BaseRouter
from app.config.config import HEADER


class GeoRoute(BaseRouter):
    def __init__(self):
        super().__init__()
        self.args = [names.ORIGIN_X, names.ORIGIN_Y, names.DESTINATION_Y,
                     names.DESTINATION_X, names.TIME, names.PRIORITY]

    def get(self):
        self._read_args()
        answer = GeoProcessor(self.data)
        return answer, HEADER
