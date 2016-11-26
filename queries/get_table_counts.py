import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select distinct count(*) as {} from {}"
TABLE_NAMES = ['movies', 'person', 'genre', 'company', 'has_cast', 'has_crew', 'has_genre', 'produced_by']

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_table_counts():
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    ret = []

    for table in TABLE_NAMES:
        cursor.execute(SQL_STATEMENT.format(table, table))
        count = rows_to_dict_list(cursor)
        ret.append(count[0])

    con.close()
    return ret