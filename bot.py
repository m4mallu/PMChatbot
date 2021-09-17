#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os
import logging

from pyrogram import Client

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

if __name__ == "__main__":
    plugins = dict(root="plugins")
    bot = Client(
        "pmbot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    bot.run()
