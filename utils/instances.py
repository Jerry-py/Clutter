from config import mongo_url
from .content import color, embed, mongodb, checks
from ..main import bot

color = color.Color
db = mongodb.MongoManager(mongo_url, "Clutter")
embed = embed.Embed(db)
checks = checks.Checks(db, bot)
