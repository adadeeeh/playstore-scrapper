import pymysql

db = pymysql.connect('localhost', 'pedro', '1', 'python')

cursor = db.cursor()

drop = """DROP TABLE IF EXISTS REVIEW"""
create = """CREATE TABLE REVIEW (
    id int not null,
    name char(40),
    rating int,
    date varchar(255),
    comment text )"""

try:
    cursor.execute(create)
except:
    cursor.execute(drop)
    cursor.execute(create)

db.close()