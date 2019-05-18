from app.route.route_auth import Auth
from app.route.route_favicon import Favicon
from app.route.route_register import Register
from app.route.route_session import Session


ROUTES = {
    Register: '/register',
    Auth: '/auth',
    #Search: '/search/<string:field>/<string:query>',
    # Nomenclature: '/get_list/{text:type}/{text:id_user}',
    Favicon: '/favicon.ico',
    Session: '/session'
}
