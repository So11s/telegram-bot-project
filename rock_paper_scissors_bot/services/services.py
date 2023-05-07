import random

from lexicon.lexicon_ru import LEXICON_RU


def get_bot_choice():
    return random.choice(('rock', 'paper', 'scissors'))


def _normalizate_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if user_answer == LEXICON_RU[key]:
            return key
    raise Exception


def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalizate_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
