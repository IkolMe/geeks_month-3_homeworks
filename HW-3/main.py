import asyncio
from aiogram.types import BotCommand
from aiogram.filters import Command
from utils.statesform import Questions
from bot import bot, dp
from handlers import form
from handlers.start import start_router


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Start bot'),
        BotCommand(command='form', description='Начать опрос')
    ])
    dp.include_router(start_router)
    dp.message.register(form.get_form, Command('form'))
    dp.message.register(form.get_name, Questions.GET_NAME)
    dp.message.register(form.get_last_name, Questions.GET_LAST_NAME)
    dp.message.register(form.get_gender, Questions.GET_GENDER)
    dp.message.register(form.get_fav_show, Questions.GET_FAV_SHOW)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
