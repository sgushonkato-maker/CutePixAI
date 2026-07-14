import asyncio

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

    print("🌙 CutePix AI запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
