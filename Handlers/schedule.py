import asyncio
from aiogram import types, Dispatcher
from config import bot
from decouple import config
import aioschedule
from parserHandler import parser

"""Каждый день в 12 00, Бот отправляет новости"""


def news_alarm(message: types.Message):
    news = parser.scrapy_script_news()
    for i in news:
        bot.send_message(message.chat.id, 'Time to check News!', i)


async def scheduler():
    aioschedule.every().day.at("12:00").do(news_alarm)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(news_alarm, lambda word: 'news' in word.text)
