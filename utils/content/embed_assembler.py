from typing import Tuple

import discord

from .mongo_manager import MongoManager
from ...config import Defaults as de


class EmbedAssembler:

    def __init__(self, database: MongoManager):
        self.db = database

    def _get_assets(self, id: str, name: str) -> Tuple[str, str]:
        return self.db.get(f"{id}.emojis.{name}", de.emojis.get(name, "")), self.db.get(f"{id}.colors.{name}",
                                                                                        de.colors.get(name,
                                                                                                      discord.Embed.Empty))  # .get with a default beacuse why not

    def success(self, title: str, description: str = "", *, id) -> discord.Embed:
        emoji, color = self._get_assets(id, "success")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def error(self, title: str, description: str = "", *, id) -> discord.Embed:
        emoji, color = self._get_assets(id, "error")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def warning(self, title: str, description: str = "", *, id) -> discord.Embed:
        emoji, color = self._get_assets(id, "warning")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def info(self, title: str, description: str = "", *, id) -> discord.Embed:
        emoji, color = self._get_assets(id, "info")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed
