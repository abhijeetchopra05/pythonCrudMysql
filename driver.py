import db


def insert_demo():
    sql = "INSERT INTO user (email, password) VALUES (%s, %s)"
    db.insert_query(sql, ('abhi', 'abc'))


def select_demo():
    sql = "SELECT * FROM user WHERE email=%s"
    result = db.select_query(sql, 'abhi')
    print(result)


def delete_demo():
    sql = "DELETE FROM user WHERE email=%s"
    db.delete_query(sql, 'abhi')


if __name__ == '__main__':
    insert_demo()
    select_demo()
    delete_demo()

