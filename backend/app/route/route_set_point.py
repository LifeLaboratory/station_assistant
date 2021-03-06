from app.api.base import base_name as names
from app.api.base.base_router import BaseRouter
from app.api.src.touches_from_api import add_new_point
from app.config.config import HEADER


class RouteSetPoint(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.x, names.y, names.TYPE, names.NAME, names.DESCRIPTION,
                                 names.DATETIME, names.TIME, names.RATING]

    def post(self):
        self._read_args()
        add_new_point(self.data)
        return 'OK', HEADER


    def options(self):
        return "OK", 200, {'Access-Control-Allow-Origin': '*',
                                 'Access-Control-Allow-Methods': 'GET,POST,DELETE,PUT,OPTIONS',
                                 'Access-Control-Allow-Headers': 'X-Requested-With,Content-Type'}
