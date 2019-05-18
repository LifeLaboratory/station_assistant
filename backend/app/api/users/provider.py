import app.api.base.base_name as names
import app.api.base.base_errors as errors
from app.api.base.base_sql import Sql


class UsersProvider:
    @staticmethod
    def auth_user(args):
        query = """
  insert into "session"("session", "id_user")
  select md5(random()::text || clock_timestamp()::text)::uuid
    , "id_user"
    from (
      select "id_user"
      from "users"
      where "login" = '{Login}'
        and "password" = '{Password}'
      limit 1
    )
    where "id_user" is not null
    returning "session" as "Session"
        """
        data = Sql.exec(query=query, args=args)
        return

    @staticmethod
    def select_user(args):
        if args[names.PAGE] == "client":
            args[names.PAGE] = 0
        if args[names.PAGE] == "employee":
            args[names.PAGE] = 1
        query = """
                    insert into "session"("session", "id_user")
                    select md5(random()::text || clock_timestamp()::text)::uuid
                    , "id_user"
                    from (
                      select (
                      select "id_user"
                      from "users"
                      where "login" = '{Login}'
                        and "password" = '{Password}'
                        and "privilege" = {Pages}
                      limit 1
                      ) )"id_user"
                    where "id_user" is not null
                    returning "session" as "Session"
                """.format(Login=args[names.LOGIN], Password=args[names.PASSWORD], Pages=args[names.PAGE])
        # print(query)
        try:
            auth_data = Sql.exec(query=query)
        except:
            return errors.SQL_ERROR, None
        if auth_data == errors.SQL_ERROR or auth_data[0] is None:
            return errors.SQL_ERROR, None
        else:
            return errors.OK, auth_data[0]

    @staticmethod
    def select_status_user(args):
        query = """
  select "status_pack"
  from "users"
  where "id_user" = (select id_user from session where session = '{Session}')
                """.format(**args)
        # print(query)
        try:
            auth_data = Sql.exec(query=query)
        except:
            return errors.SQL_ERROR, None
        if auth_data == errors.SQL_ERROR:
            return errors.SQL_ERROR, None
        else:
            return errors.OK, auth_data[0]
