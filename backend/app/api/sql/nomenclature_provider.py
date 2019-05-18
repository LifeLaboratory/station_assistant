from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_list():
        query = """
    select *
    from nomenclature
                """
        # print(query)
        return Sql.exec(query=query)
