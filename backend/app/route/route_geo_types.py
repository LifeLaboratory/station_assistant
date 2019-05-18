# coding=utf-8
from app.api.base.base_router import BaseRouter
from app.config.config import HEADER
from app.api.src.geo.provider import Provider


class GeoTypesRoute(BaseRouter):
    def __init__(self):
        super().__init__()

    def get(self):
        answer = Provider().get_types()
        return answer, HEADER
