import os

from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("token")  # bot token

error_webhook = os.getenv("error_webhook")  # error reporting webhook

mongo_url = os.getenv("mongo_url")  # mongodb connecting url

bot_invite = "SOON"  # bot invite

support_server = "SOON"  # bot support server invite

bot_version = "0.1b"  # bot version


class defaults:
    emojis = {
        "success": "<:success:889206855321157683>",
        "error": "<:error:911240678342819870>",
        "warning": "<:warning:889206830637666334>",
        "info": "<:info:889206906588106824>"
    }

    colors = {
        "success": 0x34c789,
        "error": 0xff005c,
        "warning": 0x006aff,
        "info": 0x656479
    }
