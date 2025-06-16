from src.utils import server_status, services_status, check_perm
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Router
from time import sleep

main_router = Router()

@main_router.message(CommandStart())
async def start(msg: Message, bot: Bot):
     text = server_status() + services_status()
     if check_perm(msg.from_user.id):
        bot_msg = await msg.answer(text, parse_mode='Markdown')
        while True:
            text = server_status() + services_status()
            sleep(5)
            try:
                await bot.edit_message_text(
                    text,
                    chat_id=bot_msg.chat.id,
                    message_id=bot_msg.message_id,
                    parse_mode='Markdown'
                    )

            except TelegramBadRequest as e:
                if "message is not modified" in str(e):
                    continue
