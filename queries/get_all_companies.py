import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select distinct name from company "
                    "order by company.name")

def rows_to_array(cursor):
    return [row[0] for row in cursor]

def get_all_companies():
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    cursor.execute(SQL_STATEMENT)

    ret = rows_to_array(cursor)

    con.close()
    return ret
