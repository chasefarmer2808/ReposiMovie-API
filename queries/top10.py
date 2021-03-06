import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select * from (select * from MOVIES where budget > 0 and rating_count > 50 order by rating_average desc, popularity desc) where rownum <= 10"
#top 10 movies all time

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_top10():

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret