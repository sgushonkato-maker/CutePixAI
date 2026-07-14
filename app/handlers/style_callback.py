import asyncio

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.services.ai_generator import generate_image
from app.services.telegram_files import upload_photo_to_fal
from app.states.art_state import ArtState

router = Router()


STYLE_NAMES = {
    "style_anime": "🎀 Аниме",
    "style_shoujo": "🩷 Сёдзё",
    "style_darkcute": "🖤 Дарк Кьют",
    "style_ghibli": "🌿 Ghibli",
    "style_fantasy": "✨ Фэнтези",
}


@router.callback_query(
    ArtState.waiting_style,
    F.data.startswith("style_"),
)
async def select_style(
    callback: CallbackQuery,
    state: FSMContext,
):

    style = callback.data

    data = await state.get_data()

    photo_id = data.get("photo_id")

    if not photo_id:
        await callback.answer(
            "Фото не найдено.",
            show_alert=True,
        )
        await state.clear()
        return

    await state.set_state(ArtState.generating)

    await callback.answer()

    message = await callback.message.edit_text(
        f"""
🌙 <b>Луннышко...</b>

✨ Уже начинаю творить магию!

🎨 Стиль:
<b>{STYLE_NAMES.get(style, "Аниме")}</b>
"""
    )

    await asyncio.sleep(1)

    await message.edit_text(
        "🌙 Беру немного лунного света... ✨"
    )

    image_url = await upload_photo_to_fal(
        callback.bot,
        photo_id,
    )

    await message.edit_text(
        "💖 Добавляю чуточку магии..."
    )

    result = await generate_image(
        image_url=image_url,
        style=style,
    )

    if result is None:

        await message.edit_text(
            """
😢 Не удалось создать арт.

Попробуй ещё раз немного позже.
"""
        )

        await state.clear()
        return

    await message.edit_text(
        "🎨 Последние штрихи..."
    )

    await callback.message.answer_photo(
        photo=result,
        caption="""
🌙 <b>Готово, Луннышко!</b>

✨ Надеюсь, тебе понравится!

💖 Спасибо, что творишь вместе с CutePix AI.
""",
    )

    await state.clear()