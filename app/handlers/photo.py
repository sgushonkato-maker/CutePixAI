from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.photo)
async def get_photo(message: Message):

    photo = message.photo[-1]

    await message.answer(
        "🌸 Фото получено!\n\nТеперь выбери стиль 👇"
    )