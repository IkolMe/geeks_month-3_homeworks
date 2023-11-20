import asyncio
from bot import bot, dp
from handlers.start import start_router
from db import *


async def main():
    dp.include_router(start_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
