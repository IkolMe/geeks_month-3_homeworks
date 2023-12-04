import asyncio
from bot import bot, dp
from handlers import *


async def main():
    dp.include_router(group_admin_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
