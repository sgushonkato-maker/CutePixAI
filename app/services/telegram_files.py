import os
import tempfile

import fal_client
from aiogram import Bot


async def upload_photo_to_fal(
    bot: Bot,
    file_id: str,
) -> str:
    """
    Скачивает фотографию из Telegram,
    загружает её в Fal CDN
    и возвращает URL.
    """

    telegram_file = await bot.get_file(file_id)

    with tempfile.NamedTemporaryFile(
        suffix=".jpg",
        delete=False,
    ) as tmp:

        temp_path = tmp.name

    try:

        await bot.download_file(
            telegram_file.file_path,
            destination=temp_path,
        )

        image_url = await fal_client.upload_file(
            temp_path
        )

        return image_url

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)