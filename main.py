from config import dp, bot, URL
from decouple import config
import asyncio

from aiogram.utils import executor
from aiogram import types
from Handlers import commands
import bd_map


async def on_startup(_):
    await bot.set_webhook(URL)
    print("Bot is online")


async def on_shutdown(dp):
    await bot.delete_webhook()


commands.register_handler_default(dp)

if __name__ == "__main__":
    bd_map.sql_create()
    # executor.start_polling(dp, skip_updates=True)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(config("PORT", default=5000))
    )
