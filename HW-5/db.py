import sqlite3

db = sqlite3.connect('db/db.sqlite3')
c = db.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT,
    categoryId INTEGER,
    FOREIGN KEY (categoryId) REFERENCES categories(id)
)''')


def get_from_db(table):
    c.execute(f'''SELECT * FROM {table}''')
    return c.fetchall()
