from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path=None):
    env: Env = Env()
    env.read_env(path)

    tg_bot = TgBot(token=env("BOT_TOKEN"))

    return Config(tg_bot=tg_bot)
