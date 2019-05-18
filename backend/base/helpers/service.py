# -*- coding: utf-8 -*-
import json
from datetime import date, datetime


class Gis:
    @staticmethod
    def __converter_data(param):
        if isinstance(param, date):
            return param.strftime('%Y.%m.%d %H:%M:%S')
        if isinstance(param, datetime):
            return param.strptime(param, '%Y.%m.%d %H:%M:%S')

    @staticmethod
    def converter(js):
        """
        Метод преобразовывает передаваемый json в Dict и наоборот
        :param js: str или json
        :return: str или dict преобразованный элемент
        """
        return json.dumps(js, default=Gis.__converter_data) if isinstance(js, dict) \
            else json.loads(js)



