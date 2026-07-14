from app.database.db import register_user
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_menu import get_main_menu
from app.config import USER_NAME, BOT_CHARACTER

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    text = f"""
🌙 <b>Привет, {USER_NAME}!</b>

Я <b>{BOT_CHARACTER}</b> — помощница <b>CutePix AI</b>. 💖

✨ Здесь ты сможешь превращать свои фотографии в красивые ИИ-арты.

🎀 Бесплатные стили:
• Аниме
• Сёдзё
• Дарк Кьют
• Ghibli
• Фэнтези

Выбери действие в меню ниже.
"""

    await register_user(message.from_user) 
    await message.answer(
        text,
        reply_markup=get_main_menu()
    )