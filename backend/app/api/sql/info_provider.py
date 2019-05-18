from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_info(args):
        query = """
    select *
    from nomenclature
    where "id_nom" = {id_nom}
                """
        # print(query)
        return Sql.exec(query=query, args=args)
