import sqlite3

db = sqlite3.connect('../db.sqlite3')


def createTable():
    with db:
        c = db.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS followers(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                username TEXT
            )
        ''')


def add_user(message):
    with db:
        c = db.cursor()
        c.execute('''
                INSERT INTO followers(user_id, username)
                VALUES (?, ?)
            ''', (
            message.from_user.id,
            message.from_user.username
        ))


def resetTable():
    with db:
        c = db.cursor()
        c.execute('''DELETE FROM followers WHERE id > 0''')


def getUsers():
    with db:
        c = db.cursor()
        c.execute('''SELECT * from followers''')
        return c.fetchall()
