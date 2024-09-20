import asyncio
import logging
from aiogram import Dispatcher,Bot
from config import TOKEN
from hendlers import router
from aiogram.client.bot import DefaultBotProperties


bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')