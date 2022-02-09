from typing import List

import discord

from .mongo_manager import MongoManager


class EmbedAssembler:

    def __init__(self, database: MongoManager):
        self.db = database

    def _get_emoji(self, id: str, emoji: str) -> str:
        return self.db.get(f"{id}.emojis.{emoji}", "")

    def _get_color(self, id: str, color: str) -> int:
        return self.db.get(f"{id}.colors.{color}", discord.Embed.Empty)

    def success(self, title: str, description: str = "", *, id, fields: List[dict] = []) -> discord.Embed:
        emoji, color = self._get_emoji(id, "success"), self._get_color(id, "success")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def error(self, title: str, description: str = "", *, id, fields: List[dict] = []) -> discord.Embed:
        emoji, color = self._get_emoji(id, "error"), self._get_color(id, "error")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def warning(self, title: str, description: str = "", *, id, fields: List[dict] = []) -> discord.Embed:
        emoji, color = self._get_emoji(id, "warning"), self._get_color(id, "warning")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def info(self, title: str, description: str = "", *, id, fields: List[dict] = []) -> discord.Embed:
        emoji, color = self._get_emoji(id, "info"), self._get_color(id, "info")
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed
