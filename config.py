"""class colors:

    success = 0x34c789

    error = 0xff005c

    warning = 0x006aff


class emojis:

    success = "<:success:889206855321157683>"

    error = "<:error:911240678342819870>"

    warning = "<:warning:889206830637666334>"

    info = "<:info:889206906588106824>"""
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")
error_webhook = os.getenv("error_webhook")
mongo_url = os.getenv("mongo_url")
