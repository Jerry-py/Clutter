import platform

from discord.ext import commands

import config
from utils import checks, embed


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(checks.send_messages)
    async def info(self, ctx):
        await ctx.channel.trigger_typing()
        await ctx.reply(
            embed=embed.info(
                "Bot info",
                f"Bot Version {config.bot_version}\nRunning on Python {platform.python_version()}\nMade by RGBCube#4777",
                guild_id=ctx.guild.id,
            ),
            mention_author=False,
        )


def setup(bot):
    bot.add_cog(Info(bot))
