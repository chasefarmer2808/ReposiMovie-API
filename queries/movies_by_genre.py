import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select * from (select m.* "
                 "from "
                    "movies m "
                    "inner join has_genre hg on m.movie_id = hg.movie_id "
                    "inner join genre g on g.genre_id = hg.genre_id "
                 "where "
                    "{} "
                 "group by m.movie_id, m.title, m.budget, m.overview, m.popularity, m.poster_path, m.release_date, m.rating_average, m.rating_count, m.revenue, m.run_time "
                 "having count(*) = {}"
                 "order by popularity desc)")


def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_genre(genres, limit):
    global SQL_STATEMENT
    statement = SQL_STATEMENT

    num_genres = len(genres)

    condition_sting = ''

    for i in range(0, num_genres):
        gen = "lower(g.name) like '{}'".format(genres[i].lower())

        if i != num_genres - 1:
            gen = gen + ' or '

        condition_sting = condition_sting + gen

    if limit == 0:
        statement += ' where rownum > {}'
    else:
        statement += ' where rownum <= {}'

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(statement.format(condition_sting, num_genres, limit).replace('\n', ''))

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret
