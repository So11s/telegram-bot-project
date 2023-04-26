from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from lexicon.lexicon import LEXICON_RU


@dp.message_handler(CommandStart())
async def process_start_command(message: Message):
    await message.reply(text=LEXICON_RU["/start"])


@dp.message_handler(CommandHelp())
async def process_help_command(message: Message):
    await message.reply(text=LEXICON_RU["/help"])
