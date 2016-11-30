import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select * from person where lower(name) like {}"

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_people_by_name(name, limit):
    global SQL_STATEMENT
    statement = SQL_STATEMENT

    if '%' not in name:
        name = name.replace("'", "''").replace("’", "''").replace("ʼ", "''").lower()
        name = '\'%' + name + '%\''

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    if limit == 0:
        statement += ' and rownum > {}'
    else:
        statement += ' and rownum <= {}'

    cursor.execute(statement.format(name, limit))

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret
