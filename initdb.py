import pymysql

host = 'localhost'
user = 'root'
password = ''
dbname = 'crawl'

def get_cursor(db):
    return db.cursor()

def create_db():
    db = pymysql.connect(host, user, password, dbname)
    cursor = db.cursor()
    drop = """DROP TABLE IF EXISTS REVIEW"""
    create = """CREATE TABLE REVIEW (
        id int,
        name char(40),
        rating int,
        date varchar(255),
        comment text ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_bin;"""
    try:
        cursor.execute(create)
    except:
        cursor.execute(drop)
        cursor.execute(create)
    return db