import unittest
import requests as req
from app.config.config import HOST
import app.api.base.base_name as names
from app.api.src.authentication import auth
from app.api.helpers.service import Gis


class TestAuth(unittest.TestCase):
    def test_auth_back_client(self):
        data = {
                names.LOGIN: 'boris',
                names.PASSWORD: 'boris'
                }
        data = req.post('http://127.0.0.1/auth', data=data)
        self.assertEqual(data.status_code, 200)
        self.assertIsNotNone(data.text)
        print(data.text)
        return

    def test_register_back_client(self):
        data = {
                names.LOGIN: 'boris2',
                names.PASSWORD: 'boris',
                names.NAME: 'boris'
                }
        data = req.post('http://127.0.0.1/register', data=data)
        self.assertEqual(data.status_code, 200)
        self.assertIsNotNone(data.text)
        print(data.text)
        return

    def test_list_nom_back_client(self):
        data = req.get('http://127.0.0.1/get_list')
        self.assertEqual(data.status_code, 200)
        self.assertIsNotNone(data.text)
        print(data.text)
        return

    def test_search_nom_back_client(self):
        data = req.get('http://127.0.0.1/search/code/терафлю')
        self.assertEqual(data.status_code, 200)
        self.assertIsNotNone(data.text)
        print(data.text)
        return

    def test_info_nom_back_client(self):
        data = req.get('http://127.0.0.1/info/1')
        self.assertEqual(data.status_code, 200)
        self.assertIsNotNone(data.text)
        print(data.text)
        return

    def test_auth_back_staff(self):
        data = {
                names.LOGIN: 'andrey',
                names.PASSWORD: 'andrey',
                names.PAGE: 'employee'
                }
        result = auth(data)
        self.assertEqual(result[0], 200)
        self.assertTrue(result[1], None)
        return

    def test_auth_front_client(self):
        s = req.Session()
        data = {
                names.LOGIN: "ololol' and 1=2 or id_user=65 or 1=2--",
                names.PASSWORD: "boris",
                names.PAGE: 'client'
                }
        r = s.post(HOST + '/api/v1/auth', data=data)
        result = Gis.converter(r.text)
        print(result)
        self.assertTrue(result.get(names.SESSION, None), None)
        return

    def test_auth_front_staff(self):
        s = req.Session()
        data = {
                names.LOGIN: 'andrey',
                names.PASSWORD: 'andrey',
                names.PAGE: 'employee'
                }
        r = s.post(HOST + '/api/v1/auth', data=data)
        result = Gis.converter(r.text)
        self.assertTrue(result.get(names.SESSION, None), None)
        return

    def test_auth_none(self):
        s = req.Session()
        data = {names.LOGIN: 'boris'}
        r = s.post(HOST + '/api/v1/auth', data=data)
        result = Gis.converter(r.text)
        self.assertEqual(result.get(names.SESSION), None)
        return


if __name__ == '__main__':
    unittest.main()
