import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = ("select movies.title, movies.movie_id, movies.poster_path from movies, has_crew, person "
                 "where movies.movie_id = has_crew.movie_id and "
                 "has_crew.person_id = person.person_id and "
                 "has_crew.job = 'Director' and "
                 "lower(person.name) like {}")

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movies_by_director(name):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    ret = {}

    if '%' not in name:
        name = name.replace("'", "''").replace("’", "''").replace("ʼ", "''").lower()
        name = '\'%' + name + '%\''

    cursor.execute(SQL_STATEMENT.format(name))

    ret = rows_to_dict_list(cursor)
    return ret