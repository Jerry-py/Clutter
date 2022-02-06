import os

from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("token")  # bot token

error_webhook = os.getenv("error_webhook")  # error reporting webhook

mongo_url = os.getenv("mongo_url")  # mongodb connecting url

bot_invite = "SOON"  # bot invite

support_server = "SOON"  # bot support server invite
