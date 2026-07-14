from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def styles_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(text="🎀 Аниме", callback_data="anime")
    kb.button(text="🩷 Сёдзё", callback_data="shoujo")

    kb.button(text="🖤 Дарк Кьют", callback_data="darkcute")
    kb.button(text="🌿 Ghibli", callback_data="ghibli")

    kb.button(text="✨ Фэнтези", callback_data="fantasy")

    kb.button(text="🔒 📖 Манхва", callback_data="premium")
    kb.button(text="🔒 🧛 Вампир", callback_data="premium")
    kb.button(text="🔒 🍓 Милота 100 уровня", callback_data="premium")

    kb.adjust(2,2,1,1,1,1)

    return kb.as_markup()