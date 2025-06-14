from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.utils import get_status_server
from time import sleep

main_router = Router()

@main_router.message(CommandStart())
async def start(msg: Message, bot: Bot):
     bot_msg = await msg.answer(get_status_server())
     while True:
        sleep(3)
        await bot.edit_message_text(
            get_status_server(),
            chat_id=bot_msg.chat.id,
            message_id=bot_msg.message_id
            )

@main_router.message()
async def echo(msg):
    await msg.answer(msg.text)
