import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env (локально)
load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "❌ BOT_TOKEN не найден. Добавь его в файл .env или в переменные окружения Render."
    )

# База данных
DATABASE_NAME = "cutepix.db"

# Стартовые значения для новых пользователей
START_CRYSTALS = 100
START_ENERGY = 5
MAX_ENERGY = 5

# Название бота
BOT_NAME = "CutePix AI"

# Персонаж бота
BOT_CHARACTER = "Луна"

# Обращение к пользователю
USER_NAME = "Луннышко"

# Бесплатные стили
FREE_STYLES = [
    "🎀 Аниме",
    "🩷 Сёдзё",
    "🖤 Дарк Кьют",
    "🌿 Ghibli",
    "✨ Фэнтези",
]

# Premium-стили
PREMIUM_STYLES = [
    "📖 Манхва",
    "🧛 Вампир",
    "🍓 Милота 100 уровня",
]