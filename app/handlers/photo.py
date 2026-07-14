from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.styles import styles_keyboard
from app.states.art_state import ArtState

router = Router()


@router.message(ArtState.waiting_photo)
async def receive_photo(
    message: Message,
    state: FSMContext,
):

    if not message.photo:

        await message.answer(
            "🥺 Луннышко...\n\n"
            "Мне нужна именно фотография 📷💖"
        )

        return

    photo = message.photo[-1]

    await state.update_data(
        photo_id=photo.file_id
    )

    await state.set_state(
        ArtState.waiting_style
    )

    await message.answer(
        """
🌙 Какая замечательная фотография! 💖

✨ Теперь осталось выбрать стиль.

После этого я начну творить настоящее волшебство 👇
""",
        reply_markup=styles_keyboard(),
    )