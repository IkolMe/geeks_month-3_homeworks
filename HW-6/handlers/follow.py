import sqlite3
from datetime import datetime
from bot import scheduler, bot
from aiogram import Router, F, types
from db.queries import (
    add_user
)


db = sqlite3.connect('../db.sqlite3')
followers = []
with db:
    c = db.cursor()
    c.execute('''SELECT user_id FROM followers''')

follow_router = Router()


@follow_router.message(F.text == 'ПОДПИСАТЬСЯ')
async def follow(message: types.Message):
    await message.answer('Вы подписались на рассылку.')
    add_user(message)
    scheduler.add_job(
        send,
        'date',
        run_date=datetime(2024, 1, 1, 0, 0, 0),
        kwargs={'chat_id': message.from_user.id}
    )


async def send(chat_id: int):
    await bot.send_message(chat_id=chat_id, text='с нг')
