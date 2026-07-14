from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "🎨 Создать арт")
async def create_art(message: Message):
    await message.answer(
        "🌙 Луннышко, отправь фотографию, которую хочешь превратить в арт! 💖"
    )
    await state.set_state(ArtState.waiting_photo)