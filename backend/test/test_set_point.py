# coding=utf-8

import unittest
import requests as req
from app.api.base import base_name as names
from app.api.base.base_sql import Sql
from app.api.src.touches_from_api import add_new_point

class TestSetPoint(unittest.TestCase):

    def test_set_point(self):

        # origin_x = 55.02999
        # origin_y = 82.921098
        # type_point = 'museum'
        #
        # data = {
        #     names.x: origin_x,
        #     names.y: origin_y,
        #     names.TYPE: type_point,
        #     names.NAME: 'Музей имени Меня!',
        #     names.DESCRIPTION: 'Приходите и восхищайтесь!',
        #     names.DATETIME: "2019-03-31 21:03:30",
        # }
        origin_x = 55.03721400913637
        origin_y = 82.89763175646169
        type_point = "event"

        # data = {
        #     names.x: origin_x,
        #     names.y: origin_y,
        #     names.TYPE: type_point,
        #     names.NAME: 'Музей имени Меня!',
        #     names.DESCRIPTION: 'Приходите и восхищайтесь!',
        #     names.DATETIME: "2019-03-31 21:03:30",
        # }



        data = {"y":82.89763175646169,
         "x":55.03721400913637,
         "type":"event",
         "name":"12312312",
         "description":"213213123",
         "datetime":"2019-03-31 21:03:30",
         "time":"",
         "rating":100}

        req.post('http://127.0.0.1:13452/set_point', data=data)

        check_geo = Sql.exec(query="""select
                                        id
                                      from
                                        Geo
                                      where
                                        x = {origin_x}
                                        and y = {origin_y}
                                        and type = '{type_point}'
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
                                                    limit 1)
                                    """.format(point_1=check_geo[0]['id'], point_2=check_geo[0]['id']))

        self.assertEqual(True, bool(check_path))

        Sql.exec('delete from Geo where id = {}'.format(check_geo[0]['id']))
        Sql.exec("""delete from geo_distance
                    where
                      point_1 = {point_1}
                      or point_2 = {point_2}
                 """.format(point_1=check_geo[0]['id'], point_2=check_geo[0]['id']))


if __name__ == '__main__':
    unittest.main()
