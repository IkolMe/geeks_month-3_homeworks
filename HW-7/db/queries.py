import sqlite3
from parsel import Selector
from parser import *


def create_table():
    with sqlite3.connect('db/db.sqlite3') as db:
        c = db.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS apartments(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            address TEXT,
            price_dollar TEXT,
            price_local TEXT
        )''')


def insert_data(selector):
    with sqlite3.connect('db/db.sqlite3') as db:
        c = db.cursor()
        c.execute('''
            INSERT INTO apartments(title, address, price_dollar, price_local) 
            VALUES (?, ?, ?, ?)
        ''', (get_title(selector),
              get_address(selector),
              get_price_dollar(selector),
              get_price_local(selector)))
