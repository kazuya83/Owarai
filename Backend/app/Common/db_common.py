import psycopg2
import psycopg2.extras
import global_value as g

class DBConnection:
    def __init__(self, database_name:str=None):
        self.con = psycopg2.connect(host=g.DB_HOST,
                            database=g.DB_DATABASE if database_name is None else database_name,
                            user=g.DB_USER,
                            password=g.DB_PASS)

    def execute_select_sql(self, sql, parameters=None):
        cursor = self.con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if parameters is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)
        results = cursor.fetchall()
        dict_result = []
        for row in results:
            dict_result.append(dict(row))
        self.con.commit()
        cursor.close()
        self.con.close()
        return dict_result

    def execute_sql(self, sql, parameters=None) -> None:
        cursor = self.con.cursor()
        if parameters is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)
        self.con.commit()
        self.con.close()