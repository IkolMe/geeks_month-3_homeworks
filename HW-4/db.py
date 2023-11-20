import sqlite3

db = sqlite3.connect('db.sqlite3')
c = db.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS goods(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
category TEXT NOT NULL,
added DATE,
price REAL NOT NULL
)''')


def get_all_products():
    c.execute('SELECT * FROM goods')
    return c.fetchall()


print(get_all_products())
