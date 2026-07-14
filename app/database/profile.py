from aiogram import Router
from aiogram.types import Message

from app.database.db import get_profile

router = Router()


@router.message(lambda message: message.text == "👤 Профиль")
async def profile(message: Message):

    profile = await get_profile(message.from_user.id)

    if profile is None:
        await message.answer(
            "❌ Профиль не найден.\n\nНапиши /start"
        )
        return

    crystals, energy, premium, referrals, streak = profile

    premium_text = "💎 Premium" if premium else "❌ Не активен"

    text = f"""
🌙 <b>Профиль Луннышка</b>

👤 {message.from_user.first_name}

🆔 <code>{message.from_user.id}</code>

━━━━━━━━━━━━━━

🌙 Кристаллы
<b>{crystals}</b>

⚡ Энергия
<b>{energy}/5</b>

💎 Статус
<b>{premium_text}</b>

👥 Приглашено друзей
<b>{referrals}</b>

🔥 Серия входов
<b>{streak}</b> дней
"""

    await message.answer(text)