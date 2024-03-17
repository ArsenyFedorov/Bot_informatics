from aiogram import Dispatcher, Bot
import os
import asyncio
from handlers import handlers_router
from data_base.user import User
from data_base.result_test import ResultTest
from user_data import fsm_router

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(handlers_router)
dp.include_router(fsm_router)


def on_start():
    print("Bot запущен")
    print("База данных", end=" ")
    try:
        User.great_table()
        print("Подключено", end=" ")
        ResultTest.great_table()
        print(" и эта тоже")
    except:
        print("Не подключено")


async def start_bot():
    dp.startup.register(on_start)
    # Пока бот выключен все запросы удаляются
    await bot.delete_webhook(drop_pending_updates=True)
    # бот сам проверяет запросы
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
