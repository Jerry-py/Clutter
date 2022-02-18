import discord
from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def config(self, ctx):
        pass

    @config.command()
    @commands.guild_only()
    async def channels(self, ctx, role: discord.Member):
        pass


def setup(bot):
    bot.add_cog(Ping(bot))
