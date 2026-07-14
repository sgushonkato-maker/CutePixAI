import asyncio

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.services.generator import fake_generation
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
    F.data.startswith("style_")
)
async def select_style(callback: CallbackQuery, state: FSMContext):

    style = callback.data

    await state.update_data(style=style)
    
    data = await state.get_data()
    
    photo_id = data["photo_id"]

    await state.set_state(ArtState.generating)

    message = await callback.message.edit_text(
        f"""
🌙 <b>Луннышко...</b>

✨ Уже начинаю творить магию...

🎨 Стиль:
<b>{STYLE_NAMES[style]}</b>
"""
    )

    await callback.answer()

    await asyncio.sleep(2)

    await message.edit_text(
        "🌙 Беру немного лунного света... ✨"
    )

    await asyncio.sleep(2)

    await message.edit_text(
        "💖 Добавляю чуточку магии..."
    )

    await asyncio.sleep(2)

    await message.edit_text(
        "🎨 Почти закончила..."
    )

    image_url = await upload_photo_to_fal(
    callback.bot,
    photo_id
)

result = await generate_image(
    image_url,
    style
)

if result is None:

    await callback.message.answer(
        "😢 Что-то пошло не так.\nПопробуй ещё раз."
    )

    await state.clear()

    return

await callback.message.answer_photo(

    photo=result,

    caption="""
🌙 <b>Готово, Луннышко!</b>

✨ Надеюсь тебе понравится 💖
"""
)

await state.clear()

    await asyncio.sleep(1)

    await message.edit_text(
        """
🖼 <b>Готово!</b>

✨ Пока это тестовая версия CutePix AI.

Совсем скоро здесь появится настоящий ИИ 💖
"""
    )

    await state.clear()