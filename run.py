from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from os import getenv
import asyncio
from src.server import Server

load_dotenv()
bot = Bot(getenv('TOKEN'))
dp = Dispatcher()
server = Server()

@dp.message(CommandStart())
async def echo(msg):
    await msg.answer(
f'''
CPU: {server.cpu_used} %
Memory used: {server.memory_used}GB ({server.memory_percent}%)
''')

async def start_bot(): await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())

