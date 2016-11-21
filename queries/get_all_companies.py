import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select distinct company.company_id, company.name from company, produced_by "
                    "where company.company_id = produced_by.company_id")

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_all_companies():
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    cursor.execute(SQL_STATEMENT)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret