from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.utils import executor
from TOKEN import TOKEN


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.reply('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.reply('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на фотографии
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


# Этот хендлер будет срабатывать на аудио
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)


# Это хендлер будет срабатывать на стикер
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=f"Давай что-нибудь умное, а не '{message.text}'")


dp.register_message_handler(process_start_command, commands=['start'])
dp.register_message_handler(process_help_command, commands=['help'])
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_audio_echo, content_types=['audio'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_echo)


if __name__ == '__main__':
    executor.start_polling(dp)