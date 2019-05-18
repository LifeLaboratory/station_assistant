from app.route.route_auth import Auth
from app.route.route_favicon import Favicon
from app.route.route_register import Register
from app.route.route_session import Session
from app.route.route_geo import GeoRoute
from app.route.route_geo_types import GeoTypesRoute
from app.route.route_all_touch import AllTouch
from app.route.route_set_point import RouteSetPoint

ROUTES = {
    Register: '/register',
    Auth: '/auth',
    #Search: '/search/<string:field>/<string:query>',
    # Nomenclature: '/get_list/{text:type}/{text:id_user}',
    Favicon: '/favicon.ico',
    Session: '/session',
    GeoRoute: '/geo',
    GeoTypesRoute: '/geo_types',
    AllTouch: '/all_touch',
    RouteSetPoint: '/set_point'
}
