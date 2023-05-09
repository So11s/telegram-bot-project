from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.filters import CommandStart, Text

env: Env = Env()
env.read_env()

BOT_TOKEN: str = env('BOT_TOKEN')

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

inline_button_1 = InlineKeyboardButton(text='Кнопка 1',
                                       callback_data='button_1_pressed')
inline_button_2 = InlineKeyboardButton(text='Кнопка 2',
                                       callback_data='button_2_pressed')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[inline_button_1],
                                                                       [inline_button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.reply(text='Это инлайн-кнопки. Нажми на любую!',
                        reply_markup=keyboard)


@dp.callback_query(Text(text=['button_1_pressed']))
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата кнопка 1':
        await callback.message.edit_text(
            text='Была нажата кнопка 1',
            reply_markup=callback.message.reply_markup)
    await callback.answer()


@dp.callback_query(Text(text=['button_2_pressed']))
async def process_buttons_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата кнопка 2':
        await callback.message.edit_text(
            text='Была нажата кнопка 2',
            reply_markup=callback.message.reply_markup)
    await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
