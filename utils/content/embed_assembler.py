from typing import List

import discord

from .mongo_manager import MongoManager


class EmbedAssembler:

    def __init__(self, database: MongoManager):
        self.db = database

    def success(self, title: str, description: str = "", *, id, fields: List[dict] = None) -> discord.Embed:
        emoji, color = self.db.get(f"{id}.emojis.success", ""), self.db.get(f"{id}.colors.success", discord.Embed.Empty)
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def error(self, title: str, description: str = "", *, id, fields: List[dict] = None) -> discord.Embed:
        emoji, color = self.db.get(f"{id}.emojis.warning", ""), self.db.get(f"{id}.colors.error", discord.Embed.Empty)
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def warning(self, title: str, description: str = "", *, id, fields: List[dict] = None) -> discord.Embed:
        emoji, color = self.db.get(f"{id}.emojis.warning", ""), self.db.get(f"{id}.colors.warning", discord.Embed.Empty)
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed

    def info(self, title: str, description: str = "", *, id, fields: List[dict] = None) -> discord.Embed:
        emoji, color = self.db.get(f"{id}.emojis.info", ""), self.db.get(f"{id}.colors.warning", discord.Embed.Empty)
        _embed = discord.Embed(
            title=f"{emoji} {title}", description=description, color=color)
        for field in fields:
            _embed.add_field(name=field.get("title", ""), value=field.get("value", ""))
        return _embed
