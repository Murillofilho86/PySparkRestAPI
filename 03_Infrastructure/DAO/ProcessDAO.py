import datetime
from DAO.BaseDAO import BaseDAO

class ProcessDAO(BaseDAO):

    def Add(step, token, data):
        query = """
                insert into process
                    (step_id, token, data, date)
                values (%s, %s, %s, %s)
                """
        base = BaseDAO()
        base.Execute(query, (step, token, data, datetime.datetime.now()))