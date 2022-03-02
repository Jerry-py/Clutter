from typing import Tuple

import discord

from ...config import defaults
from .mongodb import MongoManager


class Embed:
    def __init__(self, database: MongoManager):
        self.db = database

    def _get_assets(self, guild_id: str, name: str) -> Tuple[str, str]:
        return self.db.get(f"{guild_id}.emojis.{name}", defaults.emojis.get(name, "")), self.db.get(
            f"{guild_id}.colors.{name}", defaults.colors.get(name, discord.Embed.Empty)
        )  # .get with a default beacuse why not

    def success(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "success")
        return discord.Embed(title=f"{emoji} {title}", description=description, color=color)

    def error(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "error")
        return discord.Embed(title=f"{emoji} {title}", description=description, color=color)

    def warning(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "warning")
        return discord.Embed(title=f"{emoji} {title}", description=description, color=color)

    def info(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "info")
        return discord.Embed(title=f"{emoji} {title}", description=description, color=color)
