# coding=utf8
import json
import requests as req
from app.api.helpers.service import Gis as gs
from app.api.base.base_sql import Sql
from app.api.base import base_name as names

def get_from_google(query):
    """
    :param query: достопримечательности+город
    :return: list с точками
    """
    key = "AIzaSyDMIfc6_9K7574xu18dG6ayTuAWsZtEOgE"
    s = req.Session()
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}&language=ru".format(query,
                                                                                                          key)
    answer = s.get(url)
    answer = gs.converter(answer.text)['results']
    result = []
    for res in answer:
        js = {"name": res["name"],
              "description": res["place_id"],
              "x": None,
              "y": None,
              "rating": 0,
              "time": 0}
        if js["rating"]:
            js["rating"] = res["rating"]
        else:
            js["rating"] = 0
        js["x"] = res["geometry"]["location"]["lat"]
        js["y"] = res["geometry"]["location"]["lng"]
        js["type"] = res["types"][0]
        result.append(js)
    return result


def get_google(data):
    s = req.Session()
    key = "AIzaSyDMIfc6_9K7574xu18dG6ayTuAWsZtEOgE"
    url = """https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&mode=walking
    &origins={}&destinations={}&key={}""".format(data[0], data[1], key)
    answer = s.get(url)
    answer = json.loads(answer.text)['rows'][0]['elements'][0]['duration']['text'].split()
    if len(answer) > 2:
        return int(answer[0])*60+int(answer[2])
    else:
        return int(answer[0])


def set_time(point):
    """Установка времени пребывания на точке"""
    point['time'] = 30

def set_rating(point):
    """Установка популярности точки"""
    point['rating'] = 100

def add_new_point(new_point):
    path_list = []
    set_time(new_point)
    set_rating(new_point)
    sql = " INSERT INTO Geo (Name, X, Y, Type, Descript, Rating, Time) VALUES (\'{}\', {}, {}, \'{}\', \'{}\', {}, {}) RETURNING id".format(
        new_point[names.NAME],
        float(new_point[names.x]),
        float(new_point[names.y]),
        new_point[names.TYPE],
        new_point[names.DESCRIPTION],
        int(new_point[names.RATING]),
        int(new_point[names.TIME]))

    new_id = Sql.exec(query=sql)[0]['id']

    sql_cross_join = """
    select
      geo.id new_id,
      geo1.id other_id,
      geo.x::text || ',' || geo.y::text new_xy,
      geo1.x::text || ',' || geo1.y::text other_xy
    from
      geo
      cross join geo geo1
    where
      geo.id = {}
    """.format(new_id)

    paths_points = Sql.exec(query=sql_cross_join)

    for path in paths_points:
        other_id = path['other_id']
        data = [path['new_xy'], path['other_xy']]
        answer = get_google(data) if new_id != other_id else 0

        path_list.append('"{%s,%s,%s}"' % (new_id, other_id, answer))
        path_list.append('"{%s,%s,%s}"' % (other_id, new_id, answer)) if new_id != other_id else None

    data_insert = "'{%s}'" % ','.join(path_list)

    sql_insert = """insert into geo_distance
                      (point_1, point_2, distance)
                    select
                      t._data[1],
                      t._data[2],
                      t._data[3]
                    from
                      (
                      select _un::integer[] _data from unnest({data_insert}::text[]) _un
                      ) t
                      """.format(data_insert=data_insert)
    Sql.exec(sql_insert)


if __name__ == '__main__':
    list_places = [
        'accounting',
        'airport',
        'amusement_park',
        'aquarium',
        'art_gallery',
        'bakery',
        'bar',
        'beauty_salon',
        'bicycle_store',
        'book_store'
        'bowling_alley',
        'cafe',
        'campground',
        'church',

]
    for place in list_places:
        list_points = get_from_google(place+'+Новосибирск')
        for point in list_points:
            add_new_point(point)
    print
