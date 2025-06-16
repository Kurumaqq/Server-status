from aiogram import Bot, Dispatcher
from src.route import main_router
from src.config import Config
import asyncio

config = Config()
bot = Bot(config.token)
dp = Dispatcher()

async def start_bot(): 
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

