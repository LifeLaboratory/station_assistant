# coding=utf8
import json
import requests as req
from app.api.helpers.service import Gis as gs
from app.api.base.base_sql import Sql


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

    set_time(new_point)
    set_rating(new_point)
    sql = " INSERT INTO Geo (Name, X, Y, Type, Descript, Rating, Time) VALUES (\'{}\', {}, {}, \'{}\', \'{}\', {}, {})".format(
        new_point["name"],
        float(new_point["x"]),
        float(new_point["y"]),
        new_point["type"],
        new_point["description"],
        int(new_point["rating"]),
        int(new_point["time"]))
    Sql.exec(query=sql)

    sql = "SELECT id FROM Geo WHERE X={} AND Y={}".format(new_point["x"], new_point["y"])
    new_point["id"] = Sql.exec(query=sql)
    new_point["id"] = int(new_point["id"][0]['id'])
    points = Sql.exec(query="SELECT id, x, y FROM Geo WHERE id <> (SELECT last_value from geo_id_seq)")
    for i in range(len(points)):
        data = []
        disti = str(points[i]['x']) + "," + str(points[i]['y'])
        distj = str(new_point['x']) + "," + str(new_point['y'])
        data.append(disti)
        data.append(distj)
        answer = get_google(data)
        print(points[i]['id'], new_point['id'], answer)
        sql = "INSERT INTO geo_distance (point_1, point_2, distance) VALUES ({}, {}, {})".format(
            points[i]['id'],
            new_point['id'],
            answer)
        Sql.exec(query=sql)

        Sql.exec(query="INSERT INTO geo_distance (point_1, point_2, distance) VALUES ({}, {}, {})".format(
            new_point['id'],
            points[i]['id'],
            answer))


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
