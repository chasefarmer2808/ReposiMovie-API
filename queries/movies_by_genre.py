import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select m.* "
                 "from "
                    "movies m "
                    "inner join has_genre hg on m.movie_id = hg.movie_id "
                    "inner join genre g on g.genre_id = hg.genre_id "
                 "where "
                    "{} "
                 "group by m.movie_id, m.title, m.budget, m.overview, m.popularity, m.poster_path, m.release_date, m.revenue, m.run_time "
                 "having count(*) = {}"
                 "order by popularity desc")


def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_genre(genres, limit):
    num_genres = len(genres)

    condition_sting = ''

    for i in range(0, num_genres):
        gen = "g.name like '{}'".format(genres[i])

        if i != num_genres - 1:
            gen = gen + ' or '

        condition_sting = condition_sting + gen

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT.format(condition_sting, num_genres).replace('\n', ''))

    ret = rows_to_dict_list(cursor)

    if limit == None:
        limit = len(ret)

    con.close()
    return ret[0:limit]