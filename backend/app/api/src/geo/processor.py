from app.api.sql.register_provider import Provider
from app.api.base import base_name as names
from .provider import Provider
from .path import Path


def assemly_data(data):
    data_origin = (float(data.get(names.ORIGIN_X)), float(data.get(names.ORIGIN_Y)))
    data_destination = (float(data.get(names.DESTINATION_X)), float(data.get(names.DESTINATION_Y)))
    index_priority = []
    types = Provider().get_types()
    data[names.PRIORITY] = ['point_of_interest', 'florist', 'aquarium', 'church', 'park', 'amusement_park', 'restaurant',
                            'atm', 'bar', 'museum', 'bakery', 'accounting', 'airport', 'zoo', 'bank', 'pet_store', 'local_government_office']
    for priority in data.get(names.PRIORITY):
        index_priority.append(types.get(priority, 0))
    return (data_origin, data_destination), types, index_priority


def GeoProcessor(data):
    provider = Provider()
    datas, types, index_priority = assemly_data(data)
    answer = Path(datas[0], datas[1], data.get(names.TIME), index_priority, types).result
    if not answer['route']:
        return []
    route = answer['route'][0]
    new_route = []
    for i in range(len(route['name'])):
        dict_route = {}
        dict_route[names.NAME] = route[names.NAME][i]
        dict_route[names.x] = route['X'][i]
        dict_route[names.y] = route['Y'][i]
        dict_route[names.TIME] = route[names.TIME][i]
        dict_route[names.DESCR] = route[names.DESCR][i]
        dict_route[names.TYPE] = route[names.TYPE][i]
        new_route.append(dict_route)
    return new_route

