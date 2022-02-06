import discord
import config
from utils import embed, mongo as db
from utils.mod_event import ModEvent

class ModLogs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_modlog(self, event: ModEvent):
        actions = {
            "ban": "User banned",
            "unban": "User unbanned",
            "kick": "User kicked",
            "mute": "User muted",
            "unmute": "User unmuted",
            "moderate": "User's nickname moderated"
        }
        _embed = embed.warning(actions.get(
            event.action, f"Something broke while trying to get the action ”{event.action}” from the list"))
        _embed.add_field(title="Moderator", description=f"**Mention:** {event.moderator.mention}\n**Tag:** {escape_markdown(event.moderator)}\n**ID:** {event.moderator.id}")
        _embed.add_field(title="Member", description=f"**Mention:** {event.member.mention}\n**Tag:** {escape_markdown(event.member)}\n**ID:** {event.member.id}")
        if event.ends_at != 0:
            ends_at = f"**Ends at:** <t:{event.ends_at}:F>"
        else:
            ends_at = ""
        _embed.add_field(title="Action", description=f"**Type:** {action.capitalize()}\n{ends_at}")
        if event.reason != "":
            _embed.add_field(title="Reason", description=event.reason)

        channel = await self.bot.fetch_channel(mongo.get(f"{event.guild_id}.channels.mod_log"), 0)

        if channel != 0:
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(ModLogs(bot))