import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select distinct person.name, person.person_id from person, has_cast "
                 "where person.person_id = has_cast.person_id "
                 "order by person.name")

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_all_cast():
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    cursor.execute(SQL_STATEMENT)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret