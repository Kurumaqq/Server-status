from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
import asyncio
from src.route import main_router

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()

async def start_bot(): 
    dp.include_router(main_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

