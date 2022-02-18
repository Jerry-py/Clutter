from typing import Tuple

import discord

from .mongodb import MongoManager
from ...config import defaults


class Embed:

    def __init__(self, database: MongoManager):
        self.db = database

    def _get_assets(self, guild_id: str, name: str) -> Tuple[str, str]:
        return self.db.get(f"{guild_id}.emojis.{name}", defaults.emojis.get(name, "")), self.db.get(
            f"{guild_id}.colors.{name}",
            defaults.colors.get(name,
                                discord.Embed.Empty))  # .get with a default beacuse why not

    def success(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "success")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def error(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "error")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def warning(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "warning")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed

    def info(self, title: str, description: str = "", *, guild_id) -> discord.Embed:
        emoji, color = self._get_assets(guild_id, "info")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        return _embed
