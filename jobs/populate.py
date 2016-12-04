import cx_Oracle
import requests, json
import datetime
import time
import yaml
from config.config import *

DATE_FORMAT = '%Y-%m-%d'
API_KEY = api_key

MIN_DATE = '2015-01-01'
SORT_BY = 'primary_release_date.asc'
LANGUAGE = 'en'
DISCOVER_URL = 'https://api.themoviedb.org/3/discover/movie'
ID_URL = 'https://api.themoviedb.org/3/movie/{}'

DISCOVER_PAYLOAD = {'api_key': API_KEY,
                    'primary_release_date.gte': MIN_DATE,
                    'sort_by': SORT_BY,
                    'original_language': LANGUAGE,
                    'vote_count.gte': 1}

ID_PAYLOAD = {'api_key': API_KEY}
SLEEP_TIME_SECONDS = 11

ORACLE_CONN_STRING = sql_login

SELECT_STATEMENT = 'select ID from Movie where ID = {}'
INSERT_STATEMENT = "insert into Movie values ('{}', to_date('{}', \'YYYY-MM-DD\'), '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
MAX_DATE_STATEMENT = "select max(release_date) from Movies"

con = cx_Oracle.connect(ORACLE_CONN_STRING)
#con.close()
cursor = con.cursor()


def request_movie_db(url, payload):
    ret = requests.get(url, params=payload).text
    ret = json.loads(ret)

    try:
        if ret['status_code']:
            time.sleep(SLEEP_TIME_SECONDS)

            ret = requests.get(url, params=payload).text
            ret = json.loads(ret)

    except KeyError:
        print('Have not reached limit')

    return ret

def get_max_date():
    cursor.execute(MAX_DATE_STATEMENT)

    res = cursor.fetchall()

    if res:
        date = res[0][0]
        DISCOVER_PAYLOAD['primary_release_date.gte'] = date.strftime(DATE_FORMAT)
        return res

#get_max_date()

r = request_movie_db(DISCOVER_URL, DISCOVER_PAYLOAD)
print(r)

bad_char_count = 0

for i in range(1, r['total_pages']):  #For each page
    print('######', i)
    DISCOVER_PAYLOAD['page'] = i
    r = request_movie_db(DISCOVER_URL, DISCOVER_PAYLOAD)

    for j in range(0, len(r['results'])):  #for each movie in a page
        curr_id = r['results'][j]['id']
        print(curr_id)

        #todo:
        #1. check for release date

        curr_movie = request_movie_db(ID_URL.format(str(curr_id)), ID_PAYLOAD)

        curr_movie['title'] = curr_movie['title'].replace("'", "`")

        try:
            curr_movie['overview'] = curr_movie['overview'].replace("'", "`")
        except AttributeError:
            pass

        cursor.execute(SELECT_STATEMENT.format(curr_id))
        res = cursor.fetchall()

        #if len(res) == 0:
        statement = INSERT_STATEMENT.format(curr_movie['title'], curr_movie['release_date'], str(curr_movie['budget']), str(curr_movie['revenue']), str(curr_movie['popularity']), curr_movie['overview'], curr_movie['poster_path'], str(curr_movie['runtime']), str(curr_id))

        try:
            cursor.execute(statement)
            print('inserting: ', statement)
            con.commit()
        except UnicodeEncodeError:
            bad_char_count += 1
            print(bad_char_count)
        except cx_Oracle.IntegrityError:
            print(statement)
