import random

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.utils import executor
from TOKEN.TOKEN import TOKEN


BOT_TOKEN: str = TOKEN

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)

ATTEMPTS: int = 5

users: dict = {}

def get_random_number() -> int:
    return random.randint(1, 100)

@dp.message_handler(commands=["start"])
async def process_start_command(message: Message):
    await message.reply('Привет!\nДавай сыграем в игру "Угадай число"?\n\n'
                         'Чтобы получить правила игры и список доступных '
                         'команд - отправьте команду /help')
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
                                        'secret_number': None,
                                        'attempts': None,
                                        'total_games': 0,
                                        'wins': 0,
                                       }

@dp.message_handler(commands=["help"])
async def process_help_command(message: Message):
    await message.reply(f'Правила игры:\n\nЯ загадываю число от 1 до 100, '
                         f'а вам нужно его угадать\nУ вас есть {ATTEMPTS} '
                         f'попыток\n\nДоступные команды:\n/help - правила '
                         f'игры и список команд\n/cancel - выйти из игры\n'
                         f'/stat - посмотреть статистику\n\nДавай сыграем?')

@dp.message_handler(commands=["stat"])
async def process_stat_command(message: Message):
    await message.reply(
                    f'Всего игр сыграно: '
                    f'{users[message.from_user.id]["total_games"]}\n'
                    f'Игр выиграно: {users[message.from_user.id]["wins"]}')

@dp.message_handler(commands=["cancel"])
async def process_cancel_command(message: Message):
    if users[message.from_user.id]["in_game"]:
        await message.reply('Вы вышли из игры. Если захотите сыграть '
                             'снова - напишите об этом')
        users[message.from_user.id]["in_game"] = False
    else:
        await message.answer('А мы итак с вами не играем. '
                             'Может, сыграем разок?')

@dp.message_handler(Text(equals=['Да', 'Давай', 'Сыграем', 'Игра',
                       'Играть', 'Хочу играть'], ignore_case=True))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        await message.reply('Ура!\n\nЯ загадал число от 1 до 100, '
                             'попробуй угадать!')
        users[message.from_user.id]["in_game"] = True
        users[message.from_user.id]["attempts"] = ATTEMPTS
        users[message.from_user.id]["secret_number"] = get_random_number()
    else:
        await message.answer('Пока мы играем в игру я могу '
                             'реагировать только на числа от 1 до 100 '
                             'и команды /cancel и /stat')

@dp.message_handler(Text(equals=['Нет', 'Не', 'Не хочу', 'Не буду'], ignore_case=True))
async def process_negative_answer(message: Message):
    if not users[message.from_user.id]["in_game"]:
        await message.reply('Жаль :(\n\nЕсли захотите поиграть - просто '
                             'напишите об этом')
    else:
        await message.reply('Мы же сейчас с вами играем. Присылайте, '
                             'пожалуйста, числа от 1 до 100')

@dp.message_handler(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_number_answer(message: Message):
    if users[message.from_user.id]["in_game"]:
        if int(message.text) == users[message.from_user.id]["secret_number"]:
            await message.reply('Ура!!! Вы угадали число!\n\n'
                                 'Может, сыграем еще?')
            users[message.from_user.id]["in_game"] = False
            users[message.from_user.id]["total_games"] += 1
            users[message.from_user.id]["wins"] += 1
        elif int(message.text) > users[message.from_user.id]["secret_number"]:
            await message.reply('Мое число меньше')
            users[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < users[message.from_user.id]["secret_number"]:
            await message.reply('Мое число больше')
            users[message.from_user.id]['attempts'] -= 1

        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(
                f'К сожалению, у вас больше не осталось '
                f'попыток. Вы проиграли :(\n\nМое число '
                f'было {users[message.from_user.id]["secret_number"]}'
                f'\n\nДавайте сыграем еще?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
        else:
            await message.answer('Мы еще не играем. Хотите сыграть?')

@dp.message_handler()
async def process_other_text_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.reply('Мы же сейчас с вами играем. '
                             'Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.reply('Я довольно ограниченный бот, давайте '
                             'просто сыграем в игру?')

if __name__ == "__main__":
    executor.start_polling(dp)