from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import environs

env = environs.Env()

env.read_env()

BOT_TOKEN: str = env("BOT_TOKEN")

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Яндекс',
    url='www.ya.ru')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Goggle',
    url='www.google.com')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[url_button_1], [url_button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.reply(text='Это инлайн кнопки с параметром "url"',
                        reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
