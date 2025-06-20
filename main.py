import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from handlers.general import basic_router
from handlers.reg_handlers import reg_router
from utils.my_commands import custom_commands


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode="HTML",
            link_preview_is_disabled=True
        )
    )
    await bot.set_my_commands(custom_commands)
    dp = Dispatcher()
    dp.include_routers(
        reg_router,
        basic_router,
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
