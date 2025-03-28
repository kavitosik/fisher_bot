import asyncio
import os
from dotenv import find_dotenv, load_dotenv
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from privat_chat import setup_privat_handlers
from group import setup_group_handlers
from channel import setup_channel_handlers


load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")


async def main():
    logger.add("file.log",
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days",
               backtrace=True,
               diagnose=True)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    setup_privat_handlers(dp)
    setup_group_handlers(dp)
    setup_channel_handlers(dp, bot)

    logger.info("Бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        logger.info("Бот остановился")


if __name__ == "__main__":
    asyncio.run(main())
