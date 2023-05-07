import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


# Инициализация логгера
logger = logging.getLogger(__name__)


async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    # Выводим в консоль информацию о начале работе бота
    logging.info('Starting bot')

    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Игнорируем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
