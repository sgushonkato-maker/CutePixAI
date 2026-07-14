from aiogram import Router
from aiogram.types import Message

from app.database.db import get_profile

router = Router()

from app import config  # Потом заменим автоматически


def progress_bar(value: int, maximum: int = 10) -> str:
    filled = min(value, maximum)
    empty = maximum - filled

    return "🟪" * filled + "⬜" * empty


@router.message(lambda message: message.text == "👥 Пригласить друга")
async def referral(message: Message):

    profile = await get_profile(message.from_user.id)

    if profile is None:
        await message.answer("Сначала нажми /start 💖")
        return

    referrals = profile[3]

    link = (
    f"https://t.me/{config.BOT_USERNAME}"
    f"?start={message.from_user.id}"
    )
    await message.answer(
        f"""
🌙 <b>Приглашай Луннышек!</b>

💎 За каждого друга

+100 Лунных кристаллов ✨

━━━━━━━━━━━━━━

👥 Приглашено

<b>{referrals}</b>

{progress_bar(referrals)}

🎁 До следующей награды

<b>{max(10-referrals,0)}</b>

━━━━━━━━━━━━━━

🔗 Твоя ссылка

<code>{link}</code>
"""
    )