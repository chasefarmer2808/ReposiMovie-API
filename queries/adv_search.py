import cx_Oracle

from config.config import *
from population.helper import noApos

ORACLE_CONN_STRING = sql_login

SQL_STATEMENT = (
                "WITH {} "
                "SELECT DISTINCT lnm0.movie_id, lnm0.title, lnm0.release_date, lnm0.budget, lnm0.revenue, lnm0.popularity, lnm0.rating_average, lnm0.rating_count, lnm0.overview, lnm0.poster_path, lnm0.run_time "
                    "FROM {} "
                    "{} "
                "INTERSECT "
                "SELECT * FROM ( "
                )

SQL_STATEMENT_DEFAULT = (
                "SELECT m.* FROM Movies m "
                    "INNER JOIN has_genre hg ON m.movie_id = hg.movie_id "
                    "INNER JOIN Genre g ON g.genre_id = hg.genre_id "
                    "INNER JOIN produced_by pb ON m.movie_id = pb.movie_id "
                    "INNER JOIN Company c ON c.company_id = pb.company_id "
                "WHERE "
                    "LOWER(m.title) like '%{}%' "
                    "AND TO_DATE(m.release_date, 'YYYY-MM-DD') > TO_DATE('{}', 'MM-DD-YYYY') "
                    "AND TO_DATE(m.release_date, 'YYYY-MM-DD') < TO_DATE('{}', 'MM-DD-YYYY') "
                    "AND m.rating_average {} "
                    "AND m.rating_count {} "
                    "AND m.revenue {} "
                    "AND m.budget {} "
                    "AND m.run_time {} "
                    "{} "
                    "{} "
                "GROUP BY m.movie_id, m.title, m.budget, m.overview, m.popularity, m.poster_path, m.release_date, m.rating_average, m.rating_count, m.revenue, m.run_time "
                "HAVING COUNT(DISTINCT g.name) >= {} "
                "AND COUNT(DISTINCT c.name) >= {} "
                "ORDER BY m.popularity DESC"
                )

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    columns = [column.lower() for column in columns]
    return [dict(zip(columns, row)) for row in cursor]

def get_movies_advanced(title, startDate, endDate, avgRating, ratingCount, revenue, budget, runtime, genres, companies, people, limit):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()
    ret = {}

    genreConditions = ""
    companyConditions = ""

    if (len(genres) > 0):
        genreConditions += "AND ("
        for i in range(0, len(genres)):
            if (i > 0):
                genreConditions += "OR "
            genreConditions += "g.name = '" + noApos(genres[i]) + "' "
        genreConditions += ") "

    if (len(companies) > 0):
        companyConditions += "AND ("
        for i in range(0, len(companies)):
            if (i > 0):
                companyConditions += "OR "
            companyConditions += "c.name = '" + noApos(companies[i]) + "' "
        companyConditions += ") "

    default = SQL_STATEMENT_DEFAULT.format(title.lower(), startDate, endDate, avgRating, ratingCount, revenue, budget, runtime, genreConditions, companyConditions, len(genres), len(companies))

    if not people:
        cursor.execute(default)
    else:
        table = (
            "likeNameMovie{} AS "
            "(SELECT * FROM nameMovie nm "
            "WHERE nm.name like '%{}%') "
            )
        tables = table.format(0,noApos(people[0]))
        fromTable = "likeNameMovie{} lnm{}"
        fromTables = fromTable.format(0,0)
        notEqual = "lnm0.movie_id = lnm{}.movie_id "
        if (len(people) == 1):
            notEquals = ""
        else:
            notEquals = "WHERE "
        for i in range(1,len(people)):
            if people[i]:
                tables += ", "
                tables += table.format(i,noApos(people[i]))
                fromTables += ", "
                fromTables += fromTable.format(i,i)
                if (i > 1):
                    notEquals += "AND "
                notEquals += notEqual.format(i,i)

        query = SQL_STATEMENT.format(tables, fromTables, notEquals).replace('\n', '') + default + ")"
        cursor.execute(query)

    ret = rows_to_dict_list(cursor)

    con.close()
    return ret[0:limit]


