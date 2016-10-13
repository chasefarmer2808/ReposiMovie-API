import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select * from movies where lower(title) like {}"

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_title(title):

    if '%' not in title:
        title = title.replace("'", "''").replace("’", "''").replace("ʼ", "''").lower()
        title = '\'%' + title + '%\''

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT.format(title))

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret
