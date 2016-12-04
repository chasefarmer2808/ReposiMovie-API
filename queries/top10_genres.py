import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login
SQL_STATEMENT = "select * from ( select genre.NAME, avg(movies.POPULARITY), avg(movies.RATING_AVERAGE) from movies, has_genre, genre where movies.MOVIE_ID = has_genre.MOVIE_ID AND genre.GENRE_ID = has_genre.GENRE_ID and budget > 0 group by genre.name order by avg(movies.POPULARITY) desc) where rownum <= 10"

#Most Popular Genres
#could change the average of the movie ratings of each genre and sort by that


def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_top10_genres():

    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret