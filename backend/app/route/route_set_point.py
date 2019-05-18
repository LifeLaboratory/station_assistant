from app.api.base import base_name as names
from app.api.base.base_router import BaseRouter
from app.api.src.touches_from_api import add_new_point
from app.config.config import HEADER


class RouteSetPoint(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = self.args = [names.ORIGIN_X, names.ORIGIN_Y, names.TYPE, names.TIME, names.DESCRIPTION,
                                 names.DATETIME, names.TIME, names.RATING]

    def post(self):
        self._read_args()
        add_new_point(self.data)
        return 'OK', HEADER
