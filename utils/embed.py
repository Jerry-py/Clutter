from utils import mongo as db
import discord


def success(guild_id: int, title: str, description: str = ""):
    emoji, color = db.get(f"{guild_id}.emojis.success", ""), db.get(f"{guild_id}.colors.success", "")
    _embed = discord.Embed(
        title=f"{emoji} {title}", description=description, color=color)
    return _embed


def error(title: str, description: str = ""):
    emoji, color = db.get(f"{guild_id}.emojis.warning", ""), db.get(f"{guild_id}.colors.error", "")
    _embed = discord.Embed(
        title=f"{emoji} {title}", description=description, color=color)
    return _embed


def warning(title: str, description: str = ""):
    emoji, color = db.get(f"{guild_id}.emojis.warning", ""), db.get(f"{guild_id}.colors.warning", "")
    _embed = discord.Embed(
        title=f"{emoji} {title}", description=description, color=color)
    return _embed

def info(title: str, description: str = ""):
    emoji, color = db.get(f"{guild_id}.emojis.info", ""), db.get(f"{guild_id}.colors.warning", "")
    _embed = discord.Embed(
        title=f"{emoji} {title}", description=description, color=color)
    return _embed
