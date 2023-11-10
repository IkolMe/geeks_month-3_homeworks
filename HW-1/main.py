import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from random import choice

TOKEN = '6387182695:AAFFZFBiEOKnW6SEOGodIHucZdWxN1jXCEg'
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'Hi, {message.from_user.first_name}')


@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    await message.answer(f'''Your info:
    
id: {message.from_user.id}
first_name: {message.from_user.first_name}
username: {message.from_user.username}''')


@dp.message(Command('picture'))
async def picture(message: types.Message):
    pics = os.listdir('images')
    random_pic = choice(pics)
    pic_path = os.path.join('images', random_pic)

    file = types.FSInputFile(pic_path)
    await message.answer_photo(
        photo=file
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
