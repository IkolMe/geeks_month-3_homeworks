import asyncio
from bot import bot, dp, scheduler
from aiogram.types import BotCommand
from handlers import *
from db.queries import createTable


async def on_startup(dispatcher):
    createTable()


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Get started')
    ])
    dp.startup.register(on_startup)
    dp.include_router(start_router)
    dp.include_router(follow_router)
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
