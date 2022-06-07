from config import dp, bot, Dispatcher
from aiogram import types
from parserHandler import parser
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

"""Функция запуска парсера Аниме сайта"""
async def parsed_anime(message: types.Message):
    parsed = parser.scrapy_script()
    for i in parsed:
        await bot.send_message(message.chat.id, i)

"""Функция запуска парсера новостного сайта"""
async def parsed_news(message: types.Message):
    parsed = parser.scrapy_script_news()
    for i in parsed:
        await bot.send_message(message.chat.id, i)



"""Команда старта"""
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Hello ")
    await bot.send_message(message.chat.id, '__,,,^._.^,,,__')




"""Помощь для просмотра всех доступных команд"""
async def help(message: types.Message):
    await message.reply("/start \n/"
                        "/news - Fresh News in KG\n"
                        "/anime - Top Anime")


def register_handler_default(dp: Dispatcher):
    dp.register_message_handler(parsed_anime, commands=["anime"])
    dp.register_message_handler(parsed_news, commands=["news"])
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(help, commands=["help"])
