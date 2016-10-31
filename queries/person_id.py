import cx_Oracle

from config.config import *

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT1 = (
    "select * from person "
        "where person_id = {}"
                 )

SQL_STATEMENT2 = (
    "select m.movie_id, m.title, m.release_date, m.poster_path, hc.role from person p "
        "join has_cast hc "
            "on p.person_id = hc.person_id "
        "join movies m "
            "on hc.movie_id = m.movie_id "
        "where p.person_id = {}"
                 )

SQL_STATEMENT3 = (
    "select m.movie_id, m.title, m.release_date, m.poster_path, hc.job, hc.department from person p "
        "join has_crew hc "
            "on p.person_id = hc.person_id "
        "join movies m "
            "on hc.movie_id = m.movie_id "
        "where p.person_id = {}"
                 )

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_person_by_id(person_id):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    cursor.execute(SQL_STATEMENT1.format(person_id).replace('\n', ''))

    person = rows_to_dict_list(cursor)

    if cursor.rowcount == 0:
        ret = {'error' : 'Error: person not found'}

    else:
        ret = person[0]
        cursor.execute(SQL_STATEMENT2.format(person_id).replace('\n', ''))
        ret['roles'] = rows_to_dict_list(cursor)
        cursor.execute(SQL_STATEMENT3.format(person_id).replace('\n', ''))
        ret['jobs'] = rows_to_dict_list(cursor)

    con.close()
    return ret
