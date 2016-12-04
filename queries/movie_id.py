import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT1 = (
    "select * from movies "
        "where movie_id = {}"
                 )

SQL_STATEMENT2 = (
    "select p.*, hc.role, hc.ord from movies m "
        "join has_cast hc "
            "on m.movie_id = hc.movie_id "
        "join person p "
            "on hc.person_id = p.person_id "
        "where m.movie_id = {}"
                 )

SQL_STATEMENT3 = (
    "select p.*, hc.job, hc.department from movies m "
        "join has_crew hc "
            "on m.movie_id = hc.movie_id "
        "join person p "
            "on hc.person_id = p.person_id "
        "where m.movie_id = {}"
                 )

SQL_STATEMENT4 = (
    "select g.* from movies m "
        "join has_genre hg "
            "on m.movie_id = hg.movie_id "
        "join genre g "
            "on hg.genre_id = g.genre_id "
        "where m.movie_id = {}"
                 )

SQL_STATEMENT5 = (
    "select c.* from movies m "
        "join produced_by pb "
            "on m.movie_id = pb.movie_id "
        "join company c "
            "on pb.company_id = c.company_id "
        "where m.movie_id = {}"
                 )

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movie_by_id(movie_id):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT1.format(movie_id).replace('\n', ''))

    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    movie = [dict(zip(columns, row)) for row in cursor]

    if cursor.rowcount == 0:
        ret = {'error' : 'Error: movie not found'}

    else:
        ret = movie[0]
        cursor.execute(SQL_STATEMENT2.format(movie_id).replace('\n', ''))
        ret['cast'] = rows_to_dict_list(cursor)
        cursor.execute(SQL_STATEMENT3.format(movie_id).replace('\n', ''))
        ret['crew'] = rows_to_dict_list(cursor)
        cursor.execute(SQL_STATEMENT4.format(movie_id).replace('\n', ''))
        ret['genres'] = rows_to_dict_list(cursor)
        cursor.execute(SQL_STATEMENT5.format(movie_id).replace('\n', ''))
        ret['production_companies'] = rows_to_dict_list(cursor)

    con.close()
    return ret
