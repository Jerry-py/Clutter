"""
USAGE:

from utils.mod_event import ModEvent

event = ModEvent(moderator=ctx.author, member=member, action="ban", guild_id=ctx.guild.id, reason=reason, ends_at=unixtime)

self.bot.dispatch("modlog", event)
"""
import discord


class ModEvent:
    def __init__(
        self,
        *,
        moderator: discord.Member,
        member: discord.Member,
        action: str,
        guild_id: int,
        reason: str = "",
        ends_at: int = 0,
        automod: bool = False
    ):
        self.moderator = moderator
        self.member = member
        self.action = action
        self.guild_id = guild_id
        self.reason = reason
        self.ends_at = ends_at
        self.automod = automod
