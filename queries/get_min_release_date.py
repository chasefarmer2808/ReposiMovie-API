import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select min(release_date) from movies"

def get_min_release_date():
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT)

    ret = cursor.fetchall()[0][0]#rows_to_dict_list(cursor)

    con.close()
    return ret