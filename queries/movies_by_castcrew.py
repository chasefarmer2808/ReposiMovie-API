import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = (
                "WITH {} "
                "SELECT DISTINCT lnm0.movie_id, lnm0.title, lnm0.budget, lnm0.overview, lnm0.popularity, lnm0.rating_average, lnm0.rating_count, lnm0.poster_path, lnm0.release_date, lnm0. revenue, lnm0.run_time "
                    "FROM {} "
                    "{} "
                    "order by lnm0.popularity desc "
                )

SQL_STATEMENT_DEFAULT = "SELECT * FROM Movies"

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_castcrew(name):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    ret = {}

    if not name:
        cursor.execute(SQL_STATEMENT_DEFAULT)
    elif not name[0]:
        cursor.execute(SQL_STATEMENT_DEFAULT)
    else:
        table = (
            "likeNameMovie{} AS "
            "(SELECT * FROM nameMovie nm "
            "WHERE nm.name like '%{}%') "
            )
        tables = table.format(0,name[0])
        fromTable = "likeNameMovie{} lnm{}"
        fromTables = fromTable.format(0,0)
        notEqual = "lnm0.movie_id = lnm{}.movie_id "
        if (len(name) == 1):
            notEquals = ""
        else:
            notEquals = "WHERE "
        for i in range(1,len(name)):
            if name[i]:
                tables += ", "
                tables += table.format(i,name[i])
                fromTables += ", "
                fromTables += fromTable.format(i,i)
                if (i > 1):
                    notEquals += "AND "
                notEquals += notEqual.format(i,i)

        cursor.execute(SQL_STATEMENT.format(tables, fromTables, notEquals).replace('\n', ''))

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret


