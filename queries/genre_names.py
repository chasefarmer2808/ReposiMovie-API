import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select name from genre"

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_genres():

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT)

    #ret = cursor.fetchall()
    ret = []

    for row in cursor:
        ret.append(row[0])

    con.close()
    return ret