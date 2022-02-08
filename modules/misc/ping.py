import time

from discord.ext import commands

from utils import embed


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["p", "latency"])
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.channel.trigger_typing()
        before = time.monotonic()
        message = await ctx.reply("** **", mention_author=False)
        ping = (time.monotonic() - before) * 1000
        await message.edit(embed=embed.info(ctx.guild.id, "Ping statistics",
                                            f"**API latency:** `{int(ping)}ms`\n**Bot latency:** `{round(self.bot.latency * 1000)}ms`"))


def setup(bot):
    bot.add_cog(Ping(bot))
