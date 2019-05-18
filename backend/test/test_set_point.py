# coding=utf-8

import unittest
import requests as req
from app.api.base.base_sql import Sql

class TestSetPoint(unittest.TestCase):

    def test_set_point(self):

        origin_x = 0
        origin_y = 0
        type_point = 'museum'

        data = {
            'origin_x': origin_x,
            'origin_y': origin_y,
            'type': type_point,
            'name': 'Музей имени Меня!',
            'description': 'Приходите и восхищайтесь!',
            'datetime': 'infinity',
        }

        req.post('http://90.189.168.29:13451/set_point', data=data)

        check_geo = Sql.exec(query="""select
                                        id
                                      from
                                        Geo
                                      where
                                        x = {origin_x}
                                        and y = {origin_y}
                                        and type = {type_point})
                                      limit 1
                                      """.format(origin_x=origin_x, origin_y=origin_y, type_point=type_point))

        self.assertEqual(True, bool(check_geo))

        check_path = Sql.exec(query="""select exists(select
                                                      1
                                                    from
                                                      geo_distance
                                                    where
                                                      point_1 = {point_1}
                                                      or point_2 = {point_2}
                                                    limit 1
                                    """.format(point_1=check_geo[0]['id'], point_2=check_geo[0]['id']))

        self.assertEqual(True, bool(check_path))

        Sql.exec('delete from Geo where id = {}'.format(check_geo[0]['id']))
        Sql.exec("""delete from geo_distance
                    where
                      point_1 = {point_1}
                      or point_2 = {point_2}
                 """.format(point_1=check_geo[0]['id'], point_2=check_geo[0]['id']))