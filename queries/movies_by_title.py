import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_title(title):

    if '%' not in title:
        title = title.replace("'", "''").replace("’", "''").replace("ʼ", "''")
        title = '\'%' + title + '%\''

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    sql_statement = "select * from movies where title like {}".format(title)

    cursor.execute(sql_statement)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret
