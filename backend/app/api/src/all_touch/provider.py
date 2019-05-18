from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_touch():
        query = """
        select * from geo
        """
        return Sql.exec(query=query)
