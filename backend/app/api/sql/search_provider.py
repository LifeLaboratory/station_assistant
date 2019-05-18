from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def search_nom(args):
        query = """
    select *
    from nomenclature
    where "{field}" = '{query}'
     """
        # print(query)
        return Sql.exec(query=query, args=args)
