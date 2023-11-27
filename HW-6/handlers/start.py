import sqlite3
from aiogram import Router, types, F
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='ПОДПИСАТЬСЯ')
            ]
        ]
    )
    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         f'Нажмите кнопку <b>ПОДПИСАТЬСЯ</b> для получения поздравления с новым годом 2024.01.01',
                         parse_mode='HTML',
                         reply_markup=kb)

