import cx_Oracle
import requests, json

from config.config import *

ORACLE_CONN_STRING = sql_login

def get_movie(title):
    con = cx_Oracle.connect(ORACLE_CONN_STRING)
    cursor = con.cursor()

    sql_statement = "select * from movies where title like {}".format(title)

    cursor.execute(sql_statement)

    ret = cursor.fetchall()

    con.close()

    return ret
