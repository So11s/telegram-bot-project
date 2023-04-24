from typing import Dict, List

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from TOKEN.TOKEN import TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


class NumberInMessage(BoundFilter):
    async def check(self, message: Message):
        numbers = []
        for word in message.text.split():
            normalizer_word = word.replace('.', '').replace(',', '').strip()
            if normalizer_word.isdigit():
                numbers.append(normalizer_word)

        if numbers:
            return {'numbers': numbers}
        return False


@dp.message_handler(Text(startswith='найди числа', ignore_case=True), NumberInMessage())
async def process_if_numbers(message: Message, numbers: List[str]):
    await message.reply(text=f'Нашел: {", ".join(numbers)}')

@dp.message_handler(Text(startswith='найди числа', ignore_case=True))
async def process_if_numbers(message: Message):
    await message.reply(text="Не нашел чисел :(")


if __name__ == "__main__":
    executor.start_polling(dp)