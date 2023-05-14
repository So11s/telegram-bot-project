from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from environs import Env

env: Env = Env()
env.read_env()

BOT_TOKEN: str = env('BOT_TOKEN')

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

big_button_1: InlineKeyboardButton = InlineKeyboardButton(text='Большая кнопка 1',
                                                          callback_data='big_button_1_pressed')

big_button_2: InlineKeyboardButton = InlineKeyboardButton(text='Большая кнопка 2',
                                                          callback_data='big_button_2_pressed')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[big_button_1], [big_button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки. Нажми на любую.',
                         reply_markup=keyboard)


@dp.callback_query(Text(text=['big_button_1_pressed']))
async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата Большая кнопка 1':
        await callback.message.edit_text(text='Была нажата Большая кнопка 1',
                                         reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 1',
                          show_alert=True)


@dp.callback_query(Text(text=['big_button_2_pressed']))
async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата Большая кнопка 2':
        await callback.message.edit_text(text='Была нажата Большая кнопка 2',
                                         reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 2')


if __name__ == '__main__':
    dp.run_polling(bot)
