import aiosqlite

from app.config import (
    DATABASE_NAME,
    START_CRYSTALS,
    START_ENERGY,
)


async def init_db():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            telegram_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,

            crystals INTEGER DEFAULT 100,
            energy INTEGER DEFAULT 5,

            premium INTEGER DEFAULT 0,
            referrals INTEGER DEFAULT 0,

            invited_by INTEGER DEFAULT NULL,
            last_bonus TEXT,

            streak INTEGER DEFAULT 1,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        await db.commit()


async def register_user(user, invited_by=None):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            """
            SELECT telegram_id
            FROM users
            WHERE telegram_id=?
            """,
            (user.id,)
        )

        exists = await cursor.fetchone()

        if exists:
            return False

        await db.execute(
            """
            INSERT INTO users(
                telegram_id,
                username,
                first_name,
                crystals,
                energy,
                invited_by
            )
            VALUES(?,?,?,?,?,?)
            """,
            (
                user.id,
                user.username,
                user.first_name,
                START_CRYSTALS,
                START_ENERGY,
                invited_by
            )
        )

        if invited_by:

            await db.execute(
                """
                UPDATE users
                SET

                    referrals = referrals + 1,

                    crystals = crystals + 100

                WHERE telegram_id=?
                """,
                (invited_by,)
            )

        await db.commit()

        return True


async def get_profile(user_id):

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            """
            SELECT
                crystals,
                energy,
                premium,
                referrals,
                streak
            FROM users
            WHERE telegram_id=?
            """,
            (user_id,)
        )

        return await cursor.fetchone()