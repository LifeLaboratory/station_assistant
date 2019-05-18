from auth.route.route_auth import Service
from auth.route.route_favicon import Favicon
from auth.route.route_session import Session


ROUTES = {
    Service: '/auth',
    Favicon: '/favicon.ico',
    Session: '/session'
}
