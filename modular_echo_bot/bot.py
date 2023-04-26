import asyncio

from aiogram import Bot, Dispatcher, executor
from modular_echo_bot.config_data.config import load_config, Config
from handlers import user_handlers, other_handlers


async def main() -> None:
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher(bot=bot)

    # Регистрируем роутеры в диспетчере


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await executor.start_polling(dp)


if __name__ == '__main__':
    asyncio.run(main())