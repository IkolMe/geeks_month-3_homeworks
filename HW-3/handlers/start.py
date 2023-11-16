from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, <strong>{message.from_user.username}</strong>!'
                         f' Введите /form для начала опроса', parse_mode='HTML')

