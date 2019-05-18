from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def check_user(args):
        query = """
  select 1
  from users
  where "login" = '{login}'
    and "password" = '{password}'
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_types():
        get_sql = """select distinct type FROM geo"""
        dict_type = Sql.exec(query=get_sql)
        result = []
        for d in dict_type:
            result.append(d["type"])
        return {"data": result}

