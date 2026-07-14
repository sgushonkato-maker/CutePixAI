from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

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

    await state.set_state(ArtState.generating)

    await callback.message.edit_text(
        f"""
🌙 <b>Луннышко...</b>

✨ Уже начинаю творить магию!

🎨 Стиль:
<b>{STYLE_NAMES[style]}</b>

⏳ Обычно это занимает меньше минуты.

Не закрывай чат 💖
"""
    )

    await callback.answer()