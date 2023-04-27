from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon import LEXICON_RU


# Инициализируем роутер уровня модуля
router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.reply(text=LEXICON_RU["/start"])


@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.reply(text=LEXICON_RU["/help"])
