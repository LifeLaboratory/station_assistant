from app.api.sql.register_provider import Provider
from app.api.base import base_name as names
from .provider import Provider
import json


def AllProcessor(data):
    provider = Provider()
    list_touch = provider.get_touch()
    return list_touch

