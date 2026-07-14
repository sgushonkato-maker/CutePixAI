from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


PREMIUM_STYLES = {
    "premium_manhwa": "📖 Манхва",
    "premium_vampire": "🧛 Вампир",
    "premium_supercute": "🍓 Милота 100 уровня",
}


@router.callback_query(F.data.startswith("premium_"))
async def premium_style(callback: CallbackQuery):

    style = PREMIUM_STYLES.get(callback.data, "Этот стиль")

    await callback.answer()

    await callback.message.answer(
        f"""
🔒 <b>{style}</b>

🌙 Луннышко...

Этот стиль доступен только владельцам <b>CutePix Premium</b>. 💎

✨ Premium открывает:

• 📖 Эксклюзивные стили
• ⚡ Быструю генерацию
• 🖼 HD качество
• 🌸 Новые функции раньше всех
"""
    )