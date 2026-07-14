from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def styles_keyboard():
    kb = InlineKeyboardBuilder()

    kb.button(text="🎀 Аниме", callback_data="style_anime")
    kb.button(text="🩷 Сёдзё", callback_data="style_shoujo")

    kb.button(text="🖤 Дарк Кьют", callback_data="style_darkcute")
    kb.button(text="🌿 Ghibli", callback_data="style_ghibli")

    kb.button(text="✨ Фэнтези", callback_data="style_fantasy")

    kb.button(text="🔒 📖 Манхва", callback_data="premium_manhwa")
    kb.button(text="🔒 🧛 Вампир", callback_data="premium_vampire")
    kb.button(text="🔒 🍓 Милота 100 уровня", callback_data="premium_supercute")

    kb.adjust(2, 2, 1, 1, 1, 1)

    return kb.as_markup()