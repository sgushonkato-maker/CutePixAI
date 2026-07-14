import asyncio

from app.handlers.referral import router as referral_router
from app.handlers.premium_callback import router as premium_router
from app.handlers.style_callback import router as style_router
from app.handlers.photo import router as photo_router
from app.handlers.create_art import router as create_art_router
from app.handlers.profile import router as profile_router
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN
from app.handlers.start import router as start_router


async def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN не найден. Добавь его в переменные окружения Render или в файл .env."
        )

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(create_art_router)
    dp.include_router(photo_router)
    dp.include_router(style_router)
    dp.include_router(premium_router)
    dp.include_router(referral_router)

    print("🌙 CutePix AI запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
