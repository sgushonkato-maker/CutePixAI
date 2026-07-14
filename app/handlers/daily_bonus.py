from datetime import date

import aiosqlite
from aiogram import Router
from aiogram.types import Message

from app.config import DATABASE_NAME

router = Router()

BONUS = 50


@router.message(lambda message: message.text == "🎁 Бонус дня")
async def daily_bonus(message: Message):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            """
            SELECT crystals, last_bonus
            FROM users
            WHERE telegram_id=?
            """,
            (message.from_user.id,),
        )

        user = await cursor.fetchone()

        if not user:
            await message.answer("Нажми /start 💖")
            return

        crystals, last_bonus = user

        today = str(date.today())

        if last_bonus == today:

            await message.answer(
                "🌙 Луннышко!\n\n"
                "🎁 Сегодня ты уже получила бонус.\n\n"
                "Возвращайся завтра 💖"
            )

            return

        crystals += BONUS

        await db.execute(
            """
            UPDATE users
            SET crystals=?, last_bonus=?
            WHERE telegram_id=?
            """,
            (
                crystals,
                today,
                message.from_user.id,
            ),
        )

        await db.commit()

    await message.answer(
        f"""
🎉 <b>Подарок получен!</b>

🌙 +{BONUS} Лунных кристаллов

Теперь у тебя:

<b>{crystals}</b> 🌙
"""
    )