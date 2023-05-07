from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU


router: Router = Router()

@router.message()
async def send_other_answer(message: Message):
    await message.reply(text=LEXICON_RU['other_answer'])
