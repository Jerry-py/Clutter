from discord.ext import commands

import config
from utils import embed


class Invite(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def invite(self, ctx):
        await ctx.reply(embed=embed.main(ctx.guild.id, "Invite me",
                                         f"**Bot invite:** {config.bot_invite}\n**Support server:** {config.support_server}"),
                        mention_author=False)


def setup(bot):
    bot.add_cog(Invite(bot))
