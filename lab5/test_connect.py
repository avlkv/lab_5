import MySQLdb as pymysql

db = pymysql.connect(
    host='localhost',
    user='dbadmin',
    password='123321',
    db='first_db'
)

c = db.cursor()

c.execute('INSERT INTO books (name, description) VALUES (%s, %s);',('Book','Book desciption'))

db.commit()

c.execute('SELECT * FROM books;')

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
