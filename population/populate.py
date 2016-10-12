import cx_Oracle
import requests
from config import *
from helper import *
import time
import math
import os

os.environ["NLS_LANG"] = ".AL32UTF8"

last_page = 0 #0 if new year or last page printed (before error)

db = cx_Oracle.connect(sql_login)
cursor = db.cursor()

#helper functions for testing, don't uncomment
#resetTables(cursor)
#deleteTables(cursor)
#remakeTables(cursor)
db.commit()

#prints number of records in each table
printCount(cursor)

start_time = time.time()
movie = 'https://api.themoviedb.org/3/movie/'

for year in range(2015,2016):
    discover = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&primary_release_year=' + str(year) + '&api_key=' + api_key + '&page='
    records = 0
    for page in range(last_page + 1,101):
        r1 = requests.get(discover + str(page)).json()
        while ('results' not in r1):
            time.sleep(.25)
            r1 = requests.get(discover + str(page)).json()
        r1 = r1['results']
        for i in range(0,20):
            skip = 0
            if ((r1[i]['original_language'] == 'en') and (r1[i]['id'] not in [])):#[50400,51200,51245,68381,72098,91186,106530,121106,132563,139300,191112,213478,231935,257836,268207,292871,293122,321392])):
                r2 = requests.get(movie + str(r1[i]['id']) + '?api_key=' + api_key).json()
                while ('status_code' in r2):
                    if (r2['status_code'] != 25):
                        skip = 1
                        break
                    time.sleep(.25)
                    r2 = requests.get(movie + str(r1[i]['id']) + '?api_key=' + api_key).json()
                if skip:
                    continue
                if ('en' not in [o['iso_639_1'] for o in r2['spoken_languages']]):
                    continue
                dbcall = 'insert into movies values(' + str(r2['id']) + ','
                dbcall = dbcall + "N'" + noApos(r2['title']) + "',"
                dbcall = dbcall + "'" + str(r2['release_date']) + "',"
                dbcall = dbcall + str(r2['budget']) + ','
                dbcall = dbcall + str(r2['revenue']) + ','
                dbcall = dbcall + str(r2['popularity']) + ','
                dbcall = dbcall + "N'" + noApos(r2['overview']) + "',"
                dbcall = dbcall + "'" + str(r2['poster_path']) + "',"
                dbcall = dbcall + str(r2['runtime']) + ")"
                cursor.execute(dbcall)
                records = records + 1
                for genre in r2['genres']:
                    dbcall = 'select count(*) from genre where genre_id = ' + str(genre['id'])
                    if (cursor.execute(dbcall).fetchall()[0][0] == 0):
                        dbcall = 'insert into genre values(' + str(genre['id']) + ','
                        dbcall = dbcall + "'" + noApos(genre['name']) + "')"
                        cursor.execute(dbcall)
                        records = records + 1
                    dbcall = 'insert into has_genre values(' + str(r2['id']) + ','
                    dbcall = dbcall + str(genre['id']) + ')'
                    cursor.execute(dbcall)
                    records = records + 1
                for company in r2['production_companies']:
                    dbcall = 'select count(*) from company where company_id = ' + str(company['id'])
                    if (cursor.execute(dbcall).fetchall()[0][0] == 0):
                        dbcall = 'insert into company values(' + str(company['id']) + ','
                        dbcall = dbcall + "'" + noApos(company['name']) + "')"
                        cursor.execute(dbcall)
                        records = records + 1
                    dbcall = 'insert into produced_by values(' + str(r2['id']) + ','
                    dbcall = dbcall + str(company['id']) + ')'
                    cursor.execute(dbcall)
                    records = records + 1
                r3 = requests.get(movie + str(r1[i]['id']) + '/credits?api_key=' + api_key).json()
                while ('status_code' in r3):
                    time.sleep(.25)
                    r3 = requests.get(movie + str(r1[i]['id']) + '/credits?api_key=' + api_key).json()
                for person in r3['cast']:
                    dbcall = 'select count(*) from person where person_id = ' + str(person['id'])
                    if (cursor.execute(dbcall).fetchall()[0][0] == 0):
                        dbcall = 'insert into person values(' + str(person['id']) + ','
                        dbcall = dbcall + "N'" + noApos(person['name']) + "',"
                        dbcall = dbcall + "'" + str(person['profile_path']) + "')"
                        cursor.execute(dbcall)
                        records = records + 1
                    dbcall = 'insert into has_cast values(' + str(r2['id']) + ','
                    dbcall = dbcall + str(person['id']) + ','
                    dbcall = dbcall + "N'" + noApos(str(person['character'])) + "',"
                    dbcall = dbcall + str(person['order']) + ')'
                    cursor.execute(dbcall)
                    records = records + 1
                for person in r3['crew']:
                    dbcall = 'select count(*) from person where person_id = ' + str(person['id'])
                    if (cursor.execute(dbcall).fetchall()[0][0] == 0):
                        dbcall = 'insert into person values(' + str(person['id']) + ','
                        dbcall = dbcall + "N'" + noApos(person['name']) + "',"
                        dbcall = dbcall + "'" + str(person['profile_path']) + "')"
                        cursor.execute(dbcall)
                        records = records + 1
                    dbcall = 'insert into has_crew values(' + str(r2['id']) + ','
                    dbcall = dbcall + str(person['id']) + ','
                    dbcall = dbcall + "N'" + noApos(str(person['job'])) + "',"
                    dbcall = dbcall + "N'" + noApos(str(person['department'])) + "')"
                    cursor.execute(dbcall)
                    records = records + 1
        db.commit()
        elapsed = time.time() - start_time
        print("page:", page, "Total time: ", math.floor(elapsed/3600),":", (math.floor(elapsed/60))%60,":",math.floor(elapsed)%60)


elapsed = time.time() - start_time

cursor.close()
db.close()

print(records)
print("Total time: ", math.floor(elapsed/3600),":", (math.floor(elapsed/60))%60,":",math.floor(elapsed)%60)
