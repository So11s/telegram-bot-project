from dataclasses import dataclass
from environs import Env
from typing import List


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: List[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


env: Env = Env()
env.read_env()

tg_bot = TgBot(token=env("BOT_TOKEN"),
               admin_ids=env("ADMIN_IDS"))

db = DatabaseConfig(database=env("DATABASE"),
                    db_host=env("DB_HOST"),
                    db_user=env("DB_USER"),
                    db_password=env("DB_PASSWORD"))

config = Config(tg_bot=tg_bot, db=db)

print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('DATABASE:', config.db.database)
print('DB_HOST:', config.db.db_host)
print('DB_USER:', config.db.db_user)
print('DB_PASSWORD:', config.db.db_password)