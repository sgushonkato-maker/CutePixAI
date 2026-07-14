from app import config


async def load_bot_info(bot):
    me = await bot.get_me()

    config.BOT_USERNAME = me.username