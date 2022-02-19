from config import mongo_url

from ..main import bot
from .content import checks, color, embed, mongodb

color = color.Color
db = mongodb.MongoManager(mongo_url, "Clutter")
embed = embed.Embed(db)
checks = checks.Checks(db, bot)
