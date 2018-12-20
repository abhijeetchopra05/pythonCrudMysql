#  With Python 3 MYSQLdb is not supported which is a very popular python package for mysql so we will use PyMySQL which is
#  similar to MYSQLdb and implements Python Database API v2.0. It basically provides a interface to connect python to mysql server.


import pymysql.cursors  # importing pymysql if cannot find the package run pip install PyMySQL
import logging


def db_connect():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='example',
                           cursorclass=pymysql.cursors.DictCursor)


def insert_query(sql,param):
    db = db_connect()
    try:
        cursor = db.cursor()
        cursor.execute(sql, param)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        logging.error("Failed insert query: %s", e)
        db.rollback()
        db.close()


def select_query(sql,param):
    db = db_connect()
    try:
        cursor = db.cursor()
        cursor.execute(sql,param)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        if result:
            return result
        else:
            return None
    except Exception as e:
        logging.error("Failed select query", e)
        db.close()
        return None


def delete_query(sql,param):
    db = db_connect()
    try:
        cursor = db.cursor()
        cursor.execute(sql,param)
        db.commit()
        print(cursor.rowcount, "records deleted")
        cursor.close()
        db.close()
    except Exception as e:
        logging.error("Failed delete operation", e)
        db.close()
