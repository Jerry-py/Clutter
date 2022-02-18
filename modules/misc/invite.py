from discord.ext import commands

import config
from utils import embed, checks


class Invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks.send_messages)
    async def invite(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.reply(embed=embed.info("Invite me",
                                         f"**Bot invite:** {config.bot_invite}\n**Support server:** {config.support_server}"),
                        mention_author=False, guild_id=ctx.guild.id)


def setup(bot):
    bot.add_cog(Invite(bot))
