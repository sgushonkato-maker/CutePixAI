from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_menu():
    keyboard = [
        [
            KeyboardButton(text="🎨 Создать арт"),
        ],
        [
            KeyboardButton(text="👤 Профиль"),
            KeyboardButton(text="✨ Стили"),
        ],
        [
            KeyboardButton(text="💎 Premium"),
            KeyboardButton(text="👥 Пригласить друга"),
        ],
        [
            KeyboardButton(text="🎁 Бонус дня"),
            KeyboardButton(text="💌 Поддержка"),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выбери действие, Луннышко 🌙"
    )