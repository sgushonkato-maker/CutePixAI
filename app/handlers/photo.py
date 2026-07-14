from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.photo)
async def get_photo(message: Message):

    photo = message.photo[-1]

    from app.keyboards.styles import styles_keyboard
    
    await message.answer(
    "🌸 Фото получено!\n\nВыбери стиль, Луннышко 💖",
    reply_markup=styles_keyboard()
)