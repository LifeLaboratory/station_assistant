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
        get_sql = """select distinct type FROM geo where type!='point_of_interest' and type!='church' and type !='park' and
                type!='museum' and type!='zoo' and type!='funeral_home' and type!='premise' and type!='art_gallery'
                """
        dict_type = Sql.exec(query=get_sql)
        result = []
        for d in dict_type:
            result.append(d["type"])
        return {"data": result}

