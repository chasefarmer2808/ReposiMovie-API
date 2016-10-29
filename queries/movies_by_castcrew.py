import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = (
                "WITH likeNameMovie1 AS "
                    "(SELECT * FROM nameMovie nm "
                     "WHERE nm.name like '{}'), "
                     "likeNameMovie2 AS "
                    "(SELECT * FROM nameMovie nm "
                     "WHERE nm.name like '{}') "
                "SELECT DISTINCT lnm1.movie_id, lnm1.title, lnm1.budget, lnm1.overview, lnm1.popularity, lnm1.poster_path, lnm1.release_date, lnm1. revenue, lnm1.run_time "
                    "FROM likeNameMovie1 lnm1, likeNameMovie2 lnm2 "
                    "WHERE lnm1.movie_id = lnm2.movie_id "
                    "AND lnm1.name <> lnm2.name "
                )

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_castcrew(name1, name2, limit):
    if '%' not in name1:
        name1 = '%' + name1 + '%'

    if '%' not in name2:
        name2 = '%' + name2 + '%'

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT.format(name1, name2).replace('\n', ''))

    ret = rows_to_dict_list(cursor)

    if limit == None:
        limit = len(ret)

    con.close()
    return ret[0:limit]


