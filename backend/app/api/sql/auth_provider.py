from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def auth_user(args):
        query = """
    select id_user
    from users
    where "login" = '{login}'
      and "password" = '{password}'
                """
        # print(query)
        return Sql.exec(query=query, args=args)
