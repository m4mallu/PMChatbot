#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    ADMIN = int(os.environ.get("ADMIN"))
