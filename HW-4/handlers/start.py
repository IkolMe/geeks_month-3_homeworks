from aiogram import Router, types
from aiogram.filters import Command
from db import *

start_router = Router()
table = ''
for row in get_all_products():
    table += f'\n{row}'


@start_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(text=f'Привет, <b>{message.from_user.first_name}</b>'
                              f'Список товаров: {table}',
                         parse_mode='HTML')
