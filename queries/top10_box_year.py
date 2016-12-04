import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select * from ( select * from MOVIES where RELEASE_DATE like {} AND budget > 0  order by (REVENUE - BUDGET) desc) where rownum <= 10"
#top 10 box office movies of the year

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_top10_box_year(year):

    if '%' not in year:
        year = year.replace("'", "''").replace("’", "''").replace("ʼ", "''")
        year = '\'%' + year + '%\''

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    test = SQL_STATEMENT.format(year)

    cursor.execute(SQL_STATEMENT.format(year))

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret