import unittest
from app.api.base.base_sql import Sql
from app.api.src.touches_from_api import get_google

class TestSetPathIfNotExists(unittest.TestCase):

    def test_set_path_if_not_exists(self):

        # sql_query = """table Geo """
        #
        # sql_query = 'select * from Geo where x = 0'
        #
        # result = Sql.exec(sql_query)
        #
        # print(result)
        # for row in result:
        #     print(row)
        #
        # print('\nGeo_distance\n')
        #
        # sql_query = """table geo_distance """
        #
        # result = Sql.exec(sql_query)
        #
        # for row in result:
        #     print(row)

        sql_query = """table Geo """
        points = Sql.exec(sql_query)
        inc = 1
        for i in points:
            for j in points:
                print ('step {}'.format(str(inc)))
                inc += 1
                answer = None
                is_exists = Sql.exec(query="""select
                                                exists(select 1 from geo_distance where point_1 = {po1} and point_2 = {po2}) tuda,
                                                exists(select 1 from geo_distance where point_1 = {po2} and point_2 = {po1}) obratno
                                                """.format(po1=i['id'], po2=j['id']))

                if is_exists[0]['tuda'] is False or is_exists[0]['obratno'] is False:
                    print(is_exists)

                    if i['id'] == j['id']:
                        answer = 0
                    data = []
                    disti = str(i['x']) + "," + str(i['y'])
                    distj = str(j['x']) + "," + str(j['y'])
                    data.append(disti)
                    data.append(distj)
                    answer = answer if answer else get_google(data)
                    print(i['id'], j['id'], answer)
                    sql = "INSERT INTO geo_distance (point_1, point_2, distance) VALUES ({}, {}, {})".format(
                        i['id'],
                        j['id'],
                        answer)
                    Sql.exec(query=sql)

                    Sql.exec(query="INSERT INTO geo_distance (point_1, point_2, distance) VALUES ({}, {}, {})".format(
                        j['id'],
                        i['id'],
                        answer))

        print('MISSION COMPLEATE')