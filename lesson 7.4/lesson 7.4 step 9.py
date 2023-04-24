from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from aiogram.utils import executor
from TOKEN.TOKEN import TOKEN
from typing import List


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

admin_ids: List[int] = [776568435]

class IsAdmin(BoundFilter):
    def __init__(self, admin_ids: List[int]) -> None:
        self.admin_ids = admin_ids

    async def check(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

@dp.message_handler(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.reply(text='You are admin')

@dp.message_handler()
async def answer_if_not_admins_update(message: Message):
    await message.reply(text='You are not admin')

if __name__ == "__main__":
    executor.start_polling(dp)