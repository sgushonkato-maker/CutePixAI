from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.states.art_state import ArtState

router = Router()


@router.message(lambda message: message.text == "🎨 Создать арт")
async def create_art(message: Message, state: FSMContext):

    await state.set_state(ArtState.waiting_photo)

    await message.answer(
        "🌙 <b>Жду твою фотографию, Луннышко!</b>\n\n"
        "📷 Отправь одно изображение.\n\n"
        "✨ Я превращу его в настоящее маленькое чудо 💖"
    )