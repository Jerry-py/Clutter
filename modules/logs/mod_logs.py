from discord.ext import commands
from discord.utils import escape_markdown

from utils import ModEvent, db, embed


class ModLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.actions = {
            "ban": "User banned",
            "unban": "User unbanned",
            "kick": "User kicked",
            "mute": "User muted",
            "unmute": "User unmuted",
            "moderate": "User's nickname moderated",
        }

    @commands.Cog.listener()
    async def on_modlog(self, event: ModEvent):
        channel = await self.bot.fetch_channel(db.get(f"{event.guild_id}.channels.mod_log"), 0)
        await channel.trigger_typing()
        if channel == 0:
            return
        auto_text = "Automod action: " if event.automod else ""
        _embed = embed.warning(
            auto_text
            + self.actions.get(
                event.action, f"Something broke while trying to get the action ”{event.action}” from the list"
            ),
            guild_id=event.guild_id,
        )
        if not event.automod:
            _embed.add_field(
                title="Moderator",
                description=f"**Mention:** {event.moderator.mention}\n**Tag:** {escape_markdown(str(event.moderator))}\n**ID:** {event.moderator.id}",
            )
        _embed.add_field(
            title="Member",
            description=f"**Mention:** {event.member.mention}\n**Tag:** {escape_markdown(str(event.member))}\n**ID:** {event.member.id}",
        )
        ends_at = f"**Ends at:** <t:{event.ends_at}:F>" if event.ends_at != 0 else ""
        _embed.add_field(title="Action", description=f"**Type:** {event.action.capitalize()}\n{ends_at}")
        if event.reason != "":
            _embed.add_field(title="Reason", description=event.reason)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(ModLogs(bot))
