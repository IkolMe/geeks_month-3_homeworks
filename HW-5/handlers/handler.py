import sqlite3
from aiogram import Router

db = sqlite3.connect('../db.sqlite3')
c = db.cursor()

handler_router = Router()

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
