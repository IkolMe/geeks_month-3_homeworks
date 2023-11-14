import asyncio
from aiogram.types import BotCommand
from bot import bot, dp
from handlers import (
    start_router,
    address_router,
    about_router
)


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Начать')
    ])
    dp.include_router(start_router)
    dp.include_router(address_router)
    dp.include_router(about_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
